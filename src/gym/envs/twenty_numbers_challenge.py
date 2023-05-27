import gymnasium as gym
import numpy as np
from gymnasium import spaces
import random

class TwentyNumbersChallenge(gym.Env):
    def __init__(self) -> None:

        self.vector_size = 20
        self.vector = np.zeros(self.vector_size, dtype=np.int32)
        self.random_number = random.randint(1, 1000)

        self.observation_space = spaces.Dict(
            {
                "random_number": spaces.Box(low=0, high=1000, dtype=np.int64),
                "list_of_numbers" : spaces.Box(low=0,high=1000, shape=(self.vector_size,), dtype=np.int32)
            }
        )

        self.action_space = spaces.Discrete(20)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.random_number = random.randint(1, 10000)
        self.vector = np.zeros(self.vector_size, dtype=np.int32)

        return 

    def step(self, action):
        pass

    def render(self):
        print("Current list of numbers is: ", self.vector)
        print("The random number is: ", self.random_number)

    def close(self):
        pass

if __name__ == '__main__':

    env = TwentyNumbersChallenge()
    print("------Beginning of the game---------")
    env.reset()
    env.render()
