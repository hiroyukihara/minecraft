#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block
import math


def setup_ground (mc, bid):
    size = 64
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-100,-100,pos.z-100,pos.x+100,-1,pos.z+100,block.GRASS)
    mc.setBlocks(pos.x-100,0,pos.z-100,pos.x+100,1000,pos.z+100,block.AIR.id)

    mc.setBlocks(pos.x, 0, pos.z, pos.x+size, 1, pos.z+size, bid)
    mc.setBlocks(pos.x, 1, pos.z, pos.x+size, 50, pos.z+size, block.AIR.id)
    mc.setBlocks(pos.x+1, 0, pos.z+1, pos.x+size-1, 50, pos.z+size-1,block.AIR.id)

def rasen (mc,bid):
    phase = 0.00
    high = 0
    pos = mc.player.getPos()
    hankei = 31
    for x in range(1,7200):
        mc.setBlock(pos.x+(math.cos(math.pi*(phase/360))*hankei)+32,high,pos.z+(math.sin(math.pi*(phase/360))*hankei)+32,bid)
        phase += 1.00
        if x%72 == 0:
            high += 1

mc = minecraft.Minecraft.create("192.168.11.12")
mc.postToChat("Start: rasen1")


setup_ground(mc, block.BRICK_BLOCK.id)
rasen(mc, block.BRICK_BLOCK.id)
mc.postToChat("End: rasen1")
print "End"
