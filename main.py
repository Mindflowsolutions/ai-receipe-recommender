import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home

st.set_page_config(
    page_title="AI Recipe Finder",
    page_icon="🍴",
    layout="wide",  # Full-width layout
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar Design with Enhanced Styles
        with st.sidebar:
            st.markdown(
                """
                <style>
                /* Sidebar background */
                .css-1d391kg { 
                    background-color: #121212; /* Darker background for sidebar */
                    padding: 20px;
                    border-right: 2px solid #07a9e3;
                }

                /* Sidebar menu items */
                .css-1l02zno {
                    padding: 0;
                }

                /* Add a glow effect on hover */
                .nav-link:hover {
                    background-color: rgba(0, 212, 255, 0.1); /* Soft glow on hover */
                    color: #07a9e3;
                }

                /* Custom hover for selected item */
                .selected {
                    background: linear-gradient(90deg, rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 35%, rgba(0, 212, 255, 1) 100%);
                    box-shadow: 0px 4px 15px rgba(0, 212, 255, 0.6);
                    font-weight: bold;
                    color: white;
                }

                /* Title text in sidebar */
                .menu-title {
                    font-size: 24px;
                    font-weight: bold;
                    color: #07a9e3;
                    text-align: center;
                    margin-bottom: 15px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Sidebar Menu
            st.markdown('<div class="menu-title">AI Recipe Finder</div>', unsafe_allow_html=True)  # Add a custom title
            app = option_menu(
                menu_title='',  # Menu title is replaced with custom title
                options=['Home', 'Account', 'About'],
                icons=['house', 'person', 'info-circle'],  # Icons for each section
                menu_icon='list',  # Icon for the sidebar menu
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#121212"},
                    "icon": {"color": "white", "font-size": "22px"}, 
                    "nav-link": {
                        "font-size": "18px",
                        "color": "white",
                        "text-align": "left",
                        "margin": "10px",
                        "border-radius": "5px",
                        "--hover-color": "#07a9e3",
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(90deg, rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 35%, rgba(0, 212, 255, 1) 100%)",
                        "color": "white",
                        "font-weight": "bold",
                        "box-shadow": "0px 4px 15px rgba(0, 212, 255, 0.6)",
                    },
                },
            )
            
        # Load the corresponding app page
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "About":
            about.app()

# Create an instance of MultiApp and call run
app = MultiApp()
app.run()


     