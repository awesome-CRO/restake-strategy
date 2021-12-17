from typing import List

from src.config import StakingConfigSingleton


class RewardAnalyzer:
    def __init__(self) -> None:
        self.current_amount = StakingConfigSingleton.get().init_amount
        self.rate = StakingConfigSingleton.get().staking_reward_rate
        self.cost = StakingConfigSingleton.get().restake_cost

    def compute_possible_rewards(self,
                                 interval_range: List[float]) -> List[float]:
        raise NotImplementedError()

    def _compute_total_reward_with_interval(self, interval: float) -> float:
        return 0

    def _compute_interval_reward(self, interval_length: float) -> float:
        return 0