import pandas as pd

years = ['2017', '2018', '2019', '2020']
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
#
# for year in years:
#     url = str.format(year)
#     print url

url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

df = pd.read_html(url, header=0)
df.to_csv('test.csv', encoding='utf-8')
