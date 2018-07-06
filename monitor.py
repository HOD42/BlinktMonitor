#!/usr/bin/python3
import blinkt
import json
import time
import urllib.parse
from queryNewRelic import QueryNewRelic
from extractValue import ExtractValue

bright=2.5
cpu_bright=0.5
disk_bright=1
net_bright=0.25
delay=30
net_scale=300000/100
account='YourAccount'
queryKey='YourQueryKey'
hostnames='OLDCSSTEST'

while True:
    raw_nrql="SELECT average(cpuPercent) FROM SystemSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q1=QueryNewRelic(url,queryKey)
    q1.get_response()
    if q1.json_response == None:
        print("No q1")
        cpu_web01=0
        cpu_web04=0
        cpu_web02=0
        cpu_app01=0
        cpu_app02=0
        cpu_sql01=0
    else:
        cpu_web01=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTWEB01')
        print("cpu_web01=",end='')
        print(cpu_web01)

        cpu_web04=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTWEB04')
        print("cpu_web04=",end='')
        print(cpu_web04)

        cpu_web02=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTWEB02')
        print("cpu_web02=",end='')
        print(cpu_web02)

        cpu_app01=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTAPP01')
        print("cpu_app01=",end='')
        print(cpu_app01)
    
        cpu_app02=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTAPP02')
        print("cpu_app02=",end='')
        print(cpu_app02)
    
        cpu_sql01=ExtractValue.get_value(q1.json_response, 'OLDCSSTESTSQL01')
        print("cpu_sql01=",end='')
        print(cpu_sql01)

    #
    
    raw_nrql="SELECT average(totalUtilizationPercent) FROM StorageSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q2=QueryNewRelic(url,queryKey)
    q2.get_response()
    if q2.json_response == None:
        print("No q2")
        disk_web01=0
        disk_web04=0
        disk_web02=0
        disk_app01=0
        disk_app02=0
        disk_sql01=0
    else:   
        disk_web01=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTWEB01')
        print("disk_web01=",end='')
        print(disk_web01)

        disk_web04=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTWEB04')
        print("disk_web04=",end='')
        print(disk_web04)

        disk_web02=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTWEB02')
        print("disk_web02=",end='')
        print(disk_web02)

        disk_app01=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTAPP01')
        print("disk_app01=",end='')
        print(disk_app01)
    
        disk_app02=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTAPP02')
        print("disk_app02=",end='')
        print(disk_app02)
    
        disk_sql01=ExtractValue.get_value(q2.json_response, 'OLDCSSTESTSQL01')
        print("disk_sql01=",end='')
        print(disk_sql01)

    #

    raw_nrql="SELECT average(receiveBytesPerSecond) FROM NetworkSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q3=QueryNewRelic(url,queryKey)
    q3.get_response()
    if q3.json_response == None:
        print("No q3")
        netr_web01=0
        netr_web04=0
        netr_web02=0
        netr_app01=0
        netr_app02=0
        netr_sql01=0
    else:  
        netr_web01=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTWEB01')
        print("netr_web01=",end='')
        print(netr_web01)

        netr_web04=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTWEB04')
        print("netr_web04=",end='')
        print(netr_web04)

        netr_web02=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTWEB02')
        print("netr_web02=",end='')
        print(netr_web02)

        netr_app01=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTAPP01')
        print("netr_app01=",end='')
        print(netr_app01)
    
        netr_app02=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTAPP02')
        print("netr_app02=",end='')
        print(netr_app02)
    
        netr_sql01=ExtractValue.get_value(q3.json_response, 'OLDCSSTESTSQL01')
        print("netr_sql01=",end='')
        print(netr_sql01)

    #
    
    raw_nrql="SELECT average(transmitBytesPerSecond) FROM NetworkSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q4=QueryNewRelic(url,queryKey)
    q4.get_response()
    if q4.json_response == None:
        print("No q4")
        nett_web01=0
        nett_web04=0
        nett_web02=0
        nett_app01=0
        nett_app02=0
        nett_sql01=0
    else:     
        nett_web01=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTWEB01')
        print("nett_web01=",end='')
        print(nett_web01)

        nett_web04=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTWEB04')
        print("nett_web04=",end='')
        print(nett_web04)

        nett_web02=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTWEB02')
        print("nett_web02=",end='')
        print(nett_web02)

        nett_app01=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTAPP01')
        print("nett_app01=",end='')
        print(nett_app01)
    
        nett_app02=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTAPP02')
        print("nett_app02=",end='')
        print(nett_app02)
    
        nett_sql01=ExtractValue.get_value(q4.json_response, 'OLDCSSTESTSQL01')
        print("nett_sql01=",end='')
        print(nett_sql01)

    #
    
    cpu_web01=cpu_web01*cpu_bright
    disk_web01=disk_web01*disk_bright
    net_tot_web01=netr_web01+nett_web01
    net_tot_web01=(net_tot_web01/net_scale)*net_bright
    print("NET_TOT_WEB01=",end='')
    print(net_tot_web01)

    cpu_web04=cpu_web04*cpu_bright
    disk_web04=disk_web04*disk_bright
    net_tot_web04=netr_web04+nett_web04
    net_tot_web04=(net_tot_web04/net_scale)*net_bright
    print("NET_TOT_WEB04=",end='')
    print(net_tot_web04)

    cpu_web02=cpu_web02*cpu_bright
    disk_web02=disk_web02*disk_bright
    net_tot_web02=netr_web02+nett_web02
    net_tot_web02=(net_tot_web02/net_scale)*net_bright
    print("NET_TOT_WEB02=",end='')
    print(net_tot_web02)

    cpu_app01=cpu_app01*cpu_bright
    disk_app01=disk_app01*disk_bright
    net_tot_app01=netr_app01+nett_app01
    net_tot_app01=(net_tot_app01/net_scale)*net_bright
    print("NET_TOT_APP01=",end='')
    print(net_tot_app01)

    cpu_app02=cpu_app02*cpu_bright
    disk_app02=disk_app02*disk_bright
    net_tot_app02=netr_app02+nett_app02
    net_tot_app02=(net_tot_app02/net_scale)*net_bright
    print("NET_TOT_APP02=",end='')
    print(net_tot_app02)

    cpu_sql01=cpu_sql01*cpu_bright
    disk_sql01=disk_sql01*disk_bright
    net_tot_sql01=netr_sql01+nett_sql01
    net_tot_sql01=(net_tot_sql01/net_scale)*net_bright
    print("NET_TOT_SQL01=",end='')
    print(net_tot_sql01)

# Modify output for BLINKT here.

    print("- - - - - - - - BLINKT! - - - - - - - -")
    blinkt.set_all(1, 0, 0)
    blinkt.show()
    time.sleep(0.05)
    blinkt.set_all(0, 1, 0)
    blinkt.show()
    time.sleep(0.05)
    blinkt.set_all(0, 0, 1)
    blinkt.show()
    time.sleep(0.05)



# Show minimal brightness on first LED
    blinkt.set_pixel(0,1,1,1)
    blinkt.set_pixel(1,cpu_web01,net_tot_web01,disk_web01)
    blinkt.set_pixel(2,cpu_web04,net_tot_web04,disk_web04)
    blinkt.set_pixel(3,cpu_web02,net_tot_web02,disk_web02)
    blinkt.set_pixel(4,cpu_app01,net_tot_app01,disk_app01)
    blinkt.set_pixel(5,cpu_app02,net_tot_app02,disk_app02)    
    blinkt.set_pixel(6,cpu_sql01,net_tot_sql01,disk_sql01)
# Show what 33% looks like on last LED
    blinkt.set_pixel(7,33*bright,33*bright,33*bright)
    blinkt.show()

    time.sleep(delay)

# End
