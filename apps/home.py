import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__, path="/")
# Helper function to create cards
def create_card(title, button_text, button_link):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H5(title, className="text-center"),
                style={"height": "10vh"},
            ),
            dbc.CardFooter(
                dbc.Button(
                    button_text,
                    href=button_link,
                    color="primary",
                    className="mt-3",
                )
            ),
        ],
        body=True,
        color="dark",
        outline=True,
    )

# Layout for the Welcome page
layout = html.Div(
    [
        dbc.Container(
            [
                # Title Section
                dbc.Row(
                    dbc.Col(
                        html.H1(
                            "Welcome to the Mobility Dashboard",
                            className="text-center",
                        ),
                        className="mb-5 mt-5",
                    )
                ),
                # Description Section
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    html.Div([
                                        html.P("MobilitySafe: Increasing safety and sustainability of micro-mobility modes in pandemic"),
                                        html.P("""The MobilitySafe project aims to develop a map-based tool to help individuals navigate cities in times of pandemic and conflict.
                                                Walking and Cycling in India.
                                                In times of pandemic and conflict, public transport and vehicle sharing services are frequently halted or avoided, and many people turn to cycling or walking for small distances.
                                                By partnering and working with urban development companies and agencies, such as GIZ India and Deloitte India, alongside local authorities, MobilitySafe aims to provide an open app and web-based utility to help users determine safe walking and cycling routes that avoid transmission spots or conflict zones.
                                                Led by Dr. Devanjan Bhattacharya, Trained Research Fellow, the project will initially focus on the Indian pilot cities of Bhuvaneshwar and New Delhi, which were selected by the German Government for special support on their way to becoming Smart Cities.
                                        """),
                                        html.P("The Mobility Dashboard is live, and the data is available on this site and also on request."),
                                        html.P("MobilitySafe is funded by the ESRC Impact Acceleration Account scheme."),
                                        html.Hr(),  # Add a horizontal rule to separate the main content from the key features
                                        html.H5("Key Features"),
                                        html.Ul([
                                            html.Li("Real-time updates: Stay informed about changing conditions."),
                                            html.Li("Customizable routes: Plan your journey based on your preferences."),
                                            html.Li("Community-driven: Help us make your city safer for everyone."),
                                        ]),
                                        html.P("Let's build a safer, healthier city together."),
                                    ], style={"text-align":"justify"})
                                )
                            ),
                            className="mb-4",
                            width=7
                        ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                html.Img(src="assets/safepathimage.jpeg", className="card-img-top"), style={"text-align":"justify"},
                            ),
                        ),
                        className="mb-4",
                        width=5
                    )
                    ]
                ),


                # Cards Section
                dbc.Row(
                    [
                        dbc.Col(
                            create_card(
                                "Read more about our work",
                                "Read more..",
                                "https://www.law.ed.ac.uk/research/research-projects/mobilitysafe",
                            ),
                            className="mb-4",
                        ),

                        dbc.Col(
                            create_card(
                                "Check out demo",
                                "Demo",
                                "http://65.2.142.95:8000/trip-planner",
                            ),
                            className="mb-4",
                        ),
                    ],
                    className="mb-5",
                ),
                # Acknowledgment Section
                dbc.Row(
                    dbc.Col(
                        html.A(
                            "Special thanks to the University of Edinburgh for funding this project",
                            href="https://www.ed.ac.uk/",
                            className="text-center",
                        ), width=12
                    )
                ),
            ]
        )
    ]
)
