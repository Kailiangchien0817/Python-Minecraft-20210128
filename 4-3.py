#4-3 方塊躲貓貓
from mcpi.minecraft import Minecraft
LC = Minecraft.create()
from random import randrange

for i in range (10):
    x,y,z = LC.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        LC.setBlock(x,y,z,35,color)
        
        
ans = randrange(0,16)
while True:
    hits = LC.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        block = LC.getBlockWithData(a.pos)
        data = block.data
        
        if data == ans:
            LC.postToChat("恭喜你找到啦！！！")
            LC.setBlock(a.pos,57)
            break
        
        elif data < ans:
            LC.postToChat("找錯囉~~~ 找大一點的吧！")
    
        elif data > ans:
            LC.postToChat("找錯囉~~~ 找小一點的吧！")