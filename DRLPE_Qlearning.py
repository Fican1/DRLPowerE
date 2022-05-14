# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:01:45 2022

@author: fican
使用Qlearning，这部分为Qlearning的思维决策文件
"""


import numpy as np
import pandas as pd


class QLearning:
    def __init__(self, statesNum, learningRate=0.01, rewardDecay=0.9, eGreedy=0.9):
        self.ALPHA = learningRate # 学习率
        self.GAMMA = rewardDecay # 奖励衰减
        self.EPSILON = eGreedy # 贪婪度
        #self.qTable = pd.DataFrame(columns=self.actions, dtype=np.float64) # q值表
        self.ACTION = ['increase', 'decrease'] # 行为决策
        self.statesNum = statesNum # 管子数量
        self.qTable = [] # q表，取决于电路管子数量
        
    def buildQtable(self):# 维度，动作
        qTable = pd.DataFrame(
            np.zeros((self.statesNum, len(self.actions))),     # q_table 的初始值 n_states为行数， len(actions)为列数
            columns=self.actions,    # 列的名字
        )
    '''
    def chooseAction(self, observation): # 行为决策
        self.checkStateExist(observation)
        if np.random.uniform() < self.epsilon: # 选择最佳的行为，既q值最高
            qTarget = R + GAMMA * qTable.iloc[stateNext, :].max()
        else:
            # 随机选择
            pass
        return action
    '''
    def chooseAction(self, state):# state代表第几行，表示球的位置 
        stateActions = qTable.iloc[state, :] # 输出小球状态那一行的q值,既获取action中，left和right的值
        if(np.random.uniform() > self.EPSILON) or ((stateActions == 0).all()): 
            # 如果行动那一栏全部为空或者超过贪婪度，代表要随机选取行动
            actionName = np.random.choice(self.ACTION)# 随机选取
        else:# 正常情况下，贪婪选取（选择最优的）
            actionName = stateActions.idxmax() # 选取表中最大值
        return actionName

    def learn(self, state, action, reward, stateNext): # 学习过程
        # q估计（qPredict）源于qTable
        qPredict = qTable.loc[state, action] # q预测值是根据当前的状态和动作确定值
        if stateNext != 'terminal': # 如果没结束
            # qTarget = 奖励值 + 奖励衰减*qTable的最大值
            qTarget = reward + self.GAMMA * qTable.iloc[stateNext, :].max()   # 只要下一步没到终点
        else:
           # qTarget = 奖励值
            qTarget = reward
        # q表格等于q现实-q估计
        qTable.loc[state, action] += self.ALPHA * (qTarget - qPredict)  # 更改q表中的数据

    #def checkStateExist(self, state):
        # 更新时会对qTable一直更新，如果有新的动作就把值贴到后面