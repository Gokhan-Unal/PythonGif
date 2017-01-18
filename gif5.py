
from moviepy.editor import *

def time_symetrize(clip):
    #returns the clip played forwards the n backwards
    return concatenate([clip, clip.fx(vfx.time_mirror)])

clip = (VideoFileClip("frozen_trailer.mp4", audio=False).subclip(36.5, 36.9).resize(0.5).crop(x1=189, x2=433).fx(time_symetrize))

clip.write_gif('sven.gif', fps=15, fuzz=2)