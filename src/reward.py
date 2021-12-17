from typing import List


class RewardAnalyzer:
    def compute_possible_rewards(self,
                                 interval_range: List[float]) -> List[float]:
        raise NotImplementedError()

    def _compute_total_reward_with_interval(self, interval: float) -> float:
        return 0