DEFAULT_INIT_AMOUNT = 1000
DEFAULT_RESTAKE_COST = 0.0002
DEFAULT_STAKING_REWARD_RATE = 0.13


class StakingConfig:
    def __init__(self,
                 init_amount=DEFAULT_INIT_AMOUNT,
                 restake_cost=DEFAULT_RESTAKE_COST,
                 staking_reward_rate=DEFAULT_STAKING_REWARD_RATE) -> None:
        self._init_amount = init_amount
        self._restake_cost = restake_cost
        self._staking_reward_rate = staking_reward_rate


class StakingConfigSingleton:
    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = StakingConfig()
        return cls._instance