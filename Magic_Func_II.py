class CustomIntFloatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value + ' is not valid\nOnly Integers and floats are valid values \nin CustomIntFloat(dict) '


class CustomIntFloat(dict):

    empty_dict = {}

    def __init__(self, key=None, value=None):
        print(key,value)
        if key is None:
            CustomIntFloat.empty_dict = {}

        elif len(key) == 1 and isinstance(value, (int, float)):
            dict.__setitem__(self, key, value)
        else:
            zipped = zip(key, value)
            for tup in zipped:
                if isinstance(tup[1], (int, float)):
                    dict.__setitem__(self, tup[0], tup[1])
                else:
                    raise CustomIntFloatError(tup[1])

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise CustomIntFloatError(value)
        return dict.__setitem__(self, key, value)


x = CustomIntFloat(['a','b','c'],[1,-1,0])  

print(x)