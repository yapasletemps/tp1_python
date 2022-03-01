class syraclass:

    def __init__(self,n):
	    self.n=n

    def syracuse(self):
        while self.n !=1:
            print(self.n, end = ',')
            if (self.n%2==1):
                self.n = self.n*3+1
            else:
                self.n=self.n/2

