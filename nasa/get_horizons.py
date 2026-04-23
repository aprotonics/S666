from helium import *


file = "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_last_bodies_parameters.txt"

strokes_to_read = str()
last_day_parameter = str()
horizons_body_id = str()

with open(file=file, mode="rt", encoding="utf-8") as f:
    
    strokes_to_read = f.readlines()
    last_day_parameter = strokes_to_read[1].rstrip().split("=")[1].split(".")[2]
    horizons_body_id = strokes_to_read[0].rstrip().split("=")[1]

horizons_body_id = int(horizons_body_id)


file = f"/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/" \
        f"scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/horizons/horizons_bodies_{horizons_body_id}.txt"

stroke_number = int()

with open(file=file, mode="rt", encoding="utf-8") as f:
    
    strokes_to_read = f.readlines()

    for i in range(len(strokes_to_read)):
        stroke_number = i
        stroke = strokes_to_read[i]

        substr_index = stroke.find(str(horizons_body_id))

        if substr_index >= 0:

            break

print(f" {strokes_to_read[stroke_number].split("          ")[1].strip()}")
