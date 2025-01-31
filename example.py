#!/bin/python
import gym, gym_mupen64plus
from gym import wrappers
from os import path

env = gym.make('Mario-Kart-Luigi-Raceway-v0')
video_log_path = '/src/gym-mupen64plus/gym_mupen64plus/ROMs/videos'
env = wrappers.Monitor(env, video_log_path,write_upon_reset=True, force=True,
                           video_callable=lambda x: True)
env.reset()

print("NOOP waiting for green light")
for i in range(18):
    (obs, rew, end, info) = env.step([0, 0, 0, 0, 0]) # NOOP until green light

print("GO! ...drive straight as fast as possible...")
for i in range(50):
    (obs, rew, end, info) = env.step([0, 0, 1, 0, 0]) # Drive straight

print("Doughnuts!!")
for i in range(10):
    if i % 100 == 0:
        print("Step " + str(i))
    (obs, rew, end, info) = env.step([-80, 0, 1, 0, 0]) # Hard-left doughnuts!
    (obs, rew, end, info) = env.step([-80, 0, 0, 0, 0]) # Hard-left doughnuts!

# env.reset()
# print("Reseted!")
for i in range(10):
    env.step([-80, 0, 1, 0, 0])

done = False
while not done:
    obs, rew, done, info = env.step([-80, 0, 1, 0, 0])

raw_input("Press <enter> to exit... ")

env.reset()
env.close()
