import os
import time

initial_dir = os.listdir(r"E:/Temp")
dir_path = r"E:/Temp"

while True:

  new_dir = os.listdir(r"E:/Temp")
  if(initial_dir != new_dir):
    for _ in range(len(new_dir)):
      if(new_dir[_] not in initial_dir):
        if(new_dir[_][len(new_dir[_])-4:] == ".txt"):        
            os.rename("{}/{}".format(dir_path,new_dir[_]),"{}/{}".format(dir_path,"Text Files/{}".format(new_dir[_])))
            print("{}/{}".format(dir_path,new_dir[_]))
            print("{}/{}".format(dir_path,"Text Files/{}".format(new_dir[_])))

  time.sleep(1)
