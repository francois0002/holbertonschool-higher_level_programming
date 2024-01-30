#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    def square_element(x):
        return x ** 2

    def square_row(row):
        return list(map(square_element, row))

    result_matrix = list(map(square_row, matrix))

    return result_matrix
