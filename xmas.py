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