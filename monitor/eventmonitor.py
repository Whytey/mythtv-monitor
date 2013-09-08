'''
Created on 07/09/2013

@author: djwhyte
'''

from MythTV import BEEventConnection, BEEventMonitor
from MythTV.static import BACKEND_SEP
from gi.repository import GObject
import logging
import re

class SystemEventMonitor(GObject.GObject, BEEventMonitor):
    
    SYSTEM_EVENT = "system_event"
    
    __gsignals__ = {
        SYSTEM_EVENT: (GObject.SIGNAL_RUN_LAST, None, (GObject.TYPE_PYOBJECT,))
    }

    
    def __init__(self):
        GObject.GObject.__init__(self)

        BEEventMonitor.__init__(self, '192.168.0.100', False, True, None)
        self.__logger = logging.getLogger("monitor.Blah")
        self.__logger.info("Initialised")


    def _neweventconn(self):
        return BEEventConnection(self.host, self.port, 'test-script', level = 3)

    def eventMonitor(self, event=None):
        if event is None:
            return re.compile('.*SYSTEM_EVENT')
        self.__logger.debug("Got a raw event: %s" % event)

        payload = event.split(BACKEND_SEP)[1].split(" ")[1:]
        
        msg = {}
        msg[u"type"] = payload[0]
        for i in range(1, len(payload[1:]), 2):
            msg[payload[i].lower()] = payload[i+1]
            
        self.__logger.debug("Got a payload of: %s" % msg)
        
        self.emit(self.SYSTEM_EVENT, msg)
