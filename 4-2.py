#4-2 神秘圖騰(前後右左上下)

from mcpi.minecraft import Minecraft
LC = Minecraft.create()
import random

x,y,z = LC.player.getTilePos()

for i in range(20):
    r=random.randrange(1,7)
    if r == 1:
        LC.setBlocks(x,y,z,x,y,z+4,169)
        z = z+4
    if r == 2:
        LC.setBlocks(x,y,z,x,y,z-4,169)
        z = z-4
    if r == 3:
        LC.setBlocks(x,y,z,x+4,y,z,169)
        x = x+4
    if r == 4:
        LC.setBlocks(x,y,z,x-4,y,z,169)
        x = x-4
    if r == 5:
        LC.setBlocks(x,y,z,x,y+4,z,169)
        y = y+4
    if r == 6:
        LC.setBlocks(x,y,z,x,y-4,z,169)
        y = y-4