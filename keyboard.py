#!/usr/bin/env python
# coding=utf-8
from Tkinter import *
from datetime import datetime, timedelta

mapping = {
    'b': 0,
    'u': 1,
    'i': 2,
    'o': 3,
    'p': 4}

decoder = {
"#----": ["SPACE", "SPACE", "SPACE", "SPACE",  "NEW"],
"#--#-":   ["A",     "`",     "6",     "ä",     "F6"],
"#-##-":   ["B",     "{",    "LEFT",   "",    "BREAK"],
"-#-#-":   ["C",     "]",    ",",     "ĉ",    "COPY"],
"#---#":   ["D",     "/",    ".",     "",      ""],
"--#--":   ["E",     "[",    "2",     "é",     "F2"],
"##---":   ["F",     "?",    "4",     "¿",     "F4"],
"---##":   ["G",     "=",    "9",     "ĝ",     "F9"],
"##--#":   ["H",     "#",   "HOME",   "ĥ",    "HELP"],
"---#-":   ["I",     "!",    "3",     "í",     "F3"],
"-#--#":   ["J",     ";",    ":",     "ĵ",     ""],
"-####":   ["K",     "@",   "",       "",      ""],
"-##--":   ["L",     "_",     "7",    "",       "F7"],
"--###":   ["M",     ">",    "-",     "—",    "F12"],
"----#":   ["N",     ")",  "RIGHT",   "ñ",    "NUM"],
"--##-":   ["O",     "|",    "8",     "ö",     "F8"],
"####-":   ["P",     "}",    "+",   "PASTE", "PASTE"],
"##-#-":   ["Q",     "'",    "PGUP",  "",      "QUIT"],
"#-#--":   ["R",     "$",     "5",     "€",     "F5"],
"-#---":   ["S",     "*",     "1",     "ß",     "F1"],
"#-###":   ["T",     "%",     "~",    "",    ""],
"-###-":   ["U",     "&",     "0",     "ü",    "F10"],
"-#-##":   ["V",     "(",    "DOWN",   "ŭ", ""],
"#####":   ["W",     "<",    "INS",    "", ""],
"##-##":   ["X",     "\\",   "PGDOWN",  "", ""],
"#--##":   ["Y",     "^",     "UP",    "ÿ", ""],
"###--":   ["Z",     "\"",    "END",    "ŝ",    "F11"],
"--#-#": ["RESET", "RESET", "RESET", "RESET", "RESET"],
"-##-#": ["RESET", "RESET", "RESET", "RESET", "RESET"],
"#-#-#": ["RESET", "RESET", "RESET", "RESET", "RESET"],
"###-#": ["RESET", "RESET", "RESET", "RESET", "RESET"]
    }

downstack = 0

chord = ['-', '-', '-', '-', '-']
lastdown = datetime.now()
arpeggio = False

def print_chord():
    global chord
    global arpeggio
    if arpeggio:
        print "".join(chord) + " ARPEGGIO"
    else:
        c = "".join(chord)
        if c in decoder:
            print c + " " + decoder[c][0]
        else:
            print c

def add_to_chord(character):
    global chord
    chord[mapping[character]] = '#'

def clear_chord():
    global chord
    chord = ['-', '-', '-', '-', '-']

def keyup(e):
    if not e.char in mapping:
        return
    global downstack
    downstack -= 1
    if downstack == 0:
        print_chord()
        clear_chord()
        global arpeggio
        arpeggio = False
    now = datetime.now()
    millis = (now - lastdown).microseconds / 1000
    # print millis
    # print 'up', e.char

def keydown(e):
    if not e.char in mapping:
        return
    global downstack
    global lastdown
    downstack += 1
    now = datetime.now()
    millis = (now - lastdown).microseconds / 1000
    if downstack == 2 and millis > 80:
        global arpeggio
        # print "ARPEGGIO"
        arpeggio = True

    add_to_chord(e.char)
    lastdown = datetime.now()
    # print cc datetime.now()
    # print 'down', e.char

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()
