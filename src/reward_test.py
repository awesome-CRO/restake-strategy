from src.config import StakingConfigSingleton
from src.reward import RewardAnalyzer


def setConfig():
    config = StakingConfigSingleton.get()
    config.init_amount = 100
    config.restake_cost = 1
    config.staking_reward_rate = 0.1


def test_compute_interval_reward():
    setConfig()
    analyzer = RewardAnalyzer()
    reward = analyzer.compute_interval_reward(100, 365)
    assert (reward == 10)
    reward = analyzer.compute_interval_reward(100, 36.5)
    assert (reward == 1)
