import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

DIRECTORY = os.getcwd()+'/line_images'

completed = [ 
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Samanata',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Akshar-Unicode',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Kalam-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Aparajita',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Halant-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Nirmala',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/NotoSans-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Hind-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Amita-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Sanskrit2003',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/VesperLibre-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Shobhika-Regular', 
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Kadwa-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/GIST-DGROTDhruv',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Kurale-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Glegoo-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Ranga-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Baloo-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/GIST-DVOTMohini',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Lohit-Devanagari',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Rajdhani-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Samyak-Devanagari',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Amiko-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Tillana-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/SakalBharati-Normal',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Gargi',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/RhodiumLibre-Regular',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/utsaah',
    '/home/ubuntu/practice/sanskrit-ocr/line_images/Jaldi-Regular'
    ]

for subdir, dirs, files in os.walk(DIRECTORY):
    print(subdir, dirs)
    if subdir not in completed:
        for (i,f) in enumerate(files):
            print('loop2: ', i)
            if f.endswith(".jpg") or f.endswith(".png"):
                im = Image.open(subdir+'/'+f)
                gray = im.convert("L")
                gray.save(subdir+'/'+f[0:f.find('.')]+".jpg")
                if f.endswith(".png"):
                    gray = plt.imread(subdir+'/'+f[0:f.find('.')]+".jpg")
                    rows = set([])
                    columns = set([])
                    for i in range(gray.shape[0]):
                        for j in range(gray.shape[1]):
                            if gray[i][j]<128:
                                rows.add(i)
                                columns.add(j)
                    roi = gray[min(rows):max(rows)+1, min(columns):max(columns)+1]
                    im_cvt = Image.fromarray(roi)
                    im_cvt.save(subdir+'/'+f[0:f.find('.')]+".jpg")




for subdir, dirs, files in os.walk(DIRECTORY):
    for f in files:
        if f.endswith('.png'):
            os.remove(subdir+'/'+f)