# coding=utf-8
from PIL import Image
import cv2
import os

image_width = 200
image_height = 250


# 本程序用于前期，对 SVM 的训练集图片进行统一尺寸修改
# 此处设置的尺寸是 200*250 ，这个尺寸要与之后进行检测时的滑动窗口大小相同

def fixed_size1(filePath, savePath):
    """按照固定尺寸处理图片"""
    im = Image.open(filePath)
    if im.mode == "P":
        im = im.convert('RGB')
    if im.mode == "RGBA":
        im = im.convert('RGB')
    out = im.resize((image_width, image_height), Image.ANTIALIAS)
    out.save(savePath)


def fixed_size2(filePath, savePath):
    """按照固定尺寸处理图片"""
    im = Image.open(filePath)
    if im.mode == "P":
        im = im.convert('RGB')
    if im.mode == "RGBA":
        im = im.convert('RGB')
    width, height = im.size
    center_x, center_y = width // 2, height // 2
    half_width = image_width // 2
    half_height = image_height // 2
    left = center_x - half_width
    top = center_y - half_height
    right = center_x + half_width
    bottom = center_y + half_height
    # 使用切片来裁剪图像
    out = im.crop((left, top, right, bottom))
    out.save(savePath)


def changeSize():
    filePath = r'F:\0大三上\软件工程\new_picture_source\raw_pos'
    destPath = r'F:\0大三上\软件工程\new_picture_source\pos'
    # filePath = r'C:\Users\96172\Desktop\testpicture'
    # destPath = r'C:\Users\96172\Desktop\testpicture256'

    if not os.path.exists(destPath):
        os.makedirs(destPath)
    for root, dirs, files in os.walk(filePath):
        for file in files:
            if file[-1] == 'g':
                fixed_size1(os.path.join(filePath, file), os.path.join(destPath, file))
    print('Done')


if __name__ == '__main__':
    changeSize()
