class NumOperations(object):
    
    def __init__(self, math_list):
        self.math_list = math_list

    def __sub__(self, other):
        minuslst = []
        print(self.math_list)
        print(other.math_list)
        zipped = zip(self.math_list, other.math_list)
        for tup in zipped:
            minuslst.append(tup[0] - tup[1])
        
        return NumOperations(minuslst)

    def __add__(self, other):
        addlst = [x + y for x, y in zip(self.math_list, other.math_list)]
        return NumOperations(addlst)

    def __mul__(self, other):
        mullst = [x * y for x, y in zip(self.math_list, other.math_list)]
        return NumOperations(mullst)

    def __repr__(self):
        return str(self.math_list)


x = NumOperations([100, 90, 80, 70, 60])
y = NumOperations([10, 9, 8, 7, 6])

p = x - y
print('Subtraction: ' + str(p))



'''


z = x + y
q = x * y

print('Addition: ' + str(z))
print('Multiplication: ' + str(q))
'''