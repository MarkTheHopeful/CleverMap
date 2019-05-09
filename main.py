#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
from os import path


class Dictionary:
    container = dict()

    def __init__(self, filename):
        try:
            inpt = open(filename, "r")
            n = int(inpt.readline())
            for i in range(n):
                opr, count = inpt.readline().split("$")
                count = int(count)
                self.container[opr] = count
            inpt.close()
        except IOError:
            print("It seems like file", filename, "is not found. Dictionary is initialized empty.")
        except TypeError:
            print("Well, check your dictionary file", filename, "Dictionary is initialized empty.")
        except Exception:
            print("O_O Enter debug mode please, something is really wrong.")

    def save(self, filename):
        if path.exists(filename):
            src = path.realpath(filename)
            head, tail = path.split(src)
            print("path:" + head)
            print("file:" + tail)
            dst = src + ".bak"
            shutil.copy(src, dst)
            try:
                outp = open(filename, "w")
                print(len(self.container), file=outp)
                for pair in self.container:
                    print(pair, sep="$", file=outp)
                outp.close()
            except IOError:
                print("Saving failed. Your backup file is", dst)
        else:
            outp = open(filename, "w")
            print(len(self.container), file=outp)
            for pair in self.container:
                print(pair, sep="$", file=outp)
            outp.close()
