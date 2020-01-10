class LogSystem:
    def __init__(self):
        self.logs=[]
        self.granularity = {'Year':4, 'Month':7, 'Day':10, 'Hour':13, 'Minute':16, 'Second': 19}

    def put(self, id, timestamp):
        self.logs.append((id,timestamp))

    def retrieve(self, s, e, gra):
        i=self.granularity[gra]
        begin=s[:i]
        end=e[:i]
        arr=[]
        for id, timestamp in self.logs:
            if begin<=timestamp[:i]<=end:
                arr.append(id)
        return sorted(arr)
        # return sorted(id for id, timestamp in self.logs if begin <= timestamp[:i]<=end)

obj=LogSystem()
print(obj.granularity)
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print(obj.logs)
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))

