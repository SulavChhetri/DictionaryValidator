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


def type1(value,standard,input):
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
        raise TypeError(f"The standard of {input} must be a dictionary")
    else:
        for item in value:
            if(type(item)==str):
                itemlist = value[item]
                for items in itemlist:
                    validator(items,standard)
            else:
                validator(item,standard)


def validator(dictionary, validationrule):
    if dictionary.keys()!=validationrule.keys():
       print("The keys in dictionary and Validation dictionary are different!")
       return False
    else:
        for key in validationrule:
            value = dictionary[key]
            rule = validationrule[key]
            for function in rule.keys():
                if(function=='type' and type1(value,rule[function],key)==False):
                    return False
                elif(function=='minlength' and minlength(value,rule[function],key)==False):
                    return False
                elif(function=='maxlength' and maxlength(value,rule[function],key)==False):
                    return False
                elif(function=='isGreaterthan' and isGreaterthan(value,rule[function],key)==False):
                    return False
                elif(function=='isLessthan' and isLessthan(value,rule[function],key)==False):
                    return False
        return True

if __name__ == "__main__":
    print(validator(d,valrule))