# coding=utf-8
from moviepy.editor import *


# In what follows we import MoviePy, we open the video file, we select the part between 1’22.65 (1 minute 22.65 seconds)
#  and 1’23.2, reduce its size (to 30% of the original) and save it as a GIF:
clip = (VideoFileClip("frozen_trailer.mp4").subclip((1,22.65), (1, 23.2)).resize(0.8))
clip.write_gif("use_your_head.gif")
