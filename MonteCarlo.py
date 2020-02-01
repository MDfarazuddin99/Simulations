import numpy as np
import matplotlib.pyplot as plt

ans = np.zeros(1000)

for t in range(1000):
    num_iterations = 1000
    exp_time = 0
    while(1):
        r = np.floor(np.random.uniform(0,3))
        if( r == 0):
            exp_time+=6
            ans[t] = exp_time
            break
        elif(r==1):
            exp_time+=3

        elif(r==2):
            exp_time+=9
print(ans[0:20])
print(ans[-20:])
mean = np.zeros(1000)+np.mean(ans)
plt.plot(mean,"r")
plt.plot(ans,)
# plt.x
plt.ylabel("Weight time, average={}".format(mean[0]))
plt.xlabel("experiments")
plt.show()
