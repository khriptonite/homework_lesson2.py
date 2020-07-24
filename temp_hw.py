
##DATA
unit_symbol = "℃"
unit_name = "celsius"

# meteo data 4 times a day 
locality_name = "Chisinau"
date          = "24.07.2020"
temp_mo = 10
temp_no = 30
temp_ev = 25
temp_ni = 6

## calculations
temp_avg  = (temp_mo + temp_no + temp_ev + temp_ni) / 4
temp_min  = min(temp_mo , temp_no , temp_ev , temp_ni)
temp_max  = max(temp_mo , temp_no , temp_ev , temp_ni)

is_hot_day = temp_no >= 25
is_cold_night = temp_ni < 10
not_cold_night = temp_ni >= 14   #HW3: temp de la care noaptea ar putea fi socotita calda
hot_all_day = is_hot_day == not_cold_night #HW3: am folostit acest operator de comparare pt a afla dacă task-urile sunt corecte

## presentation
print("#" * 60)
print("locality: " + locality_name)
print("date:     " + date)
print("avg Temp: " + str(round(temp_avg, 1)) + unit_symbol) #HW2: am adaugat functia round pt avg temp, am limitat zecimalele la 1
print("min Temp: " + str(temp_min) + unit_symbol)
print("max Temp: " + str(temp_max) + unit_symbol)
print("Hot day?\n\t " + str(is_hot_day))
print("Cold night?\n\t " + str(is_cold_night))  
print("Hot during 24h?\n\t " + str(hot_all_day)) #HW3: raspunsul la intrebare
print("#" * 60)
