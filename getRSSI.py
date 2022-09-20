from bluepy.btle import Scanner, DefaultDelegate, ScanEntry, BluepyHelper
from bluepy import btle
import time
import pickle

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

class GetRSSI:
    def __init__(self,timer = 10):
        print("Connecting")
        
        try:
            self.get_values(timer)
        except btle.BTLEDisconnectError:
            pass 

    def get_values(self,timer):
        while True:
            scanner = Scanner().withDelegate(ScanDelegate())
            scanner.clear()
            scanner.start(passive=False)
            print("Initialising ...")
            try:
                scanner.process(timer)
            except Exception as e :
                print(e)
            finally:
                print("Finished")
                scanner.stop()
            time.sleep(0.2)    

while True:
    GetRSSI()    

"""

    def process(self, timeout=10.0):
        if self._helper is None:
            raise BTLEInternalError(
                                "Helper not started (did you call start()?)")
        start = time.time()
        while True:

            self.dump_to_file(self.rssi_list)
            resp = self._waitResp(['scan', 'stat'], 5)
            if resp is None:
                print("Scanning off")
                break

            respType = resp['rsp'][0]
            if respType == 'stat':
                # if scan ended, restart it
                if resp['state'][0] == 'disc':
                    self._mgmtCmd(self._cmd())

            elif respType == 'scan':
                # device found
                addr = binascii.b2a_hex(resp['addr'][0]).decode('utf-8')
                addr = ':'.join([addr[i:i+2] for i in range(0,12,2)])
                if not ((addr == "a0:d7:95:d5:d5:c3") or (addr == "3f:40:da:d8:15:01") or (addr == "69:2f:52:1b:ee:32)):
                    time.sleep(0.2)
                    continue
                if addr in self.scanned:
                    dev = self.scanned[addr]
                else:
                    dev = ScanEntry(addr, self.iface)
                    self.scanned[addr] = dev
                isNewData = dev._update(resp)
                if self.delegate is not None:
                    self.delegate.handleDiscovery(dev, (dev.updateCount <= 1), isNewData)
                if dev.addr == "a0:d7:95:d5:d5:c3":
                    self.rssi_list[0] = dev.rssi
                    print("1")
                if dev.addr == "3c:24:9f:d0:91:c3":
                    self.rssi_list[1] = dev.rssi       
                    print("2")
                if dev.addr == "10:b4:d7:70:ff:e6":
                    self.rssi_list[2] = dev.rssi       
                    print("3")    
                print("update")    
                 
            else:
                raise BTLEInternalError("Unexpected response: " + respType, resp)    

    def dump_to_file(self,rssi_list):
        try:
            outfile= open("/usr/local/lib/python3.8/dist-packages/bluepy/rssi_values.txt","wb")
            pickle.dump(self.rssi_list,outfile)
            outfile.close()
        except Exception as e:
            print(e)    

"""

"""

    def process(self, timeout=10.0):
        if self._helper is None:
            raise BTLEInternalError(
                                "Helper not started (did you call start()?)")
        start = time.time()
        while True:
            if timeout:
                remain = start + timeout - time.time()
                if remain <= 0.0: 
                    break
            else:
                remain = None
            resp = self._waitResp(['scan', 'stat'], remain)
            if resp is None:
                break

            respType = resp['rsp'][0]
            if respType == 'stat':
                # if scan ended, restart it
                if resp['state'][0] == 'disc':
                    self._mgmtCmd(self._cmd())

            elif respType == 'scan':
                # device found
                addr = binascii.b2a_hex(resp['addr'][0]).decode('utf-8')
                addr = ':'.join([addr[i:i+2] for i in range(0,12,2)])
                if addr in self.scanned:
                    dev = self.scanned[addr]
                else:
                    dev = ScanEntry(addr, self.iface)
                    self.scanned[addr] = dev
                isNewData = dev._update(resp)
                if self.delegate is not None:
                    self.delegate.handleDiscovery(dev, (dev.updateCount <= 1), isNewData)
                 
            else:
                raise BTLEInternalError("Unexpected response: " + respType, resp)

"""
