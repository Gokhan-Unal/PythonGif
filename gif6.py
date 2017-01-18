from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.0.3-Q16\convert.exe"})

def time_symetrize(clip):
    #returns the clip played forwards the n backwards
    return concatenate([clip, clip.fx(vfx.time_mirror)])


olaf = (VideoFileClip("frozen_trailer.mp4", audio=False).subclip((1, 21.6), (1,22.1)).resize(.5).speedx(0.5).fx(time_symetrize))

text = (TextClip("In my nightmares\nI see rabbits.", fontsize=30, color='white', font="Amiri-Bold", interline=-25).set_pos((20, 190)).set_duration(olaf.duration))

composition = CompositeVideoClip([olaf, text])
composition.write_gif('olaf.gif', fps=10, fuzz=2)