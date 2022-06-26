import os
import moviepy.editor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

dest_path = ".\\tracked_frames"
targ_path = "./dataset"
interval = 3

for class_title in os.listdir(dest_path):
    # print(class_title)
    for activity in os.listdir(dest_path + '//' + class_title):
        # print(activity)
        for video_title in os.listdir(dest_path + '//' + class_title + '//' +activity):
            start_time = 0
            end_time = start_time + interval
            count = 0
            video_path = dest_path + '//' + class_title + '//' +activity + '//' +video_title
            video_title = video_title[0:-4]
            clip = moviepy.editor.VideoFileClip(video_path)
            print(f'{class_title} - {activity} - {video_title}')
            while (start_time<clip.duration):
                exec(f'ffmpeg_extract_subclip(video_path,start_time,end_time, targetname="{targ_path}/{class_title}/{video_title}_{count}.avi")') 
                count+=1
                start_time = end_time
                end_time = start_time + interval