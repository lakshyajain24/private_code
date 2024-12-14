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
#                                     html.H4(className="my-2 mx-3", children="Jobs"),
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
#                                                     dbc.Label(
#                                                         "Select Type",
#                                                         html_for="bike-trips-time-slider",
#                                                         className="my-3 mx-3",
#                                                     ),
#                                                     dcc.Dropdown(
#                                                         id="type-dropdown",
#                                                         style={"color": "black"},
#                                                         className="m-3",
#                                                         placeholder="Select mode",
#                                                         options=[
#                                                             {
#                                                                 "label": "cycling",
#                                                                 "value": "cycling",
#                                                             },
#                                                             {
#                                                                 "label": "walking",
#                                                                 "value": "walking",
#                                                             },
#                                                         ],
#                                                     ),
#                                                     dcc.Dropdown(
#                                                         id="kind-dropdown",
#                                                         style={"color": "black"},
#                                                         className="mx-3",
#                                                         placeholder="Select a location",
#                                                         options=[
#                                                             {
#                                                                 "label": "All Jobs",
#                                                                 "value": "alljobs",
#                                                             },
#                                                             {
#                                                                 "label": "ATM's",
#                                                                 "value": "atms",
#                                                             },
#                                                             {
#                                                                 "label": "College",
#                                                                 "value": "college",
#                                                             },
#                                                             {
#                                                                 "label": "Hospitals",
#                                                                 "value": "hospitals",
#                                                             },
#                                                             {
#                                                                 "label": "Parks",
#                                                                 "value": "parks",
#                                                             },
#                                                             {
#                                                                 "label": "Schools",
#                                                                 "value": "schools",
#                                                             },
#                                                             {
#                                                                 "label": "Shopping",
#                                                                 "value": "shopping",
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
#                         dbc.Spinner(html.Div(id="jobs-map-loading"), color="success"),
#                     ],
#                 ),
#             ],
#         )
#     ]
# )


# @app.callback(
#     Output("jobs-map-loading", "children"),
#     [
#         Input("type-dropdown", "value"),
#         Input("kind-dropdown", "value"),
#     ],
# )
# def load_output(type_job, kind):
#     html_file = None
#     if type_job == "cycling" and kind == "alljobs":
#         html_file = "AllJobs_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "atms":
#         html_file = "ATMs_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "college":
#         html_file = "College_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "hospitals":
#         html_file = "Hospital_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "parks":
#         html_file = "Parks_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "schools":
#         html_file = "Schools_Cycling_Latest.html"
#     elif type_job == "cycling" and kind == "shopping":
#         html_file = "Shops_Cycling_Latest.html"
#     elif type_job == "walking" and kind == "alljobs":
#         html_file = "AllJobs_Walking_Latest.html"
#     elif type_job == "walking" and kind == "atms":
#         html_file = "ATMs_Walking_Latest.html"
#     elif type_job == "walking" and kind == "college":
#         html_file = "College_Walking_Latest.html"
#     elif type_job == "walking" and kind == "hospitals":
#         html_file = "Hospital_Walking_Latest.html"
#     elif type_job == "walking" and kind == "parks":
#         html_file = "Parks_Walking_Latest.html"
#     elif type_job == "walking" and kind == "schools":
#         html_file = "Schools_Walking_Latest.html"
#     elif type_job == "walking" and kind == "shopping":
#         html_file = "Shops_Walking_Latest.html"
#     if html_file:
#         return html.Iframe(
#             src=app.get_asset_url("jobs/html/" + html_file),
#             style={"width": "100%", "height": "100vh"},
#             sandbox="allow-scripts",
#         )
