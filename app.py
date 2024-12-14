import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Initialize Dash app
app = dash.Dash(
    __name__,
    pages_folder="apps",
    use_pages=True,  # Enables Dash Pages for routing
    external_stylesheets=[dbc.themes.DARKLY],
)
app.title = "Mobility Dashboard"
server = app.server

# Define the navigation bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/logo.png", height="40px")),
                        dbc.Col(dbc.NavbarBrand("Mobility Dashboard", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href="/")),
                        dbc.NavItem(dbc.NavLink("Trip Planner", href="/trip-planner")),
                        dbc.NavItem(dbc.NavLink("Bike Trips", href="/bike-trips")),
                        dbc.NavItem(dbc.NavLink("Bikebility", href="/bike-index")),
                        dbc.NavItem(dbc.NavLink("Jobs Visualization", href="/jobs")),
                        dbc.NavItem(dbc.NavLink("About Us", href="/about")),
                    ],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)


# Callback for toggling navbar
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


# Define app layout with dynamic page content
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        dash.page_container,  # Automatically includes pages
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
