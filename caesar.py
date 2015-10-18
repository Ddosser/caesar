#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import base64


__author__ = "Ddosser"
__version__ = "v0.1"

LETTERS = "".join([chr(i) for i in xrange(32,127)])

class Caesar(object):
    """docstring for Caesar"""
    def __init__(self):
        super(Caesar, self).__init__()
        
    def caesar_encode(self, raw_str, key):
        code = ""
        for c in raw_str:
            if c in LETTERS:
                num = LETTERS.find(c)
                num += key
                if num >= len(LETTERS):
                    num -= len(LETTERS)
                elif num < 0:
                    num += len(LETTERS)
                code += LETTERS[num]
            else:
                code += c
        return code

    def caesar_decode(self, en_str):
        plain = ""
        for key in range(1, len(LETTERS)):
            for c in en_str:
                if c in LETTERS:
                    num = LETTERS.find(c)
                    num -= key
                    if num < 0:
                        num += len(LETTERS)
                    plain += LETTERS[num]
                else:
                    plain += c
            plain += '   [' + str(key) + ']\n'

        return plain

def usage():
    print '*'*60
    print "Usage: python caesar.py -[e <-k key>|d] [-f <file>] [-o <file>]"
    print "-e       escape input string or file."
    print "-k       the key of Caesar."
    print "-d       caesar string."
    print "-f       input from file."
    print "-o       output to file."
    print "-h       for help."
    print '*'*60
    exit(0)

def main():
    args = sys.argv
    ed = Caesar()

    if len(args) < 2 or '-h' in args:
        usage()

    if '-e' in args:
        if '-k' not in args:
            usage()
        key = int(args[3])
        flag = False
    elif '-d' in args:
        flag = True
    else:
        usage()

    if '-f' in args:
        in_file = args[4]
        r = open(in_file, "r")
        raw_str = r.read()
        r.close()
    else:
        raw_str = raw_input("请输入：")

    if flag:
        result = ed.caesar_decode(raw_str)
    else:
        result = ed.caesar_encode(raw_str, key)

    if '-o' in args:
        out_file = args[6]
        w = open(out_file, "w")
        w.write(result.encode('utf-8'))
        w.close()
    else:
        print flag and "解密结果：" or "加密结果："
        print "\033[1;32m" + result + "\033[0m"
       
if __name__ == '__main__':
    main()

