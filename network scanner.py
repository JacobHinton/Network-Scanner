###Network scanner

import scapy.all as scapy
import argparse

def getArguments():
    argument = argparse.ArgumentParser()
    argument.add_argument('-t', '--target', dest='target', help='Target Address(es)')
    target = argument.parse_args()

    if !target.target:
        argument.error("[-] Invalid input: value must be a valid address")
    return target

def scanTarget(ip):
    arpFrame = scapy.ARP(pdst = ip)
    broadcastFrame= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpPacket = broadcastFrame/arpFrame
    deviceList = scapy.srp(broadcastFrame, timeout = 1, verbose = False)[0]
    output=[]
    for i in range(len(deviceList)):
        TempDict = {"ip" : deviceList[i][1].psrc, "mac" : deviceList[i][1].hwsrc}
        result.append(tempDict)
    return output

if __name__ == "__main__":
    ip = getArguments()
    output = scanTargets(ip)
    for pc in output:
        print("{}\t{}".format(pc["ip"], pc["mac"]))
