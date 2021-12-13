#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Simple Revpi IO Example 
# Uses revpimodio library https://revpimodio.org by Sven Sager
#
# Prerequisites:
# - Use a RevPi Core or Connect and attach and configure a DIO Module
#
# Note: revpimodio2 comes already pre-installed on the official revolution pi raspbian os images

import revpimodio2
import time


#from playsound import playsound
#playsound("//home//pi//Xmas-Snack-Machine-Revpi-Python//jingle-bells.mp3")



rpi1 = revpimodio2.RevPiModIO(autorefresh=True)
rpi2 = revpimodio2.RevPiModIO(autorefresh=True)
rpi3 = revpimodio2.RevPiModIO(autorefresh=True)
rpi4 = revpimodio2.RevPiModIO(autorefresh=True)
rpi5 = revpimodio2.RevPiModIO(autorefresh=True)
rpi6 = revpimodio2.RevPiModIO(autorefresh=True)
rpi7 = revpimodio2.RevPiModIO(autorefresh=True)
rpi8 = revpimodio2.RevPiModIO(autorefresh=True)
rpi9 = revpimodio2.RevPiModIO(autorefresh=True)
rpi10 = revpimodio2.RevPiModIO(autorefresh=True)
rpi11 = revpimodio2.RevPiModIO(autorefresh=True)
rpi12 = revpimodio2.RevPiModIO(autorefresh=True)




def play_1():
    rpi1.io.O_1.value = 1
    time.sleep(0.3)
    rpi1.io.O_1.value = 0
    time.sleep(0.3)

def play_2():
    rpi2.io.O_2.value = 1
    time.sleep(0.3)
    rpi2.io.O_2.value = 0
    time.sleep(0.3)

def play_3():
    rpi3.io.O_3.value = 1
    time.sleep(0.3)
    rpi3.io.O_3.value = 0
    time.sleep(0.3)

def play_4():
    rpi4.io.O_4.value = 1
    time.sleep(0.3)
    rpi4.io.O_4.value = 0
    time.sleep(0.3)

def play_5():
    rpi5.io.O_5.value = 1
    time.sleep(0.3)
    rpi5.io.O_5.value = 0
    time.sleep(0.3)

def play_6():
    rpi6.io.O_6.value = 1
    time.sleep(0.3)
    rpi6.io.O_6.value = 0
    time.sleep(0.3)

def play_7():
    rpi7.io.O_7.value = 1
    time.sleep(0.3)
    rpi7.io.O_7.value = 0
    time.sleep(0.3)

def play_8():
    rpi8.io.O_8.value = 1
    time.sleep(0.3)
    rpi8.io.O_8.value = 0
    time.sleep(0.3)

def play_9():
    rpi9.io.O_9.value = 1
    time.sleep(0.3)
    rpi9.io.O_9.value = 0
    time.sleep(0.3)

def play_10():
    rpi10.io.O_10.value = 1
    time.sleep(0.3)
    rpi10.io.O_10.value = 0
    time.sleep(0.3)

def play_11():
    rpi11.io.O_11.value = 1
    time.sleep(0.3)
    rpi11.io.O_11.value = 0
    time.sleep(0.3)

def play_12():
    rpi12.io.O_12.value = 1
    time.sleep(0.3)
    rpi12.io.O_12.value = 0
    time.sleep(0.3)

def play_2(AllPins):
    rpi.io.O_1.value = 1
    time.sleep(0.1)
    rpi.io.O_1.value = 0
    time.sleep(0.1)

def pause_2():
    time.sleep(0.2)


def pause_4():
    time.sleep(0.4)



#Jingle
play_1()
play_2()

#Bells
play_11()
play_12()
pause_11()

#Jingle
play_3()
play_10()
#Bells
play_4()
play_9()
pause_2(),


#Jin
play_5()
play_6()
pause_2()
#Gle
play_7()
play_8()
pause_2()
#All
play_3()
play_4()
pause_2()
#The
play_9()
play_10()
pause_2()
#Way
play_1()
play_2()
pause_4()


#Oh What Fun
play_11()
play_12()
pause_2()

#All
play_2()

#it  
play_5()
play_6()
pause_2()
#Is
play_7()
play_8()
pause_4()
#To
play_3()
play_4()
pause_2()
#Ride
play_9()
play_10()
pause_2()
#In
play_1()
play_2()
pause_2()
#A
play_11()
play_12()
pause_2()
#One
play_11()
play_12()
pause_2()
#Horse
play_1()
play_2()

pause_2()
#Open
play_9()
play_10()
pause_2()
#Sleigh
play_3()
play_4()
pause_4()


if __name__ == '__main__':
    Thread(target = play_1).start()
    Thread(target = play_2).start()
    Thread(target = play_3).start()
    Thread(target = play_4).start()
    Thread(target = play_5).start()
    Thread(target = play_6).start()
    Thread(target = play_7).start()
    Thread(target = play_8).start()
    Thread(target = play_9).start()
    Thread(target = play_10).start()
    Thread(target = play_11).start()
    Thread(target = play_12).start()