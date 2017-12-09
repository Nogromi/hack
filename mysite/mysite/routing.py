from channels.routing import route
channel_routing = [
    route('http.request', 'selforder.consumers.http_request_consumer')
]