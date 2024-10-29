import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()

# Define parameters for data generation
def generate_data(date_start='2024-01-01', date_end='2024-12-31', num_users=1000, num_sessions=2000, num_conversions=500, num_transactions=300):
    # Convert date range to datetime
    date_start = datetime.strptime(date_start, '%Y-%m-%d')
    date_end = datetime.strptime(date_end, '%Y-%m-%d')
    
    # Define helper functions
    def random_date():
        """Generate random datetime within the date range."""
        return fake.date_time_between(start_date=date_start, end_date=date_end)

    def random_age():
        return random.choice(['18-24', '25-34', '35-44', '45-54', '55-64', '65+'])
    
    def random_goal():
        return random.choice(['Sign-up', 'Purchase', 'Newsletter Subscription', 'Download'])
    
    def random_source():
        return random.choice(['Google', 'Facebook', 'Twitter', 'Email Campaign', 'Direct'])

    # Generate Users table
    users_data = {
        "User_ID": list(range(1, num_users + 1)),
        "Age": [random_age() for _ in range(num_users)],
        "Gender": [random.choice(['Male', 'Female']) for _ in range(num_users)],
        "Location": [fake.country() for _ in range(num_users)],
        "Device": [random.choice(['Mobile', 'Desktop', 'Tablet']) for _ in range(num_users)],
        "Operating_System": [random.choice(['Windows', 'iOS', 'Android', 'MacOS']) for _ in range(num_users)],
    }
    users_df = pd.DataFrame(users_data)

    # Generate Sessions table
    sessions_data = {
        "Session_ID": list(range(1, num_sessions + 1)),
        "User_ID": [random.choice(users_data["User_ID"]) for _ in range(num_sessions)],
        "Start_Time": [random_date() for _ in range(num_sessions)],
        "End_Time": [random_date() for _ in range(num_sessions)],
        "Session_Duration": [random.randint(30, 600) for _ in range(num_sessions)],  # in seconds
        "Bounce_Rate": [round(random.uniform(0, 100), 2) for _ in range(num_sessions)],
        "Pages_per_Session": [random.randint(1, 10) for _ in range(num_sessions)],
    }
    sessions_df = pd.DataFrame(sessions_data)

    # Generate Traffic Sources table
    traffic_sources_data = {
        "Source_ID": list(range(1, num_sessions + 1)),
        "Session_ID": sessions_data["Session_ID"],
        "Source": [random_source() for _ in range(num_sessions)],
        "Medium": [random.choice(['Organic', 'Paid', 'Social', 'Referral']) for _ in range(num_sessions)],
        "Campaign": [fake.word() if random.random() > 0.5 else None for _ in range(num_sessions)],
        "Keyword": [fake.word() if random.random() > 0.7 else None for _ in range(num_sessions)],
    }
    traffic_sources_df = pd.DataFrame(traffic_sources_data)

    # Generate Pages table
    pages_data = {
        "Page_ID": list(range(1, num_sessions * 3 + 1)),
        "Session_ID": [random.choice(sessions_data["Session_ID"]) for _ in range(num_sessions * 3)],
        "Page_URL": [fake.uri() for _ in range(num_sessions * 3)],
        "Page_Title": [fake.sentence(nb_words=3) for _ in range(num_sessions * 3)],
        "Pageviews": [random.randint(1, 20) for _ in range(num_sessions * 3)],
        "Average_Time_on_Page": [random.randint(10, 300) for _ in range(num_sessions * 3)],  # in seconds
        "Exit_Rate": [round(random.uniform(0, 100), 2) for _ in range(num_sessions * 3)],
    }
    pages_df = pd.DataFrame(pages_data)

    # Generate Conversions table
    conversions_data = {
        "Conversion_ID": list(range(1, num_conversions + 1)),
        "Session_ID": [random.choice(sessions_data["Session_ID"]) for _ in range(num_conversions)],
        "Goal_Type": [random_goal() for _ in range(num_conversions)],
        "Goal_Completion": [random.choice([True, False]) for _ in range(num_conversions)],
        "Goal_Value": [round(random.uniform(10, 500), 2) if random.random() > 0.5 else 0 for _ in range(num_conversions)],
        "Transaction_ID": [random.randint(1, num_transactions) if random.random() > 0.5 else None for _ in range(num_conversions)],
    }
    conversions_df = pd.DataFrame(conversions_data)

    # Generate Transactions table
    transactions_data = {
        "Transaction_ID": list(range(1, num_transactions + 1)),
        "Conversion_ID": [random.choice(conversions_data["Conversion_ID"]) for _ in range(num_transactions)],
        "Revenue": [round(random.uniform(20, 2000), 2) for _ in range(num_transactions)],
        "Product_ID": [random.randint(1000, 9999) for _ in range(num_transactions)],
        "Quantity": [random.randint(1, 10) for _ in range(num_transactions)],
        "Coupon_Code": [fake.lexify(text='????-####') if random.random() > 0.7 else None for _ in range(num_transactions)],
    }
    transactions_df = pd.DataFrame(transactions_data)

    # Save DataFrames to CSV with handling for large files
    save_large_csv(users_df, 'Users')
    save_large_csv(sessions_df, 'Sessions')
    save_large_csv(traffic_sources_df, 'Traffic_Sources')
    save_large_csv(pages_df, 'Pages')
    save_large_csv(conversions_df, 'Conversions')
    save_large_csv(transactions_df, 'Transactions')

def save_large_csv(df, filename, rows_per_file=1_000_000):
    """Saves large DataFrame to multiple CSV files if rows exceed limit."""
    os.makedirs('synthetic_data', exist_ok=True)
    total_rows = len(df)
    if total_rows > rows_per_file:
        for i in range(0, total_rows, rows_per_file):
            df_chunk = df[i:i + rows_per_file]
            df_chunk.to_csv(f'synthetic_data/{filename}_part_{i // rows_per_file + 1}.csv', index=False)
    else:
        df.to_csv(f'synthetic_data/{filename}.csv', index=False)

# Example usage
generate_data(
    date_start='2020-01-01', 
    date_end='2024-12-31', 
    num_users=1000, 
    num_sessions=5000, 
    num_conversions=170, 
    num_transactions=210
)
