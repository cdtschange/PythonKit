from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocal(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))
        
factory = protocol.Factory()
factory.protocol = TSServProtocal
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()