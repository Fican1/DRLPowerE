# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:01:45 2022

@author: fican
使用Qlearning，这部分为Qlearning的思维决策文件
"""


import numpy as np
import pandas as pd


class QLearning:
    def __init__(self, actions, learningRate=0.01, rewardDecay=0.9, eGreedy=0.9):
        self.actions = actions  # 行为
        self.lr = learningRate # 学习率
        self.gamma = rewardDecay # 奖励衰减
        self.epsilon = eGreedy # 贪婪度
        self.qTable = pd.DataFrame(columns=self.actions, dtype=np.float64) # q值表

    def chooseAction(self, observation): # 行为决策
        self.checkStateExist(observation)
        if np.random.uniform() < self.epsilon: # 选择最佳的行为，既q值最高
            pass
        else:
            # 随机选择
            pass
        return action

    def learn(self, s, a, r, s_): # 学习过程
        # q估计（qPredict）源于qTable
        if s_ != 'terminal': #如果结束
            # qTarget = 奖励值 + 奖励衰减*qTable的最大值
        else:# 行为还没结束
           # qTarget = 奖励值
        # q表格等于q现实-q估计


    def checkStateExist(self, state):
        # 更新时会对qTable一直更新，如果有新的动作就把值贴到后面