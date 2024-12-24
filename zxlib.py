

def greet(name):
    return f"Hello, {name}!"

def say():
    print("Hello")
    
import matplotlib.pyplot as plt
def paint(image_data):
    plt.figure(figsize=(2, 2))
    plt.imshow(image_data, cmap='binary')

import pandas as pd
from pandas import DataFrame
    
def paint_history(history):
    # 将训练历史转换为DataFrame
    df = pd.DataFrame(history.history)
    # 设置图表大小
    plt.figure(figsize=(8, 5))
    # 绘制DataFrame中的数据
    df.plot()
    # 添加标题和标签
    plt.title('Model Training History')
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    # 显示网格
    plt.grid(True)
    # 显示图表
    plt.show()