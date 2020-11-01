class Logger:
    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str):
        if message not in self.logs:
            self.logs[message] = timestamp
            return True
        if timestamp - self.logs[message] >= 10:
            self.logs[message] = timestamp
            return True
        return False


logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))
