#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import sys
from awsMQTTconnect import Com, Pub
from sensing import Sensor
from counter import Count


sensor = Sensor()
com = Com()
pub = Pub()
count = Count()

def loop():
    sub_t_count = 0
    pub_flag = 0
    enter_count = 0
    rest_count = 0
    alert_flag = 0
    alert_type = 0
    t0 = datetime.datetime.now()

    while True:
        sig_enter = sensor.enter_detect()
        sig_rest = sensor.rest_detect()

        enter_count = count.motion_count(sig_enter, enter_count)
        rest_count = count.motion_count(sig_rest, rest_count)
        bool, sub_t_count = pub.publish_motion_count(sub_t_count, enter_count, rest_count)
        #print(enter_count, rest_count)
        if bool == True: 
            enter_count = 0
            rest_count = 0

        t0, pub_flag, alert_flag, alert_type = count.time_count(t0, sig_rest, pub_flag, alert_flag, alert_type)
        if alert_flag == 1 and alert_type == 1:
            message = "15 hours passed without sensor response"
            bool, pub_flag = pub.publish_alert(pub_flag, message)
        elif alert_flag == 1 and alert_type == 2:
            message = "Now, warning going on"
            bool, pub_flag = pub.publish_alert(pub_flag, message)

        
        time.sleep(1)


if __name__ == '__main__':
    try:
        time.sleep(90)

        #wifi connection confirmation and MQTT connection
        com.get_ssid()
        com.aws_connect()

        #Main loop execution
        loop()

    except KeyboardInterrupt:
        sys.exit()
