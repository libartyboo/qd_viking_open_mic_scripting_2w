import os
import sys
from datetime import datetime

today = datetime.today()

extention = str(sys.argv[1])
size = int(sys.argv[2])
size_kb = size * 1048576

date_marker = today.strftime("%Y%m%d_%H%M%S")
filename = f"py_{date_marker}_size_.{extention}"

file = open(filename, "w")
file.seek(size_kb) 
file.write("\x00")
file.close()

print("done")