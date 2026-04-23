from helium import *
import time


day = time.ctime(time.time()).split(" ")[2]


file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_last_bodies_parameters.txt"

strokes_to_read = str()
last_day_parameter = str()

with open(file=file, mode="rt", encoding="utf-8") as f:
    
    strokes_to_read = f.readlines()

    last_day_parameter = strokes_to_read[1].rstrip().split("=")[1].split(".")[2]

    if last_day_parameter == "":
        last_day_parameter = 1

file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_bodies_parameters.txt"

strokes_to_read = str()
day_parameter = str()

with open(file=file, mode="rt", encoding="utf-8") as f:
    
    strokes_to_read = f.readlines()

    day_parameter = strokes_to_read[1].rstrip().split("=")[1].split(".")[2]


day = int(day)
day_parameter = int(day_parameter)
last_day_parameter = int(last_day_parameter)

is_parsed = False

if day_parameter == last_day_parameter == day:
    
    is_parsed = True

if is_parsed:
    print("NASA parsing was")
else:
    print("NASA parsing not was")
