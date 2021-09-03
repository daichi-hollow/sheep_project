import random 
import numpy as np 
import matplotlib.pyplot as plt

# random.seed(1)
def main():
    
    sheep_w = [1,1,1,1,1,1,1,1,1,1] 
    wolf_w = [1,1,1,1,1.5,2,2.5,3,3.5,4] 
    times = [0,1,2,3,4,5,6,7,8,9]

    for i in range(int(input("count?"))):
        
        sheep_times = random.choices(times,weights=sheep_w,k=5)
        wolf_time = random.choices(times,weights=wolf_w)

        bool = np.array(sheep_times) == wolf_time # bool型を作成

        alive_times = np.array(sheep_times)[bool == 0] # timeを抽出
        dead_times = np.array(sheep_times)[bool == 1]

        for i in set(alive_times):
            sheep_w[i] += 0.1
        for i in set(dead_times):
            sheep_w[i] -= 0.1

    print(np.round(sheep_w))
    print(sheep_w)
    x = [1,2,3,4,5,6,7,8,9,10]
    y1 = np.array(np.round(sheep_w))
    y2 = wolf_w * np.array(np.mean(sheep_w)) * 0.3
    plt.bar(np.array(x),y1,width=0.3,label="sheeps")
    plt.bar(np.array(x)+0.3,y2,width=0.3,label="wolves")
    plt.legend(loc=2)
    # plt.xticks(x,np.array(x)+1)
    plt.show()
    label = ["1","2","3","4","5","6","7","8","9","10"]
    plt.pie(sheep_w,labels=label, counterclock=False, startangle=90)
    
    
    
if __name__ == "__main__":
  main()

