#! /usr/bin/env python
# coding: utf-8

from PIL import Image
import argparse
# 命令行参数工具
# 此处不是重点，故而不做讲解，具体参见 (https://docs.python.org/2/library/argparse.html)

parser = argparse.ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()
imgpath = args.file
# 变量ascii_char: 存储用于显示图片的字符种类。我们要注意到，这个list的最后一个元素是空格，这表示，我们
# 将使用空格来代替原图片中灰度值最高的像素点（在灰度图像中，灰度值最高为255，代表白色，最低为0，代表黑色）。
# list中的第一个元素是$，这表示我们将使用$来代替原图片中灰度值最低的像素点。其余字符依此类推。
ascii_char = list(r"$@&%B#=-. ")


# 把RGB转为灰度值，并且返回该灰度值对应的字符标记
def select_ascii_char(r, g, b):
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)  # ‘RGB－灰度值’转换公式
    unit = 256.0/len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)]


# 返回给定路径图片的字符表示，用户在此还可以指定输出字符画的宽度和高度
def output(imgpath, width=100, height=100):
    im = Image.open(imgpath)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""

    for h in xrange(height):
        for w in xrange(width):
            txt += select_ascii_char(*im.getpixel((w, h))[:3])  # 此处请看详解（1）
        txt += '\n'
    return txt


def save_as_txtfile(txt):
    with open('imgtochar.txt', 'wb') as f:
        f.write(txt)


if __name__ == '__main__':
    print output(imgpath, 120, 90)
    save_as_txtfile(output(imgpath, 120, 90))