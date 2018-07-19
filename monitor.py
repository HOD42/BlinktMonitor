#!/usr/bin/python3
from outputToBlinkt import OutputToBlinkt
import json
import time
import urllib.parse
from queryNewRelic import QueryNewRelic
from extractValue import ExtractValue
import configparser
config=configparser.ConfigParser()
config.read("config.txt")
account = config.get('NewRelic', 'account')
queryKey = config.get('NewRelic', 'queryKey')
queryTimeout = float(config.get('NewRelic', 'queryTimeout'))
hostnames = config.get('Hosts', 'hostnames')
pollDelay = int(config.get('Delays', 'pollDelay'))
net_scale = int(config.get('Scales', 'net_scale'))
global_bright = float(config.get('Brightness', 'global_bright'))
cpu_bright = float(config.get('Brightness', 'cpu_bright'))
disk_bright = float(config.get('Brightness', 'disk_bright'))
net_bright = float(config.get('Brightness', 'net_bright'))
cpu_error_value = float(config.get('Brightness', 'cpu_error_value'))/cpu_bright
disk_error_value = float(config.get('Brightness', 'disk_error_value'))/disk_bright
net_error_value = float(config.get('Brightness', 'net_error_value'))/net_bright

while True:
    # 1st query (for CPU)
    raw_nrql="SELECT average(cpuPercent) FROM SystemSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q1=QueryNewRelic(url,queryKey,queryTimeout)
    q1.get_response(queryTimeout)
    if q1.json_response == None:
        print("No q1")
        cpu_web01=cpu_web04=cpu_web02=cpu_app01=cpu_app02=cpu_sql01=cpu_error_value
    else:
        cpu_web01=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB01')
        print("cpu_web01="+str(cpu_web01))
        cpu_web04=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB04')
        print("cpu_web04="+str(cpu_web04))
        cpu_web02=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB02')
        print("cpu_web02="+str(cpu_web02))
        cpu_app01=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTAPP01')
        print("cpu_app01="+str(cpu_app01))    
        cpu_app02=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTAPP02')
        print("cpu_app02="+str(cpu_app02))   
        cpu_sql01=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTSQL01')
        print("cpu_sql01="+str(cpu_sql01))

    # 2nd query (for disk)    
    raw_nrql="SELECT average(totalUtilizationPercent) FROM StorageSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q2=QueryNewRelic(url,queryKey,queryTimeout)
    q2.get_response(queryTimeout)
    if q2.json_response == None:
        print("No q2")
        disk_web01=disk_web04=disk_web02=disk_app01=disk_app02=disk_sql01=disk_error_value
    else:   
        disk_web01=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB01')
        print("disk_web01="+str(disk_web01))
        disk_web04=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB04')
        print("disk_web04="+str(disk_web04))
        disk_web02=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB02')
        print("disk_web02="+str(disk_web02))
        disk_app01=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTAPP01')
        print("disk_app01="+str(disk_app01))
        disk_app02=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTAPP02')
        print("disk_app02="+str(disk_app02))
        disk_sql01=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTSQL01')
        print("disk_sql01="+str(disk_sql01))

    # 3rd query (for network receive and transmit = net_tot)
    raw_nrql="SELECT average(receiveBytesPerSecond) + average(transmitBytesPerSecond) as 'net_tot' FROM NetworkSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
# NOTE: The above query does not contain 'average' in the response, so need to parse for 'result' rather than 'average'.
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q3=QueryNewRelic(url,queryKey,queryTimeout)
    q3.get_response(queryTimeout)
    if q3.json_response == None:
        print("No q3")
        net_tot_web01=net_tot_web04=net_tot_web02=net_tot_app01=net_tot_app02=net_tot_sql01=net_error_value
    else:  
        net_tot_web01=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB01')
        print("net_tot_web01="+str(net_tot_web01))
        net_tot_web04=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB04')
        print("net_tot_web04="+str(net_tot_web04))
        net_tot_web02=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB02')
        print("net_tot_web02="+str(net_tot_web02))
        net_tot_app01=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTAPP01')
        print("net_tot_app01="+str(net_tot_app01))
        net_tot_app02=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTAPP02')
        print("net_tot_app02="+str(net_tot_app02))
        net_tot_sql01=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTSQL01')
        print("net_tot_sql01="+str(net_tot_sql01))

    # Process query results (scale/brightness)
    
    cpu_web01=cpu_web01*cpu_bright*global_bright
    disk_web01=disk_web01*disk_bright*global_bright
    net_tot_web01=(net_tot_web01/net_scale)*net_bright*global_bright

    cpu_web04=cpu_web04*cpu_bright*global_bright
    disk_web04=disk_web04*disk_bright*global_bright
    net_tot_web04=(net_tot_web04/net_scale)*net_bright*global_bright

    cpu_web02=cpu_web02*cpu_bright*global_bright
    disk_web02=disk_web02*disk_bright*global_bright
    net_tot_web02=(net_tot_web02/net_scale)*net_bright*global_bright

    cpu_app01=cpu_app01*cpu_bright*global_bright
    disk_app01=disk_app01*disk_bright*global_bright
    net_tot_app01=(net_tot_app01/net_scale)*net_bright*global_bright

    cpu_app02=cpu_app02*cpu_bright*global_bright
    disk_app02=disk_app02*disk_bright*global_bright
    net_tot_app02=(net_tot_app02/net_scale)*net_bright*global_bright

    cpu_sql01=cpu_sql01*cpu_bright*global_bright
    disk_sql01=disk_sql01*disk_bright*global_bright
    net_tot_sql01=(net_tot_sql01/net_scale)*net_bright*global_bright

# Modify output for BLINKT here.
    OutputToBlinkt.set_values(1,1,1,
                             cpu_web01,net_tot_web01,disk_web01,
                             cpu_web04,net_tot_web04,disk_web04,
                             cpu_web02,net_tot_web02,disk_web02,
                             cpu_app01,net_tot_app01,disk_app01,
                             cpu_app02,net_tot_app02,disk_app02,
                             cpu_sql01,net_tot_sql01,disk_sql01,
                             25*global_bright,25*global_bright,25*global_bright)
                             
    time.sleep(pollDelay)

# End
