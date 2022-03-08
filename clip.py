import moviepy as mp
from moviepy.editor import *
import pathlib

#Put all files in the same directory as clip.py

archive_name = "full.mp4" #Name of the video you want to clip
clip_name = "clip.mp4" #Final name
logo_name = "watermark.png" #Logo name
slash = "\\"
start_time = "00:00:00" #Change here
end_time =  "00:00:00" #Change Here

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

path = str(pathlib.Path(__file__).parent.resolve())

full_path = path + slash + archive_name
full_path_logo = path + slash + logo_name
print(full_path)
clip = VideoFileClip(full_path)
clip = clip.subclip(get_sec(start_time), get_sec(end_time))
logo = ImageClip(full_path_logo).set_duration(clip.duration).set_pos(("center","bottom"))
final = CompositeVideoClip([clip, logo])
final_dest = path + slash + clip_name
final.write_videofile(final_dest, audio_codec='aac')