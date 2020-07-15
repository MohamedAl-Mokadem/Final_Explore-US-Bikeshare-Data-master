import time
import calendar
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
    city_option=['chicago','new york city','washington']
    while True:
        city =input('\nPlease choose a city to explore\nit should be one of the following cities (chicago, new york city, washington):')
        city=city.lower()
        while city not in city_option:
            city =input('\nOops, the city entered is not in the list!\nPlease try again and choose a city to explore\nit should be one of the following cities (chicago, new york city, washington):')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month_option=['all','january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month =input('\nAnd in which month do you want to explore? \nOr maybe you can see all by write all\n') 
        month =month.lower()
        while month not in month_option:
            month =input('\nSorry, there must be a typo\nplease choose one in the list ("all" or ("january" "february" "march" "april" "may" "june" "july" "august" "september" "october" "november" ,"december":))')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_option = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True:
        day =input('\n Do you want to specify day to explore or all days?\n*you can write all or write the day you want:') 
        day = day.lower()
        while day not in days_option:
            day =input('\nOops there must be a typo, so please choose from this list ( "all" or ("sunday" "monday" "tuesday" "wednesday" "thursday" "friday" "saturday")):')
        else:
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
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    while month != 'all':
        break
    else:
        print('\n The most common month is:    ',df['month'].apply(lambda x: calendar.month_abbr[x]).mode()[0])

    # TO DO: display the most common day of week
    while day != 'all':
        break
    else:
        print('\n The most common day of week is:    ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\n The most common start hour:    ',df['Start Time'].dt.hour.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n The most commonly used start station is:    ', df['Start Station'].mode().sort_values(ascending=False)[0])

    # TO DO: display most commonly used end station
    print('\n The most commonly used end station is:    ', df['End Station'].mode().sort_values(ascending=False)[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\n The most frequent combination of start station and end station trip:    \n', df.groupby(['Start Station','End Station'])['End Station'].count()\
                             .sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\ntotal travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("\nmean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:", df.groupby(['User Type'])['User Type'].count())
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("counts of gender:", df.groupby(['Gender'])['Gender'].count())
    else:
        print("sorry we don't have enough data about Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("earliest, most recent, and most common year of birth is:", int(df['Birth Year'].max()))
    else:
        print("sorry we don't have enough data about Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, month, day)
        
        restart_options = ['yes','no']
        Flags_options = ['yes','no']
        
        flag =input('\n Do you want to continue and explore statistics on the most popular stations and trip ? Enter yes or no.\n') 
        flag = flag.lower()
        while flag not in Flags_options:
            flag =input('\nOops there must be a typo, so please enter yes or no:\n')
        if flag == 'yes':
            station_stats(df)
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            restart = restart.lower()
            while restart not in restart_options:
                restart =input('\nOops there must be a typo, so please enter yes or no:\n')
            if restart.lower() != 'yes':
                print("Thank you for being with us")
                break
            else:
                continue
            break
            
        flag =input('\n Do you want to continue and explore statistics on the total and average trip duration ? Enter yes or no.\n') 
        flag = flag.lower()
        while flag not in Flags_options:
            flag =input('\nOops there must be a typo, so please enter yes or no:\n')
        if flag == 'yes':
            trip_duration_stats(df)
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            restart = restart.lower()
            while restart not in restart_options:
                restart =input('\nOops there must be a typo, so please enter yes or no:\n')
            if restart.lower() != 'yes':
                print("Thank you for being with us")
                break
            else:
                continue
            break
        
        flag =input('\n Do you want to continue and explore statistics on bikeshare users? Enter yes or no.\n') 
        flag = flag.lower()
        while flag not in Flags_options:
            flag =input('\nOops there must be a typo, so please enter yes or no:\n')
        if flag == 'yes':
            user_stats(df, city)
        else:
            restart = input('\Would you like to restart? Enter yes or no.\n')
            restart = restart.lower()
            while restart not in restart_options:
                restart =input('\nOops there must be a typo, so please enter yes or no:\n')
            if restart.lower() != 'yes':
                print("Thank you for being with us")
                break
            else:
                continue
            break
        restart = input('\nThat is all we have for now, Would you like to countinue with another city? Enter yes or no.\n')
        while restart not in restart_options:
                flag =input('\nOops there must be a typo, so please enter yes or no:\n')
        if restart.lower() != 'yes':
            print("Thank you for being with us")
            break


if __name__ == "__main__":
	main()
