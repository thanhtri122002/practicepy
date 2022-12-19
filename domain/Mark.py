class Mark:
    def __init__(self,sid,mark,cid)->None:
        self.__sid =sid
        self.__mark = mark
        self.__cid = cid
    
    def setSid(self,sid):
        self.__sid = sid
    
    def getSid(self):
        return self.__sid

    def setMark(self,mark):
        self.__mark = mark
    
    def getMark(self):
        return self.__mark
    
    def setCid(self,cid):
        self.__cid = cid
    
    def getCid(self):
        return self.__cid
    
    