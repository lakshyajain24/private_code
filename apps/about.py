import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__, path="/about")

# Helper function to generate team member cards
def create_team_member_card(name, img_src, role, description, link, link_text):
    return dbc.Card(
        [
            dbc.CardHeader(html.Img(src=img_src, className="card-img-top", alt=name)),
            dbc.CardFooter(
                dbc.Col(
                    [
                        html.H4(name),
                        html.Br(),
                        html.P(description),
                        html.Br(),
                        html.A(link_text, href=link, target="_blank"),
                        html.Br(),
                        html.P(f"Role: {role}"),
                    ],
                    className="text-center",
                ),
            ),
        ],
        body=True,
        color="dark",
        outline=True,
    )


layout = html.Div(
    [
        dbc.Container(
            [
                # Title Section
                dbc.Row(
                    dbc.Col(
                        html.H1("About Us", className="text-center"),
                        className="mb-5 mt-5",
                    )
                ),

                # Goals Section
                dbc.Row(
                    dbc.Col(
                        [
                            html.H3(
                                "Increasing safety and sustainability of micro-mobility modes in a pandemic",
                                className="text-center mb-4",
                            ),
                            html.H5("AIMS/GOALS:", className="mb-3 font-weight-bold"),
                            html.P(
                                """In this time of pandemic COVID-19, public vehicles like buses, metro, and vehicle-sharing services are either unavailable 
                                or avoided due to safety concerns. This situation has left users with limited options, leading to increased traffic despite reduced 
                                long-distance commuting. Cycling and walking are emerging as safe alternatives, and authorities are promoting bike lanes 
                                and walkways for safe local commutes. This project aims to promote safer, sustainable urban mobility solutions through 
                                multi-criteria route planning for cyclists and pedestrians."""
                            ),
                        ],
                        className="mb-5",
                    )
                ),

                # Approach Section
                dbc.Row(
                    dbc.Col(
                        [
                            html.H5("APPROACH:", className="mb-3 font-weight-bold"),
                            html.P(
                                """We propose a multi-criteria route planning technique that prioritizes user safety by avoiding potential COVID-19 hotspots 
                                such as hospitals, containment zones, and crowded areas. The system will visualize these hotspots and provide safer, 
                                shorter routes for walking and cycling. Authorities can use the data to plan bike lanes and walkways, ensuring better 
                                infrastructure and user safety."""
                            ),
                        ],
                        className="mb-5",
                    )
                ),

                # Outputs Section
                dbc.Row(
                    dbc.Col(
                        [
                            html.H5("OUTPUTS:", className="mb-3 font-weight-bold"),
                            html.P(
                                """The developed system will include a web portal providing real-time safe routes for users, based on data from civic 
                                authorities and spatial data providers. The visualization will display various zones (e.g., red, orange, green) and safe paths 
                                dynamically updated in real-time. The open-source architecture can be integrated into municipal portals."""
                            ),
                            html.A(
                                "Read the full research paper here.",
                                href="https://www.mdpi.com/2220-9964/10/8/571/htm",
                                target="_blank",
                            ),
                        ],
                        className="mb-5",
                    )
                ),

                # Team Members Section
                dbc.Row(
                    dbc.Col(html.H5("TEAM MEMBERS:", className="mb-3 font-weight-bold")),
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            create_team_member_card(
                                "Dr. Devanjan Bhattacharya",
                                "assets/devanjan.png",
                                "Principal Investigator",
                                """Marie Skłodowska-Curie Actions Fellow, University of Edinburgh.""",
                                "https://www.law.ed.ac.uk/people/dr-devanjan-bhattacharya",
                                "Profile",
                            ),
                            className="mb-4",
                        ),
                        dbc.Col(
                            create_team_member_card(
                                "Sumit Mishra",
                                "assets/sumit.png",
                                "Research Consultant",
                                """The Robotics Program, Korea Advanced Institute of Science and Technology.""",
                                "https://sumitmishra209.wixsite.com/mysite",
                                "Profile",
                            ),
                            className="mb-4",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            create_team_member_card(
                                "Atanshi Chaturvedi",
                                "assets/atanshi.png",
                                "Research Intern",
                                """Data Analyst, The Smart Cube, Noida, India.""",
                                "#",
                                "Profile",
                            ),
                            className="mb-4",
                        ),
                        dbc.Col(
                            create_team_member_card(
                                "Nikhil Singh",
                                "assets/nikhil.png",
                                "Research Intern",
                                """Department of Information Technology, Manipal University, Jaipur.""",
                                "#",
                                "Profile",
                            ),
                            className="mb-4",
                        ),
                    ]
                ),

                # Acknowledgment Section
                dbc.Row(
                    dbc.Col(
                        [
                            html.H5("Acknowledgment:", className="mb-3 font-weight-bold"),
                            html.P(
                                """This project is funded by the UKRI ESRC Impact Acceleration Grant and other funding bodies. We also acknowledge 
                                support from the European Union's Horizon 2020 research program."""
                            ),
                            html.Img(src="assets/uni.png", className="w-50 mb-3"),
                            html.Img(src="assets/giz.png", className="w-50"),
                        ],
                        className="mb-5",
                    )
                ),
            ]
        )
    ]
)
