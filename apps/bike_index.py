from dash_bootstrap_components._components.Row import Row
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash
from dash import callback
from dash import get_asset_url
import pydeck as pdk
import pandas as pd
import math

#from app import app
from config import *

dash.register_page(__name__, path="/bike-index")

MOBILITY_DATA = (
    "https://sumit-mobility-web.s3.eu-west-2.amazonaws.com/bike_trips_stops.csv"
)
bike_trips_stops_df = None


layout = dbc.Container(
    [
        dbc.Row(
            className="my-3",
            children=[
                dbc.Col(
                    # style={"background-color": "red"},
                    className="mr-4",
                    children=[
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4(
                                        className="my-2 mx-3",
                                        children="BIKEABILITY ON DIFFERENT STATION",
                                    ),
                                    html.P(
                                        className="my-4 mx-3",
                                        children=[
                                            """General trends for bike trips in city of Bhubaneswar."""
                                        ],
                                    ),
                                    dbc.Form(
                                        className="mt-4",
                                        children=[
                                            dbc.Col(
                                                [
                                                    dcc.Dropdown(
                                                        id="bike-trips-loc-dropdown",
                                                        style={"color": "black"},
                                                        className="mx-3",
                                                        placeholder="Select a location",
                                                        options=[
                                                            {
                                                                "label": "Bhubaneswar",
                                                                "value": "BBSR",
                                                            }
                                                        ],
                                                    ),
                                                ]
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                            className="mt-3",
                        ),
                    ],
                ),
                dbc.Col(
                    className="my-3 p-3",
                    width=12,
                    lg=6,
                    children=[
                        dbc.Spinner(
                            id="bike-trips-spinner",
                            color="primary",
                        ),
                    ],
                ),
            ],
        )
    ]
)

# when the location is changed, update the map in the spinner
@callback(
    Output("bike-trips-spinner", "children"),
    [Input("bike-trips-loc-dropdown", "value")],
)
def update_map(loc):
    if loc == "BBSR":
        return (
            html.Iframe(
                src=get_asset_url("Bike_index.html"),
                style={"width": "100%", "height": "100vh"},
                sandbox="allow-scripts",
            ),
        )
