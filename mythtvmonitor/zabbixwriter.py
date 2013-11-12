'''
Created on 08/08/2013

@author: djwhyte
'''
import logging
import subprocess

class ZabbixWriter():
    
    __ZABBIX_KEY = "mythtv.system.event"
    __ZABBIX_HOST = "mythBE1"

    
    def __init__(self):
        
        self.__logger = logging.getLogger(__name__)
        
        self.__zabbix_server = "192.168.0.100"
        self.__logger.info("Initialised")

        
    def handle_system_event(self, object, msg):
        self.__logger.debug("Handling system event")
        
        
        self.__logger.debug("Calling zabbix_sender with system event: %s"  % msg)
        try:
            process_args = ['zabbix_sender', '-z', self.__zabbix_server, '-s', self.__ZABBIX_HOST, '-k', self.__ZABBIX_KEY, '-o', str(msg)]
            self.__logger.debug("Calling subprocess: %s" % process_args)
            subprocess.call(process_args)
        except OSError, e:
            self.__logger.exception(e)
            
        return True
