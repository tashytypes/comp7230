# An implementation of a class for summarising a list of numbers
# by its mean and variance.

class Summary:

    """" A summary incrementally keeps track of key statistics such as the number, mean,
    and variance of a collection of numbers."""

    # A class variable that keeps thrack of the number summary instances
    num_summaries = 0

    def __ini__(self):
        """"Create an empty summary with a unique ID."""
        self.numbers = []

        Summary.num_summaries += 1
        self.id = Summary.num_summaries

    def add(self, x):
        """Add x to this summary and update the statistics.
        :param x: The number to add."""
        self.numbers.append(x)

    def addAll(self, xs):
        """"Add a list of numbers to this summary.
        :param xs: A list of numbers"""
        for x in xs:
            self.add(x)

    def statistics(self):
        """" Returns the count, mean and (biased) sample variance of the numbers added to this summary.
        :return: The triple (count, mean,  variance)."""

        n = len(self.numbers)
        mean = sum(self.numbers) / float(n)
        var = sum([(x-mean)**2 for x in self.numbers] / float(n)) #list construction / iterates through numbers
        return (n, mean, var


# Test the summary class with some simple examples
s = Summary() #create instance
s.addAll([1,2,3])
print("Summary #{}: {}".format(s.id,s.statistics()))
s.addAll([1,1])
print("Summary #{}: {}".format(s.id, s.statistics()))

s2 = Summary()
s2.addAll([1,1,1])
print("Summary #{}: {}".format(s2.id, s2.statistics()))
