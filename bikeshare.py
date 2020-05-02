import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #user inputs a city
    print("Please specify a city: Chicago, New York, or Washington.")
    while True:
        city= input("> ")
        city = city.lower()
        if ("chicago" in city) or ("new york" in city) or ("washington" in city):
            print()
            break
        else:
            print("Please choose one of the following: Chicago, New York, or Washington.")

    # have user input a month
    print("Please specify a month, between January and June.")
    print("... or type \"All\" for all months:")
    while True:
        month = input("> ")
        month = month.lower()
        if ("all" in month):
            month = "0"
            break
        elif ("january" in month):
            month = "1"
            break
        elif ("february" in month):
            month = "2"
            break
        elif ("march" in month):
            month = "3"
            break
        elif ("april" in month):
            month = "4"
            break
        elif ("may" in month):
            month = "5"
            break
        elif ("june" in month):
            month = "6"
            break
        else:
            print("Not a valid month.  Please try again.")
    print()

    #have user specify a day of the year, via integer
    print("Please specify a day of the week in the following format:")
    print("Mon = 0, Tues = 1, Wed = 2, Thurs = 3, Fri = 4, Sat = 5, Sun = 6")
    print("... or, type 7 to choose ALL DAYS")
    while True:
        try:
            raw_day = int(input(">"))
            if (raw_day >= 0) and (raw_day <= 7):
                day = str(raw_day)
                break
            else:
                print("Please choose a date by typing a number between 0 - 7.")
        except ValueError:
            print("That's not a number")
    print()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #convert city value to *.csv file name
    if ("new york" in city):
        city = ("new_york_city.csv")
    elif ("chicago" in city):
        city = ("chicago.csv")
    else:
        city = ("washington.csv")
    df = pd.read_csv(city)

    #convert start time and end time to panda datetime objects
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])

    #filter by month
    if ("0" not in month):
        df = df[df["Start Time"].dt.month == int(month)]

    #filter by dayofweek
    if ("7" not in day):
        df = df[df["Start Time"].dt.dayofweek == int(day)]

    print()

    return df

def view_bike_data(df):
    """Displays raw data for the user to view, if they choose"""

    print("Would you like to view the 5 lines of raw data? Please type Yes or No")
    a = 0
    to_view = "y"
    while (to_view in ["y", "yes"]) and (a+5 < df.shape[0]):
        to_view = input("> ")
        to_view = to_view.lower()
        if ("y" in to_view) or ("yes" in to_view):
            print(df.iloc[a:a+5])
            a += 5
            print("Would you like to see more? (Yes or No)")
        elif ("n" in to_view) or ("no" in to_view):
            print()
            break
        else:
            print("Please enter Yes or No")

    print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    comm_month = int(df["Start Time"].dt.month.mode())
    print("The most common month of travel is: ", comm_month, "\n")

    # TO DO: display the most common day of week
    comm_day = int(df["Start Time"].dt.dayofweek.mode())
    print("The most common day of travel is: ", comm_day, "\n")

    # TO DO: display the most common start hour
    comm_hour = int(df["Start Time"].dt.hour.mode())
    print("The most common Start Hour is: ", comm_hour, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_start_station = (df["Start Station"].mode())
    print("The most commonly used Start Station was:\n", comm_start_station, "\n")

    # TO DO: display most commonly used end station
    comm_end_station = df["End Station"].mode()
    print("The most commonly used End Station was:\n", comm_end_station, "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip"] = df["Start Station"] + " - " + df["End Station"]
    comm_trip = df["Trip"].mode()
    print("the most frequent combination of Start Station and End Station Trip was:\n", comm_trip, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["Travel Time"] = df["End Time"] - df["Start Time"]
    travel_time_sum = df["Travel Time"].sum()
    print("Total Travel time during this period was: ", travel_time_sum, "\n")

    # TO DO: display mean travel time
    travel_time_mean = df["Travel Time"].mean()
    print("The Mean Travel Time during this period was: ", travel_time_mean, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("Here are the counts of User Types:\n", user_type_count, "\n")

    # TO DO: Display counts of gender
    gender_count = df["Gender"].value_counts()
    print("Here are the counts of Gender:\n", gender_count, "\n\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    min_birth_year = df["Birth Year"].min()
    print("The earliest birth year is: ", int(min_birth_year), "\n")
    max_birth_year = df["Birth Year"].max()
    print("The most recent birth year is:", int(max_birth_year), "\n")
    comm_birth_year = df["Birth Year"].mode()
    print("The most common birth year is:", int(comm_birth_year), "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_bike_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
