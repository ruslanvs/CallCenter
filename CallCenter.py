calls = []

class Call( object ):
    def __init__ ( self, id = "-", callerName = "-", callerPhnNumber = "-", timeOfCall = "-", reasonForCall = "-" ):
        self.id = id
        self.callerName = callerName
        self.callerPhnNumber = callerPhnNumber
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall
        calls.append( self )
    def displayCalls( self ): # for a specific call or all calls?
        print self.id
        print self.callerName
        print self.callerPhnNumber
        print self.timeOfCall
        print "reason: ", self.reasonForCall
        return self
        

class CallCenter( object ):
    def __init__( self, callList = [], queueSize = 0 ):
        # self.instancelist = [ Call() for i in range(2) ]
        self.callList = callList
        self.queueSize = queueSize
    def addCall( self, newCall ):
        self.callList.append( newCall )
        self.queueSize = len( self.callList )
        print "Adding a call to the list..."
        print "self.callist", self.callList
        print "queue size", self.queueSize

    def removeFirstCall( self ): #this does not delete the instance itself
        self.callList.pop(0)
        self.queueSize = len( self.callList )
        print "Deleting the first call from the list..."
        print "queue size", self.queueSize

    def printNameNumber( self ):
        print "Printing the current list names and numbers..."
        for i in self.callList:
            print i.callerName, i.callerPhnNumber
        print "Queue length:", self.queueSize



call1 = Call( "1", "Peter", "123-456-7889", "2:34 pm",  "Wanted to talk to someone" )
call2 = Call( "14", "Sam", "345-452-3452", "4:54 am", "Nothing important" )
call3 = Call( "39", "Tom", "442-457-8254", "1:34 pm", "Life threatening emergency")
call4 = Call( "57", "Anna", "487-381-5281", "5:72 pm", "Wanted a recepy of a pie")

call1.displayCalls()
call2.displayCalls()
call3.displayCalls()


valleyCallCenter = CallCenter()
valleyCallCenter.addCall( call1 )
valleyCallCenter.addCall( call2 )
valleyCallCenter.addCall( call3 )
valleyCallCenter.addCall( call4 )
valleyCallCenter.printNameNumber()

valleyCallCenter.removeFirstCall()

valleyCallCenter.printNameNumber()

# print valleyCallCenter.callList[0].callerName



# print valleyCallCenter.callList

# calls[0].displayCalls()
# print calls[0]
# del calls[0]
# print call1
# print calls[0]
# del call1
# print call1

# print call1["id"]
# call1.displayCalls()

