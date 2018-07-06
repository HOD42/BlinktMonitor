class ExtractValue():
    def __init__(self, json_packet, hostname):
        self.json_packet=json_packet
        self.hostname=hostname
        self.value=None

    def get_value(json_packet, hostname):
        import json
        #print("Start parsing hostnames looking for ",end='')
        #print(hostname)
        for this_hostname in json_packet['facets']:
            #print("this_hostname=",end='')
            #print(this_hostname['name']+"...")
            if this_hostname['name']==hostname:
                #print("value=",end='')
                value=this_hostname['results'][0]['average']
                #print(value)
                return(value)
        # Not found hostname
        print("Not found!")
        return(None)
        
