# Start at Partitioning the Dataset on page 69
import random
rs = random.randint(0, 1000)
import numpy as np
from sklearn.datasets import make_classification

a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))

#Make classifications creats a dataset, and splits them into 2 classes

#Uncomment the code, and run it a few times to see the difference in the number of samples for each class you can delete
#the commented block of code when you are done.
"""
print(a.shape)
print(len(np.where(b == 0)[0]))
print(len(np.where(b == 1)[0]))
"""

def inspect_data_1():
    """print the shape of the dataset and the number of samples for each class
    return the shape of a as a tuple"""
    a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
    pass

def inspect_data_2():
    """After inspecting the data, you should realize why the first part of th shape of a is (10000, 20)
    hover over make_classifications to see the name of the paramerter that is set to 20
    return it  as a string"""
    pass




def inspect_data_3():
    a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
    # uncomment this to see the first element of a
    # print(a[0])

    #Uncomment this to see the sorted first element of a
    #for num in sorted(a[0]):
    #    print(num)

    #Return the whole number that you think this dataset is centered around
    pass


def inspect_data_4():
    """Based on the sorted dataset above, return the whole number that you think is the 
    standard deviation of the dataset
    Remember that the standard deviation is the average distance from the mean"""

    pass

def inspect_data_5():
    """Inspect b[0], try printing it. If you want to see all the values in b without the ..., 
    you can use a for loop.
    
    For every 100 elements in b, how many do you think will be a 0 on avearge?"""

    pass

def inspect_data_6():
    """print idx, this shows the indices of the samples that are in class 1
    print the shape of x0 and y0
    print the shape of x1 and y1"""
    a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
    idx = np.where(b == 1)[0]
    x0 = a[idx,:]
    y0 = b[idx]
    #print(x0.shape)
    #print(y0.shape)

    x1 = a[np.where(b == 0)[0],:]
    y1 = b[np.where(b == 0)]
    #print(x1.shape)
    #print(y1.shape)

    #The data was randomly generated on a Normal Distribution, then randomly split into 2 classes with the weights parameter
    #hopefully you learned something from inspecting the data,
    #to pass this, return the string "I inspected the data"

    pass


def separtate_90_percent_for_training():
    """Follow the comments below"""
    a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
    idx = np.where(b == 1)[0]
    x0 = a[idx,:]
    y0 = b[idx]
    idx = np.where(b == 0)
    x1 = a[idx[0],:]
    y1 = b[idx]
    
    #Finds the number where 90% of the samples. It should be around 900 and 8100 
    #because 
    n_trn0 = int(x0.shape[0] * 0.9)
    n_trn1 = int(x1.shape[0] * 0.9)

    
    pass


a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
idx = np.where(b == 1)[0]
x0 = a[idx,:]
y0 = b[idx]
idx = np.where(b == 0)
x1 = a[idx[0],:]
y1 = b[idx]
n_trn0 = int(x0.shape[0] * 0.9)
n_trn1 = int(x1.shape[0] * 0.9)