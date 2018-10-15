import bisect


class MyCalendarTwo:

    def __init__(self):
        self.one = []
        self.two = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        right_idx1 = bisect.bisect_right(self.one, start)
        right_idx2 = bisect.bisect_right(self.two, start)
        if right_idx2 < len(self.two) and (right_idx2%2 == 1 or end > self.two[right_idx2]):
            return False
        else:
            if right_idx1 < len(self.one) and (right_idx1%2 == 1 or end > self.one[right_idx1]):
                left_idx1 = bisect.bisect_right(self.one, end)
                self.one.insert(right_idx1, start)
                self.one.insert(left_idx1+1, end)

                if right_idx1%2 == 0:
                    for i in range(right_idx1+1, left_idx1+1, 2):
                        if self.one[i] != self.one[i+1]:
                            bisect.insort_right(self.two, self.one[i])
                            bisect.insort_right(self.two, self.one[i+1])
                else:
                    for i in range(right_idx1, left_idx1+1, 2):
                        if self.one[i] != self.one[i + 1]:
                            bisect.insort_right(self.two, self.one[i])
                            bisect.insort_right(self.two, self.one[i + 1])
            else:
                self.one.insert(right_idx1, start)
                self.one.insert(right_idx1+1, end)

            return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    mc = MyCalendarTwo()
    input = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
    for item in input:
        print(mc.book(item[0], item[1]))
        print(mc.one)
        print(mc.two)
