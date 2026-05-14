"""
1  2  3  4
5  6  7  8
5  6  7  8
9 10 11 12
"""

# 请注意，这里展示的是我写的内容和Herry的内容，其中下面的写class的部分是我写的，仅供参考，Herry希望我们写的方式我写在函数，名为“another”的函数
# 但因为我有点懒，所以两种方法我都写进类里了，不过不影响理解

class Array:
    def __init__(self,n,m):#generate array
        self.n=n
        self.m=m
        i = 0
        self.array = []
        number = 1
        while i != n:
            times = 1
            small_list = []
            while times != m + 1:
                small_list.append(number)
                number = number + 1
                times = times + 1
            self.array.append(small_list)
            i = i + 1

    def display(self):
        i=0
        while i != self.n:
            x=0
            while x != self.m:
                print(self.array[i][x],end=" ")
                x = x + 1
            i=i+1
            print()
    def __str__(self):
        self.display()
        return ""

    def up(self,n,m):
        if n-1 >=0:
            return self.array[n-1][m]
        return None
    def down(self,n,m):
        if n+1<self.n:
            return self.array[n+1][m]
        return None
    def left(self,n,m):
        if m-1>=0:
            return self.array[n][m-1]
        return None
    def right(self,n,m):
        if m+1<self.m:
            return self.array[n][m+1]
        return None

    def clockwise(self):
        visited = []
        i = 0
        while i != self.n:
            visited.append([False] * self.m)
            i = i + 1

        total = self.n * self.m
        n, m = 0, 0

        print(self.array[n][m],end=" ")
        visited[n][m] = True
        i=1
        while i!= total:
            while m + 1 < self.m and not visited[n][m + 1]:
                m = m + 1
                print(self.array[n][m],end=" ")
                visited[n][m] = True
                i = i + 1

            while n + 1 < self.n and not visited[n + 1][m]:
                n = n + 1
                print(self.array[n][m],end=" ")
                visited[n][m] = True
                i = i + 1

            while m - 1 >= 0 and not visited[n][m - 1]:
                m = m - 1
                print(self.array[n][m],end=" ")
                visited[n][m] = True
                i = i + 1

            while n - 1 >= 0 and not visited[n - 1][m]:
                n = n - 1
                print(self.array[n][m],end=" ")
                visited[n][m] = True
                i = i + 1
        print()

    def anticlockwise(self):
        visited = []
        i = 0
        while i != self.n:
            visited.append([False] * self.m)
            i = i + 1
        total = self.n * self.m
        n, m = 0, 0

        print(self.array[n][m], end=" ")
        visited[n][m] = True
        i=1

        while i != total:
            while n + 1 < self.n and not visited[n + 1][m]:
                n = n + 1
                print(self.array[n][m], end=" ")
                visited[n][m] = True
                i=i+1

            while m + 1 < self.m and not visited[n][m + 1]:
                m = m + 1
                print(self.array[n][m], end=" ")
                visited[n][m] = True
                i=i+1

            while n - 1 >= 0 and not visited[n - 1][m]:
                n = n - 1
                print(self.array[n][m], end=" ")
                visited[n][m] = True
                i=i+1

            while m - 1 >= 0 and not visited[n][m - 1]:
                m = m - 1
                print(self.array[n][m], end=" ")
                visited[n][m] = True
                i=i+1
        print()

    def another_way_clockwise(self):
        horizon = self.m - 1
        vertical = self.n - 1
        n, m = 0, 0

        print(self.array[n][m], end=" ")

        while horizon > 0 and vertical > 0:
            i = 0
            while i < horizon:
                m += 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < vertical:
                n += 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < horizon:
                m -= 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < vertical - 1:
                n -= 1
                print(self.array[n][m], end=" ")
                i += 1

            horizon -= 2
            vertical -= 2

            n += 1
            m += 1

            if horizon >= 0 and vertical >= 0:
                print(self.array[n][m], end=" ")

        if vertical == 0 and horizon > 0:
            i = 0
            while i < horizon:
                m += 1
                print(self.array[n][m], end=" ")
                i += 1

        if horizon == 0 and vertical > 0:
            i = 0
            while i < vertical:
                n += 1
                print(self.array[n][m], end=" ")
                i += 1

        print()

    def another_anticlockwise(self):
        horizon = self.m - 1
        vertical = self.n - 1
        n, m = 0, 0

        print(self.array[n][m], end=" ")

        while horizon > 0 and vertical > 0:
            i = 0
            while i < vertical:
                n += 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < horizon:
                m += 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < vertical:
                n -= 1
                print(self.array[n][m], end=" ")
                i += 1

            i = 0
            while i < horizon - 1:
                m -= 1
                print(self.array[n][m], end=" ")
                i += 1

            horizon -= 2
            vertical -= 2

            n += 1
            m += 1

            if horizon >= 0 and vertical >= 0:
                print(self.array[n][m], end=" ")

        if vertical == 0 and horizon > 0:
            i = 0
            while i < horizon:
                m += 1
                print(self.array[n][m], end=" ")
                i += 1

        if horizon == 0 and vertical > 0:
            i = 0
            while i < vertical:
                n += 1
                print(self.array[n][m], end=" ")
                i += 1

        print()





"""
t
"""
a=Array(3,3)
print(Array(3,3))
a.clockwise()
a.anticlockwise()
