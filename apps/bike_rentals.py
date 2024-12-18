from dash_bootstrap_components._components.Row import Row
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash
import dash_deck
import pydeck as pdk
import pandas as pd
from datetime import datetime as dt

import time

#from app import app
from config import *
from .utils import get_geocoding_options

live_bikes_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div([
                html.P(
                    className="my-2 mx-3",
                    children=["""Select location and press button to get live updates"""]
                ),
                dbc.Form(
                    className="mt-4",
                    children=[
                        dbc.Col([
                            dcc.Dropdown(
                                id="live_loc_dropdown",
                                style={"color": "black"},
                                className="my-4 mx-3",
                                placeholder="Select a location",
                                options=[],
                                searchable=True,
                                clearable=True
                            )
                        ])
                    ]
                ),
                dbc.Row(justify="center", children=[
                    dbc.Button("Get Live Updates", color="primary", size="md", className="my-3")
                ])
            ])
        ]
    ),
    className="mt-3",
)

historical_bikes_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div([
                html.P(
                    className="my-2 mx-3",
                    children=["""Select different days using the date picker and by selecting different time intervals using slider."""]
                ),
                dbc.Form(
                    className="mt-4",
                    children=[
                        dbc.Col([
                            dcc.Dropdown(
                                id="historical_loc_dropdown",
                                style={"color": "black"},
                                className="mx-3",
                                placeholder="Select a location",
                                options=[],
                                searchable=True,
                                clearable=True
                            ),
                        ]),
                        dcc.DatePickerSingle(
                                id="date-picker",
                                className="my-3 mx-3",
                                min_date_allowed=dt(2021, 4, 1),
                                max_date_allowed=dt(2021, 9, 30),
                                initial_visible_month=dt(2021, 8, 15),
                                date=dt(2021, 8, 15).date()
                        ),
                        dbc.Col([
                            dbc.Label("Select time interval", html_for="time-slider", className="my-3 mx-3"),
                            dcc.RangeSlider(
                                id="time-slider", 
                                min=0,
                                max=12,
                                marks={val:str(val) for val in range(13)},
                                value=[3, 7]
                            ),
                            html.Div([
                                dbc.RadioItems(
                                    id="am-pm-radio",
                                    className="mt-4 mx-3 btn-group",
                                    inline=True,
                                    labelCheckedClassName="active",
                                    options=[
                                        {"label": "AM", "value": 0},
                                        {"label": "PM", "value": 1}
                                    ],
                                    value=0
                                ),
                            ], className="radio-group")
                        ]),                        
                    ]
                )
            ])
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(live_bikes_content, label="Live Bikes"),
        dbc.Tab(historical_bikes_content, label="Historical bike data"),
    ]
)



layout = dbc.Container([
    dbc.Row(
        className="my-3",
        children=[
            dbc.Col(
                #style={"background-color": "red"},
                className="mr-4",
                children=[
                    tabs,
                ]
            ),
            dbc.Col(
                className="my-3 p-3",
                width=12,
                lg=6,
                children=[
                    dbc.Spinner(html.Div(id="map-loading"), color="success"),
                ]
            )
    ])
])



@callback(
    Output('live_loc_dropdown', 'options'),
    [Input('live_loc_dropdown', 'search_value'), State("live_loc_dropdown", "options")])
def update_live_loc_options(search_query, options):
    return options + get_geocoding_options(search_query)


@callback(
    Output('historical_loc_dropdown', 'options'),
    [Input('historical_loc_dropdown', 'search_value'), State("historical_loc_dropdown", "options")])
def update_historical_loc_options(search_query, options):
    return options + get_geocoding_options(search_query)




@callback(
    Output("map-loading", "children"),
    [Input("am-pm-radio", 'value')])
def load_output(n):
    
    UK_ACCIDENTS_DATA = 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv'

    layer = pdk.Layer(
        'HexagonLayer',  # `type` positional argument is here
        UK_ACCIDENTS_DATA,
        get_position=['lng', 'lat'],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=2)

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)


    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    return dash_deck.DeckGL(
                r.to_json(),
                id="bike-map-graph",
                mapboxKey=MAPBOX_ACCESS_TOKEN,
                tooltip={"text": "1122"},
                style={"height": "80vh"}
            )

