#!/usr/bin/env python3

from __future__ import print_function
import os, sys
import PIL
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

fn = "r11-picture image.png"
im = Image.open(fn)
print(dir(im))

#im.show()
print("passing.")
im2 = im.copy()
print(im.format)
print(im.mode)
w, h = im.size
import primefac_3 as primefac
ws = list(primefac.primefac(w))
hs = list(primefac.primefac(h))
print((ws, hs))
print((w, h))

def slice_factory(level):
    def slicer(pixel):
        if pixel == level:
            return 255
        return 0
    return slicer
im3 = im.point(slice_factory(221))

def hard_slice(pixel):
    if pixel == 0:
        return 0
    return 255

imhs = im.point(hard_slice)
# iterator over flattened pixels
imhsl = list(imhs.getdata())
from scipy.fftpack import fft, ifft

def accumulate_bits(pixels):


imhslf = fft(imhsl)

#im3.show()

hi = im.histogram()


plt.plot(imhslf[:25])
plt.show()

for thing in imhsl:


#ehi = list(enumerate(hi))
ehi = list(hi)

ehi[0] = 0
plt.bar(range(len(ehi)), ehi)
print(ehi)
plt.show()

def stride_image(ws, hs):
    ims = Image.new("L", (w//ws, h//hs))
    c = 0
    for p in im.getdata():
        c += 1
        pass
    print(c)

stride_image(23, 28)
