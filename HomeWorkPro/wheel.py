import time

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