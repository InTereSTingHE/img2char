#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Author: InTereSTingHE

from PIL import Image
from tkinter.filedialog import askopenfilename, askdirectory
import argparse
import os

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('--width', type = int, default = 120) # 字符画输出宽度
parser.add_argument('--height', type = int, default = 80) # 字符画输出高度
#parser.add_argument('file')     # 输入文件
#parser.add_argument('-o', '--output')   # 输出文件

# 获取参数
args = parser.parse_args()

WIDTH = args.width
HEIGHT = args.height

# 打开对话框选择图片
IMG = askopenfilename(title='Select Image')
(path, filename) = os.path.split(IMG)
(img, ext) = os.path.splitext(filename) # 切割文件名

# 打开对话框选择输出位置
output_dir = askdirectory(title = 'Select Save Path')
OUTPUT = os.path.join(output_dir, img + '_output.txt')

# 字符表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)