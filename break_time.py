import webbrowser
import time

break_count=0
total_break=3

print(time.ctime())
while break_count<total_break:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?&v=JWUVJTnuOds")
    break_count=break_count+1
