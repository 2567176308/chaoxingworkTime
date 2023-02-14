import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.firefox.options import Options
import wheel
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
        scroll = wheel.Scroll_wheel()
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
