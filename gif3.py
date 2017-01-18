from moviepy.editor import *

#
# Many GIF makers like to freeze some parts of the GIF to reduce
# the file size and/or focus the attention on one part of the animation.
#
# In the next GIF we freeze the left part of the clip. To do so we take a
# snapshot of the clip at t=0.2 seconds, we crop this snapshot to only
# keep the left half, then we make a composite clip which superimposes the cropped snapshot on the original clip:


anna_olaf = (VideoFileClip("frozen_trailer.mp4").subclip(87.9, 88.1).speedx(0.5).resize(.4))

snapshot = (anna_olaf.crop(x2=anna_olaf.w / 2)  # remove right half
                .to_ImageClip(0.2) # snapshot of the clip at t = 0.2s
                .set_duration(anna_olaf.duration))

composition = CompositeVideoClip([anna_olaf, snapshot])
composition.write_gif('anna_olaf.gif', fps=15)