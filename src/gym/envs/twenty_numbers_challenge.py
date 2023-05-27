import gymnasium as gym
import numpy as np
from gymnasium import spaces

class TwentyNumbersChallenge(gym.Env):
    def __init__(self) -> None:
        self.observation_space = spaces.Dict(
            {
                "random_number": spaces.Box(low=0, high=1000, dtype=np.int64),
                "list_of_numbers": spaces.Discrete(n=20),
            }
        )

        self.action_space = spaces.Discrete(20)

    def reset(self, seed=None, options=None):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

    def close(self):
        pass
