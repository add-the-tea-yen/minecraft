from ursinanetworking import *

Server = UrsinaNetworkingServer("localhost", 25565)

@Server.event
def HelloFromClient(Client, Content):
    print(f"{Client} says : {Content}")

while True:
    Server.process_net_events()