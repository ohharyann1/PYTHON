#d2 = {"a": 1, "b": 2, "c": 3}

#def max_key(dict):
 #   max_value = (-1)*(2**32)
  #  for i in dict:
   #     if dict[i]>max_value:
    #        max_value = dict[i]
     #       max_key = i
    #return max_key
#print(max_key(d2))

#write a function to merge add (d1,d2) and add the value of those ket which are common in the give dictionary.
#d1 = {"a": 1, "b": 9,}
#d2 = {"b": 10 , "c": 7,}
#merge add (d1,d2) {"a": 1, "b": 19, "c": 7,}

def merge_add(d1, d2):
    result = d1.copy()
    
   
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
d1 = {"a": 1, "b": 9}
d2 = {"b": 10, "c": 7}
print(merge_add(d1, d2))