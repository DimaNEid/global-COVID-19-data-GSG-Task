import pandas as pd

def clean_covid_data(df, country="Egypt"):

    df = df[df['country'] == country].copy()      #filter by country
    df.drop_duplicates(inplace=True)              #Remove duplicates
    df['date'] = pd.to_datetime(df['date'], errors='coerce')    #format date column
    df = df.dropna(subset=['date'])                             #drop fully empty columns
    df.dropna(axis=1, how='all', inplace=True)

    important_columns = [                                           #fill missing values for key columns
        'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
        'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'
    ]
    for col in important_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0)


    columns_to_keep = important_columns + ['date', 'country', 'continent']              #drop columns we won’t use to reduce memory
    columns_to_keep = [col for col in columns_to_keep if col in df.columns]
    df = df[columns_to_keep]

    print(f"Cleaned data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

