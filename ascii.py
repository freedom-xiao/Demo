# -*- coding=utf-8 -*-

from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file',type=str, help='file name')
parser.add_argument('--width',type=int, help='image width', default = 80)
parser.add_argument('--height',type=int, help='image height', default = 80)
parser.add_argument('--output',type=str, help='output file name')
args = parser.parse_args()

#获取参数
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

length = len(ascii_char)


#256个灰阶映射到10个字符上
def get_char(r,g,b,a=256):
    
    if a == 0:
    	return ' '
    #灰阶公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = 256/length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	txt = ''

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'

	print(txt)


#字符画输出到文件
if OUTPUT:
	with open(OUTPUT,'w') as f:
		f.write(txt)
else:
	with open('output.txt','w') as f:
		f.write(txt)
