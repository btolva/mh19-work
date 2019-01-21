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

def runlength(sequence):
    isq = iter(sequence)
    vcur = next(isq)
    lcur = 1
    lmax = 1
    try:
        while True:
            vnxt = next(isq)
            if vcur != vnxt:
                lcur = 1
                vcur = vnxt
            else:
                lcur += 1
            if lcur > lmax:
                lmax = lcur
    except StopIteration as si:
        pass
    return lmax

def runlist(sequence):
    isq = iter(sequence)
    try:
        vcur = next(isq)
    except StopIteration as si:
        return 0
    lcur = 1
    lmax = 1
    try:
        while True:
            vnxt = next(isq)
            if vcur != vnxt:
                yield lcur
                lcur = 1
                vcur = vnxt
            else:
                lcur += 1
            if lcur > lmax:
                lmax = lcur
    except StopIteration as si:
        pass
    yield lcur

rlim = list(runlist(imhsl))
print("runlength max:", runlength(imhsl))
print("runlength max:", max(rlim))
#print(list(rlim))
print("bin counting:",numpy.bincount(rlim))
import pprint
pp = pprint.PrettyPrinter(indent=2).pprint
nzb = [(i, e) for (i, e) in enumerate(numpy.bincount(rlim)) if e]
print("nzb:")
pp(nzb)

print("Image size overall:",im.size)
print("Number of runs overall:", len(rlim))
print("Number of runs overall:", len(rlim)//2)
u11 = open('Ulysses_(11th_edition).txt','r')
u22 = open('Ulysses_(1922).txt', 'r')
ug = open('ulysses.txt','r')
def accum_words(lines):
    words = []
    for line in lines:
        # some punctuation becomes whitespace first
        #print(repr("h̸'-"),"    ")
        #print(bytes("\u0338'-", encoding="utf-8"))
        #print(bytes("'h̸'-", encoding="utf-8"))
        bad_punctuation = "%0123456789ſ†✠;…&*—\u0338'-—[]()•?’°/\"“””\u201d\u201c+,."
        equal_space = " " * len(bad_punctuation)
        line = line.translate("".maketrans(bad_punctuation, equal_space))
        for word in line.split():
            # remove punctuation
            word = word.translate("".maketrans('','','%0123456789/\\\'`:~£-._!, 	\t'))
            word = word.replace("œ","oe")
            word = word.replace("æ","ae")
            word = word.replace("Æ","Ae")
            if len(word) != 0:
                words.append(word)
    return words
words = accum_words(ug.readlines())
print(len(words))
#ulens = [len(list(ui)) for ui in (u11, u22, ug)]

#print(ulens)
#print(words[:15])
#print(words[705:715])
print("first ten runs:",rlim[:20:2])
mismatch = []
for i in range(1,len(rlim)):
    try:
        if rlim[-2*i] != len(words[-i]):
            if len(mismatch) == 0:
                print("mismatch: ",words[-i], len(words[-i]), rlim[-2*i])
                print("context: ", rlim[-2*i - 14: -2*i+16:2])
                print("badtext: ", list(map(len,words[-i-7:-i+8])))
                #print("context: ", rlim[-2*i - 4: -2*i+6:2], list(map(len,words[-i-2:-i+3])))
            mismatch.append((i,words[-i]))
    except IndexError:
        break
    except Exception as e:
        print(repr(e))
        break
print (mismatch[10::-1])
print ("mismatch len:",len(mismatch))
print("MATCH FRACTION: {0:.1f}%".format(100.*(len(rlim)*.5 - len(mismatch)) / len(rlim)))
if len(mismatch) == 0:
    mismatch.append([0,])
print("MATCH FRACTION: {0:.1f}%".format(100.*(mismatch[0][0]) / len(rlim)))
print (mismatch[-10:])



# find all cases in which an odd numbered item isn't 1.
anomalies = [(idx, val) for (idx, val) in enumerate(rlim[::1]) if (idx % 2) and (val != 1)]
print(anomalies[:40])
sys.exit(0)

print('raw image values, first 32',numpy.array(im)[0,:32])

#print('negative 210 neighborhood',rlim[-430:-410:2])
plt.imshow(imhsd)
plt.show()
#
import numpy_game_of_life as game
## do things...
#if 1:
#    i = h - 705
#    nh = h-i
#    nw = (w*h) // (h-i)
#
#    imrs = imhsdf[-nw*nh:].reshape(nw, nh)
#    imrs = numpy.not_equal(imrs, 0)
#    # kind of test the Life implementation with random inputs.
#    #imrs = numpy.random.randint(0,2,size=(100,100),dtype='uint8')
#    while True:
#        plt.clf()
#        plt.imshow(imrs[:100,:100])
#        plt.ion()
#        plt.show()
#        plt.pause(0.01)
#        imrs = game.step(imrs)
#
#while True:
#    plt.pause(.001)

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
