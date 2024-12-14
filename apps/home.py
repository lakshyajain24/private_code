import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__, path="/")
# Helper function to create cards
def create_card(title, button_text, button_link):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H4(title, className="text-center"),
                style={"height": "20vh"},
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
                    dbc.Col(
                        html.H5(
                            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                        ),
                        className="mb-4",
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.H5(
                            """Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer 
                            took a galley of type and scrambled it to make a type specimen book.""",
                        ),
                        className="mb-5",
                    )
                ),
                # Cards Section
                dbc.Row(
                    [
                        dbc.Col(
                            create_card(
                                "Read more about our work",
                                "Read more..",
                                "https://mobility-web-deploy.herokuapp.com",
                            ),
                            className="mb-4",
                        ),
                        dbc.Col(
                            create_card(
                                "Access the code used to build this dashboard",
                                "GitHub",
                                "https://github.com/mobility-dashboard",
                            ),
                            className="mb-4",
                        ),
                        dbc.Col(
                            create_card(
                                "Check out demo",
                                "Demo",
                                "https://mobility-web-deploy.herokuapp.com/trip-planner",
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
                        )
                    )
                ),
            ]
        )
    ]
)
