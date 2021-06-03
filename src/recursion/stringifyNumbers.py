# StringifyNumbers --> Write a function that takes in an object and finds all the values which are numbers and converts 
# them to strings. 

def stringifyNumbers(obj):
    for key,value in obj.items():
        if type(value) is int:
            obj[key] = str(value)
        elif type(value) is dict:
            stringifyNumbers(value)
        else:
            pass
    return obj


obj1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringifyNumbers(obj1))

obj1 = {
    "num": '1',
    "test": [],
    "data": {
        "val": '4',
        "info": {
            "isRight": True,
            "random": '66'
        }
    }
}