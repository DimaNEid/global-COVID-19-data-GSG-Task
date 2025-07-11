import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, countries):
    plt.figure(figsize=(12, 6))
    for country in countries:
        country_df = df[df['country'] == country]
        plt.plot(country_df['date'], country_df['total_cases'], label=country)
    plt.legend()
    plt.title("COVID-19 Total Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_vax_vs_death_rate(df):
    latest_df = df.sort_values('date').groupby('country').last().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='total_vaccinations', y='total_deaths', data=latest_df)
    plt.title("Vaccinations vs. Deaths per Country")
    plt.xlabel("Total Vaccinations")
    plt.ylabel("Total Deaths")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_case_heatmap(df):
    pivot_table = df.pivot_table(values='total_cases', index='country', columns='date', aggfunc='max')
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot_table, cmap="Reds", cbar_kws={'label': 'Total Cases'})
    plt.title("Global COVID-19 Case Hotspots Over Time")
    plt.xlabel("Date")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()
