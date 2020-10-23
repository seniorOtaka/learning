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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago","new york city","washington"]
    cities_names = ', '.join(cities)

    while True:
        city = input("Cities List ({})\n Enter City name from the list above: ".format(cities_names))
        city = city.lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)
    months = ["all","january","february","march","april","may","june","july","august","september","october","november","december"]
    months_names = ', '.join(months)
    while True:
        month = input("Months list ({})\n Enter month name from the list above: ".format(months_names))
        month = month.lower()
        if month in months:
            break

     # get user input for day of week (all, monday, tuesday, ... sunday) 
    week_days = ["all","monday","tuesday","wednesday","thuresday","friday","saturday","sunday"]   
    week_days_names = ', '.join(week_days)       
    while True:
        day = input("Week days list ({})\nEnter day name from the list above: ".format(week_days_names))
        day = day.lower()
        if day in week_days:
            break
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    # display the most common start hour       
    print('Most Common Start Hour:', popular_hour)
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month (from 1 to 12)
    popular_month = df['month'].value_counts().idxmax()
    # display the most common month
    print('Most Common Month:', popular_month)
    # extract week day from the Start Time column to create a weekday column
    df['week_day'] = df['Start Time'].dt.day_name()
    # find the most common weekday 
    popular_week_day = df['week_day'].value_counts().idxmax()
    # display the most common week day       
    print('Most Common week day:', popular_week_day)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()
    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()
    # display most frequent combination of start station and end station trip
    # most_frequent_stations_combination = df['Start Station','End Station'].value_counts().idxmax()
    df["Trip"] = "from"+" " + df["Start Station"]+" "+ "to" +" "+ df["End Station"]
    most_frequent_stations_combination = df['Trip'].mode()[0]

    print("Most used Start Station: ",most_commonly_used_start_station)
    print("Most used End Station: ",most_commonly_used_end_station)
    print("Most frequent combination of start station and end station trip: ",most_frequent_stations_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("total travel time: ",total_travel_time)
    print("mean travel time: ",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types:\n",user_types)
    
    # Display counts of gender
    if 'Gender' in df.index:
        user_gender = df['Gender'].value_counts()
        print("Count of Gender:\n",user_gender)
    else:
        print("No Gender data available for this city.")
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.index:
        earliest_year = df['Birth Year'].dropna(0).min()
        print("Earliest year of birth: ",earliest_year)
        most_recent_year = df['Birth Year'].dropna(0).max()
        print("Most recent year of birth: ",most_recent_year)
        most_common_year = df['Birth Year'].dropna(0).value_counts().idxmax()
        print("Most common year of birth: ",most_common_year)
    else:
        print("No birth year data available for this city.")
    
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

        counter = 0
        while True:
            choice = input("Do you want to see the next five rows of raw data? (Y/N)")
            if choice.lower() == 'y':
                print(df.iloc[counter:counter+5])
                counter =+ 5
            elif choice.lower() == 'n':
                break
            else:
                continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
