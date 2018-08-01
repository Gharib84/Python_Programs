from datetime import datetime
import locale

def arr_date():
    while True:
        date_str = input(" Enter Your Arrival Date (YYYY-MM-DD) ? ")
        try:
            arr_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(" Invalid Date PLease Try Again")
            continue
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arr_date < today:
            print("arrival date must be today or later try again")
            continue
        else:
            return arr_date

def get_departure_date(arrival_date):
    while True:
        dep_str = input(" Enter Departure Date (YYYY-MM-DD) ? ")
        try:
            departure_date = datetime.strptime(dep_str,"%Y-%m-%d" )
        except ValueError:
            print(" Invalid Date PLease Try Again ")
            continue
        if departure_date <= arrival_date:
            print(" Departure Date Must Be after arrival date ")
        else:
            return departure_date


def main():
    print(" The Hotel Reservation Program\n")
    while True:
        arriaval_date = arr_date()
        departure_date = get_departure_date(arriaval_date)
        print()

        rate = 85.0
        rate_message = ""
        if arriaval_date.month == 8:
            rate = 105.0
            rate_message = " heigh seasons "
            total_nights = (departure_date - arriaval_date).days
            coast = rate * total_nights
            date_format = "%B, %d, %Y"
            locale.setlocale(locale.LC_ALL, "")
            print("\tarrival date: " ,  arriaval_date.strftime(date_format))
            print("\tDeparture Date: " , departure_date.strftime(date_format))
            print("\tNightly Rates: ", locale.currency(rate), rate_message)
            print("\tTotal Nieghts: ", total_nights)
            print("\tTotal Price",  locale.currency(coast))
            print()

            result = input(" continue (y/n) ")
            if result.lower() != "y":
                print("bye")
                break
                

if __name__ == '__main__':
    main()
    
            


    



            

            

    
