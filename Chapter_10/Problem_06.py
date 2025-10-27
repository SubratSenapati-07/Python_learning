# NOthing happens

from random import randint
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf,fromm,to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fromm} to {to}")

    def getStatus(slf,trainNo):
        print(f"Train no: {slf.trainNo} is running on time")
    
 
    def getFare(slf,trainNo, fromm,to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fromm} to {to} is {randint(500,800)}")

s = Train(547)
s.book("Tata","Kaima")
s.getStatus(589)
s.getFare(589,"Chaina","India")