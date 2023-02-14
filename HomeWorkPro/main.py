import time
from loading import animation
import dao
from selenium_chaoxing import SerachWork
import getpass
import curses

def switch_choice(argument):
    start_time = time.time()
    while time.time() - start_time < 5:
        argument = input("使用新密码请输入1，使用上次密码请输入2:\n")
        if argument in ["1","2"]:
            break
    if argument == "1":
        id = input("请输入电话号码：")
        pwd = getpass.getpass("请输入密码(不会显示密码)：")
        dao.save_id_pwd(id=id,pwd=pwd)
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return

    elif argument == "2":
        id,pwd = dao.load_data()
        work = SerachWork()
        work.search(id=id,pwd=pwd)
        return
if __name__ == '__main__':
    # animat = animation.Animation()
    # animat.animation()
    curses.wrapper(animation)
    argument = ""
    switch_choice(argument=argument)