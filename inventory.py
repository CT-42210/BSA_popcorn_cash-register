import sys
import time
import os
import setup
import easter_eggs

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def spreadsheet():
    pop_type =  open("pop_type.txt")
    pop_number = open("pop_quantity.txt")
    pop_price = open("pop_price.txt")

