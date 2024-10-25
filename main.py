from xml.etree.ElementPath import ops
import pygame as pg
import math
import random

from app import App
from aquarium import Aquarium
from fish import Fish
from sprite import Sprite

app = App ( size = (800,800),fps= 30 ,name = "aboba")
app.start()
app.main_loop()
