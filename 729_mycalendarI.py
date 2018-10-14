"""
Big idea: binary search
"""

class MyCalendar:

    def __init__(self):
        self.once = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        h = 0
        e = len(self.once) - 1
        mid = int((h + e) / 2)

        if len(self.once) == 0:
            self.once.append([start, end])
            return True

        if len(self.once) == 1:
            start_ = max(start, self.once[0][0])
            end_ = min(end, self.once[0][1])
            if start_ < end_:
                return False
            else:
                if start > self.once[0][0]:
                    self.once.append([start, end])
                else:
                    self.once.insert(0, [start, end])
                return True

        flag = 0
        while h < e:
            mid = int((h + e)/2)
            if end <= self.once[mid][0]:
                e = mid
                flag = 1
            elif end > self.once[mid+1][0]:
                h = mid + 1
                flag = 2
            else:  # self.once[mid][0] < end <= self.once[mid+1][0]
                flag = 3
                break

        if flag == 1:
            self.once.insert(0, [start, end])
            return True

        if flag == 2:
            if start < self.once[-1][1]:
                return False
            else:
                self.once.append([start, end])
                return True

        if flag == 3:
            if start < self.once[mid][1]:
                return False
            else:  # start >= self.once[mid][1]
                self.once.insert(mid+1, [start, end])
                return True


if __name__ == '__main__':
    mc = MyCalendar()
    print(mc.book(10,20))
    print(mc.book(15, 25))
    print(mc.book(20, 30))
    print(mc.book(5, 8))
    print(mc.book(8, 9))
    print(mc.once)
