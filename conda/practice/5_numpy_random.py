import numpy as np

for _ in range(5):
    np.random.seed(100)
    random_list = np.random.randint(5, size=3)
    print(random_list)