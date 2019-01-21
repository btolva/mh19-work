#!/usr/bin/env python3
import numpy

# code from StackExchange.
def step(world):
    (wd, ht) = world.shape
    print("Doing a step with world shape:",wd,ht)
    print(repr(world))

    neighbors = numpy.zeros((wd, ht), dtype='uint8')
    neighbors[1:] += world[:-1]
    neighbors[:-1] += world[1:]
    neighbors[:,1:] += world[:,:-1]
    neighbors[:,:-1] += world[:,1:]
    neighbors[1:,1:] += world[:-1,:-1]
    neighbors[:-1,:-1] += world[1:,1:]
    neighbors[1:,:-1] += world[:-1,1:]
    neighbors[:-1,1:] += world[1:,:-1]

    world &= (neighbors == 2)
    world |= (neighbors == 3)
    return world

