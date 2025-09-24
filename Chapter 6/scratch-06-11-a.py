class Length:
    def __init__(self, cm):
        self._cm = cm

    @property
    def cm(self):
        return self._cm
    
    @cm.setter
    def cm(self, value):
        self._cm = value

    @property
    def inches(self):
        return self._cm / 2.54
    
    @inches.setter
    def inches(self, value):
        self._cm = value * 2.54

length2 = Length(3)
print("3 centimeters is " + str(length2.inches) + " inches.")
length2.inches = 3
print(str(length2.inches) + " inches is " + str(length2.cm) + " centimeters.")
        