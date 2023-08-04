# def print_matrix_integer(matrix=[[]]):
#     if not matrix:
#         print(end="\n")
#         return
    
#     for row in matrix:
#         for k in range(len(row)):
#             if k < len(row) - 1:
#                 print("{:d}".format(row[k]), end=" ")
#             else:
#                 print("{:d}".format(row[k]))
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    
    for row in matrix:
        row_length = len(row)
        for m in range(row_length):
            if m!= 0:
                print(" ", end="")
            print("{:d}".format(row[m]), end="")
        print()