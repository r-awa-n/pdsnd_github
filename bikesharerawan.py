import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ""
    while city!="chicago" and city!="new york city" and city!="washington":
        city=input("Would you like to see data for Chicago, New york, or Washington?").strip().lower()
        if city!="chicago" and city!="new york city" and city!="washington":
            print("Invalid city!! Please enter either 'Chicago', 'New York City', or 'Washington'.\n")



    valid_months = ['january','february','march','april','may','june']
    month=""
    while month not in valid_months and month!="all":
        month = input("Which Month?").lower()
        if month not in valid_months and month!="all":
            print("Invalid month!! \n")



    day_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=""
    while day not in day_of_week and day!="all":
        day = input("Which Day?").lower()
        if day not in day_of_week and day!="all":
            print("Invalid day!! \n")

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
    print(df)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    df['End Time'] = pd.to_datetime(df['End Time'])

    # filtering on monthe type
    if month != 'all':

        month = months.index(month.lower()) + 1

        df = df[df['month'] == month]

    # filtering on date type
    if day != 'all':
        # filtering on day in week
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Extract hour from 'Start Time'
    df['hour'] = df['Start Time'].dt.hour

    # Display most common month only if not filtered
    if month == 'all':
        common_month_idx = df['month'].mode()[0]
        common_month = months[common_month_idx - 1]
        print(f"The most common month is: {common_month}")

    # Display most common day only if not filtered
    if day == 'all':
        common_day = df['day_of_week'].mode()[0]
        print(f"The most common day is: {common_day}")

    # Display most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"The most common hour is: {common_hour}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


