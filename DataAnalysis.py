import pandas as pd
import plotly.express as px

table = pd.read_csv('COVID-19 WEEKLY TRENDS IN EUROPE.csv')
print(table)
print(table.info())

print(table['Country, Other'].value_counts())
print(table['Country, Other'].value_counts(normalize=True).map('{:.1%}'.format))


graph = px.histogram(table, x='Country, Other', color='Deaths in the last 7 days')
graph_ = px.histogram(table, x='Country, Other', color='Cases in the last 7 days')
graph.show()
graph_.show()

