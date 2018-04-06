# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:42:51 2018

@author: 
"""

import os
from PIL import Image, ImageFilter

import ocr_common

# #对单个图像进行ocr识别 返回文本
# #
def pickup_text_in_image(imagefile):
    #取得文件名
    filename = os.path.basename(imagefile)
    
    image = Image.open(imagefile)
    text = ocr_common.ocr_imagetotext(image)
    
    outputfile = 'output' + '/' + filename + '.txt'
    txtfile = open(outputfile,'wb+')
    txtfile.write(text.encode('utf-8'))
    txtfile.close()
    
    return text


# #对某文件夹下 批量图像进行ocr识别 返回文本
# #
def pickup_text_in_imgpath(imagepath):
    # 设定识别的文字保存 的路径
    outputpath = 'output' + '/'
    
    # 查找指定目录下所有图像
    imglists = os.listdir(imagepath)
    jpglists = filter(lambda x: x.endswith('png'), imglists)
    
    # 对每个图像识别文字 并保存为txt
    for each_img in jpglists:
        imagefile = imagepath + each_img
        outputfile = outputpath + each_img + '.txt'
        print(outputfile)
        
        image = Image.open(imagefile)
        text = ocr_common.ocr_imagetotext(image)
        
        # 保存文字为txt文件
        txtfile = open(outputfile,'wb+')
        txtfile.write(text.encode('utf-8'))
        txtfile.close()
    
    
    return text


