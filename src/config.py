DEFAULT_INIT_AMOUNT = 1000
DEFAULT_RESTAKE_COST = 0.0002
DEFAULT_STAKING_REWARD_RATE = 0.13


class StakingConfig:
    def __init__(self,
                 init_amount=DEFAULT_INIT_AMOUNT,
                 restake_cost=DEFAULT_RESTAKE_COST,
                 staking_reward_rate=DEFAULT_STAKING_REWARD_RATE) -> None:
        self.init_amount = init_amount
        self.restake_cost = restake_cost
        self.staking_reward_rate = staking_reward_rate
        self.ready = False


class StakingConfigSingleton:
    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = StakingConfig()
        return cls._instance