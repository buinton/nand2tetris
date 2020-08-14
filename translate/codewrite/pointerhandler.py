#!/usr/bin/python3

def pointer(pointer):
    def pointerswitch(arg):
        switch = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
            "temp": "TMP"}
        return switch.get(arg)

    out = pointerswitch(pointer)
    return out
