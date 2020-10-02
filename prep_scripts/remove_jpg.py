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
    if subdir not in completed:
        print(subdir)


