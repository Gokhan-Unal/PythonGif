from moviepy.editor import *
import pygame
import numpy
import cv2

kris_sven = (VideoFileClip("frozen_trailer.mp4").subclip((1, 13.4), (1, 13.9)).resize(0.5).crop(x1=145, x2=400))

kris_sven.write_gif("kris_sven.gif")