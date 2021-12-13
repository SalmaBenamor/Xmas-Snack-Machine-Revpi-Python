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



rpi = revpimodio2.RevPiModIO(autorefresh=True)


#play 1/4 note
def play_4(io):
    exec("rpi.io.O_" + str(io) + ".value = 1")  
    time.sleep(0.3)
    exec("rpi.io.O_" + str(io) + ".value = 0")  
    time.sleep(0.3)


def pause_2():
    time.sleep(0.2)

def pause_4():
    time.sleep(0.4)

#Jingle
play_4(1)
play_4(2)
#Bells
play_4(4)
play_4(12)
pause_2()

#Jingle
play_4(3)
play_4(10)
#Bells
play_4(4)
play_4(9)
pause_2()


#Jin
play_4(5)
play_4(6)
pause_2()
#Gle
play_4(7)
play_4(8)
pause_2()
#All
play_4(3)
play_4(4)
pause_2()
#The
play_4(9)
play_4(10)
pause_2()
#Way
play_4(1)
play_4(2)
pause_4()


#Oh What Fun
play_4(11)
play_4(12)
pause_2()


#it  
play_4(5)
play_4(6)
pause_2()
#Is
play_4(7)
play_4(8)
pause_4()
#To
play_4(3)
play_4(4)
pause_2()
#Ride
play_4(9)
play_4(10)
pause_2()
#In
play_4(1)
play_4(2)
pause_2()
#A
play_4(11)
play_4(12)
pause_2()
#One
play_4(11)
play_4(12)
pause_2()
#Horse
play_4(1)
play_4(2)
pause_2()
#Open
play_4(9)
play_4(10)
pause_2()
#Sleigh
play_4(3)
play_4(4)
pause_4()