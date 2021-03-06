
import numpy as np

def sigmoid (Z):
    A = 1 / (1 + np.exp(-Z))
    return A

def sigmoid_derivative (A):
    return A * (1 - A)

def tanh (Z):
    # return (np.exp(z) - np.exp(-z)) / np.exp(z) + np.exp(-z)
    return np.tanh(Z)

def tanh_derivative (A):
    # 1 - A ^ 2
    return 1 - np.power(A, 2)

def ReLU (Z):
    return np.maximum(0,Z)

def ReLU_derivative (A):
    return 1. * (A > 0)