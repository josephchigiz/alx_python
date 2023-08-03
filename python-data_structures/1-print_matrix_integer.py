def print_matrix_integer(matrix=[[]]):
  
  for row in matrix:
  
    for m in range(len(row)):
  
      if m < len(row) -1:
        print("{:d}".format(row[m]), end=" ")
      else:
        print("{:d}".format(row[m]))