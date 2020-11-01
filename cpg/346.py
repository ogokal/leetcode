
class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.st = []
        self.size = size
        self.last = 0
    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here

        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param = obj.next(val)
        if len(self.st) < self.size:
            self.st.append(val)
            self.last += val
            return self.last / len(self.st)
        else:
            self.last -= self.st.pop(0)
            self.last += val
            self.st.append(val)
            return self.last / self.size
