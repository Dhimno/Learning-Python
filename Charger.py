max_watt_charger = 120
max_watt_phone = 120
if max_watt_charger > max_watt_phone or max_watt_phone > max_watt_charger:
    optimal_charging = min(max_watt_phone, max_watt_charger)
    print('Charging at ' + str(optimal_charging) + 'Watt')
else:
    print('Charging at maximum speed')