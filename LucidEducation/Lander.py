from tkinter import*
from math import*
root=Tk()
c=Canvas(root,width=800,height=600,bg="black")
c.pack()
Pi=3.14159265
class Lander:
    def __init__(self,xinit,yinit,θinit,vxinit,vyinit,radius):
        self.x=xinit
        self.y=yinit
        self.θ=θinit
        self.vx=vxinit
        self.vy=vyinit
        self.radius=radius
        self.Δθ=0
        self.thrust=0
        self.flamex1=0
        self.flamey1=0
        self.flamex2=0
        self.flamey2=0
        coords=[-40,0,40,0,55,-15,55,-35,25,-60,-25,-60,-55,-35,-55,-15,
                -40,0,-60,7,-60,25,-30,33,-25,33,-30,58,-25,58,-25,63,-40,
                63,-40,58,-35,58,-30,33,5,33,14,48,-14,48,-5,33,30,33,35,
                58,40,58,40,63,25,63,25,58,30,58,25,33,30,33,60,25,60,7,
                40,0]
        self.poly=c.create_polygon(coords,outline="#804040",fill="#000000",
                                   width=1)
        self.flame=c.create_line(1,1,2,2,fill="black")
        self.xy=[]
        self.rt=[]
        for i in range(0,len(coords),2):
            x=coords[i]
            y=coords[i+1]
            r=sqrt(x**2+y**2)*self.radius/64
            t=atan2(y,x)
            self.rt.append(r)
            self.rt.append(t)
    def draw(self):
        self.xy=[]
        for i in range(0,len(self.rt),2):
            r=self.rt[i]
            t=self.rt[i+1]
            self.xy.append(self.x+r*cos(t+self.θ))
            self.xy.append(self.y+r*sin(t+self.θ))
        c.delete(self.poly)
        self.poly=c.create_polygon(self.xy,outline="#dddddd",fill="#000000",
                                   width=2)
    def move(self):
        self.vy+=.01
        self.x+=self.vx
        self.y+=self.vy
        self.θ+=self.Δθ
        if(self.thrust>0):
           self.vx+=self.thrust*cos(self.θ-Pi/2)
           self.vy+=self.thrust*sin(self.θ-Pi/2)
        self.draw()
        if(self.thrust>0):
            flamex1=self.x+cos(self.θ+Pi/2)*self.radius*.75
            flamey1=self.y+sin(self.θ+Pi/2)*self.radius*.75
            flamex2=self.x+cos(self.θ+Pi/2)*self.radius*1.4
            flamey2=self.y+sin(self.θ+Pi/2)*self.radius*1.4
            c.delete(self.flame)
            self.flame=c.create_line(flamex1,flamey1,flamex2,flamey2,
                                     fill="#ff4400",width=8)
        c.after(10,self.move)
    def thrust_on(self):
        self.thrust=.025
    def thrust_off(self):
        self.thrust=0
        c.delete(self.flame)
    def rotate_left(self):
        self.Δθ=-.01
    def rotate_right(self):
        self.Δθ=+.01
    def rotate_stop(self):
        self.Δθ=0
def left_turn(event):
    lander.rotate_left()
def right_turn(event):
    lander.rotate_right()
def stop_turn(event):
    lander.rotate_stop()
def thrust(event):
    lander.thrust_on()
def coast(event):
    lander.thrust_off()
c.bind_all("<KeyPress-Left>",left_turn)
c.bind_all("<KeyPress-Right>",right_turn)
c.bind_all("<KeyRelease-Left>",stop_turn)
c.bind_all("<KeyRelease-Right>",stop_turn)
c.bind_all("<KeyPress-Up>",thrust)
c.bind_all("<KeyRelease-Up>",coast)
lander=Lander(100,100,0,1,-1,20)
lander.draw()
lander.move()
mainloop()
