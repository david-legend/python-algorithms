# NestedEvenSum --> Write a recursive function to return the sum of all even numbers in an object which may contain nested objects

def nestedEvenSum(obj, sum=0):
    for value in obj.values():
        if type(value) is int:
            if value%2==0:
                sum+=value
        elif type(value) is dict:
            sum+=nestedEvenSum(value)
        else:
            pass
    return sum


obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


print(nestedEvenSum(obj1)) #6
print(nestedEvenSum(obj2)) #10
