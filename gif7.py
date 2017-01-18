from moviepy.editor import *


castle = (VideoFileClip("frozen_trailer.mp4", audio=False).subclip(22.8, 23.2).speedx(0.2).resize(.6))

d = castle.duration

castle = castle.crossfadein(d / 2)

composition = (CompositeVideoClip([castle, castle.set_start(d/2), castle.set_start(d)]).subclip(d/2, 3*d/2))

composition.write_gif('castle.gif', fps=5, fuzz=5)