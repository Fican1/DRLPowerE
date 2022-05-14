# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:00:15 2022

@author: fican

强化学习的运行主文件
"""

import DRLPE_sim 
import DRLPE_Qlearning 


def update():
    
        
        # 初始化 state 的观测值
        state = Env.reset()

        for episode in range(100): #训练回合数
            # RL 大脑根据 state 的观测值挑选 action
            action = RLQ.chooseAction()

            # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state 观测值, reward 和 done (是否是掉下地狱或者升上天堂)
            stateNext, reward, done = Env.RLStep(action)

            # RL 从这个序列 (state, action, reward, state_) 中学习
            RLQ.learn(state, action, reward, stateNext)
            
            # 将下一个 state 的值传到下一次循环
            state = stateNext

            

if __name__ == "__main__":
    Env = DRLPE_sim()
    RLQ = DRLPE_Qlearning()
    

