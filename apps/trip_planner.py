import json
from dash import dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import pandas as pd
import requests
from shapely.geometry import box, Point
import pickle
import networkx as nx
import osmnx as ox
from apps.utils import get_geocoding_options
from config import MAPBOX_ACCESS_TOKEN, DIRECTIONS_URL, directions_req_params

# Register the page
register_page(__name__, path="/trip-planner", name="Trip Planner")

# Configure osmnx settings
ox.settings.use_cache = True  # Enable caching to reuse downloaded data
ox.settings.log_console = True  # Log output to the console

# Delhi Boundary Configuration
DELHI_BOUNDARY = [76.8388830269287, 28.4042620003073, 77.3464387601731, 28.8835889894397]
DELHI_BBOX = box(*DELHI_BOUNDARY)

# Load Graph Data
with open("assets/path_finder/delhi_graph_data.pkl", "rb") as f:
    GRAPH = pickle.load(f)
    
TO_LOCATION = []
FROM_LOCATION = []

def extract_value_from_location(location_list):
    extract_value = [v for v in location_list if v is not None]
    if len(extract_value)>0:
        return {'value':extract_value[-1]}
    else:
        return {'value':"Unknown"}

def update_from_location(from_location):
    global FROM_LOCATION  # Declare global to modify the global variable
    FROM_LOCATION.append(from_location)
    # Remove the first two elements if the list has more than 7 items.
    if len(FROM_LOCATION) > 7:
        FROM_LOCATION = FROM_LOCATION[2:]

def update_to_location(to_location):
    global TO_LOCATION  # Declare global to modify the global variable
    TO_LOCATION.append(to_location)
    # Remove the first two elements if the list has more than 7 items.
    if len(TO_LOCATION) > 7:
        TO_LOCATION = TO_LOCATION[2:]
    #print("update to location")
# Constants
COVID_HOTSPOTS_FILE = "assets/path_finder/new.csv"
DIRECTIONS_REQ_PARAMS = {"geometries": "geojson"}

# Layout for the Trip Planner page
layout=dbc.Container(
    [
        dbc.Row(
            [
                # Left Column: Trip Planner
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Trip Planner", className="my-2"),
                                html.P(
                                    """Plan your safe trip within Delhi. 
                                    COVID hotspots and other factors are considered."""
                                ),
                                # Dropdown for "From Location"
                                dbc.Row(
                                    dcc.Dropdown(
                                        id="from-location",
                                        placeholder="From Location",
                                        options=[],
                                        value=None,
                                        style={"color": "black"},
                                        className="mb-3 dropdown-black-text",
                                        persistence=True,
                                        persistence_type="local",
                                    ),
                                    className="mb-3",
                                ),
                                # Dropdown for "To Location"
                                dbc.Row(
                                    dcc.Dropdown(
                                        id="to-location",
                                        placeholder="To Location",
                                        options=[],
                                        value=None,
                                        style={"color": "black"},
                                        className="mb-3 dropdown-black-text",
                                        persistence=True,
                                        persistence_type="local",
                                    ),
                                    className="mb-3",
                                ),
                                # Avoid COVID hotspots switch
                                dbc.Row(
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Avoid COVID Hotspots", "value": 1},
                                        ],
                                        value=[],
                                        id="avoid-hotspots",
                                        switch=True,
                                    ),
                                    className="mb-3",
                                ),
                                # Layer selection
                                dbc.Row(
                                    [
                                        dbc.Label("Layers"),
                                        dbc.Checklist(
                                            options=[
                                                {"label": "Show COVID Hotspots", "value": 1},
                                            ],
                                            value=[1],
                                            id="layer-switch",
                                            switch=True,
                                        ),
                                    ],
                                    className="mb-3",
                                ),
                                # Plan Routes Button
                                dbc.Row(
                                    dbc.Button(
                                        "Plan Routes",
                                        id="plan-routes",
                                        color="primary",
                                        className="mt-3",
                                        size="lg",
                                    )
                                ),
                            ]
                        ),
                        className="mb-3",
                    ),
                    width=4,
                ),
                # Right Column: Selected Locations and Route Map
                dbc.Col(
                    [
                        # Row for Small Horizontal Cards
                        dbc.Row(
                            [
                                # Selected Locations Card 1
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H6("From Location", className="card-title"),
                                                html.Div(
                                                    id="selected-from-location",
                                                    children="From location will appear here.",
                                                    style={"font-size": "0.8em", "color": "white"},
                                                ),
                                            ]
                                        ),
                                        style={"height": "100%"},
                                    ),
                                    width=6,  # Each small card takes 50% width
                                ),
                                # Selected Locations Card 2
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H6("To Location", className="card-title"),
                                                html.Div(
                                                    id="selected-to-location",
                                                    children="To location will appear here.",
                                                    style={"font-size": "0.8em", "color": "white"},
                                                ),
                                            ]
                                        ),
                                        style={"height": "100%"},
                                    ),
                                    width=6,  # Each small card takes 50% width
                                ),
                            ],
                            style={"height": "20%"},  # Allocate 20% of the column height
                            className="mb-3",
                        ),
                        # Route Map Card
                        dbc.Row(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("Route Map", className="card-title"),
                                        html.Div(id="route-map"),
                                    ]
                                ),
                            ),
                            style={"height": "80%"},  # Allocate 80% of the column height
                        ),
                    ],
                    width=8,
                ),
            ],
        ),
    ],
    fluid=True,
)


@callback(
    Output("selected-from-location", "children"),
    Input("from-location", "value"),

)
def update_selected_locations(from_location):
    update_from_location(from_location)
    #print("location is here: " + str(from_location))
    val = extract_value_from_location(FROM_LOCATION).get('value')
    if val=="Unknown" or not val:
        return "Unknown"
    else:
        return json.loads(val).get("place_name", "Unknown")

@callback(
    Output("selected-to-location", "children"),
    Input("to-location", "value"),
)
def update_selected_locations(to_location):
    update_to_location(to_location)
    #print("location is here: " + str(to_location))
    val = extract_value_from_location(TO_LOCATION).get('value')
    if val=="Unknown" or not val:
        return "Unknown"
    else:
        return json.loads(val).get("place_name", "Unknown")



# Callback to update dropdown options
@callback(
    Output("from-location", "options"),
    [Input("from-location", "search_value")],
    prevent_initial_call=True,  # Prevent unnecessary initial execution
)
def update_from_options(search_value):
    if not search_value:
        return []
    return get_geocoding_options(search_value)

@callback(
    Output("to-location", "options"),
    [Input("to-location", "search_value")],
    prevent_initial_call=True,  # Prevent unnecessary initial execution
)
def update_to_options(search_value):
    if not search_value:
        return []
    return get_geocoding_options(search_value)


# Callback to render the map on button click
@callback(
    Output("route-map", "children"),
    [
        Input("plan-routes", "n_clicks"),
    ],
    [
        State("layer-switch", "value"),
        State("avoid-hotspots", "value"),
        State("from-location", "value"),
        State("to-location", "value"),
    ],
    prevent_initial_call=True,  # Prevent callback from running on page load
)
def render_map(n_clicks, layers, avoid_hotspots, from_value, to_value):
    # print(f"Button clicked {n_clicks} times, from_value: {from_value}, to_value: {to_value}")

    from_value = FROM_LOCATION
    to_value = TO_LOCATION
    # Your existing logic to generate map layers
    from_point = get_point_from_dropdown(from_value)
    to_point = get_point_from_dropdown(to_value)

    # Generate COVID hotspots and route layers for Leaflet
    layers_list = []

    # Add COVID hotspots layer as Scatterplot
    if layers and 1 in layers:
        covid_layer = get_covid_layer()
        for point in covid_layer:
            layers_list.append(dl.CircleMarker(
                center=point,
                radius=2,
                color="red",
                fillColor="red",
                fillOpacity=0.2,
            ))

    # Add walking route
    if from_point and to_point:
        route_coords = get_route_layer(from_point, to_point)
        if avoid_hotspots:
            avoid_route_coords = get_route_avoiding_hotspots(from_point, to_point)
            layers_list.append(dl.Polyline(positions=avoid_route_coords, color="green", weight=5))
        layers_list.append(dl.Polyline(positions=route_coords, color="blue", weight=5))

        # Leaflet map layout
        return dl.Map(
            center=[28.6139, 77.2090],
            zoom=12,
            children=[
                dl.TileLayer(url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", attribution="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/'>CARTO</a>"),
                *layers_list,
                dl.Marker(position=[from_point.y, from_point.x], children=dl.Tooltip("From Location")),
                dl.Marker(position=[to_point.y, to_point.x], children=dl.Tooltip("To Location")),
            ],
            style={"height": "60vh", "width": "98%"},
        )
    else:
        return dl.Map(
            center=[28.6139, 77.2090],
            zoom=12,
            children=[
                dl.TileLayer(url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", attribution="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/'>CARTO</a>"),
                *layers_list
            ],
            style={"height": "60vh", "width": "98%"},
        )

# Helper Functions
def get_point_from_dropdown(value):
    extract_value = [v for v in set(value) if v is not None]
    if len(extract_value)>0:
        data = json.loads(extract_value[-1])
        return Point(data["center"][0], data["center"][1])
    return None

def get_route_layer(from_point, to_point):
    coords = f"{from_point.x},{from_point.y};{to_point.x},{to_point.y}"
    try:
        response = requests.get(DIRECTIONS_URL.format(coords), params=directions_req_params).json()
        route = response.get("routes", [])[0]
        if route:
            return [[coord[1], coord[0]] for coord in route["geometry"]["coordinates"]]
    except Exception as e:
        print(f"Error fetching route: {e}")
    return []

def get_route_avoiding_hotspots(from_point, to_point):
    origin = ox.nearest_nodes(GRAPH, from_point.x, from_point.y)
    destination = ox.nearest_nodes(GRAPH, to_point.x, to_point.y)
    route = nx.shortest_path(GRAPH, source=origin, target=destination, weight="Weigh")
    return [[GRAPH.nodes[node]["y"], GRAPH.nodes[node]["x"]] for node in route]

def get_covid_layer():
    df = pd.read_csv(COVID_HOTSPOTS_FILE)
    return df[["lat", "lng"]].values.tolist()