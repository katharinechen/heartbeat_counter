import threading
import thread 
import time 
import sys 

bpm = 0 
last_save_time = 0
array = []
user_input = [None]

def print_bpm():
    """Return bpm every 10 seconds"""
    global bpm 
    threading.Timer(10.0, print_bpm).start()
    print "BPM: {0}bpm".format(bpm) 
    #for testing 
    print array 

def getting_input():
    """Check output stream for beats every second. If there is a beat, user_input is *beat*, otherwise None"""
    global user_input 
    threading.Timer(1.0, getting_input).start()
    return user_input 

def beats_counter(user_input): 
    """Calculator rolling bpm every second and set it to the global variable"""
    global bpm 
    global array 
    threading.Timer(1.0, beats_counter).start() 

    if len(array) == 60:
        array.pop([0])

    try:
        array.append(0)
    except user_input == "*beat*": 
        array.append(1)
    bpm = 60 * sum(array) / len(array)

if __name__ == "__main__":
    getting_input()
    print_bpm()
    beats_counter()