import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

from src.config import StakingConfigSingleton
from src.reward import RewardAnalyzer


def render_analysis():
    st.title('Compute Result')
    config = StakingConfigSingleton.get()
    if config.ready:
        analyzer = RewardAnalyzer()
        analyze_range = np.arange(1, 30, 1)
        possible_rewards = analyzer.compute_possible_rewards(analyze_range)
        baseline_final_amount = analyzer.compute_baseline_final_amount()
        analysis_result = pd.DataFrame()
        restake_interval_label = 'Restake Interval (days)'
        final_amount_label = 'Final Amount (CRO)'
        analysis_result[restake_interval_label] = analyze_range
        analysis_result[final_amount_label] = possible_rewards
        st.subheader('Restake Interval to Final Amount')
        st.write(analysis_result)
        st.write('Baseline Final Amount:', baseline_final_amount)
        y_range_min = min(possible_rewards) - 20
        y_range_max = max(possible_rewards) + 20
        y_data = alt.Y(final_amount_label,
                       scale=alt.Scale(domain=[y_range_min, y_range_max],
                                       clamp=True))
        chart = alt.Chart(analysis_result).mark_line().encode(
            x=restake_interval_label, y=y_data)
        st.altair_chart(chart, use_container_width=True)
    else:
        st.write('Please input the parameters in the sidebar.')
