import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lxml import etree
from selenium.webdriver.firefox.options import Options
import yaml
import getpass
import curses

class Scroll_wheel():

    def scroll(self,driver):
        original_top = 0
        while True:
            # 循环下拉滚动条
            driver.execute_script("window.scrollBy(0,300)")
            time.sleep(0.5)
            # 获取当前滚动条距离顶部的距离
            check_height = driver.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            # 如果滚动条距离上面的距离不再改变，也就是滚动后的距离和之前距离顶部的位置没有改变，说明到达最下方，跳出循环
            if check_height == original_top:
                break
            original_top = check_height
##搜寻
class SerachWork():
    def search(self,id,pwd):
        '''火狐实例'''
        # 实例化一个webdriver对象
        options_ff = Options()
        # 开启无头模式
        options_ff.add_argument('--headless')#注销该行即显示浏览器模拟登录

        driver = webdriver.Firefox(executable_path='geckodriver.exe',options=options_ff)

        # 对目标网站发起请求

        # id = input('请输入手机号码:')
        # pwd = input('请输入密码:')
        # id = '手机号'#记得注销上面两行
        # pwd = '密码'
        driver.get('https://passport2.chaoxing.com/login')
        # 输入账号密码登录
        driver.find_element(By.ID,'phone').send_keys(str(id))
        driver.find_element(By.ID,'pwd').send_keys(str(pwd))
        driver.find_element(By.ID,'loginBtn').click()
        try:
            driver.find_element(By.ID,'zne_kc_icon').click()
        except:
            pass
        try:
            driver.switch_to.frame('frame_content')
            print('正在搜寻...')

        except:
            print('请检查账号密码是否无误！')
        # 实例化一个滚轮对象
        scroll = Scroll_wheel()
        scroll.scroll(driver=driver)

        page_text = driver.page_source

        tree = etree.HTML(page_text)

        li_list = tree.xpath('//ul[@id="courseList"]/li')
        urls =[]
        # 请求每个页面
        for li in li_list:
            href = li.xpath('./div[@class="course-cover"]/a/@href')[0]
            # name = li.xpath('./div[@class="course-info"]//span/text()')[0]
            urls.append(href)
        for url in urls:
            driver.get(url=url)
            # 访问详情
            driver.find_element(By.XPATH,'//*[@id="boxscrollleft"]/div/ul[1]/li[4]/a').click()
            page_face = driver.page_source
            n = '<dd.*?>(.*?)</dd>'
            name = re.findall(n,page_face,re.S)
            name = str.strip(name[0])
            driver.switch_to.frame('frame_content-zy')

            scroll.scroll(driver)
            # 获取当前页面数据定位各个作业位置
            page_detail_text =driver.page_source

            tree_detail = etree.HTML(page_detail_text)
            li_list_detail = tree_detail.xpath('//div[@class="bottomList"]/ul/li')
            for li_detail in li_list_detail:

                HtmlStr = etree.tostring(li_detail,encoding='utf-8').decode()
                # 正则匹配查找
                ex = '<p class="overHidden2 fl">(.*?)</p>'
                xe = '<img class=.*?>(.*?)</div>'
                st = '<p class="status fl">(.*?)</p>'
                status = re.findall(st,HtmlStr,re.S)
                time = re.findall(xe,HtmlStr,re.S)
                # 控制删除已交和已过期作业，并打印输出
                if time:
                    if status[0]=='未交':
                        title = re.findall(ex,HtmlStr,re.S)
                        # 格式化
                        title = str.strip(title[0])
                        time = str.strip(time[0])
                        parm = {
                            '科目':name,
                            '作业':title,
                            '时间':time
                        }
                        print(parm)
                        # print('科目:'+name[0])
                        # print("<"+title[0]+'> :'+time[0])
        # 退出
        print('完成，记得按时完成作业哦！！！')
        driver.quit()
# 存入config.yaml
def save_id_pwd(id,pwd, file='config.yaml'):
    data = {}
    data['id'] = id
    data['pwd'] = pwd
    
    with open(file, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
# 从config.yaml中取出

def load_data(file='config.yaml'):
    with open(file, 'r') as stream:
        data = yaml.safe_load(stream)
        return data['id'], data['pwd']
# 进入动画
def animation(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    x = width // 2
    y = height // 2
    for i in range(10, 0, -1):
        stdscr.clear()
        stdscr.addstr(y, x - 5, "Loading...")
        stdscr.addstr(y + 1, x - i, "*" * (2 * i - 1))
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.clear()
    stdscr.addstr(y, x - 5, "Loading complete!")
    stdscr.refresh()
    time.sleep(2)

def switch_choice(argument):
    start_time = time.time()
    while time.time() - start_time < 5:
        argument = input("使用新密码请输入1，使用上次密码请输入2:\n")
        if argument in ["1","2"]:
            break
    if argument == "1":
        id = input("请输入电话号码：")
        pwd = getpass.getpass("请输入密码(不会显示密码)：")
        save_id_pwd(id=id,pwd=pwd)
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return

    elif argument == "2":
        id,pwd = load_data()
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return
if __name__ == '__main__':
    curses.wrapper(animation)
    argument = ""
    switch_choice(argument=argument)
