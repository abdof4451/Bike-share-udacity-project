# -*- coding: utf-8 -*-
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
    city = input("choose the city required (chicago, new york city, washington\n\n) : ").lower()
    while city not in CITY_DATA.keys():
        print('please Enter a Valid name')
        city = input("choose the city required (chicago, new york city, washington\n\n) : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True : 
        month = input("choose a month  :(january,february,march,april,may,june,all) ").lower()
        if month in months:
            break
        else:
            print('invaild input, please check your input')
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True :
        day = input("choose a day  :(monday,tuesday,wedensday,thursday,friday,saturday,sunday,all) ").lower()
        if day in days :
            break
        else:
            print ("invalid input, please check your input")

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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start hour'] = df['Start Time'].dt.hour
    # filtering the months 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
     # filtering the days
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]           

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is : {}'.format(df['month'].mode()[0]))            
      

    # TO DO: display the most common day of week
    print('the most common day is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is : {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most common end station is : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of Start station and end station trip
    df['route'] =  df['Start Station'] + "," + df['End Station']
    print ('the most common route is : {}'.format(df['route'].mode()[0]))           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time : ',(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('The average of travel time : ',(df['Trip Duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')
    


    # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in(df.columns):
            year = df['Birth Year'].fillna(0).astype('int64')
            print(f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most comon birth year is: {year.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # to make a user to choose if he want to display the data of 5 rows based on user input.
    # and this will allow the user to display more than 5 rows if he diceded to continue by typing yes in  every time he get asked "
    #"would you want to display more 5 rows ?"
    print('\nThe data is available to check...\n')
    index = 0
    user_input=input('Would You like to display 5 rows of the data? , please Enter Yes or No ').lower()
    if user_input not in ['yes','no']:
        print('You entered an invalid choice, please enter Yes or No')
        user_input=input('Would You like to display 5 rows of the data? , please Enter Yes or No ').lower()
    elif user_input != 'yes':
        print('Okay, Thank You')
    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index += 5
            user_input=input('Would You like to display more 5 rows of the data? , please Enter Yes or No ').lower()
            if user_input != 'yes':
                print('Okay, Thank You')
                break            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)         

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Okay Thank You')      
            break


if __name__ == "__main__":
	main()