from helium import *
import time


day = time.ctime(time.time()).split(" ")[2]

file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_last_bodies_parameters.txt"

last = str()

with open(file=file, mode="rt", encoding="utf-8") as f:
    last = f.readlines()

    last_id = last[0]
    last_day = last[1]
    last_month = last[1]
    last_year = last[1]

    last_id = last_id.rstrip()
    last_day = last_day.rstrip()
    last_month = last_month.rstrip()
    last_year = last_year.rstrip()
    
    last_id = last_id.split("=")[1]
    last_day = last_day.split("=")[1].split(".")[2]
    last_month = last_month.split("=")[1].split(".")[1]
    last_year = last_year.split("=")[1].split(".")[0]
    
today = day

if today > last_day:

    last_id = int(last_id)

    day = int(last_day) + 1
    month = int(last_month)
    year = int(last_year)

    if day < 10:
        day = "0" + str(day)

    if month < 10:
        month = "0" + str(month)

    year = str(year)

    file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_bodies_parameters.txt"

    with open(file=file, mode="wt", encoding="utf-8") as f:
        
        first_stroke = f"id={last_id+1}\n"
        second_stroke = f"day={year}.{month}.{day}\n"
        third_stroke = "\n"

        strokes_to_write = [first_stroke, second_stroke, third_stroke]

        f.writelines(strokes_to_write)

else:
    
    file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_bodies_parameters.txt"

    with open(file=file, mode="wt", encoding="utf-8") as f:

        first_stroke = f"id={last_id}\n"
        second_stroke = f"day={last_year}.{last_month}.{last_day}\n"
        third_stroke = "\n"

        strokes_to_write = [first_stroke, second_stroke, third_stroke]

        f.writelines(strokes_to_write)
