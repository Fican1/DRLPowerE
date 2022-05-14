# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:34:50 2022

@author: fican
"""

"""
该文件用于py调用matlab仿真使用
"""

import matlab
import matlab.engine
import time
import numpy as np
import matplotlib.pyplot as plt


class CricuitEnv:
    # 初始化
    def __init__(self):
        pass
    
    # 仿真初始化
    def simInit(self):
        pass
    
    # 使用matlab进行仿真
    def callMatlabSim(self):
        pass
    
    # 返回action的观测值
    def RLStep(self,action):
        pass
    
    # 计算观测值
    def calFitness(self):
        pass
    
'''
eng = matlab.engine.start_matlab()
env_name = 'simpleSinEnvV2'
eng.load_system(env_name)

eng.set_param('simpleSinEnvV2/Constant', 'value', str(0), nargout=0) # 初始化控制量u为0
eng.set_param('simpleSinEnvV2/pause_time', 'value', str(1), nargout=0) # 初始化第一个内部暂停时间为1s
eng.set_param(env_name, 'StopTime', str(5), nargout=0) # 设定仿真截止时间
eng.set_param(env_name, 'SimulationCommand', 'start', nargout=0) # 开启控制，会在1.1s自动pause
# 此处应该在1.1s时pause, 然后修改pause_time为2
t = np.array(eng.eval('out.t.Data')).reshape(-1)
print( 'Time: {:.2f}'.format(t[-1]))
for i1 in range(2,6,1):
    eng.set_param('simpleSinEnvV2/Constant', 'value', str(i1), nargout=0)
    eng.set_param('simpleSinEnvV2/pause_time', 'value', str(i1), nargout=0)
    eng.set_param(env_name, 'SimulationCommand', 'continue', nargout=0)
    t = np.array(eng.eval('out.t.Data')).reshape(-1)
    print( 'Time: {:.2f}'.format(t[-1]))

eng.set_param(env_name, 'SimulationCommand', 'stop', nargout=0)
t = np.array(eng.eval('out.t.Data'))
y = np.array(eng.eval('out.y.Data'))
eng.quit()
fig = plt.figure(figsize=(5, 5))
plt.plot(t, y, 'or-')
plt.show()
eng.quit() # quit Matlab engine
'''