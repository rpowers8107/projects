import mcpi.minecraft as minecraft
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Space Invaders")

grass = 47


while True:#an infinite loop that doesnt stop
    pos = mc.player.getPos()#gets playeers position
    x = pos.x
    y = pos.y
    z = pos.z

    block_beneath = mc.getBlock(x, y-1, z)

    block_beneath == grass (x,y-1,z)#if block beneath is grass spawns a blue space invader.
        
    mc.setBlocks(x+2,y+1,z,x+2,y+3,35,3)
    mc.setBlocks(x+3,y+3,z,x+3,y+4,z,35,3)
    mc.setBlocks(x+4,y+1,z,x+4,y+5,z,35,3)
    mc.setBlocks(x+5,y,z,x+6,y,z,35,3)
    mc.setBlocks(x+5,y+3,z,x+11,y+3,z,35,3)
    mc.setBlock(x+3,y+6,z,35,3)
    mc.setBlocks(x+6,y+2,z,x+9,y+2,z,35,3)
    mc.setBlocks(x+6,y+4,z,x+9,y+4,z,35,3)
    mc.setBlocks(x+11,y+1,z,x+11,y+5,z,35,12)
    mc.setBlocks(x+12,y+3,z,x+12,y+4,z,35,3)
    mc.setBlocks(x+13,y+1,z,x+13,y+3,z,35,3)
    mc.setBlocks(x+11,y+5,z,x+5,y+5,z,35,3)
    mc.setBlock(x+12,y+6,z,35,3)
    mc.setBlocks(x+10,y,z,x+9,y,z,35,3)#code for blue space invader
    
else:#if block is anything other than grass then it sets a yellow space invader. 
    mc.setBlocks(x+2,y+1,z,x+2,y+3,z,35,4)
    mc.setBlocks(x+3,y+3,z,x+3,y+4,z,35,4)
    mc.setBlocks(x+4,y+1,z,x+4,y+5,z,35,4)
    mc.setBlocks(x+5,y,z,x+6,y,z,35,4)
    mc.setBlocks(x+5,y+3,z,x+11,y+3,z,35,4)
    mc.setBlock(x+3,y+6,z,35,4)
    mc.setBlocks(x+6,y+2,z,x+9,y+2,z,35,4)
    mc.setBlocks(x+6,y+4,z,x+9,y+4,z,35,4)
    mc.setBlocks(x+11,y+1,z,x+11,y+5,z,35,4)
    mc.setBlocks(x+12,y+3,z,x+12,y+4,z,35,4)
    mc.setBlocks(x+13,y+1,z,x+13,y+3,z,35,4)
    mc.setBlocks(x+11,y+5,z,x+5,y+5,z,35,4)
    mc.setBlock(x+12,y+6,z,35,4)
    mc.setBlocks(x+10,y,z,x+9,y,z,35,4)#code for a yellow space invader



    sleep(0.1)
     
 


    


    
