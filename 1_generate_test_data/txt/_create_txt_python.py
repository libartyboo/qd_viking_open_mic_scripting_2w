import os
from datetime import datetime

today = datetime.today()

date_marker = today.strftime("%Y%m%d_%H%M%S")
filename = f"test_{date_marker}_py_.txt"

file = open(filename, "w")
file.write(f"text_{date_marker}")
file.close()

print("done")
