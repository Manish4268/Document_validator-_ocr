
import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats,adhar # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Pan Card", data_stats.app)
app.add_app("Adhar Card", adhar.app)

# The main app
app.run()