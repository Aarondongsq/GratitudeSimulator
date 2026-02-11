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

import sys
from os.path import abspath, join
from threading import Thread
from time import sleep#Python自带模块

from PIL import Image, ImageTk 
from pygame.mixer import music, init#第三方库

def resource_path(relative_path:str) -> str:
    '''
    获取文件的绝对路径。
    可以根据源代码运行和打包版，自动切换获取模式。
    路径兼容各大系统，防止你见不到将军！゜゜(´Ｏ`) ゜゜
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
class OppsSunFalls(Exception):
    '''
    如果因为意外导致将军驾崩了，那么将会这样报错
    '''
    pass

class MusicBegins:
    def __init__(self):
        '''
        当太阳坐稳扶好时，将会播放专属音乐
        让你感受将军的“恩情”！

        将军的恩情还不完！！。゜゜(´Ｏ`) ゜゜。
        '''
        # --- 加载线程 ---
        music_play = Thread(target=self.__execute, daemon=True) #启动播放线程防恩情卡死
        music_play.start()

    def __execute(self):
        '''
        播放恩情小曲，让周围的温度更快提高！
        '''
        # --- 恩情加载 ---
        init() #初始化
        music.load(resource_path(r'music\你若三冬.mp3'))

        # --- 播放恩情 ---
        while True:
            music.play()
            sleep(193) #播放时等待，防止过快停止
            music.stop()


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
        sleep(3)
        self.lift()
        #↓太阳专属音乐
        MusicBegins()

    def __set_components(self):
        '''
        负责创建一个非常新鲜的太阳，不过运行它的人记得带上墨镜！
        否则，你将变成光！
        '''
        # --- 获取太阳 ---
        self.image = self.__get_image() #有请太阳登场！

        # --- 给太阳定个位置 ---
        thesunrises = tk.Label(self, image=self.image)
        #↓剧中太阳位置
        thesunrises.pack(anchor='center', expand=True)

    def __get_image(self) -> ImageTk.PhotoImage:
        '''
        核心出装：太阳导入
        视听双结合，那才叫爽！
        '''
        try: #获取太阳
            image_data = Image.open(resource_path(r'image\sun.png')) #获取太阳居住地
            return ImageTk.PhotoImage(image_data)
        except:
            '''
            如果特殊原因导致太阳升不起来，那么直接报错
            提示用户应该检查太阳状态
            '''
            raise OppsSunFalls('哎呀！太阳升不起来了啊！太糟糕了！')

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()