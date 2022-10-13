from collections import defaultdict

d = {
    "name": "Sulav",
    "age": 22,
    "city" : "Syangja",
    "isEngineer": True
}

valrule = {
    "name" : {
        "type": str,
        'minlength':4,
        'maxlength': 10
    },
    'age': {
        'type': int,
        'isGreaterthan': 0,
        'isLessthan': 150
    },
    'city':{
        'type': str
    },
    'isEngineer':{
        'type': bool
    }
}


def mergedictionary(d1,d2):
    mergeddict = defaultdict(list)
    for dic in (d1, d2):
        for key, value in dic.items():
            mergeddict[key].append(value)
    return mergeddict

def aftermerge(merge):
    for key in merge:
            # print(key) name, cities
            #  print(merge[key]) ['Neverland', {'type': <class 'str'>}]
            # [[{'name': 'Faketown', 'population': 3}, {'name': 'Evergreen', 'population': 4}], {'type': <class 'list'>, 'item_type': <class 'dict'>, 'item_nesteddict': {'name': {'type': <class 'str'>}, 'population': {'type': <class 'int'>, 'isGreaterthan': 0}}}]


            value = merge[key][0]
            rule = merge[key][1]

            # print(rule.keys()) dict_keys(['type'])
            #             dict_keys(['type', 'item_type', 'item_nesteddict'])

            # print(value)
            # Neverland
            # [{'name': 'Faketown', 'population': 3}, {'name': 'Evergreen', 'population': 4}]




            # print(rule)
            # {'type': <class 'str'>}
            # {'type': <class 'list'>, 'item_type': <class 'dict'>, 'item_nesteddict': {'name': {'type': <class 'str'>}, 'population': {'type': <class 'int'>, 'isGreaterthan': 0}}}


            # print('\n')


            for function in rule.keys():
                if(function=='type'):
                    Type(value,rule[function],key)
                elif(function=='minlength'):
                    minlength(value,rule[function],key)
                elif(function=='maxlength'):
                    maxlength(value,rule[function],key)
                elif(function=='isGreaterthan'):
                    isGreaterthan(value,rule[function],key)
                elif(function=='isLessthan'):
                    isLessthan(value,rule[function],key)
                elif(function=='item_type'):
                    item_type(value,rule[function], key)
                elif (function == 'item_nesteddict'):
                    item_nesteddict(value,rule[function],key)

def Type(value,standard,input):
    if not type(value)==standard:
        print(f"The type of a {input} must be {standard} but is {type(value)}")
        exit('False')

def minlength(value,standard,input):
    if not len(value)>=standard:
        print(f'The minimum length of a {input} must be {standard} but is {len(value)}')
        exit("False")

def maxlength(value,standard,input):
    if not len(value)<= standard:
        print(f'The maximum length of a {input} must be {standard} but is {len(value)}')
        exit("False")

def isGreaterthan(value,standard,input):
    if not value>=standard:
        print(f'The {input} must be greater than {standard} but is {value}')
        exit('False')

def isLessthan(value,standard,input):
    if not value<=standard:
        print(f'The {input} must be less than {standard} but is {value}')
        exit("False")

def item_type(value,standard,input):
    for items in value:
        if not type(items)==standard:
            print(f'The items inside the {input} must be {standard} but is {type(items)}')
            exit("False")

def item_nesteddict(value,standard,input):
    if not type(standard)==dict:
        print(f"The standard of {input} must be a dictionary")
        exit("False")
    else:
        for item in value:
            anothermerge = mergedictionary(item, standard)
            aftermerge(anothermerge)

def validator(dictionary, validationrule):
    if dictionary.keys()!=validationrule.keys():
       print("The keys in dictionary and Validation dictionary are different!")
    else:
        merge = mergedictionary(dictionary,validationrule)
        # print(merge)
        aftermerge(merge)

        print("True")


if __name__ == "__main__":
    validator(d,valrule)