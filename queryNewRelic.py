class QueryNewRelic():   
    def __init__(self, url, queryKey, queryTimeout):
        self.url=url
        self.queryKey=queryKey
        self.queryTimeout=queryTimeout
        self.json_response=None

    def get_response(self, queryTimeout):
        from urllib.request import urlopen, Request
        import json
        url=self.url
        queryKey=self.queryKey
        queryTimeout=self.queryTimeout
        request_url=Request(url)
        request_url.add_header('Accept', 'application/json')
        request_url.add_header('X-Query-Key', queryKey)

        try:
            data = urlopen(request_url, timeout=queryTimeout).read()
        except:
            print("Request failed!")
            return None
            
        self.json_response=json.loads(data.decode())
        return self.json_response
