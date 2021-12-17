from src.config import StakingConfigSingleton
from src.ui.header import render_header
from src.ui.sidebar import render_sidebar

_ = StakingConfigSingleton.get()

render_header()
render_sidebar()