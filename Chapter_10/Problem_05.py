from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fromm,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fromm} to {to}")

    def getStatus(self,trainNo):
        print(f"Train no: {self.trainNo} is running on time")
    
 
    def getFare(self,trainNo, fromm,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fromm} to {to} is {randint(500,800)}")

s = Train(547)
s.book("Tata","Kaima")
s.getStatus(589)
s.getFare(589,"Chaina","India")