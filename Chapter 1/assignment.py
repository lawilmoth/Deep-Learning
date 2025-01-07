# We will write matrices as lists of lists, with the first list being the first row of the matrix.
# For example, the matrix
# 1  2  3
# 4  5  6
# would be represented as [[1, 2, 3], [4, 5, 6]].

# Write a function add_matrices(m1, m2) that adds m1 and m2 and returns a new matrix containing their sum.
# You can assume that m1 and m2 are the same size.
def add_matrices(m1, m2):
    """[[1, 2], [3, 4]], [[2, 2], [2, 2]] -> [[3, 4], [5, 6]]"""
    pass


# Write a function scalar_mult(s, m) that multiplies a matrix, m, by a scalar, s.
def scalar_mult(s, m):
    """3, [[1, 2], [3, 4]] -> [[3, 6], [9, 12]]"""
    pass

# Write a function that multiplies the two matrices together and returns a new matrix.
def multiply_matrices_1():
    """[[1,2,3]] * [[4], [5], [6]] -> [[32]]
    calculate correctly do not just return 32"""
    m1 = [[1,2,3]]
    m2 = [[4], [5], [6]]
    pass

def multiply_matrices_2():
    """[[1,2,3] [4,5,6]] * [[1,2],[3,4],[5,6]] -> [[22, 28], [49, 64]]
    calculate correctly do not just return 32"""
    m1 = [[1,2,3], [4,5,6]]
    m2 = [[1,2],[3,4],[5,6]]
    pass

def multiply_matrices(m1,m2):
    """Multiply two matrices together, if possible, and return the result.
    If the matrices cannot be multiplied, return None.
    The matrices could be any size"""
    pass
        

def probability_distributions():
    """Return the answer:
    What is the name of the distribution where each point is equally likely"""
    pass

def probability_distributions_2():
    """Return the answer: 
    What is the name of the distribution that is also called a bell curve"""
    pass

def statistical_tests():
    """Return the answer:
    What is the default p-value for statistical tests?"""
    pass