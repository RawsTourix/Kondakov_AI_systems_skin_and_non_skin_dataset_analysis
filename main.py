import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # Создаём тип данных для нашего датасета
    dt = np.dtype('u1, u1, u1, u1')

    # Создаём датасет
    data = np.genfromtxt('Skin_NonSkin.txt', delimiter = '\t', dtype = dt)


    # Выделяем кожу и не кожу
    data_skin = data[data['f3'] == 1]
    data_non_skin = data[data['f3'] == 2]
    
    
    # Строим графики
    plt.figure(1)
    plt.scatter(data_non_skin['f2'], data_non_skin['f1'], c = 'blue', marker = 'o', label = 'Non-Skin')
    plt.scatter(data_skin['f2'], data_skin['f1'], c = 'red', marker = 'o', label = 'Skin')
    plt.xlabel('Red')
    plt.ylabel('Green')
    plt.legend(loc = 'upper right')
    plt.title('RGB-анализ кожи и не кожи')

    plt.figure(2)
    plt.scatter(data_non_skin['f2'], data_non_skin['f0'], c = 'blue', marker = 'o', label = 'Non-Skin')
    plt.scatter(data_skin['f2'], data_skin['f0'], c = 'red', marker = 'o', label = 'Skin')
    plt.xlabel('Red')
    plt.ylabel('Blue')
    plt.legend(loc = 'upper right')
    plt.title('RGB-анализ кожи и не кожи')

    plt.figure(3)
    plt.scatter(data_non_skin['f1'], data_non_skin['f0'], c = 'blue', marker = 'o', label = 'Non-Skin')
    plt.scatter(data_skin['f1'], data_skin['f0'], c = 'red', marker = 'o', label = 'Skin')
    plt.xlabel('Green')
    plt.ylabel('Blue')
    plt.legend(loc = 'upper right')
    plt.title('RGB-анализ кожи и не кожи')
    
    plt.show()
