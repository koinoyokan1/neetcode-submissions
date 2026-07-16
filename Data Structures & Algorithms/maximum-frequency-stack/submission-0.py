'''
5:(1, [0])
7:(1, [1])
4:(1, [4])

5 7 5 4
'''
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.i = 0

    def push(self, val: int) -> None:
        if not val in self.freq:
            self.freq[val] = [1, [self.i]]
        else:
            self.freq[val][0] += 1
            self.freq[val][1].append(self.i)

        self.i += 1

    def pop(self) -> int:
        high = [0, 0, 0]

        for key in self.freq.keys():
            cnt, index = self.freq[key]
            if high[0] < cnt or (high[0] == cnt and high[1] < index[-1]):
                high[0], high[1], high[2] = cnt, index[-1], key
        
        key = high[2]
        self.freq[key][0] -= 1
        if self.freq[key][0] == 0: 
            del self.freq[key]
            return key

        self.freq[key][1].pop()
        return key



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()