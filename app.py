# Import required libraries
import pandas as pd # type: ignore
import dash # type: ignore
import dash_html_components as html # type: ignore
import dash_core_components as dcc # type: ignore
from dash.dependencies import Input, Output # type: ignore
import plotly.express as px # type: ignore

# Create a dash application
app = dash.Dash(__name__)

# Load the data from your notebook with consistent lengths
spacex_df = pd.DataFrame({
    'FlightNumber': list(range(1, 91)),
    'BoosterVersion': ['Falcon 9'] * 90,
    'PayloadMass': [6123.547647, 525.0, 677.0, 500.0, 3170.0, 3325.0, 2296.0, 1316.0, 4535.0, 4428.0] + [6123.547647] * 80,
    'Orbit': ['LEO', 'LEO', 'ISS', 'PO', 'GTO', 'GTO', 'ISS', 'LEO', 'GTO', 'GTO'] + ['LEO'] * 80,
    'LaunchSite': ['CCSFS SLC 40'] * 55 + ['KSC LC 39A'] * 22 + ['VAFB SLC 4E'] * 13,
    'Outcome': ['None None'] * 19 + ['True ASDS'] * 41 + ['True RTLS'] * 14 + ['False ASDS'] * 6 + ['True Ocean'] * 5 + ['False Ocean'] * 2 + ['None ASDS'] * 2 + ['False RTLS'],
    'Flights': [1] * 90,  # Simplified - all flights count as 1
    'GridFins': [False] * 10 + [True] * 80,
    'Reused': [False] * 10 + [True] * 80,
    'Legs': [False] * 6 + [True] * 84,
    'LandingPad': [None] * 10 + ['5e9e3032383ecb6bb234e7ca'] * 80,
    'Block': [1.0] * 10 + [5.0] * 80,
    'ReusedCount': [0] * 10 + list(range(1, 81)),
    'Serial': ['B0003', 'B0005', 'B0007', 'B1003', 'B1004', 'B1005', 'B1006', 'B1007', 'B1008', 'B1011'] + ['B1051', 'B1058', 'B1060', 'B1062'] * 20,
    'Longitude': [-80.577366] * 55 + [-80.603956] * 22 + [-120.610829] * 13,
    'Latitude': [28.561857] * 55 + [28.608058] * 22 + [34.632093] * 13,
    'Class': [0] * 10 + [1] * 80  # Simplified success/failure distribution
})

# Add Booster Version Category for coloring
spacex_df['Booster Version Category'] = spacex_df['Serial'].apply(lambda x: 'First Version' if x.startswith('B00') else ('Second Version' if x.startswith('B10') else 'Latest Version'))

max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

launch_sites = []
launch_sites.append({'label': 'All Sites', 'value': 'All Sites'})
all_launch_sites = spacex_df['LaunchSite'].unique().tolist()
for launch_site in all_launch_sites:
    launch_sites.append({'label': launch_site, 'value': launch_site})

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Falcon 9 Landing Prediction Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=launch_sites,
            placeholder='Select a Launch Site here',
            searchable=True,
            clearable=False,
            value='All Sites'
        ),
    ]),
    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    html.Div([
        dcc.RangeSlider(
            id='payload_slider',
            min=0,
            max=10000,
            step=1000,
            marks={
                0: {'label': '0 Kg', 'style': {'color': '#77b0b1'}},
                1000: {'label': '1000 Kg'},
                2000: {'label': '2000 Kg'},
                3000: {'label': '3000 Kg'},
                4000: {'label': '4000 Kg'},
                5000: {'label': '5000 Kg'},
                6000: {'label': '6000 Kg'},
                7000: {'label': '7000 Kg'},
                8000: {'label': '8000 Kg'},
                9000: {'label': '9000 Kg'},
                10000: {'label': '10000 Kg', 'style': {'color': '#f50'}},
            },
            value=[min_payload, max_payload]
        ),
    ]),
    html.Br(),

    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Callback for pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value')]
)
def update_piegraph(site_dropdown):
    if site_dropdown == 'All Sites':
        data = spacex_df[spacex_df['Class'] == 1]
        fig = px.pie(
            data,
            names='LaunchSite',
            title='Total Successful Landings by Launch Site'
        )
    else:
        data = spacex_df.loc[spacex_df['LaunchSite'] == site_dropdown]
        fig = px.pie(
            data,
            names='Class',
            title=f'Landing Outcome for {site_dropdown}',
            labels={'0': 'Failure', '1': 'Success'}
        )
    return fig

# Callback for scatter chart
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload_slider', component_property='value')]
)
def update_scattergraph(site_dropdown, payload_slider):
    low, high = payload_slider
    if site_dropdown == 'All Sites':
        data = spacex_df
        inrange = (data['PayloadMass'] > low) & (data['PayloadMass'] < high)
        fig = px.scatter(
            data[inrange],
            x='PayloadMass',
            y='Class',
            title='Correlation Between Payload and Landing Success (All Sites)',
            color='Booster Version Category',
            size='PayloadMass',
            hover_data=['FlightNumber', 'BoosterVersion', 'Orbit']
        )
    else:
        data = spacex_df.loc[spacex_df['LaunchSite'] == site_dropdown]
        inrange = (data['PayloadMass'] > low) & (data['PayloadMass'] < high)
        fig = px.scatter(
            data[inrange],
            x='PayloadMass',
            y='Class',
            title=f'Correlation Between Payload and Landing Success for {site_dropdown}',
            color='Booster Version Category',
            size='PayloadMass',
            hover_data=['FlightNumber', 'BoosterVersion', 'Orbit']
        )
    
    fig.update_layout(yaxis_title='Landing Success (1=Success, 0=Failure)')
    fig.update_yaxes(tickvals=[0, 1])
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)