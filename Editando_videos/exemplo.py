"""moviepy-1.0.3"""

from moviepy.editor import *
from moviepy.video import fx


# Puxo o video tem de ter h aqui       V
clip = VideoFileClip("Editando_videos\heport.mp4")

# Acelera o video em 2x
clip = fx.all.speedx(clip , factor=None , final_duration=150)

# Rendenizo o video
clip.write_videofile("Editando_videos\heport2.mp4")
