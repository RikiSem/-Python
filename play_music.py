import os

class Music:
    def __init__(self, path):
        self.path = path
    
    def getPath(self):
        return self.path
    
    def showMusicInPath(self):
        FilePath = open("path.sgg","w")
        FilePath.write(self.path)
        FilePath.close()
        files = []
        for root, dirs, file in os.walk(self.path):
            for mics in file:
                if(".mp3" in mics):
                    files.append(mics)
        return files

class PlayList:
    def __init__(self, name):
        self.name = name
        self.Misclist = []
    
    def AddInPlayList(self, TrackName):
        self.Misclist.append(TrackName)

    def ShowList(self):
        return self.Misclist