from scipy.spatial import distance
distance.jensenshannon([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], 2.0)
1.0
distance.jensenshannon([1.0, 0.0], [0.5, 0.5])
0.46450140402245893
distance.jensenshannon([1.0, 0.0, 0.0], [1.0, 0.0, 0.0])
0.0
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
b = np.array([[13, 14, 15, 16],
              [17, 18, 19, 20],
              [21, 22, 23, 24]])
distance.jensenshannon(a, b, axis=0)
array([0.1954288, 0.1447697, 0.1138377, 0.0927636])
distance.jensenshannon(a, b, axis=1)
array([0.1402339, 0.0399106, 0.0201815])