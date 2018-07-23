class ExtractValue():
    def __init__(self, json_packet, hostname):
        self.json_packet=json_packet
        self.hostname=hostname
        self.value=None

    def get_average(json_packet, hostname):
        import json
        for this_hostname in json_packet['facets']:
            if this_hostname['name']==hostname:
                value=this_hostname['results'][0]['average']
                return(value)
        # Not found hostname
        print("get_average didn't find hostname="+hostname)
        return(None)

# Differentiate between 'average' and 'result' responses

    def get_result(json_packet, hostname):
        import json
        for this_hostname in json_packet['facets']:
            if this_hostname['name']==hostname:
                value=this_hostname['results'][0]['result']
                return(value)
        # Not found hostname
        print("get_result didn't find hostname="+hostname)
        return(None)
        
