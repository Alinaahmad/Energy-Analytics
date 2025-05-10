
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
renewables_df = pd.read_csv("renewablePowerGeneration97-17.csv")
non_renewables_df = pd.read_csv("nonRenewablesTotalPowerGeneration.csv")
continent_df = pd.read_csv("Continent_Consumption_TWH.csv")
country_df = pd.read_csv("Country_Consumption_TWH.csv")
top20_df = pd.read_csv("top20CountriesPowerGeneration.csv")

# Step 1: Clean and Prepare Renewable Energy Data
renewables_df.columns = ['Year', 'Hydro_TWh', 'Biofuel_TWh', 'Solar_TWh', 'Geothermal_TWh']
renewables_df['Total_Renewable_TWh'] = renewables_df[['Hydro_TWh', 'Biofuel_TWh', 'Solar_TWh', 'Geothermal_TWh']].sum(axis=1)

# Step 2: Plot Renewable Generation Trend
plt.figure(figsize=(12, 6))
for col in ['Hydro_TWh', 'Biofuel_TWh', 'Solar_TWh', 'Geothermal_TWh']:
    plt.plot(renewables_df['Year'], renewables_df[col], label=col)

plt.title("Renewable Energy Generation by Source (1990–2017)")
plt.xlabel("Year")
plt.ylabel("TWh")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("renewable_energy_trend.png")

# Step 3: Top 20 Countries – Renewable vs Total Generation Bar Plot
top20_df['Total_Renewable_TWh'] = top20_df[['Hydro(TWh)', 'Biofuel(TWh)', 'Solar PV (TWh)', 'Geothermal (TWh)']].sum(axis=1)
top20_df['Renewable_Share_%'] = (top20_df['Total_Renewable_TWh'] / top20_df['Total (TWh)']) * 100

plt.figure(figsize=(12, 6))
sns.barplot(data=top20_df.sort_values('Renewable_Share_%', ascending=False),
            x='Country', y='Renewable_Share_%')
plt.xticks(rotation=45)
plt.title("Top 20 Countries by Renewable Share in Total Power Generation")
plt.tight_layout()
plt.savefig("top20_renewable_share.png")

# Step 4: Continent Consumption Heatmap (fixed with transpose)
continent_df.set_index('Year', inplace=True)
continent_transposed = continent_df.transpose()

plt.figure(figsize=(12, 6))
sns.heatmap(continent_transposed, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title("Continent-wise Energy Consumption Over Years (TWh)")
plt.xlabel("Year")
plt.ylabel("Continent")
plt.tight_layout()
plt.savefig("continent_consumption_heatmap.png")
