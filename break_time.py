import time
import webbrowser

total_breaks = 3
break_count = 0


while(break_count <  total_breaks):
        time.sleep(600)
        print("the current time :"+time.ctime())
        webbrowser.open("https://www.youtube.com/watch?v=PT2_F-1esPk")
        break_count = break_count + 1
