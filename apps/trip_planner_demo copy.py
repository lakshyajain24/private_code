# import json
# from dash import dcc, html, Input, Output, State, callback, register_page, no_update
# import dash_bootstrap_components as dbc
# import dash_deck
# # from dash.exceptions import PreventUpdate
# import pydeck as pdk
# import pandas as pd
# import requests
# from shapely.geometry import box, Point
# import pickle
# import networkx as nx
# import osmnx as ox
# from apps.utils import get_geocoding_options
# from config import *  # Ensure this contains necessary constants like MAPBOX_ACCESS_TOKEN

# # Register the page
# register_page(__name__, path="/trip-planner", name="Trip Planner")

# # Configure osmnx settings
# ox.settings.use_cache = True  # Enable caching to reuse downloaded data
# ox.settings.log_console = True  # Log output to the console

# # Delhi Boundary Configuration
# DELHI_BOUNDARY = [76.8388830269287, 28.4042620003073, 77.3464387601731, 28.8835889894397]
# DELHI_BBOX = box(*DELHI_BOUNDARY)

# # Load Graph Data
# with open("assets/path_finder/delhi_graph_data.pkl", "rb") as f:
#     GRAPH = pickle.load(f)

# # Constants
# COVID_HOTSPOTS_FILE = "assets/path_finder/new.csv"
# DIRECTIONS_REQ_PARAMS = {"alternatives": False, "steps": True, "geometries": "geojson"}

# # # Layout for the Trip Planner page
# # layout = dbc.Container(
# #     [
# #         dbc.Row(
# #             className="my-3",
# #             children=[
# #                 dbc.Modal(
# #                     [
# #                         dbc.ModalHeader("Invalid Location"),
# #                         dbc.ModalBody("Please enter a location within Delhi."),
# #                         dbc.ModalFooter(
# #                             dbc.Button("Close", id="close-modal", n_clicks=0)
# #                         ),
# #                     ],
# #                     id="invalid-location-modal",
# #                     is_open=False,
# #                     centered=True,
# #                 ),
# #                 # Input Section
# #                 dbc.Col(
# #                     children=[
# #                         dbc.Card(
# #                             dbc.CardBody(
# #                                 [
# #                                     html.H4("Trip Planner", className="my-2"),
# #                                     html.P(
# #                                         """Plan your safe trip within Delhi. 
# #                                         COVID hotspots and other factors are considered."""
# #                                     ),
# #                                     # Separate dropdowns into distinct rows
# #                                     dbc.Row(
# #                                         dcc.Dropdown(
# #                                             id="from-location",
# #                                             placeholder="From Location",
# #                                             options=[],
# #                                             className="mb-3 dropdown-black-text",
# #                                         ),
# #                                         className="mb-3 dropdown-black-text",
# #                                     ),
# #                                     dbc.Row(
# #                                         dcc.Dropdown(
# #                                             id="to-location",
# #                                             placeholder="To Location",
# #                                             options=[],
# #                                             className="mb-3 dropdown-black-text",
# #                                         ),
# #                                         className="mb-3 dropdown-black-text",
# #                                     ),
# #                                     # Checklists and buttons remain as is
# #                                     dbc.Row(
# #                                         dbc.Checklist(
# #                                             options=[
# #                                                 {
# #                                                     "label": "Avoid COVID Hotspots",
# #                                                     "value": 1,
# #                                                 },
# #                                             ],
# #                                             value=[],
# #                                             id="avoid-hotspots",
# #                                             switch=True,
# #                                         ),
# #                                         className="mb-3",
# #                                     ),
# #                                     dbc.Row(
# #                                         [
# #                                             dbc.Label("Layers"),
# #                                             dbc.Checklist(
# #                                                 options=[
# #                                                     {
# #                                                         "label": "Show COVID Hotspots",
# #                                                         "value": 1,
# #                                                     },
# #                                                 ],
# #                                                 value=[1],
# #                                                 id="layer-switch",
# #                                                 switch=True,
# #                                             ),
# #                                         ],
# #                                         className="mb-3",
# #                                     ),
# #                                     dbc.Row(
# #                                         dbc.Button(
# #                                             "Plan Routes",
# #                                             id="plan-routes",
# #                                             color="primary",
# #                                             className="mt-3",
# #                                             size="lg",
# #                                         )
# #                                     ),
# #                                 ]
# #                             ),
# #                         )
# #                     ],
# #                     width=6,
# #                 ),
# #                 # Output Map Section
# #                 dbc.Col(
# #                     dbc.Spinner(html.Div(id="route-map"), color="primary"),
# #                     width=6,
# #                 ),
# #             ],
# #         )
# #     ]
# # )

# layout = dbc.Container(
#     [
#         dbc.Row(
#             className="my-3",
#             children=[
#                 # Modal for invalid locations
#                 dbc.Modal(
#                     [
#                         dbc.ModalHeader("Invalid Location"),
#                         dbc.ModalBody("Please enter a location within Delhi."),
#                         dbc.ModalFooter(
#                             dbc.Button("Close", id="close-modal", n_clicks=0)
#                         ),
#                     ],
#                     id="invalid-location-modal",
#                     is_open=False,
#                     centered=True,
#                 ),
#                 # Input Section
#                 dbc.Col(
#                     children=[
#                         dbc.Card(
#                             dbc.CardBody(
#                                 [
#                                     html.H4("Trip Planner", className="my-2"),
#                                     html.P(
#                                         """Plan your safe trip within Delhi. 
#                                         COVID hotspots and other factors are considered."""
#                                     ),
#                                     # Dropdown for "From Location"
#                                     dbc.Row(
#                                         dcc.Dropdown(
#                                             id="from-location",
#                                             placeholder="From Location",
#                                             options=[],
#                                             className="mb-3 dropdown-black-text",
#                                         ),
#                                         className="mb-3",
#                                     ),
#                                     # Dropdown for "To Location"
#                                     dbc.Row(
#                                         dcc.Dropdown(
#                                             id="to-location",
#                                             placeholder="To Location",
#                                             options=[],
#                                             className="mb-3 dropdown-black-text",
#                                         ),
#                                         className="mb-3",
#                                     ),
#                                     # Avoid COVID hotspots switch
#                                     dbc.Row(
#                                         dbc.Checklist(
#                                             options=[
#                                                 {
#                                                     "label": "Avoid COVID Hotspots",
#                                                     "value": 1,
#                                                 },
#                                             ],
#                                             value=[],
#                                             id="avoid-hotspots",
#                                             switch=True,
#                                         ),
#                                         className="mb-3",
#                                     ),
#                                     # Layer selection
#                                     dbc.Row(
#                                         [
#                                             dbc.Label("Layers"),
#                                             dbc.Checklist(
#                                                 options=[
#                                                     {
#                                                         "label": "Show COVID Hotspots",
#                                                         "value": 1,
#                                                     },
#                                                 ],
#                                                 value=[1],
#                                                 id="layer-switch",
#                                                 switch=True,
#                                             ),
#                                         ],
#                                         className="mb-3",
#                                     ),
#                                     # Plan Routes Button
#                                     dbc.Row(
#                                         dbc.Button(
#                                             "Plan Routes",
#                                             id="plan-routes",
#                                             color="primary",
#                                             className="mt-3",
#                                             size="lg",
#                                         )
#                                     ),
#                                 ]
#                             ),
#                         )
#                     ],
#                     width=6,
#                 ),
#                 # Output Map Section
#                 dbc.Col(
#                     dbc.Spinner(html.Div(id="route-map"), color="primary"),
#                     width=6,
#                 ),
#             ],
#         )
#     ]
# )




# # # Callbacks
# # @callback(
# #     Output("invalid-location-modal", "is_open"),
# #     [Input("from-location", "from_value"), Input("to-location", "to_value"), Input("close-modal", "n_clicks")],
# #     [State("invalid-location-modal", "is_open")],
# # )
# # def validate_locations(from_value, to_value, n_clicks, is_open):
# #     """Check if the selected locations are within the Delhi boundary."""
# #     if n_clicks==1 and is_open:
# #         return False
# #     points = [
# #         get_point_from_dropdown(from_value),
# #         get_point_from_dropdown(to_value),
# #     ]
# #     if any(point and not DELHI_BBOX.contains(point) for point in points):
# #         return True
# #     return False


# @callback(
#     Output("from-location", "options"),
#     [Input("from-location", "search_value")],
# )
# def update_from_options(search_value):
#     """Update 'From Location' dropdown options."""
#     return get_geocoding_options(search_value)


# @callback(
#     Output("to-location", "options"),
#     [Input("to-location", "search_value")],
# )
# def update_to_options(search_value):
#     """Update 'To Location' dropdown options."""
#     return get_geocoding_options(search_value)


# @callback(
#     Output("route-map", "children"),
#     [
#         Input("plan-routes", "n_clicks"),  # Trigger when button is clicked
#         Input("layer-switch", "value"),
#         Input("avoid-hotspots", "value"),
#         Input("from-location", "value"),
#         Input("to-location", "value"),
#     ],
# )
# def render_map(n_clicks, layers, avoid_hotspots, from_value, to_value):
#     # Wait for button click
#     if not n_clicks or n_clicks < 1:
#         return no_update  # Do not update anything until button is clicked

#     # Debugging log
#     print(f"Button clicked {n_clicks} times, from_value: {from_value}, to_value: {to_value}")

#     # Ensure both locations are selected
#     if not from_value or not to_value:
#         return html.Div("Please select both starting and destination locations.")

#     layers_list = []

#     # Add COVID hotspots layer if selected
#     if layers and 1 in layers:
#         layers_list.append(get_covid_layer())

#     # Add route layer if locations are provided
#     from_point = get_point_from_dropdown(from_value)
#     to_point = get_point_from_dropdown(to_value)
#     if from_point and to_point:
#         if avoid_hotspots:
#             route_layer, _ = get_route_avoiding_hotspots(from_point, to_point)
#         else:
#             route_layer, _, _, _ = get_route_layer(from_point, to_point)
#         layers_list.append(route_layer)

#     # Map view state
#     view_state = pdk.ViewState(latitude=28.6139, longitude=77.2090, zoom=11, pitch=50)
#     return dash_deck.DeckGL(
#         pdk.Deck(layers=layers_list, initial_view_state=view_state).to_json(),
#         id="deck-gl",
#         mapboxKey=MAPBOX_ACCESS_TOKEN,
#         style={"height": "80vh"},
#     )


# # Helper Functions
# def get_point_from_dropdown(value):
#     """Convert dropdown value to a Point."""
#     if value:
#         data = json.loads(value)
#         print(data)
#         return Point(data["center"][0], data["center"][1])
#     return None


# def get_route_layer(from_point, to_point):
#     """Generate the route layer."""
#     coords = f"{from_point.x},{from_point.y};{to_point.x},{to_point.y}"
#     try:
#         response = requests.get(DIRECTIONS_URL.format(coords), params=DIRECTIONS_REQ_PARAMS).json()
#         route = response.get("routes", [])[0]
#         if route:
#             coordinates = route["geometry"]["coordinates"]
#             return pdk.Layer(
#                 "LineLayer",
#                 pd.DataFrame({"coordinates": coordinates}),
#                 get_path="coordinates",
#                 get_width=4,
#                 get_color=[255, 0, 0],
#             ), None, route["distance"], route["duration"]
#     except Exception as e:
#         print(f"Error fetching route: {e}")
#     return None, None, 0, 0


# def get_route_avoiding_hotspots(from_point, to_point):
#     """Generate route layer avoiding hotspots."""
#     origin = ox.nearest_nodes(GRAPH, from_point.x, from_point.y)
#     destination = ox.nearest_nodes(GRAPH, to_point.x, to_point.y)
#     route = nx.shortest_path(GRAPH, origin, destination, weight="Weigh")
#     coordinates = [[GRAPH.nodes[node]["x"], GRAPH.nodes[node]["y"]] for node in route]
#     return pdk.Layer(
#         "LineLayer",
#         pd.DataFrame({"coordinates": coordinates}),
#         get_path="coordinates",
#         get_width=4,
#         get_color=[0, 255, 0],
#     ), len(route)


# def get_covid_layer():
#     """Generate the COVID hotspots layer."""
#     df = pd.read_csv(COVID_HOTSPOTS_FILE)
#     return pdk.Layer(
#         "ScatterplotLayer",
#         df,
#         get_position=["lng", "lat"],
#         get_radius=50,
#         get_fill_color=[255, 0, 0],
#         pickable=True,
#     )
