# from dash_bootstrap_components._components.Row import Row
# import dash_html_components as html
# import dash_core_components as dcc
# import dash_daq as daq
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output, State
# import math
# import dash_deck
# import pydeck as pdk
# import pandas as pd
# from datetime import datetime as dt

# import time

# from app import app
# from config import *
# from .utils import get_geocoding_options


# # @app.callback(
# #     Output("live_loc_dropdown", "options"),
# #     [Input("live_loc_dropdown", "search_value"), State("live_loc_dropdown", "options")],
# # )
# # def update_live_loc_options(search_query, options):
# #     return options + get_geocoding_options(search_query)


# # @app.callback(Output("uk-loading", "children"), [Input("live_loc_dropdown", "value")])
# # def load_output():

# UK_ACCIDENTS_DATA = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"

# layer = pdk.Layer(
#     "HexagonLayer",  # `type` positional argument is here
#     UK_ACCIDENTS_DATA,
#     get_position=["lng", "lat"],
#     auto_highlight=True,
#     elevation_scale=50,
#     pickable=True,
#     elevation_range=[0, 3000],
#     extruded=True,
#     coverage=2,
# )

# # Set the viewport location
# view_state = pdk.ViewState(
#     longitude=-1.415,
#     latitude=52.2323,
#     zoom=6,
#     min_zoom=5,
#     max_zoom=15,
#     pitch=40.5,
#     bearing=-27.36,
# )

# # Render
# r = pdk.Deck(layers=[layer], initial_view_state=view_state)
# map_uk = dash_deck.DeckGL(
#     r.to_json(),
#     id="bike-map-graph",
#     mapboxKey=MAPBOX_ACCESS_TOKEN,
#     tooltip={"text": "1122"},
#     style={"height": "80vh"},
# )


# live_bikes_content = dbc.Card(
#     dbc.CardBody(
#         [
#             html.Div(
#                 [
#                     html.P(
#                         className="my-2 mx-3",
#                         children=[
#                             """Select location and press button to get live updates"""
#                         ],
#                     ),
#                     dbc.Form(
#                         className="mt-4",
#                         children=[
#                             dbc.FormGroup(
#                                 [
#                                     dcc.Dropdown(
#                                         id="live_loc_dropdown",
#                                         style={"color": "black"},
#                                         className="my-4 mx-3",
#                                         placeholder="Select a location",
#                                         options=[
#                                             {
#                                                 "label": "United Kingdom",
#                                                 "value": "United Kingdom",
#                                             },
#                                         ],
#                                         searchable=True,
#                                         clearable=True,
#                                     )
#                                 ]
#                             )
#                         ],
#                     ),
#                     dbc.Row(
#                         justify="center",
#                         children=[
#                             dbc.Button(
#                                 "Get Live Updates",
#                                 color="primary",
#                                 size="md",
#                                 className="my-3",
#                             )
#                         ],
#                     ),
#                 ]
#             )
#         ]
#     ),
#     className="mt-3",
# )

# layout = dbc.Container(
#     [
#         dbc.Row(
#             className="my-3",
#             children=[
#                 dbc.Col(
#                     # style={"background-color": "red"},
#                     className="mr-4",
#                     children=[
#                         live_bikes_content,
#                     ],
#                 ),
#                 dbc.Col(
#                     className="my-3 p-3",
#                     width=12,
#                     lg=6,
#                     children=[
#                         dbc.Spinner(
#                             id="uk-loading",
#                             color="primary",
#                         ),
#                     ],
#                 ),
#             ],
#         )
#     ]
# )

# # when dropdown is selected, update the map in spinnner
# @app.callback(
#     Output("uk-loading", "children"),
#     [Input("live_loc_dropdown", "value")],
# )
# def update_map(value):
#     if value == "United Kingdom":
#         return dash_deck.DeckGL(
#             r.to_json(),
#             id="bike-map-graph",
#             mapboxKey=MAPBOX_ACCESS_TOKEN,
#             tooltip={"text": "1122"},
#             style={"height": "80vh"},
#         )
