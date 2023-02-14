import time
from HomeWorkPro.loading import animation
from HomeWorkPro import dao
from HomeWorkPro.selenium_chaoxing import SerachWork
import getpass
import curses
import msvcrt
import os

def switch_choice(argument):
    start_time = time.time()
    while time.time() - start_time < 5:
        argument = input("使用新账号请输入1，使用上次账号请输入2:\n")
        if argument in ["1","2"]:
            break
    if argument == "1":
        id = input("请输入电话号码：")
        pwd = getpass.getpass("请输入密码(不会显示密码)：")
        dao.save_id_pwd(id=id,pwd=pwd)
        print("正在验证请稍后...")
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return

    elif argument == "2":
        try:
            id,pwd = dao.load_data()
        except:
            print('请先使用新账号登录')
            return
        print("正在验证请稍后...")
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return
if __name__ == '__main__':
    # animat = animation.Animation()
    # animat.animation()
    curses.wrapper(animation)
    os.system('cls')
    argument = ""
    switch_choice(argument=argument)
    print("尝试按任意键退出...")
    msvcrt.getch()