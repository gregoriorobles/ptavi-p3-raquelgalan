#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#Raquel Galán Montes

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


if __name__ == "__main__":

    try:
        fich = open(sys.argv[1], "r")
    except IOError:
        print ("no encuentra el file.smil")
        raise SystemExit
    except IndexError:
        print ("Usage: python karaoke.py file.smil")
        raise SystemExit

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    lista = cHandler.get_tags()

    for elemento in lista:
        print elemento["name"]
        for etiq in elemento:
            if etiq != "name":
                if elemento[etiq]:
                    print "\t", etiq, "=", '"', elemento[etiq], '"'
        print "\n"
