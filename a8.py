from neural import *

# print("<<<<<<<<<<<<<< nu XOR for Q1>>>>>>>>>>>>>>\n")

# xor_training_data = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]

# xorn = NeuralNet(2, 2, 1)
# xorn.train(xor_training_data)
# print(xorn.test_with_expected(xor_training_data))

# print("<<<<<<<<<<<<<< nu XOR for Q2>>>>>>>>>>>>>>\n")

# xor_training_data = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]

# xorn = NeuralNet(2, 8, 1)
# xorn.train(xor_training_data)
# print(xorn.test_with_expected(xor_training_data))

# print("<<<<<<<<<<<<<< nu XOR for Q1>>>>>>>>>>>>>>\n")

# xor_training_data = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]

# xorn = NeuralNet(2, 1, 1)
# xorn.train(xor_training_data)
# print(xorn.test_with_expected(xor_training_data))


# print("<<<<<<<<<<<<<< nu XOR for politics - table 2 >>>>>>>>>>>>>>\n")

# xor_training_data = [([0.9, 0.6, 0.8, 0.3, 0.1], [1.0]), ([0.8, 0.8, 0.4, 0.6, 0.4], [1.0]), ([0.7, 0.2, 0.4, 0.6, 0.3], [1.0]), ([0.5, 0.5, 0.8, 0.4, 0.8], [0.0]), ([0.3, 0.1, 0.6, 0.8, 0.8], [0.0]), ([0.6, 0.3, 0.4, 0.3, 0.6], [0.0])]

# xorn = NeuralNet(5, 8, 1)
# xorn.train(xor_training_data)
# print(xorn.test_with_expected(xor_training_data))

print("<<<<<<<<<<<<<< nu XOR for politics - table 3 >>>>>>>>>>>>>>\n")

xor_training_data = [([1.0, 1.0, 1.0, 0.1, 0.1]), ([0.5, 0.2, 0.1, 0.7, 0.7]), ([0.8, 0.3, 0.3, 0.3, 0.8]), ([0.8, 0.3, 0.3, 0.8, 0.3]), ([0.9, 0.8, 0.8, 0.3, 0.6])]

xorn = NeuralNet(5, 8, 1)

print(xorn.test(xor_training_data))
