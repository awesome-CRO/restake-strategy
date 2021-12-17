import streamlit as st
import pandas as pd

from src.reward import RewardAnalyzer


def render_analysis():
    analyzer = RewardAnalyzer()
    analyze_range = range(1, 360, 20)
    possible_rewards = analyzer.compute_possible_rewards(analyze_range)
    analysis_result = pd.DataFrame()
    analysis_result['index'] = analyze_range
    analysis_result['final_amount'] = possible_rewards
    analysis_result.set_index('index')
    st.line_chart(analysis_result)
