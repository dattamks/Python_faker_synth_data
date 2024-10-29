import pandas as pd
import numpy as np
from faker import Faker
import random
import os
from datetime import datetime, timedelta

fake = Faker()

def generate_dates(start_date, end_date, n):
    """Generate a list of random dates between start_date and end_date."""
    delta = end_date - start_date
    return [start_date + timedelta(days=random.randint(0, delta.days)) for _ in range(n)]

def generate_organic_engagement_metrics(n, start_date, end_date):
    """Generate synthetic organic engagement metrics data."""
    data = {
        "metric_id": [],
        "post_id": [],
        "impressions": [],
        "reach": [],
        "clicks": [],
        "ctr": [],
        "likes": [],
        "comments": [],
        "shares": [],
        "engagement_rate": [],
        "video_views": [],
        "average_watch_time": [],
    }
    
    for i in range(n):
        metric_id = i + 1
        post_id = random.randint(1, n)
        impressions = random.randint(1000, 50000)
        reach = random.randint(500, impressions)
        clicks = random.randint(0, reach)
        ctr = clicks / impressions if impressions > 0 else 0
        likes = random.randint(0, reach)
        comments = random.randint(0, reach // 10)
        shares = random.randint(0, reach // 10)
        engagement_rate = (likes + comments + shares) / impressions if impressions > 0 else 0
        video_views = random.randint(0, reach)
        average_watch_time = round(random.uniform(1.0, 5.0), 2)

        data["metric_id"].append(metric_id)
        data["post_id"].append(post_id)
        data["impressions"].append(impressions)
        data["reach"].append(reach)
        data["clicks"].append(clicks)
        data["ctr"].append(ctr)
        data["likes"].append(likes)
        data["comments"].append(comments)
        data["shares"].append(shares)
        data["engagement_rate"].append(engagement_rate)
        data["video_views"].append(video_views)
        data["average_watch_time"].append(average_watch_time)

    return pd.DataFrame(data)

def generate_audience_demographics(n):
    """Generate synthetic audience demographics data."""
    data = {
        "demographic_id": [],
        "metric_id": [],
        "location": [],
        "industry": [],
        "job_title": [],
        "seniority_level": [],
        "function": [],
        "company_size": [],
    }

    industries = ["Tech", "Finance", "Healthcare", "Education", "Retail"]
    job_titles = ["Engineer", "Manager", "Analyst", "Sales", "Developer"]
    seniority_levels = ["Entry", "Mid", "Senior", "Lead", "Director"]
    functions = ["IT", "Sales", "Marketing", "Operations", "HR"]
    company_sizes = ["Small", "Medium", "Large"]

    for i in range(n):
        demographic_id = i + 1
        metric_id = random.randint(1, n)
        location = fake.city()
        industry = random.choice(industries)
        job_title = random.choice(job_titles)
        seniority_level = random.choice(seniority_levels)
        function = random.choice(functions)
        company_size = random.choice(company_sizes)

        data["demographic_id"].append(demographic_id)
        data["metric_id"].append(metric_id)
        data["location"].append(location)
        data["industry"].append(industry)
        data["job_title"].append(job_title)
        data["seniority_level"].append(seniority_level)
        data["function"].append(function)
        data["company_size"].append(company_size)

    return pd.DataFrame(data)

def generate_paid_ad_metrics(n):
    """Generate synthetic paid ad metrics data."""
    data = {
        "ad_metric_id": [],
        "ad_id": [],
        "ad_impressions": [],
        "reach": [],
        "clicks": [],
        "ctr": [],
        "engagement_rate": [],
        "cost_per_click": [],
        "cost_per_mille": [],
        "conversions": [],
        "cost_per_conversion": [],
    }

    for i in range(n):
        ad_metric_id = i + 1
        ad_id = random.randint(1, n)
        ad_impressions = random.randint(1000, 50000)
        reach = random.randint(500, ad_impressions)
        clicks = random.randint(0, reach)
        ctr = clicks / ad_impressions if ad_impressions > 0 else 0
        engagement_rate = random.uniform(0.1, 0.5)
        cost_per_click = random.uniform(0.1, 5.0)
        cost_per_mille = cost_per_click * 1000 / ctr if ctr > 0 else 0
        conversions = random.randint(0, clicks)
        cost_per_conversion = cost_per_click * conversions if conversions > 0 else 0

        data["ad_metric_id"].append(ad_metric_id)
        data["ad_id"].append(ad_id)
        data["ad_impressions"].append(ad_impressions)
        data["reach"].append(reach)
        data["clicks"].append(clicks)
        data["ctr"].append(ctr)
        data["engagement_rate"].append(engagement_rate)
        data["cost_per_click"].append(cost_per_click)
        data["cost_per_mille"].append(cost_per_mille)
        data["conversions"].append(conversions)
        data["cost_per_conversion"].append(cost_per_conversion)

    return pd.DataFrame(data)

def generate_campaign_performance_metrics(n):
    """Generate synthetic campaign performance metrics data."""
    data = {
        "campaign_id": [],
        "ad_metric_id": [],
        "budget_spent": [],
        "total_engagements": [],
        "frequency": [],
    }

    for i in range(n):
        campaign_id = i + 1
        ad_metric_id = random.randint(1, n)
        budget_spent = random.uniform(100, 5000)
        total_engagements = random.randint(0, 50000)
        frequency = random.uniform(1.0, 10.0)

        data["campaign_id"].append(campaign_id)
        data["ad_metric_id"].append(ad_metric_id)
        data["budget_spent"].append(budget_spent)
        data["total_engagements"].append(total_engagements)
        data["frequency"].append(frequency)

    return pd.DataFrame(data)

def generate_post_level_data(n):
    """Generate synthetic post level data."""
    data = {
        "post_id": [],
        "content_id": [],
        "post_impressions": [],
        "post_reach": [],
        "post_clicks": [],
        "post_ctr": [],
        "post_engagement_rate": [],
        "likes": [],
        "video_views": [],
    }

    for i in range(n):
        post_id = i + 1
        content_id = random.randint(1, n)
        post_impressions = random.randint(1000, 50000)
        post_reach = random.randint(500, post_impressions)
        post_clicks = random.randint(0, post_reach)
        post_ctr = post_clicks / post_impressions if post_impressions > 0 else 0
        post_engagement_rate = random.uniform(0.1, 0.5)
        likes = random.randint(0, post_reach)
        video_views = random.randint(0, post_reach)

        data["post_id"].append(post_id)
        data["content_id"].append(content_id)
        data["post_impressions"].append(post_impressions)
        data["post_reach"].append(post_reach)
        data["post_clicks"].append(post_clicks)
        data["post_ctr"].append(post_ctr)
        data["post_engagement_rate"].append(post_engagement_rate)
        data["likes"].append(likes)
        data["video_views"].append(video_views)

    return pd.DataFrame(data)

def generate_followers_data(n):
    """Generate synthetic followers data."""
    data = {
        "follower_id": [],
        "total_followers": [],
        "growth_rate": [],
        "demographic_id": [],
    }

    for i in range(n):
        follower_id = i + 1
        total_followers = random.randint(1000, 100000)
        growth_rate = random.uniform(-0.1, 0.1)
        demographic_id = random.randint(1, n)

        data["follower_id"].append(follower_id)
        data["total_followers"].append(total_followers)
        data["growth_rate"].append(growth_rate)
        data["demographic_id"].append(demographic_id)

    return pd.DataFrame(data)

def generate_content_details(n):
    """Generate synthetic content details data."""
    data = {
        "content_id": [],
        "content_type": [],
        "title": [],
        "created_date": [],
    }

    content_types = ["Article", "Video", "Image"]

    for i in range(n):
        content_id = i + 1
        content_type = random.choice(content_types)
        title = fake.sentence(nb_words=6)
        created_date = fake.date_this_year()

        data["content_id"].append(content_id)
        data["content_type"].append(content_type)
        data["title"].append(title)
        data["created_date"].append(created_date)

    return pd.DataFrame(data)

def save_to_csv(df, table_name):
    """Save DataFrame to CSV, splitting into multiple files if needed."""
    os.makedirs('output', exist_ok=True)  # Create an output directory if it doesn't exist
    num_rows = len(df)
    num_files = (num_rows // 1000000) + 1  # Calculate number of files needed

    for i in range(num_files):
        start_index = i * 1000000
        end_index = start_index + 1000000
        df_chunk = df.iloc[start_index:end_index]
        df_chunk.to_csv(f'output/{table_name}_part_{i + 1}.csv', index=False)

def generate_synthetic_data(num_rows, start_date, end_date):
    """Generate synthetic data for all tables."""
    organic_engagement_metrics = generate_organic_engagement_metrics(num_rows, start_date, end_date)
    audience_demographics = generate_audience_demographics(num_rows)
    paid_ad_metrics = generate_paid_ad_metrics(num_rows)
    campaign_performance_metrics = generate_campaign_performance_metrics(num_rows)
    post_level_data = generate_post_level_data(num_rows)
    followers_data = generate_followers_data(num_rows)
    content_details = generate_content_details(num_rows)

    save_to_csv(organic_engagement_metrics, "organic_engagement_metrics")
    save_to_csv(audience_demographics, "audience_demographics")
    save_to_csv(paid_ad_metrics, "paid_ad_metrics")
    save_to_csv(campaign_performance_metrics, "campaign_performance_metrics")
    save_to_csv(post_level_data, "post_level_data")
    save_to_csv(followers_data, "followers_data")
    save_to_csv(content_details, "content_details")

if __name__ == "__main__":
    # Input parameters for data generation
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    num_rows = int(input("Enter the number of rows to generate (max 5 million): "))

    if num_rows > 5000000:
        print("Please limit the number of rows to a maximum of 5 million.")
    else:
        generate_synthetic_data(num_rows, start_date, end_date)
        print("Synthetic data generation complete. Check the 'output' folder for CSV files.")
