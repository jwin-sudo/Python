inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow:
        total_inches = total_inches + inches_snow[inches]

    print("Total snowfall inches: ", str(total_inches))


print_total_snowfall(inches_snow)
inches_snow["Thursday"] = int(
    input('How many inches of snow fell on Thursday? '))
print_total_snowfall(inches_snow)
