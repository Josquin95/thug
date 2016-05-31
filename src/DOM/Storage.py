#!/usr/bin/env python
#
# Storage.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import logging
from collections import OrderedDict
from .W3C.Events.StorageEvent import StorageEvent

log = logging.getLogger("Thug")


class Storage(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(Storage, self).__init__(*args, **kwargs)

    @property
    def length(self):
        return len(self)

    def key(self, index):
        if index > self.length:
            return None

        return self.keys()[index - 1]

    def getItem(self, key):
        try:
            return super(Storage, self).__getitem__(key)
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.setItem(key, value)

    def setItem(self, key, value):
        oldvalue = getattr(self, key, None)
        super(Storage, self).__setitem__(key, value)

        evtObject = StorageEvent('storage', log.DFT.window)
        evtObject.initStorageEvent('storage',
                                   False,
                                   False,
                                   key, 
                                   oldvalue, 
                                   value, 
                                   log.DFT.window.url, 
                                   self)
        
        log.DFT.handle_window_storage_event('onstorage', evtObject)

    def __delitem__(self, key):
        self.removeItem(key)

    def removeItem(self, key):
        oldvalue = getattr(self, key, None)
        super(Storage, self).__delitem__(key)

        evtObject = StorageEvent('storage', log.DFT.window)
        evtObject.initStorageEvent('storage',
                                   False,
                                   False,
                                   key, 
                                   oldvalue, 
                                   None, 
                                   log.DFT.window.url, 
                                   self)
   
        log.DFT.handle_window_storage_event('onstorage', evtObject)

    def clear(self):
        super(Storage, self).clear()
        self.__init__()

        evtObject = StorageEvent('storage', log.DFT.window)
        evtObject.initStorageEvent('storage',
                                   False,
                                   False,
                                   None,
                                   None,
                                   None, 
                                   log.DFT.window.url,
                                   self)
   
        log.DFT.handle_window_storage_event('onstorage', evtObject)