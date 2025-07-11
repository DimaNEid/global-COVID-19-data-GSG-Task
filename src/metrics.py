import pandas as pd

def total_cases_deaths(df):

    latest_row = df.sort_values("date").iloc[-1]         #Calculate total cases and deaths for the latest date.
    return {
        "Country": latest_row['country'],
        "Total Cases": latest_row['total_cases'],
        "Total Deaths": latest_row['total_deaths']
    }

def monthly_growth_rate(df):

    df['month'] = df['date'].dt.to_period('M')             #Calculate monthly growth rates.
    monthly = df.groupby('month')[['total_cases', 'total_deaths']].max()
    monthly['Cases Growth %'] = monthly['total_cases'].pct_change().fillna(0) * 100
    monthly['Deaths Growth %'] = monthly['total_deaths'].pct_change().fillna(0) * 100
    return monthly.reset_index()



def detect_anomalies(df, column='new_cases', threshold_factor=3):
    """
    Detects anomalies where daily new cases or deaths are unusually high.
    Threshold is defined as mean + (threshold_factor * standard deviation).
    """
    df = df.copy()
    df['value'] = df[column]

    mean_val = df['value'].mean()
    std_val = df['value'].std()
    threshold = mean_val + threshold_factor * std_val

    anomalies = df[df['value'] > threshold]

    print(f"Detected {len(anomalies)} anomalies in {column}. Threshold: {threshold:.2f}")
    return anomalies[['date', 'country', column]]
