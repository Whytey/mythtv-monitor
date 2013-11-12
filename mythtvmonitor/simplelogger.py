'''
Created on 06/09/2013

@author: djwhyte
'''
import logging

class SimpleLogger:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        
        self.__logger.info("Initialised")

    def handle_event(self, object, msg):
        print "SimpleLogger: %s" % msg
        return True