protocols = {
    "ICMP": 1,
    "UDP": 2,
    "RTM": 3,
    "IGMP": 4,
    "DNS": 5,
    "TCP": 6
}

class NetworkScheduler:
    def __init__(self, protocol):
        self.protocol = protocol

    def rcv(self, name, payload):
        
