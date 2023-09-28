import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load the dataset from the 'data' sub-folder
df = pd.read_csv('data/CFB_TransferPortal23.csv', encoding='ISO-8859-1')  # Added the encoding based on our previous discovery

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1("College Football Transfer Portal Analysis", style={'display': 'inline-block'}),
        # You can add an image here if you have one
    ]),
    
    html.P(
        "This dashboard visualizes the trends in college football transfers for 2023.",
        style={"margin": "20px"}),
    
    html.Div([
        dcc.Dropdown(
            id='data-dropdown',
            options=[
                {'label': 'By Conference', 'value': 'Conference'},
                {'label': 'By Receiving Team', 'value': 'Receiving Team'},
                {'label': 'By Position', 'value': 'Position'}
            ],
            value='Conference',
            style={'width': '50%'}
        ),
        dcc.Graph(id='data-graph')
    ]),
])

@app.callback(
    Output('data-graph', 'figure'),
    [Input('data-dropdown', 'value')]
)
def update_graph(selected_value):
    if selected_value == 'Conference':
        data = df['Conference'].value_counts()
        title = "Number of Transfers by Conference"
    elif selected_value == 'Receiving Team':
        data = df['Receiving Team'].value_counts()
        title = "Top Teams with the Most Transfers"
    else:
        data = df['Position'].value_counts()
        title = "Number of Transfers by Position"
    
    fig = px.bar(data, title=title, labels={'value': 'Number of Transfers', 'index': selected_value})
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
