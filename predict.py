# coding: utf-8

import urllib
import urllib2
import numpy as np
from PIL import Image
from sklearn.externals import joblib
import os

def verify(PicName, save=False):
    """
    """
    DstDir = os.getcwd()+"/cgi/SE/"
    model =DstDir+'model/zf_linearSVC.pkl'
    #model ='model/zf_linearSVC.pkl'
    pic_file = '%s.png'%PicName
    image = Image.open(pic_file).convert("L")
    x_size, y_size = image.size
    y_size -= 5
    piece = (x_size-22) / 8
    centers = [4+piece*(2*i+1) for i in range(4)]
    data = np.empty((4, 21 * 16), dtype="float32")
    for i, center in enumerate(centers):
        single_pic = image.crop((center-(piece+2), 1, center+(piece+2), y_size))
        data[i, :] = np.asarray(single_pic, dtype="float32").flatten() / 255.0
        if save:
            single_pic.save('%s-%s.png' % (PicName,i))
    clf = joblib.load(model)
    answers = clf.predict(data)
    answers = map(chr, map(lambda x: x + 48 if x <= 9 else x + 87 if x <= 23 else x + 88, map(int, answers)))
    return answers[0]+answers[1]+answers[2]+answers[3]
