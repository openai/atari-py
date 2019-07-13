import gym
import numpy as np


def main():
    def make_env():
        return gym.make("PongNoFrameskip-v4")

    venv = gym.vector.AsyncVectorEnv([make_env] * 3, context="fork")
    venv.reset()
    while True:
        print("loop")
        obs, rews, dones, infos = venv.step(venv.action_space.sample())


if __name__ == "__main__":
    main()