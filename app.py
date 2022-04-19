april_temps = [
    [ None , None , None , None , 5.0 , 6.0 , 7.0 ],
    [ 8.0  , 7.0  , 6.0  , 5.0  , 4.0 , 3.0 , 2.0 ],
    [ 1.0  , 2.0  , 3.0  , 4.0  , 5.0 , 6.0 , 7.0 ],
    [ 8.0  , 9.0  , 8.0  , 7.0  , 6.0 , 5.0 , 4.0 ],
    [ 3.0  , 2.0  , 1.0  , 2.0  , 3.0 , 4.0 , 5.0 ],
]


week = 3
day  = 2

#if april_temps[day] != None :
#    print (f"today's temperature {april_temps[week][day]:7.2} C")
#else:                                                              Doesn't work
 #   print("That's March )")

print (f"today's temperature {april_temps[week][day]:7.2} C")


week_f  = int(input("select the week for the forecast: ")) - 1
if week_f < 5  :
    print("forecast for all week :")

    for day_index in range(7):
     print(f"t: {april_temps[week_f][day_index]:7.3} C")
else:
    print(f"April don't have {week_f + 1} weeks")