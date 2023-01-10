基于selenium模块实现浏览器模拟登录超星平台爬取作业截止日期爬虫脚本
=====
### 说明
    浏览器后台模拟登录超星平台查看作业详细截止时间
### 环境
    Python3.10
    安装包环境：
    在已有python环境的前提下
    进入HomeWorkPro目录输入
    pip install -r requirements.txt
    
### 运行
    1、在已有python环境的前提下
    python selenium_chaoxing.py
    2、安装FireFox浏览器
    3、https://github.com/mozilla/geckodriver/releases下载geckodriver,不同操作系统下载对应新驱动，解压后将原有驱动替换即可
    
### 存在问题
    本爬虫还不够完善，欢迎大家指导
    可以直接修改源码
    如果存在错误或者爬取不全面的情况
    1、在超星首页创建新文件夹并将其他没用或者过期课程移至新文件夹中
    2、其他活动课程也不要放在根目录也一并移至新文件夹
