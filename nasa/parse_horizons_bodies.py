from helium import *
import json
import time


file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_bodies_parameters.txt"

id = str()

with open(file=file, mode="rt", encoding="utf-8") as f:
    
    strokes_to_read = f.readlines()
    id = strokes_to_read[0]  

id = int(id.split("=")[1])
body_id = f"{id}"
date_first = "2020-01-01"
date_last = "2020-12-20"


start_chrome(f"https://ssd.jpl.nasa.gov/api/horizons.api?format=json&" \
f"COMMAND='{body_id}'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&" \
f"EPHEM_TYPE='OBSERVER'&CENTER='500@399'&" \
f"START_TIME='{date_first}'&STOP_TIME='{date_last}'&STEP_SIZE='1%20d'&QUANTITIES='1,9,20,23,24,29'")

all_texts = find_all(Text())
tle_text = all_texts[0].value
tle_text_obj = json.loads(tle_text)

print("Results")
print(tle_text_obj["result"])

kill_browser()


DICT = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
}

id = int(body_id)

day = time.ctime(time.time()).split(" ")[2]
month = DICT[time.ctime(time.time()).split(" ")[1].upper()]
year = time.ctime(time.time()).split(" ")[len(time.ctime(time.time()).split(" "))-1]

if int(day) < 10:
    day = "0" + str(day)

year = str(int(year))


file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_last_bodies_parameters.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
        
    first_stroke = f"id={id}\n"
    second_stroke = f"day={year}.{month}.{day}\n"
    third_stroke = "\n"

    strokes_to_write = [first_stroke, second_stroke, third_stroke]

    f.writelines(strokes_to_write)
