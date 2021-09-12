class testo:

    def __init__(self, num, bam):
        self.num = num
        self.bam = bam
        self.value = 3

    def __bool__(self):
        print("BooL", self.num + self.bam)
        return bool(self.num)

    def __pos__(self):
        return self.num + self.bam

    def __repr__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other * 3

    def __eq__(self, other):
        return print("Yeah!")

    def __ne__(self, other):
        if self.num != other:
            print("fuck no!")
        return not self.__eq__(other)



t = testo(12, 33)

if t != 12:
    print("hmm")

bool(t)

