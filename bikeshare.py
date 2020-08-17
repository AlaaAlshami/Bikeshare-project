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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to analyze chicago, new york city or washington?")
    while city not in CITY_DATA.keys():
            print('Please, type a valid city!')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Please, choose the month you want to analyze from january to june or you can type 'all'.")
    while month not in MONTHS:
            print("your input should be either: january, february, march, april, may, june or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input("Please, choose the day you want to analyze from monday to sunday or you can type 'all'.")
    while day not in DAYS:
            print("your input should be either: monday, tuesday, wednesday, thursday, friday, saturday, sunday or 'all'.")
                  
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:k
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = int(df['month'].mode()[0])
    print("The most common month is {}.".format(common_month))
    
    # TO DO: display the most common day of week
    common_day = int(df['day'].mode()[0])
    print("The most common day of week is {}.".format(common_day))

    # TO DO: display the most common start hour
    common_hour = int(df['hour'].mode()[0])
    print("The most common start hour is {}.".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = int(df['Start Station'].mode()[0])
    print("The most common start station is {}.".format(common_start))

    # TO DO: display most commonly used end station
    common_end = int(df['End station'].mode()[0])
    print("The most common end station is {}.".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station','End Station']).size().idmax() 
    print("The most most frequent combination of start station and end station trip is {}.".format(frequent_combination))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)          
          
def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: {}.").format(total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: {}.").format(mean_time)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types:")
    print(df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    print("The counts of gender:")
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    most_recent =  int(df['Birth Year'].max())
    most_common = int(df['Birth Year'].mode()[0])
    print("The earliest birth is: {}.".format(earliest))
    print(" The most recent birth is: {}.".format(most_recent))
    print(" The most common birth is: {}.".format(most_common))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
