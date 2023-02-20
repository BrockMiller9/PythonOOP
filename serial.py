"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = self.next = start

    def __repr__(self):
        return f'<serial generator start={self.start} next={self.next}'

    def generate(self):
        """takes the next variable then adds 1, then subtracts one from the number we display on screen so we can include the first number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """resets the next variable to the input value"""
        self.next = self.start
        return self.start


serial = SerialGenerator(1)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
print(serial.generate())
print(serial.generate())
