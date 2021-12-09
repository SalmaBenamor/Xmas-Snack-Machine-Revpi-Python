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

from playsound import playsound
playsound('//home//pi//Xmas-Snack-Machine-Revpi-Python//jingle-bells.mp3')

rpi = revpimodio2.RevPiModIO(autorefresh=True)


def play_2():
    rpi.io.O_1.value = 1
    time.sleep(0.1)
    rpi.io.O_1.value = 0
    time.sleep(0.1)

def pause_2():
    time.sleep(0.2)


def pause_4():
    time.sleep(0.4)



#Jingle
play_2()

#Bells
play_2()

pause_2()

#Jingle
play_2()

#Bells
play_2()

pause_2()


#Jin
play_2()

#Gle
play_2()

#All
play_2()

#The
play_2()

#Way
play_2()

pause_2()
