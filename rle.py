#!/usr/bin/env python3

# run length extraction
import uni
import sys

LEVELS = 256

def extract(image):
    extraction_points = [[] for l in range(LEVELS)]
    run_lengths = runlist(image, extraction_points)
    return run_lengths, extraction_points

def runlist(sequence, eps):
    isq = iter(sequence)
    lcur = 0
    widx = 0
    while True:
        vnxt = next(isq)
        if vnxt == 0:
            if lcur > 0:
                yield lcur
            lcur = 0
            widx += 1
        else:
            eps[vnxt].append((widx, lcur))
            lcur += 1
    return

def nab_pixels(img, wvec, resarr):
    oidx = 0
    isq = iter(sequence)
    lcur = 0
    widx = 0
    while True:
        vnxt = next(isq)
        if vnxt == 0:
            if lcur > 0:
                yield lcur
            lcur = 0
            widx += 1
        else:
            char = words[widx][lcur]
            if char == 'z' or char == 'Z':
                resarr[oidx] = vcur
                oidx += 1
            #eps[vnxt].append((widx, lcur))
            lcur += 1
    return
    

def thist(level):
    if len(level) == 0:
        return []
    level = uni.remove_accents(level)
    # find base character somehow.
    chars = set(level)
    if len(chars) != 2:
        print(chars)
        sys.exit(0)
    tc = list(chars)[0]
    lc = tc.lower()
    uc = tc.upper()
    assert set((lc, uc)) == chars
    return runlist_char(level, lc, uc)

def throw_si():
    raise StopIteration

def empty_seq():
    yield 5
    yield 7
    throw_si()

print(list(empty_seq()))

def runlist_char(sequence, lc, uc):
    isq = iter(sequence)
    try:
        vcur = next(isq)
    except StopIteration as si:
        return
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

