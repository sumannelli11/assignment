# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:54:41 2021

@author: speed
"""

import cv2
img=cv2.imread("D:\\suman\\img\\1.jpg")
for i in range(2,102):
	cv2.imwrite("D:\\suman\\img\\"+str(i)+".jpg", img)


    

