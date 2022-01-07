import spidev as SPI
import ST7789
import RPi.GPIO as GPIO
import time
import os
import sys
import Queue
import sh
import time
import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep 

import threading
c = threading.Condition()

RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

sudo /usr/local/bin/checkra1n
