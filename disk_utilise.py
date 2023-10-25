from os import path, stat
import shutil
path= r"C:\Users\91700\Downloads\Youtube Element\Audio"
stat= shutil.disk_usage(path)
BytesPerGB = 1024 * 1024 * 1024
print("Disk Usage of ", path, "is", (stat.used)/BytesPerGB, end='\n')