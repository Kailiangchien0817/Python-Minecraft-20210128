#4-4 六個方塊
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

list2 = [[12,41,14],[35,73,86]]

myID = LC.getPlayerEntityId("lucaschien0817")
x,y,z = LC.entity.getTilePos(myID)

startX = x

for i in list2:
    for j in i:
        
        LC.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1    