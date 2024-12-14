# from dash_bootstrap_components._components.Row import Row
# import dash_html_components as html
# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output, State
# import dash_deck
# import pydeck as pdk
# import pandas as pd
# import math

# from app import app
# from config import *


# MOBILITY_DATA = (
#     "https://sumit-mobility-web.s3.eu-west-2.amazonaws.com/bike_trips_stops.csv"
# )
# bike_trips_stops_df = None


# layout = dbc.Container(
#     [
#         dbc.Row(
#             className="my-3",
#             children=[
#                 dbc.Col(
#                     # style={"background-color": "red"},
#                     className="mr-4",
#                     children=[
#                         dbc.Card(
#                             dbc.CardBody(
#                                 [
#                                     html.H4(
#                                         className="my-2 mx-3", children="Bike Trips"
#                                     ),
#                                     html.P(
#                                         className="my-4 mx-3",
#                                         children=[
#                                             """General trends for bike trips in city of Bhubaneswar."""
#                                         ],
#                                     ),
#                                     dbc.Form(
#                                         className="mt-4",
#                                         children=[
#                                             dbc.FormGroup(
#                                                 [
#                                                     dcc.Dropdown(
#                                                         id="bike-trips-loc-dropdown",
#                                                         style={"color": "black"},
#                                                         className="mx-3",
#                                                         placeholder="Select a location",
#                                                         options=[
#                                                             {
#                                                                 "label": "Bhubaneswar",
#                                                                 "value": "BBSR",
#                                                             }
#                                                         ],
#                                                         value="BBSR",
#                                                         disabled=True,
#                                                     ),
#                                                 ]
#                                             ),
#                                             dbc.FormGroup(
#                                                 [
#                                                     dbc.Label(
#                                                         "Select time interval",
#                                                         html_for="bike-trips-time-slider",
#                                                         className="my-3 mx-3",
#                                                     ),
#                                                     dcc.Dropdown(
#                                                         id="bike-trips-time-dropdown",
#                                                         style={"color": "black"},
#                                                         className="mx-3",
#                                                         placeholder="Select a time",
#                                                         options=[
#                                                             {
#                                                                 "label": "12am to 2am",
#                                                                 "value": "12am-2am",
#                                                             },
#                                                             {
#                                                                 "label": "2am to 4am",
#                                                                 "value": "2am-4am",
#                                                             },
#                                                             {
#                                                                 "label": "4am to 6am",
#                                                                 "value": "4am-6am",
#                                                             },
#                                                             {
#                                                                 "label": "6am to 8am",
#                                                                 "value": "6am-8am",
#                                                             },
#                                                             {
#                                                                 "label": "8am to 10am",
#                                                                 "value": "8am-10am",
#                                                             },
#                                                             {
#                                                                 "label": "10am to 12pm",
#                                                                 "value": "10am-12pm",
#                                                             },
#                                                             {
#                                                                 "label": "12pm to 2pm",
#                                                                 "value": "12pm-2pm",
#                                                             },
#                                                             {
#                                                                 "label": "2pm to 4pm",
#                                                                 "value": "2pm-4pm",
#                                                             },
#                                                             {
#                                                                 "label": "4pm to 6pm",
#                                                                 "value": "4pm-6pm",
#                                                             },
#                                                             {
#                                                                 "label": "6pm to 8pm",
#                                                                 "value": "6pm-8pm",
#                                                             },
#                                                             {
#                                                                 "label": "8pm to 10pm",
#                                                                 "value": "8pm-10pm",
#                                                             },
#                                                             {
#                                                                 "label": "10pm to 12am",
#                                                                 "value": "10pm-12am",
#                                                             },
#                                                         ],
#                                                     ),
#                                                 ]
#                                             ),
#                                         ],
#                                     ),
#                                 ]
#                             ),
#                             className="mt-3",
#                         ),
#                     ],
#                 ),
#                 dbc.Col(
#                     className="my-3 p-3",
#                     width=12,
#                     lg=6,
#                     children=[
#                         dbc.Spinner(
#                             html.Div(id="bike-trips-map-loading"), color="success"
#                         ),
#                     ],
#                 ),
#             ],
#         )
#     ]
# )


# @app.callback(
#     Output("bike-trips-map-loading", "children"),
#     [
#         Input("bike-trips-loc-dropdown", "value"),
#         Input("bike-trips-time-dropdown", "value"),
#     ],
# )
# def load_output(n, time_dropdown_range):
#     if time_dropdown_range == "12am-2am":
#         map_link = "my_map_0_to_2.html"
#     elif time_dropdown_range == "2am-4am":
#         map_link = "my_map_2_to_4.html"
#     elif time_dropdown_range == "4am-6am":
#         map_link = "my_map_4_to_6.html"
#     elif time_dropdown_range == "6am-8am":
#         map_link = "my_map_6_to_8.html"
#     elif time_dropdown_range == "8am-10am":
#         map_link = "my_map_8_to_10.html"
#     elif time_dropdown_range == "10am-12pm":
#         map_link = "my_map_10_to_12.html"
#     elif time_dropdown_range == "12pm-2pm":
#         map_link = "my_map_12_to_2.html"
#     elif time_dropdown_range == "2pm-4pm":
#         map_link = "my_map_2_to_4.html"
#     elif time_dropdown_range == "4pm-6pm":
#         map_link = "my_map_4_to_6.html"
#     elif time_dropdown_range == "6pm-8pm":
#         map_link = "my_map_6_to_8.html"
#     elif time_dropdown_range == "8pm-10pm":
#         map_link = "my_map_8_to_10.html"
#     elif time_dropdown_range == "10pm-12am":
#         map_link = "my_map_10_to_12.html"
#     else:
#         map_link = "my_map_0_to_2.html"

#     return html.Iframe(
#         src=app.get_asset_url(map_link),
#         style={"width": "100%", "height": "100vh"},
#         sandbox="allow-scripts",
#     )
