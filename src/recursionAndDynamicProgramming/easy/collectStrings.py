# CollectNumber --> Write a function that accepts objects and returns an array of all the 
# values in the object that have a typeof string

def collectStrings(obj):
    result = []
    for value in obj.values():
        if type(value) is str:
            result.append(value)
        elif type(value) is dict:
            result.extend(collectStrings(value))
        else:
            pass
    
    return result


obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

obj2 = {
  "name": 'John',
  "age": 23,
  "data": {
    "location": {
        "street": 23,
        "district": "Dansoman",
    }
  }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz'])
print(collectStrings(obj2)) # ['John', 'Dansoman'])