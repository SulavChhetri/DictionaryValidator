from collections import defaultdict
country = {
    'name': "Nepal",
    'cities': {'key':[{'name': 'Faketown', 'population': 3},{'name': 'Evergreen', 'population': 4}]},
 }

valcity={
     'name': {
         'type': str
     },
     'population': {
         'type': int,
         'isGreaterthan': 0,
     },
 }

valcountry ={
     'name': {'type': str},
     'cities': {
         'type': dict,
         'item_type': str,
         'item_nesteddict': valcity,
     },
 }

def mergedictionary(d1,d2):
    mergeddict = defaultdict(list)
    for dic in (d1, d2):
        for key, value in dic.items():
            mergeddict[key].append(value)
    return mergeddict

def aftermerge(merge):
    for key in merge:
            value = merge[key][0]
            rule = merge[key][1]

            for function in rule.keys():
                if(function=='type' and Type(value,rule[function],key)==False):
                    return False
                elif(function=='minlength' and minlength(value,rule[function],key)==False):
                    return False
                elif(function=='maxlength' and maxlength(value,rule[function],key)==False):
                    return False
                elif(function=='isGreaterthan' and isGreaterthan(value,rule[function],key)==False):
                    return False
                elif(function=='isLessthan' and isLessthan(value,rule[function],key)==False):
                    return False
                elif(function=='item_type' and item_type(value,rule[function], key)==False):
                    return False
                elif (function == 'item_nesteddict' and item_nesteddict(value,rule[function],key)==False):
                    return False

def Type(value,standard,input):
    if not type(value)==standard:
        print(f"The type of a {input} must be {standard} but is {type(value)}")
        return False

def minlength(value,standard,input):
    if not len(value)>=standard:
        print(f'The minimum length of a {input} must be {standard} but is {len(value)}')
        return False

def maxlength(value,standard,input):
    if not len(value)<= standard:
        print(f'The maximum length of a {input} must be {standard} but is {len(value)}')
        return False

def isGreaterthan(value,standard,input):
    if not value>=standard:
        print(f'The {input} must be greater than {standard} but is {value}')
        return False

def isLessthan(value,standard,input):
    if not value<=standard:
        print(f'The {input} must be less than {standard} but is {value}')
        return False

def item_type(value,standard,input):
    for items in value:
        if not type(items)==standard:
            print(f'The items inside the {input} must be {standard} but is {type(items)}')
            return False


def item_nesteddict(value,standard,input):
    if not type(standard)==dict:
        print(f"The standard of {input} must be a dictionary")
        return False
    else:
        for item in value:
            if(type(item)==str):
                itemlist = value[item]
                for items in itemlist:
                    anothermerge = mergedictionary(items, standard)
                    aftermerge(anothermerge)
            else:
                anothermerge = mergedictionary(item, standard)
                aftermerge(anothermerge)


def validator(dictionary, validationrule):
    if dictionary.keys()!=validationrule.keys():
       print("The keys in dictionary and Validation dictionary are different!")
       return False
    else:
        merge = mergedictionary(dictionary,validationrule)
        x = aftermerge(merge)
        if not x == False:
            return True
        else:
            return False
      


if __name__ == "__main__":
    print(validator(country,valcountry))