class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# クロージャを巧みに利用した高階関数make_averager()

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        count += 1
        total += new_value
        return total /count
    return averager

# avg = Averager()
avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

