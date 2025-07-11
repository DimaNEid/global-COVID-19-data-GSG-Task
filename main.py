# import pandas as pd
# from pathlib import Path
# from src.clean_data import clean_covid_data
#
# def load_covid_data():
#     data_path = Path("data/compact.csv")
#     df = pd.read_csv(data_path, low_memory=False)
#     return df
#
# if __name__ == "__main__":
#     df = load_covid_data()
#     egypt_df = clean_covid_data(df, country="Egypt")
#
#     egypt_df.to_csv("outputs/egypt_covid_cleaned.csv", index=False)



##########################################################


import pandas as pd
from src.clean_data import clean_covid_data
from src.metrics import total_cases_deaths, monthly_growth_rate
from pathlib import Path
from src.metrics import total_cases_deaths, monthly_growth_rate, detect_anomalies
from src.plots import plot_time_series, plot_vax_vs_death_rate, plot_case_heatmap

def load_cleaned_data():
    path = Path("outputs/egypt_covid_cleaned.csv")
    df = pd.read_csv(path, parse_dates=['date'])
    return df

if __name__ == "__main__":
    egypt_df = load_cleaned_data()

    # # Total Cases/Deaths
    # totals = total_cases_deaths(egypt_df)
    # print("Total Cases and Deaths:", totals)
    #
    # # Monthly Growth
    # growth_df = monthly_growth_rate(egypt_df)
    # growth_df.to_csv("outputs/egypt_monthly_growth_rates.csv", index=False)
    #
    # # Anomaly Detection
    # anomalies_cases = detect_anomalies(egypt_df, column='new_cases')
    # anomalies_deaths = detect_anomalies(egypt_df, column='new_deaths')
    #
    # anomalies_cases.to_csv("outputs/egypt_anomalies_cases.csv", index=False)
    # anomalies_deaths.to_csv("outputs/egypt_anomalies_deaths.csv", index=False)

    full_df = pd.read_csv("data/compact.csv", parse_dates=['date'])

    from src.plots import plot_time_series, plot_vax_vs_death_rate, plot_case_heatmap

    # Create 3 plots:
    plot_time_series(full_df, countries=['Egypt', 'United States', 'India'])
    plot_vax_vs_death_rate(full_df)
    plot_case_heatmap(full_df)


#############################################################################################