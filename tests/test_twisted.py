import sys
sys.path.append('../')

import traceback as tb
from tests import *
from txsuds import WebFault
from txsuds.client import Client
from twisted.internet import reactor
from twisted.internet import defer

setup_logging()


@defer.inlineCallbacks
def main():
    try:
        url = 'https://sec.neurofuzz-software.com/paos/genSSHA-SOAP.php?wsdl'
        print 'Test @ ( %s )' % (url)
        client = Client(url)
        yield client.connect()
        print client
        res = yield client.service.genSSHA('hello', 'sha1')
        print res
    except WebFault, f:
        print f
        print f.fault
    except Exception, e:
        print e
        tb.print_exc()

    print '\nFinished'
    reactor.stop()


reactor.callLater(0, main)
reactor.run()
