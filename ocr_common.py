# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:42:51 2018

@author: 
"""

import pytesseract
import os

# #对图像进行ocr识别 返回文本
def ocr_imagetotext(image):
    #print(image)
    # 进行ocr识别 返回文本
    text = pytesseract.image_to_string(image,lang='chi_sim')
    #print(len(text))
    #print(text)
    
    #txtfile = open('output.txt','wb+')
    #txtfile.write(text.encode('utf-8'))
    #txtfile.close()
    
    return text

# #对图像进行ocr识别 返回文本
def ocr_imagetotext_eng(image):
    #print(image)
    # 进行ocr识别 返回文本
    text = pytesseract.image_to_string(image,lang='eng')    
    return text

# #对图像进行ocr识别 返回文本
def ocr_imagetotext_pinyin(image):
    #print(image)
    # 进行ocr识别 返回文本
    text = pytesseract.image_to_string(image,lang='pinyin')
    return text

