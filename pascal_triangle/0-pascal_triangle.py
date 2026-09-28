#!/usr/bin/python3

def pascal_triangle(n):
    triangle = [[1]]
    if n == 1:
        return triangle
    triangle.append([1,1])
    if n == 2:
        return triangle

    for outer_index in range(1, n - 1):
        row = [1]
        prev_row = triangle[outer_index]

        for inner_index in range (0, len(prev_row) - 1):
            row.append(prev_row[inner_index] + prev_row[inner_index + 1])
            
        row.append(1)
        triangle.append(row)

    return triangle   
