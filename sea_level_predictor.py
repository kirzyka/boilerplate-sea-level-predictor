import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    print(df)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    plt.plot(df['Year'], slope*df['Year'] + intercept, 'r', label='Line of Best Fit (1880-2013)')
    plt.plot([df['Year'].iloc[-1], 2050], [df['CSIRO Adjusted Sea Level'].iloc[-1], slope*2050 + intercept], 'g--', label='Predicted Sea Level (1880-2050)')


    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(recent_data['Year'], slope_recent*recent_data['Year'] + intercept_recent, 'b', label='Line of Best Fit (2000-2013)')
    plt.plot([recent_data['Year'].iloc[-1], 2050], [recent_data['CSIRO Adjusted Sea Level'].iloc[-1], slope_recent*2050 + intercept_recent], 'y--', label='Predicted Sea Level (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()

    return plt.gca()