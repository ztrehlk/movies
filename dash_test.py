import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import numpy as np



data = (
    pd.read_csv("data/rotten_tomatoes_movies.csv")

)

genres = data.copy()
genres['genre'] = genres['genre'].str.split(', ')
genres = genres.explode('genre')

genres_stats = genres.groupby('genre').agg(
                        tomatoMeter_Mean=('tomatoMeter', np.mean),
                        tomatoMeter_Sum=('tomatoMeter', np.sum),
                        tomatoMeter_Median=('tomatoMeter', np.median),
                        audienceScore_Mean=('audienceScore', np.mean),
                        audienceScore_Sum=('audienceScore', np.sum),
                        audienceScore_Median=('audienceScore', np.median),
).reset_index()

app = Dash(__name__)




app.layout = html.Div(
    children=[
        html.H1(children="Movie Analytics"),
        html.P(
            children=(
                "Analyze the behavior of movies"
                " all around"
            ),
        ),
        dcc.Graph(
            figure= px.bar(genres_stats, x='genre', y='tomatoMeter_Mean',
                           text_auto='.2s')
        ),
        dcc.Graph(
            figure= px.bar(genres_stats, x='genre', y='audienceScore_Mean',
                           text_auto='.2s')
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)