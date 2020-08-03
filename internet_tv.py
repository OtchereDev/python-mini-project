class NetworkDevice():
    def __init__(self, mac_no, cache_size):
        self.mac_no = mac_no
        self.cache_size = cache_size
    def transmit(self):
        print("Requesting download...")
    def receive(self, data_size):
        if data_size > self.cache_size:
            print("Receipt Aborted : packet size too large")
            return False
        else:
            print("Received data packet")
            return True

class Television():
    def __init__(self, screen, volume_tunner):
        self.screen = screen
        self.volume_tunner = volume_tunner
    def display_video(self):
        print("displaying your video on a "+ self.screen)
    def change_volume(self,amount):
        if amount < 0:
            print("Reducing sound by "+str(-amount) + "unit(s)")
        elif amount > 0:
            print("Increasing sound by "+ str(amount)+ "unit(s)")


class InternetTv(NetworkDevice, Television):
    def __init__(self,screen, volume_tunner, mac_no, cache_size,cpu):
        self.cpu = cpu
        NetworkDevice.__init__(self, mac_no, cache_size)
        Television.__init__(self, screen, volume_tunner)
    def watch_tele(self,data_size):
        NetworkDevice.transmit(self)
        isrecieved = NetworkDevice.receive(self,data_size)
        if isrecieved:
            Television.display_video(self)
        
a_tv=InternetTv("LED screen","digital tunner","845-2a",2,"qualcom")
a_tv.watch_tele(1)
a_tv.change_volume(-1)
a_tv.watch_tele(3)
