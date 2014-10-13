#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#Raquel Galán Montes

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os


class KaraokeLocal():

    def __init__(self):
        self.formato = ""
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open('karaoke.smil'))
        self.lista = cHandler.get_tags()

    def __str__(self):
        salida = ""
        for elemento in self.lista:
            salida += elemento["name"]
            for etiq in elemento:
                if etiq != "name":
                    if elemento[etiq]:
                        salida += "\t" + etiq + '="' + elemento[etiq] + '"'
            salida += "\n"
        return salida

    def do_local(self):
        for elemento in self.lista:
            for etiq in elemento:
                if etiq != "name":
                    if elemento[etiq]:
                        if etiq == "src":
                            if elemento[etiq].find("http://") == 0:
                                recurso = elemento[etiq]
                                os.system("wget -q " + recurso)
                                descargado = elemento[etiq].split("/")[-1]
                                elemento[etiq] = descargado
if __name__ == "__main__":

    try:
        fich = open(sys.argv[1], "r")
    except IOError:
        print ("no encuentra el file.smil")
        raise SystemExit
    except IndexError:
        print ("Usage: python karaoke.py file.smil")
        raise SystemExit

    Karaoke = KaraokeLocal()
    print Karaoke
    Karaoke.do_local()
    print Karaoke
