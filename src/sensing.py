#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import parameters as para


class Sensor:
    def __init__(self):
        self.enter_pin = para.ENTER_PIN #Motion sensor signal port : GPIO 21
        self.rest_pin = para.REST_PIN #Dust sensor signal port：GPIO 15
        self.sensor_no = para.SENSOR_NO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.enter_pin, GPIO.IN)
        GPIO.setup(self.rest_pin, GPIO.IN)
       

    #Output sensor HI / LO at 1/0
    def enter_detect(self): 
        sig = 0
        if self.sensor_no == 1:
            if GPIO.input(self.enter_pin) == GPIO.HIGH:
                sig = 0
            else:
                sig = 1
        else:
            if GPIO.input(self.enter_pin) == GPIO.HIGH:
                sig = 1

        return sig


    def rest_detect(self):
        sig = 0 
        if self.sensor_no == 1:
            if GPIO.input(self.rest_pin) == GPIO.HIGH:
                sig = 0
            else:
                sig = 1
        else:
            if GPIO.input(self.rest_pin) == GPIO.HIGH:
                sig = 1

        return sig

