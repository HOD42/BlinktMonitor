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
pixel0Host = config.get('Hosts', 'pixel0Host')
pixel1Host = config.get('Hosts', 'pixel1Host')
pixel2Host = config.get('Hosts', 'pixel2Host')
pixel3Host = config.get('Hosts', 'pixel3Host')
pixel4Host = config.get('Hosts', 'pixel4Host')
pixel5Host = config.get('Hosts', 'pixel5Host')
pixel6Host = config.get('Hosts', 'pixel6Host')
pixel7Host = config.get('Hosts', 'pixel7Host')
pollDelay = int(config.get('Delays', 'pollDelay'))
net_scale = int(config.get('Scales', 'net_scale'))
global_bright = float(config.get('Brightness', 'global_bright'))
cpu_bright = float(config.get('Brightness', 'cpu_bright'))
disk_bright = float(config.get('Brightness', 'disk_bright'))
net_bright = float(config.get('Brightness', 'net_bright'))
cpu_error_value = float(config.get('Brightness', 'cpu_error_value'))/cpu_bright
disk_error_value = float(config.get('Brightness', 'disk_error_value'))/disk_bright
net_error_value = float(config.get('Brightness', 'net_error_value'))/net_bright

# q1 = red, q2 = blue, q3 = green ?

while True:
    # 1st query (for CPU)
    raw_nrql="SELECT average(cpuPercent) FROM SystemSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q1=QueryNewRelic(url,queryKey,queryTimeout)
    q1.get_response(queryTimeout)
    if q1.json_response == None:
        print("No q1")
        q1pixel1=q1pixel2=q1pixel3=q1pixel4=q1pixel5=q1pixel6=cpu_error_value
    else:
        # Trial for integer to override query
        try:
            int(pixel0Host)
            q1pixel0=float(pixel0Host)
        except:
            q1pixel0=ExtractValue.get_average(q1.json_response, pixel0Host)
        print("q1pixel0 ("+pixel0Host+")="+str(q1pixel0))
        
        #q1pixel1=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB01')    
        try:
            int(pixel1Host)
            q1pixel1=float(pixel1Host)
        except:
            q1pixel1=ExtractValue.get_average(q1.json_response, pixel1Host)
        print("q1pixel1 ("+pixel1Host+")="+str(q1pixel1))
        
        #q1pixel2=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB04')
        try:
            int(pixel2Host)
            q1pixel2=float(pixel2Host)
        except:
            q1pixel2=ExtractValue.get_average(q1.json_response, pixel2Host)
        print("q1pixel2 ("+pixel2Host+")="+str(q1pixel2))
        
        #q1pixel3=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTWEB02')
        try:
            int(pixel3Host)
            q1pixel3=float(pixel3Host)
        except:
            q1pixel3=ExtractValue.get_average(q1.json_response, pixel3Host)
        print("q1pixel3 ("+pixel3Host+")="+str(q1pixel3))
        
        #q1pixel4=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTAPP01')
        try:
            int(pixel4Host)
            q1pixel4=float(pixel4Host)
        except:
            q1pixel4=ExtractValue.get_average(q1.json_response, pixel4Host)
        print("q1pixel4 ("+pixel4Host+")="+str(q1pixel4))
        
        #q1pixel5=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTAPP02')
        try:
            int(pixel5Host)
            q1pixel5=float(pixel5Host)
        except:
            q1pixel5=ExtractValue.get_average(q1.json_response, pixel5Host)
        print("q1pixel5 ("+pixel5Host+")="+str(q1pixel5))
        
        #q1pixel6=ExtractValue.get_average(q1.json_response, 'OLDCSSTESTSQL01')
        try:
            int(pixel6Host)
            q1pixel6=float(pixel6Host)
        except:
            q1pixel6=ExtractValue.get_average(q1.json_response, pixel6Host)
        print("q1pixel6 ("+pixel6Host+")="+str(q1pixel6))

        try:
            int(pixel7Host)
            q1pixel7=float(pixel7Host)
        except:
            q1pixel7=ExtractValue.get_average(q1.json_response, pixel7Host)
        print("q1pixel7 ("+pixel7Host+")="+str(q1pixel7))

    # 2nd query (for disk)    
    raw_nrql="SELECT average(totalUtilizationPercent) FROM StorageSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q2=QueryNewRelic(url,queryKey,queryTimeout)
    q2.get_response(queryTimeout)
    if q2.json_response == None:
        print("No q2")
        q2pixel1=q2pixel2=q2pixel3=q2pixel4=q2pixel5=q2pixel6=disk_error_value
    else:   
        # Trial for integer to override query
        try:
            int(pixel0Host)
            q2pixel0=float(pixel0Host)
        except:
            q2pixel0=ExtractValue.get_average(q2.json_response, pixel0Host)
        print("q2pixel0 ("+pixel0Host+")="+str(q2pixel0))
            
        #q2pixel1=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB01')    
        try:
            int(pixel1Host)
            q2pixel1=float(pixel1Host)
        except:
            q2pixel1=ExtractValue.get_average(q2.json_response, pixel1Host)
        print("q2pixel1 ("+pixel1Host+")="+str(q2pixel1))
        
        #q2pixel2=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB04')
        try:
            int(pixel2Host)
            q2pixel2=float(pixel2Host)
        except:
            q2pixel2=ExtractValue.get_average(q2.json_response, pixel2Host)
        print("q2pixel2 ("+pixel2Host+")="+str(q2pixel2))
        
        #q2pixel3=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTWEB02')
        try:
            int(pixel3Host)
            q2pixel3=float(pixel3Host)
        except:
            q2pixel3=ExtractValue.get_average(q2.json_response, pixel3Host)
        print("q2pixel3 ("+pixel3Host+")="+str(q2pixel3))
        
        #q2pixel4=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTAPP01')
        try:
            int(pixel4Host)
            q2pixel4=float(pixel4Host)
        except:
            q2pixel4=ExtractValue.get_average(q2.json_response, pixel4Host)
        print("q2pixel4 ("+pixel4Host+")="+str(q2pixel4))
        
        #q2pixel5=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTAPP02')
        try:
            int(pixel5Host)
            q2pixel5=float(pixel5Host)
        except:
            q2pixel5=ExtractValue.get_average(q2.json_response, pixel5Host)
        print("q2pixel5 ("+pixel5Host+")="+str(q2pixel5))
        
        #q2pixel6=ExtractValue.get_average(q2.json_response, 'OLDCSSTESTSQL01')
        try:
            int(pixel6Host)
            q2pixel6=float(pixel6Host)
        except:
            q2pixel6=ExtractValue.get_average(q2.json_response, pixel6Host)
        print("q2pixel6 ("+pixel6Host+")="+str(q2pixel6))

        try:
            int(pixel7Host)
            q2pixel7=float(pixel7Host)
        except:
            q2pixel7=ExtractValue.get_average(q2.json_response, pixel7Host)
        print("q2pixel7 ("+pixel7Host+")="+str(q2pixel7))

    # 3rd query (for network receive and transmit = net_tot)
    raw_nrql="SELECT average(receiveBytesPerSecond) + average(transmitBytesPerSecond) as 'net_tot' FROM NetworkSample FACET hostname WHERE hostname LIKE '"+hostnames+"%' SINCE 1 minute ago"
# NOTE: The above query does not contain 'average' in the response, so need to parse for 'result' rather than 'average'.
    encoded_nrql=urllib.parse.quote_plus(raw_nrql)
    url='https://insights-api.newrelic.com/v1/accounts/'+account+'/query?nrql='+encoded_nrql
    q3=QueryNewRelic(url,queryKey,queryTimeout)
    q3.get_response(queryTimeout)
    if q3.json_response == None:
        print("No q3")
        q3pixel1=q3pixel2=q3pixel3=q3pixel4=q3pixel5=q3pixel6=net_error_value
    else:  
        # Trial for integer to override query
        try:
            int(pixel0Host)
            q3pixel0=float(pixel0Host)
        except:
            q3pixel0=ExtractValue.get_result(q3.json_response, pixel0Host)
        print("q3pixel0 ("+pixel0Host+")="+str(q3pixel0))
            
        #q3pixel1=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB01')    
        try:
            int(pixel1Host)
            q3pixel1=float(pixel1Host)
        except:
            q3pixel1=ExtractValue.get_result(q3.json_response, pixel1Host)
        print("q3pixel1 ("+pixel1Host+")="+str(q3pixel1))
        
        #q3pixel2=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB04')
        try:
            int(pixel2Host)
            q3pixel2=float(pixel2Host)
        except:
            q3pixel2=ExtractValue.get_result(q3.json_response, pixel2Host)
        print("q3pixel2 ("+pixel2Host+")="+str(q3pixel2))
        
        #q3pixel3=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTWEB02')
        try:
            int(pixel3Host)
            q3pixel3=float(pixel3Host)
        except:
            q3pixel3=ExtractValue.get_result(q3.json_response, pixel3Host)
        print("q3pixel3 ("+pixel3Host+")="+str(q3pixel3))
        
        #q3pixel4=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTAPP01')
        try:
            int(pixel4Host)
            q3pixel4=float(pixel4Host)
        except:
            q3pixel4=ExtractValue.get_result(q3.json_response, pixel4Host)
        print("q3pixel4 ("+pixel4Host+")="+str(q3pixel4))
        
        #q3pixel5=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTAPP02')
        try:
            int(pixel5Host)
            q3pixel5=float(pixel5Host)
        except:
            q3pixel5=ExtractValue.get_result(q3.json_response, pixel5Host)
        print("q3pixel5 ("+pixel5Host+")="+str(q3pixel5))
        
        #q3pixel6=ExtractValue.get_result(q3.json_response, 'OLDCSSTESTSQL01')
        try:
            int(pixel6Host)
            q3pixel6=float(pixel6Host)
        except:
            q3pixel6=ExtractValue.get_result(q3.json_response, pixel6Host)
        print("q3pixel6 ("+pixel6Host+")="+str(q3pixel6))

        try:
            int(pixel7Host)
            q3pixel7=float(pixel7Host)
        except:
            q3pixel7=ExtractValue.get_result(q3.json_response, pixel7Host)
        print("q3pixel7 ("+pixel7Host+")="+str(q3pixel7))

    # Process query results (scale/brightness)
    
    q1pixel1=q1pixel1*cpu_bright*global_bright
    q2pixel1=q2pixel1*disk_bright*global_bright
    q3pixel1=(q3pixel1/net_scale)*net_bright*global_bright

    q1pixel2=q1pixel2*cpu_bright*global_bright
    q2pixel2=q2pixel2*disk_bright*global_bright
    q3pixel2=(q3pixel2/net_scale)*net_bright*global_bright

    q1pixel3=q1pixel3*cpu_bright*global_bright
    q2pixel3=q2pixel3*disk_bright*global_bright
    q3pixel3=(q3pixel3/net_scale)*net_bright*global_bright

    q1pixel4=q1pixel4*cpu_bright*global_bright
    q2pixel4=q2pixel4*disk_bright*global_bright
    q3pixel4=(q3pixel4/net_scale)*net_bright*global_bright

    q1pixel5=q1pixel5*cpu_bright*global_bright
    q2pixel5=q2pixel5*disk_bright*global_bright
    q3pixel5=(q3pixel5/net_scale)*net_bright*global_bright

    q1pixel6=q1pixel6*cpu_bright*global_bright
    q2pixel6=q2pixel6*disk_bright*global_bright
    q3pixel6=(q3pixel6/net_scale)*net_bright*global_bright

# Modify output for BLINKT here.
    OutputToBlinkt.set_values(
                             q1pixel0,q3pixel0,q2pixel0,
                             q1pixel1,q3pixel1,q2pixel1,
                             q1pixel2,q3pixel2,q2pixel2,
                             q1pixel3,q3pixel3,q2pixel3,
                             q1pixel4,q3pixel4,q2pixel4,
                             q1pixel5,q3pixel5,q2pixel5,
                             q1pixel6,q3pixel6,q2pixel6,
                             q1pixel7,q3pixel7,q2pixel7,
                             )
                             
    time.sleep(pollDelay)

# End
