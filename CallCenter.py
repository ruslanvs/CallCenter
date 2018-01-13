class Call( object ):
    def __init__ ( self, id = "-", callerName = "-", callerPhnNumber = "-", timeOfCall = "-", reasonForCall = "-" ):
        self.id = id
        self.callerName = callerName
        self.callerPhnNumber = callerPhnNumber
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall
    def displayCalls( self, id ): # for a specific call or all calls?
        print self.id
        print self.callerName
        print self.callerPhnNumber
        print self.timeOfCall
        print self.reasonForCall
        

class CallCenter( object ):
    def __init__( self, *calls, queueSize ):
        self.calls = Call
        self.queueSize = queueSize
        print self.calls
    def add( self ):
        pass

call1 = Call( "1", "Peter", "123-456-7889", "wanted to talk to someone" )
call2 = Call()
call3 = Call()

print Call