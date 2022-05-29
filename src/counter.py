#!/usr/bin/python
# -*- coding: utf-8 -*-import time
import datetime
import parameters as para


class Count:
    def __init__(self):
        return

    #timedeltaが15時間以上だったらemergency_signal=1をIoT coreに飛ばす
    def time_count(self, t0, sig, pub_flag, alert_flag, alert_type): 
        #timedelta取得
        delta = datetime.datetime.now() - t0 
        td_seconds = int(delta.total_seconds())
        #print(t0, sig, pub_flag, alert_flag, alert_type, td_seconds)

        if sig == 1:
            t0 = datetime.datetime.now()
            alert_flag = 0
            alert_type = 0
            pub_flag = 0
        #delta_calculation()#トリガー：⊿t>54000秒(15時間)を判定する
        elif alert_type == 0 and alert_flag == 0 and td_seconds >= 54000:
            t0 = datetime.datetime.now()
            alert_flag = 1
            alert_type = 1
            pub_flag = 0
        #センサーに反応がない場合、以後1時間おきにSNS topicへpublish
        elif alert_type >= 1 and alert_flag == 1 and td_seconds >= 3600:
            t0 = datetime.datetime.now()
            alert_flag = 1
            alert_type = 2
            pub_flag = 0
                    
        return t0, pub_flag, alert_flag, alert_type


    #If the sensor has HI output, increment the counter
    def motion_count(self, sig, motion_count):
            
        if sig == 1:
            motion_count = motion_count + 1

        return motion_count