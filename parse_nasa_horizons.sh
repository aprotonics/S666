#!/bin/bash

bodies_parameters_path="/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/nasa_bodies_parameters.txt"

i=""

while IFS= read -r line; do
 
  i="${line:3:3}"
  
  break

done < $bodies_parameters_path

echo " "

python3 "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts/nasa/parse_horizons_bodies.py" > "/home/time_traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/horizons/horizons_bodies_${i}.txt"

echo " "

