import numpy as np
import matplotlib.pyplot as plt
def labeling_classes():
    """Labeling classes as integers rather than strings saves space in 
    memory. Return the label for frogs according to the example chart at the 
    begginning of Chapter 4 """
    pass 


def types_of_features_2():
    """
    Which type of data would you use to classify

    Grade Level

    return the letter that you think is correct
    a. Floating Point
    b. Internval Number
    c. Ordinal Number
    d. Categorical Values"""
    pass


def types_of_features_3():
    """
    Which type of data would you use to classify

    Letter Grade in a class

    return the letter that you think is correct
    a. Floating Point
    b. Internval Number
    c. Ordinal Number
    d. Categorical Values"""
    pass


def types_of_features_4():
    """
    Which type of data would you use to classify

    Height

    return the letter that you think is correct
    a. Floating Point
    b. Internval Number
    c. Ordinal Number
    d. Categorical Values"""
    pass


def inspect_data():
    """Call the function below to inspect the data
    return the answer to this statement:
    As the years increase, the age of first time mothers _______"""

    
    x = np.array([i for i in range(2005,2022)])
    y = np.array([25.2,25.0,25.0,25.1, 25.2,25.4,25.6,25.8,26.0,26.3,26.4,26.6,26.8,26.9,27.0,27.1,27.3])

    plt.scatter(x,y)
    plt.xlabel("Year")
    plt.ylabel("Age of First Time Mothers")
    plt.title("Age of First Time Mothers by Year")
    plt.show()

#inspect_data()

def interpolation_problem():
    x = np.array([i for i in range(2005,2022)])
    y = np.array([25.2,25.0,25.0,25.1, 25.2,25.4,25.6,25.8,26.0,26.3,26.4,26.6,26.8,26.9,27.0,27.1,27.3])
    plt.scatter(x,y)

    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    plt.plot(x, m*x + c, 'r', label='Fitted line')

    plt.xlabel("Year")
    plt.ylabel("Age of First Time Mothers")
    plt.title("Age of First Time Mothers by Year")
    plt.show()

    # line y = mx + c
    # y = 0.15x + -276.5, x is the Year
    # 0.15 is the increase in age of first time mothers per year

    # Based on the dataset, predict the age of first time mothers in 2025
    #return the age of first time mothers in 2025
    print(m,c)
    


#interpolation_problem()

def extrapolation_problem():
    x = np.array([i for i in range(2005,2022)])
    y = np.array([25.2,25.0,25.0,25.1, 25.2,25.4,25.6,25.8,26.0,26.3,26.4,26.6,26.8,26.9,27.0,27.1,27.3])
    plt.scatter(x,y)

    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    plt.plot(x, m*x + c, 'r', label='Fitted line')

    plt.xlabel("Year")
    plt.ylabel("Age of First Time Mothers")
    plt.title("Age of First Time Mothers by Year")
    plt.show()

    # line y = mx + c
    # y = 0.15x + -276.5, x is the Year
    # 0.15 is the increase in age of first time mothers per year

    # Based on the dataset, predict the age of first time mothers in 2800
    #return the age of first time mothers in 2800
    print(m*2800 + c)



#extrapolation_problem()

def prior_class_probabilities():
    """Read Prior Class Probablites on page 60
    When the class probabilities are really rare, what ratio did the book suggest
    return the ratio as a string. No spaces"""
    pass

def data_set_size():
    """Read Data Set Size on page 62
    What is the cheeky answer to how much data you need?
    return the answer"""
    pass


def data_set_size_2():
    """Read Data Set Size on page 62
    What is  the problem with increasing sample size beyond a certain point?
    return __________ returns"""
    pass