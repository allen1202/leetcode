class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            return -1

        else:
            res = self.stack2.pop()
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return res