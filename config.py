import configparser

# Create the configuration file
config = configparser.ConfigParser()
config['DEFAULT'] = {'companies': 'AAPL,AMZN,DIS,MSFT,TSLA'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
companies = config['DEFAULT']['companies'].split(',')

print(companies)
# Output: ['IBM', 'AAPL', 'GOOG', 'MSFT', 'AMZN']
