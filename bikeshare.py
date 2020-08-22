import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ' '
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Would you like to analyze data for chicago, new york city, or washington?')
        if city in ['chicago', 'washington','new york city']:
            break
        else:
            print("Please, enter a valid city")          
            
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ' '
    while month not in MONTHS:
         month = input("Please, choose the month you want to analyze from january to june or you can type 'all'.")
         if month in MONTHS:
            break
         else:
            print("your input should be either: january, february, march, april, may, june or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ' '
    while day not in DAYS:
         day = input("Please, choose the day you want to analyze from monday to sunday or you can type 'all'.")
         if day in DAYS:
            break
         else:
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
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
     df = df[df['day_of_week'] == day]   
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0])))
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is {}.".format(common_day))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print("The most common start hour is {}.".format(common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common start station is {}.".format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most common end station is {}.".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most most frequent combination of start station and end station trip is {}.".format(frequent_combination))  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: {}.".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: {}.".format(mean_time))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types:")
    print(df['User Type'].value_counts())    
    
    if city != 'washington':
        # Display counts of gender
        print("The counts of gender:")
        print(df['Gender'].value_counts())
       
def Birth_Year(df):    
 if 'Birth_Year' != 'washington':
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['birth_year'].min())
    most_recent = int(df['birth_year'].max())
    most_common = int(df['birth_year'].mode())
    print("The earliest birth is: {}.".format(earliest))
    print(" The most recent birth is: {}.".format(most_recent))
    print(" The most common birth is: {}.".format(most_common))
    print("\nThis took %s seconds." % (time.time() - start_time))
 else:
        print("Data is not available in your city")
print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
