from vpython import *
import math
g = 9.8               
r = 1   
speed = eval(input('speed(0~62m/s):'))
angle = eval(input('angle(0~90°):'))
vx = round(speed * math.sin(math.radians(angle)),1)
vy = round(speed * math.cos(math.radians(angle)),1)
scene = canvas(title="水平拋射模擬", width=1680, height=800, x = 0,y = 0,background=color.black)#設定畫面
floors = box(length=392, height=0.1, width=4, color=color.blue)                  
ball = sphere(radius = r,  color=color.red, make_trail=True)    
timer = label(pos=vector(200, 100, 0), text="t =  s", space=50, height=24,border=4, font="monospace")
distance = label(pos=vector(200, 90, 0), text="   m", space=50, height=24,border=4, font="monospace")                              


ball.pos = vector(-196.0, r+0.1, 0.0)    
ball.v = vector(vx, vy , 0.0)       

dt = 0.001        
t = 0              
while ball.pos.y >= (r+0.1):       
    rate(1000)           
    t += dt
    timer.text = "t = {:.1f} s".format(t)   
    distance.text = "{:.1f} m".format(ball.pos.x+196)  
    ball.pos += ball.v*dt
    ball.v.y +=  (-g*dt)
