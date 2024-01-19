#Define a function called spiral which will ask the user to enter an integer and then will return a matrix with a spiral clockwise filling
#starting from "1" and reaching the square of this value
#For example if the user input was "5", it will fill the matrix from 1 till 25
# If the input was 4, it will draw the matrix as below
# [1,2,3,4]
# [12,13,14,5]
# [11,16,15,6]
# [10,9,8,7]

def spiral():
  n = int(input("Please enter your matrix size"))

  matrix = [[0 for i in range(n)] for j in range(n)]

  top = 0
  bottom = n-1
  left = 0
  right = n-1
  direction = 0 # 0: right, 1: down, 2: left, 3: up
  counter = 1
  
  #The while loop is used to check if the counter is still less than or equal to the sqaure of the entered value
  #In this case the function will return the answer if the counter finishes 16 and checks if 17 less than or equal 4 to the power 2
  while counter <=n**2:
    
    if direction == 0:
      for i in range(left, right+1):
        matrix[top][i] = counter
        counter += 1
      top += 1

    elif direction == 1:
      for i in range(top, bottom+1):
        matrix[i][right] = counter
        counter += 1
      right -= 1

    elif direction == 2:
      for i in range(right, left-1, -1):
        matrix[bottom][i] = counter
        counter += 1
      bottom -= 1

    elif direction == 3:
      for i in range(bottom, top-1, -1):
        matrix[i][left] = counter
        counter += 1
      left += 1

    direction = (direction + 1) % 4

  return matrix

print(spiral())







  
  


      



