class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = 0
        n = len(matrix)
        # print(n)
        while x < 4:
            print("matrix test ", matrix[2][2])
            print("x is ", x)
            for y in range(n - 1):
                print("y is ", y)
                print("before:")
                print(matrix)
                matrix[x][x + y], matrix[x][n - 1 - x - y], matrix[n - 1 - x][n - 1 - x - y], matrix[n - 1 - x - y][x] = \
                matrix[n - 1 - x - y][x + y], matrix[x][x + y], matrix[x][n - 1 - x - y], matrix[n - 1 - x][
                    n - 1 - x - y]
                print("after:")
                print(matrix)

            #                 holder = matrix[x][n-x-1-y] #11
            #                 matrix[x][n-x-1-y] = matrix[x][x+y] # 5->11

            #                 holder = matrix[n-1-x][n-1-x]#16
            #                 matrix[n-1-x][n-1-x] = matrix[x][n-x-1-y] # 11->16
            #                 holder = matrix[n-1-x][x] #15
            #                 matrix[n-1-x][x]= matrix[n-1-x] [n-1-x]  # 16-> 15
            #                 matrix[n-1-x][x] = matrix[x][n-x-1-y]

            x += 1
        print(matrix)

#needs work https://leetcode.com/problems/rotate-image/
#looked in solution found something similar to what i was thinking
# https://leetcode.com/problems/rotate-image/discuss/741130/Java-0ms-8-lines