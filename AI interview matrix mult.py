def matrix_mult(x,y):

    #make sure the shapes match so we can perform matrix multiplication
    assert len(x[0]) == len(y)

    #create the result with the correct shape
    result = [[0 for j in range(len(y[0]))] for i in range(len(x))]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result

x = [[1,2],[3,4]]
y = [[1,2],[3,4]]
assert [[7,10],[15,22]] == matrix_mult(x,y)
x = [[1,2,3],[3,4,5]]
y = [[1,2],[3,4],[5,6]]
assert [[22,28],[40,52]] == matrix_mult(x,y)

# If everything works, then nothings prints and programs runs normally, but if mistake, then raises an AssertionError