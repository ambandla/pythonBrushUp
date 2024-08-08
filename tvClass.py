class tv():
    def __init__(self):
        self.powerState = "off"
        self.muteState = "on"
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.currentChannel = 2
        self.currentVolume = 0
        self.maxVolume = 100
        self.nChannels = len(self.channelList)

    def power(self):
        self.powerState = 'off' if self.powerState == 'on' else 'on'        
        # if self.powerState == "off":
        #     self.powerState = "on"
        # else:
        #     self.powerState = "off"
        return self.powerState
    
    def volumeUp(self):
        if self.muteState == 'on':
            self.muteState = 'off'
            return self.currentVolume
        if self.currentVolume + 1 > self.maxVolume:
            print('Volume cannot exceed', self.maxVolume)
            return None
        self.currentVolume += 1
        return self.currentVolume
    
    def volumeDown(self):
        if self.muteState == 'on':
            self.muteState = 'off'
            return self.currentVolume
        if self.currentVolume - 1 < 0:
            print('Volume cannot be less than 0')
            return None
        self.volumeDown -= 1
        return self.currentVolume
    
    def channelUp(self):
        if self.currentChannel == self.channelList[-1]:
            self.currentChannel = self.channelList[0]
        else:
            self.currentChannel = self.channelList[self.channelList.index(self.currentChannel) + 1]
        return self.currentChannel
    
    def channelDown(self):
        if self.currentChannel == self.channelList[0]:
            self.currentChannel = self.channelList[-1]
        else:
            self.currentChannel = self.channelList[self.channelList.index(self.currentChannel) - 1]
        return self.currentChannel
    def mute(self):
        self.muteState = 'on' if self.muteState == 'off' else 'off'
        return self.muteState

    def setChannel(self, channel):
        if channel not in self.channelList:
            print('Channel not available')
            return None
        self.currentChannel = channel
        return self.currentChannel
    

tv1= tv()
print (tv1.channelList)
print (tv1.muteState)
print (tv1.powerState)
print(tv1.currentChannel)
tv1.channelUp()
print(tv1.currentChannel)
tv1.channelUp()
print(tv1.currentChannel)
tv1.channelDown()
print(tv1.currentChannel)