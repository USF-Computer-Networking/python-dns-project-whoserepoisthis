""" 
project1.py
Name : Edward Ra
- Finds DNS address of domain
- Finds the hostname of an IP address (REVERSE DNS)
- usage: python ./project1.py -a google.com
- usage: python ./project1.py -p 198.27.234.184

"""
import argparse
import socket
import dns.resolver

def DNS(type, domainName):
    if type == "A":
        print("  Address")
    if type == "PTR":
        print("     IP")
    dnsresolver = dns.resolver.Resolver()
    query = dnsresolver.query(domainName, type)
    for rdata in query:
        print(rdata)

def main():

    arg = argparse.ArgumentParser()

    arg.add_argument('-a', '--address', default=False, help="Returns DNS Address")
    arg.add_argument('-i', '--ptr', default=False, help="Returns hostname when given ip")

    args = arg.parse_args()

    try:
        if args.address is not False:
            dnsresolver = dns.resolver.Resolver()
            query = dnsresolver.query(args.address, "A")
            for data in query:
                print("ip = {}".format(data))
        elif args.ptr is not False:
            dnsresolver = dns.resolver.Resolver()
            query = dnsresolver.query('.'.join(reversed(args.ptr.split("."))) + ".in-addr.arpa", "PTR")
            for data in query:
                print("hostname = {}".format(data))
        else:
            arg.print_help()
    except:
        print "error with entry"
        
main()