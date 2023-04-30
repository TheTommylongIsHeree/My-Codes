import turtle
from getch import pause
import time
import os
import platform
t = turtle.Turtle()
s = turtle.Screen()
radius = 100
a = 1

while a in range (361):
    t.fd(radius * 2 * 3.14 / 360)
    t.rt(1)
    a = a + 1
print("The turtle has completed in drawing the circle with a radius of", radius)
pause("Press any key to continue")
print("Setting up to draw the triangle. Please wait...")
a = 1
t.lt(30)
t.rt(90)
t.pd()
b = 1
pause("Set up completed successfully, drawing the filled triangle when any key is pressed")
while b == 1:
    t.fd(a)
    t.rt(120)
    t.fd(a)
    t.rt(120)
    t.fd(a)
    t.rt(120)
    print("The turtle has complete in drawing a triangle with a of" , a,", a of the next triangle is", a + 1)
    a = a + 1
    time.sleep(0.25)
    if a == 175 or a >> 175:
        print("The turtle has complete in drawing a filled triangle with a of" , a)
        b = 0
pause("PROGRAM STOPPED, PRESS ANY KEY TO EXIT")
exit()
time.sleep(10)
print("10 second has passed and program has NOT stopped yet!!")
print("Trying to taskkill python in a few seconds")
time.sleep(5)
plt = platform.system()

if plt == "Windows":
    os.system("taskkill /im python.exe /f")
else:
    os.system("killall python")
    os.system("killall python3")
    os.system("killall py")
time.sleep(10)
print("i give up, time to reboot your pc lol")
time.sleep(5)
if plt == "Windows":
    os.system("shutdown -t 0 -r -f")
else:
    os.system("sudo reboot")
    os.system("reboot")