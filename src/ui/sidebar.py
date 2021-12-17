import streamlit as st

from src.config import StakingConfigSingleton


def render_sidebar():
    st.sidebar.header('CRO Staking Strategy')
    init_amount = st.sidebar.number_input('Initial CRO Amount',
                                          step=1e-6,
                                          format="%.6f")
    staking_reward_rate = st.sidebar.number_input('Staking Reward (p.a.)',
                                                  step=1e-6,
                                                  format="%.6f")
    restake_cost = st.sidebar.number_input('Restake Cost (fixed CRO)',
                                           step=1e-6,
                                           format="%.6f")
    config = StakingConfigSingleton.get()
    config.init_amount = init_amount
    config.staking_reward_rate = staking_reward_rate
    config.restake_cost = restake_cost
    ready = st.sidebar.button('Start Analysis')
    config.ready = ready