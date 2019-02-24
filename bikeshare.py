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
    city = None
    while city not in CITY_DATA.keys():
        city = input('Would you like to see data for Chicago, New York City or Washington?')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input('Which month? January, February, March, April, May or June? Or all?')
        month = month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satsurday', 'sunday']
    while day not in days:
        day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Satsurday, Sunday? Or all?')
        day = day.lower()

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

    CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df

def display(df):
    i = 0
    while True:
        answer = input('Do you want to display 5 more datas?/n(if you don\'t, please input \'stop\'.)')
        i = i + 5
        print(df.head(i))
        if answer.lower() == 'stop':
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Popular day:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' ~ ' + df['End Station']
    popular_route = df['Route'].mode()[0]
    print('Most Popular end station:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average Travel Time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender

    try:
        gender_list = df['Gender'].value_counts()
        print(gender_list)
    except KeyError:
        print('Gendar,No data.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = min(df['Birth Year'])
        print('Earliest Birth Year:', earliest_birth_year)
        most_recent_birth_year = max(df['Birth Year'])
        print('Most Recent Birth Year:', most_recent_birth_year)

        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', most_common_birth_year)

    except KeyError:
        print('Birth year,no data.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
