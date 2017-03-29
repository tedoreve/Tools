# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:22:15 2017

@author: tedoreve
"""

from moviepy.editor import VideoFileClip, concatenate_videoclips

data = VideoFileClip('../data/Gintama.mp4')

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip1 = data.subclip(50,60)
clip2 = data.subclip(100,110)

final_clip = concatenate_videoclips([clip1,clip2])
## Generate a text clip (many options available ! )
#txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
#txt_clip = txt_clip.set_pos('center').set_duration(10)
# 
## Overlay the text clip above the first clip
#final_clip = CompositeVideoClip([clip, txt_clip])
 
# write the result to a file in any format
final_clip.to_videofile("myHolidays_edited.avi",fps=60, codec='mpeg4')