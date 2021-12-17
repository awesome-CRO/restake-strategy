import streamlit as st

from src.config import StakingConfigSingleton


def render_sidebar():
    st.sidebar.header('CRO Staking Strategy')
    init_amount = st.sidebar.number_input('Initial CRO Amount')
    staking_reward_rate = st.sidebar.number_input('Staking Reward (p.a.)')
    restake_cost = st.sidebar.number_input('Restake Cost (fixed CRO)')
    config = StakingConfigSingleton.get()
    config.init_amount = init_amount
    config.staking_reward_rate = staking_reward_rate
    config.restake_cost = restake_cost