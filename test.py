import re
import subprocess


COMMAND_PREFIX_DURATION = 'youtube-dl --get-duration'
def getDuration(url):
    duration = subprocess.getstatusoutput(COMMAND_PREFIX_DURATION +" "+ url)[1]
    print("视频长度：",duration)
    return duration

getDuration("https://www.youtube.com/watch?v=N0z4jQlz6zY")