import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ')
        city = city.title()
        if city not in ['Chicago', 'New York', 'Washington']:
            print('Please check your input!')
        else:
            print(city)
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    time_filter = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter. ')
    if time_filter.title() == 'Month':
        while True:
            day = 'all'
            month = input('Which month? January, February, March, April, May or June?')
            month = month.title()
            if month not in ['January','February','March', 'April', 'May', 'June']:
                print('Please check your input!')
            else:
                print(month)
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if time_filter.title() == 'Day':
        while True:
            month = 'all'
            day_input = input('Which day? Please type a day M, Tu, W, Th, F, Sa, Su')
            day_input = day_input.title()
            if day_input not in ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']:
                print('Please check your input!')
            else:
                weekday = {'Su':'Sunday', 'M':'Monday', 'Tu':'Tuesday', 'W':'Wednesday', 'Th':'Thursday', 'F':'Friday', 'Sa':'Saturday'}
                day = weekday[day_input]
                print(day)
                break

    if time_filter.title() == 'Both':
        while True:
            month = input('Which month? January, February, March, April, May or June?')
            month = month.title()
            if month not in ['January','February','March', 'April', 'May', 'June']:
                   print('Please check your input!')
            else:
                   print(month)
                   break
        while True:
            day_num = input('Which day? Please type your response as an integer (e.g., 1=Sunday).')
            weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            if int(day_num) not in range(1,8):
                print('Please check your input!')
            else:
                day = weekday[int(day_num) - 1]
                print(day)
                break

    if time_filter.title() == 'None':
        month = 'all'
        day = 'all'

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Frequent Start Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print('Most Frequent Trip:', popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type']= df['User Type'].dropna(axis=0)
    count_user_type = df['User Type'].value_counts()
    print('Total Count of User Type:', count_user_type)
    # TO DO: Display counts of gender
    df['Gender']= df['Gender'].dropna(axis=0)
    count_gender = df['Gender'].value_counts()
    print('Total Count of Gender:', count_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    morst_recent_year = df['Birth Year'].max()
    popular_birth_year = df['Birth Year'].mode()[0]
    print('Earliest:', earliest_year)
    print('Most Recent Year:', morst_recent_year)
    print('Birth Year:', popular_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats1(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type']= df['User Type'].fillna(0)
    count_user_type = df['User Type'].value_counts()
    print('Total Count of User Type:', count_user_type)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df):
    # Display five lines of City Data
    df = df.reset_index()
    df =df.rename({'Unnamed: 0':'Transaction ID'}, axis=1)
    row = 0
    while True:
       display_rawdata = input('Would you like to see five lines of City Data? ')
       if display_rawdata.lower() == 'yes':
           print(df.loc[row: row+4,'Transaction ID':'hour'])
           row += 5
           continue
       else:
           break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if city != 'Washington':
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_rawdata(df)

        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats1(df)
            display_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
