import moviepy as mp
from moviepy.editor import *
import pathlib
from pytube import YouTube
from pytube.cli import on_progress

#Change Youtube Link here
yt_link = "https://www.youtube.com/watch?v=P8sCHqcvpmQ&ab_channel=MBL-MovimentoBrasilLivre"
#Change Time Here
start_time = "00:00:30" 
end_time =  "00:00:50"
#Logo name
logo_name = "watermark.png"
#Final Name
clip_name = "clip.mp4" 
#Just some stuff
slash = "\\"
path = str(pathlib.Path(__file__).parent.resolve())

#CORE
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

print("YouTube video download in progress....\n")
archive_name = "full.mp4"
yt = YouTube(yt_link,on_progress_callback=on_progress)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path = path , filename = archive_name)

full_path = path + slash + archive_name
full_path_logo = path + slash + logo_name
print("Cutting video....")
clip = VideoFileClip(full_path)
clip = clip.subclip(get_sec(start_time), get_sec(end_time))
logo = ImageClip(full_path_logo).set_duration(clip.duration).set_pos(("center","bottom"))
final = CompositeVideoClip([clip, logo])
final_dest = path + slash + clip_name
final.write_videofile(final_dest, audio_codec='aac')