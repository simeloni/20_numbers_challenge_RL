import gymnasium as gym
from gymnasium import spaces


class TwentyNumbersChallenge(gym.Env):
    def __init__(self) -> None:
        self.observation_space = spaces.Discrete(20)
        self.action_space = spaces.Discrete(20)
