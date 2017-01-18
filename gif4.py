import moviepy.video.tools.drawing as dw
from moviepy.editor import *


anna_kris = (VideoFileClip("frozen_trailer.mp4", audio=False).subclip((1, 38.15), (1, 38.5)).resize(.5))

# coordinates p1, p2 define the edges of the mask
mask = dw.color_split(anna_kris.size, p1=(445, 20), p2=(345, 275), grad_width=5)

snapshot = (anna_kris.to_ImageClip().set_duration(anna_kris.duration).set_mask(ImageClip(mask, ismask=True)))

composition = CompositeVideoClip([anna_kris, snapshot]).speedx(0.2)

composition.write_gif('anna_kris.gif', fps=15, fuzz=3)