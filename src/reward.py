from typing import List

from src.config import StakingConfigSingleton


class RewardAnalyzer:
    def __init__(self) -> None:
        self.init_amount = StakingConfigSingleton.get().init_amount
        self.rate = StakingConfigSingleton.get().staking_reward_rate
        self.cost = StakingConfigSingleton.get().restake_cost
        self.annual_length = 365.0

    def compute_possible_rewards(self,
                                 interval_range: List[float]) -> List[float]:
        total_amount_list = []
        for interval_length in interval_range:
            total_amount = self.compute_total_amount_with_interval_length(
                interval_length)
            total_amount_list.append(total_amount)
        return total_amount_list

    def compute_total_amount_with_interval_length(
            self, interval_length: float) -> float:
        cycles = int(self.annual_length / interval_length)
        current_amount = self.init_amount
        for _ in range(cycles):
            interval_reward = self.compute_interval_reward(
                current_amount, interval_length)
            current_amount += (interval_reward - self.cost)
        return current_amount

    def compute_interval_reward(self, current_amount: float,
                                interval_length: float) -> float:
        annual_reward = current_amount * self.rate
        interval_reward = annual_reward * interval_length / self.annual_length
        return interval_reward
