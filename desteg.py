#!/usr/bin/env python3

from __future__ import print_function
import os, sys
import PIL
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fft2
import numpy

have_matplots = False
have_imshows = False

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
if have_imshows:
    imhs.show()
# iterator over flattened pixels
imhsl = list(imhs.getdata())
imhsd = numpy.array(imhs)
imhsdf = imhsd.flatten()

# scan through slices:
if 1:
    for i in range(23 * 28):
        a = i // 23
        b = i % 23
        imhsds = imhsd[b::23,a::28]
        plt.clf()
        plt.imshow(imhsds)
        plt.ion()
        plt.show()
        plt.pause(.001)

# shrink in one dimension...
if 1:
    for i in range(w):
        nw = w-i
        nh = (w*h) // (w-i)

        imrs = imhsdf[:nw*nh].reshape(nw, nh)
        plt.clf()
        plt.imshow(imrs)
        plt.ion()
        plt.show()
        plt.pause(.001)


print(imhsl[0:128])
#def accumulate_bits(pixels):


imhslf = numpy.abs(fft(imhsl))
imhsdf = numpy.abs(fft2(imhsd))

imhsdf[0][0] = 0
if have_imshows:
    plt.imshow(imhsdf)
    plt.show()

if have_imshows:
    pass
    #im3.show()

hi = im.histogram()


if have_matplots:
    plt.plot(imhslf[:25])
    plt.show()

#for thing in imhsl:


#ehi = list(enumerate(hi))
ehi = list(hi)

ehi[0] = 0
if have_matplots:
    plt.bar(range(len(ehi)), ehi)
print(ehi)
if have_matplots:
    plt.show()

def stride_image(ws, hs):
    ims = Image.new("L", (w//ws, h//hs))
    c = 0
    for p in im.getdata():
        c += 1
        pass
    print(c)

stride_image(23, 28)
