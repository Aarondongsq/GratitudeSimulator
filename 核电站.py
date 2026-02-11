'''
    将军模拟器 - 太阳能电池板
    Copyright (C) 2026  Chung Chai Aaron Dong

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    --- 特别补充说明 ---
    1. 严禁倒卖本代码（包括其中的一部分）或将其用于商业洗稿。
    2. 严禁 Gitee、GitCode 等平台在未经作者书面许可的情况下，私自镜像、克隆
       或通过爬虫抓取本项目用于增加平台KPI等。
    3. 任何违反 GPL v3 协议的行为，作者保留在开源社区公示及追究法律责任的权利。
'''
import tkinter as tk
import tkinter.messagebox as msgbox 
import sys
from os.path import abspath, join#Python自带模块

from PIL import Image, ImageTk #第三方库

def resource_path(relative_path:str) -> str:
    '''
    获取文件的绝对路径。
    针对VS调试器的坏脾气，会有检查函数，确认自己是否在VS的调试模式。
    '''

    # ↓拆分文件路径，再重新组合，确保每个系统都能用该软件晒到太阳
    relative_path = join(*(relative_path.split('\\')))

    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")

    return join(base_path, relative_path)
#==================== 类定义 ====================
class MainWindow(tk.Tk):
    def __init__(self):
        '''
        创建一个全屏置顶的窗口，让太阳能够放置！

        让世界“热闹”起来吧！         ——芙宁娜
        '''
        super().__init__()
        self.title('太阳能电池板')
        self.attributes('-fullscreen', True)
        self.attributes('-topmost', True) #负责全屏和置顶窗口
        self.protocol('WM_DELETE_WINDOW', lambda: None) # 让用户无法关闭这个窗口

        self.__set_components() #放置一位闪耀的太阳！

    def __set_components(self):
        '''
        负责创建一个非常新鲜的太阳，不过运行它的人记得带上墨镜！
        否则，你将变成光！
        '''
        pass

    def __get_image(self, get_path:str) -> ImageTk.PhotoImage:
        '''
        核心出装：太阳、太阳专属BGM导入
        视听双结合，那才叫爽！

        get_path：指定文件路径。
        '''
        pass

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()