import numpy as np

def simple_random():
    # Create a generator instance
    rng = np.random.default_rng(seed=42)

    # Generate 5 random floats between 0 and 1
    floats = rng.random(5)
    print(floats)

    floats = np.random.rand(5)
    print(floats)

    floats = np.random.ranf(5)
    print(floats)

    # Generate 5 random integers between 0 and 10 (exclusive)
    integers = rng.integers(0, 10, size=5)   # 1d integer array
    print(integers)

    rints = rng.integers(low=0, high=10, size=3)  # specify the keyword arguments
    print(rints)
    
    arr2 = np.random.randint(5, 15, size=(2, 2, 4))  # 3D integer array
    print(arr2)

    # randn - Normally distributed values.
    arr2 = np.random.randn(5, 3)   # 2D float array
    print(arr2)

    # rand - Uniformly distributed values.
    arr2 = np.random.rand(5, 3)    # 2D float array
    print(arr2)


simple_random()