import streamlit as st

from src.config import StakingConfigSingleton
from src.ui.analysis import render_analysis
from src.ui.header import render_header
from src.ui.sidebar import render_sidebar

_ = StakingConfigSingleton.get()

st.set_page_config(layout='wide')

render_header()
render_sidebar()
render_analysis()