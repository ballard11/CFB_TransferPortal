import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the dataset from the 'data' sub-folder
df = pd.read_csv('data/CFB_TransferPortal23.csv', encoding='ISO-8859-1')

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# Generate the figures for the bar graphs
def generate_figure(data, title, x_label):
    fig = px.bar(data, title=title, labels={'value': 'Number of Transfers', 'index': x_label})
    return fig

fig_conference = generate_figure(df['Conference'].value_counts(), "Number of Transfers by Conference", 'Conference')
fig_team = generate_figure(df['Receiving Team'].value_counts().head(15), "Top 15 Teams with Most Transfers", 'Receiving Team')
fig_position = generate_figure(df['Position'].value_counts(), "Number of Transfers by Position", 'Position')

app.layout = html.Div([
    html.Div([
        html.H1("College Football Transfer Portal Analysis", style={'display': 'inline-block'}),
        # You can add an image here if you have one
    ]),
    
    html.P(
        "This dashboard visualizes the trends in college football transfers for 2023.",
        style={"margin": "20px"}),
    
    html.Div([
        dcc.Graph(figure=fig_conference, id='conference-graph'),
        dcc.Graph(figure=fig_team, id='team-graph'),
        dcc.Graph(figure=fig_position, id='position-graph')
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
