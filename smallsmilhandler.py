#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#Raquel Galán Montes

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.etiq = {"root-layout", "region", "img", "audio", "textstream"}
        self.atrib = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
            }

    def startElement(self, name, attrs):
        dic = {}
        if name in self.etiq:
            dic["name"] = name
            for i in self.atrib[name]:
                dic[i] = attrs.get(i, "")
            self.lista.append(dic)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

    print cHandler.get_tags()
