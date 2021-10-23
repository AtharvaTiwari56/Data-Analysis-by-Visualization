import pandas as pd
import plotly.express as px

df = pd.read_csv('data7.csv')
grouped_df = df.groupby('level', as_index=False)['attempt']
mean_df = grouped_df.mean()
mean_df = mean_df.reset_index()
print(mean_df)

graph = px.scatter(mean_df, x= df['student_id'], y=df['level'], color=df['attempt'])
graph.update_traces(marker = dict(size=20))
graph.show()