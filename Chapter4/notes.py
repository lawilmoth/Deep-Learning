import numpy as np
from sklearn.datasets import make_classification



a,b = make_classification(n_samples=1000, weights=(0.25, 0.75))
idx = np.where(b == 1)[0]
print(a.shape)