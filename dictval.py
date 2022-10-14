#dictionary contains a list which contains another
country = {
    'name': 'Neverland',
    'cities': [
        {'name': 'Faketown', 'population': 3},
        {'name': 'Evergreen', 'population': 4}
    ],
 }

valcity={
     'name': {
        'type': str,
        'minlength':4,
        'maxlength': 10
     },
     'population': {
         'type': int,
         'minimum': 0,
     },
 }

valcountry ={
     'name': {'type': str},
     'cities': {
         'type': list,
         'item_nesteddict': valcity,
     },
 }
#The following types of dictionaries are accepted by our function

#First Type/Simple one
# d = {
#     "name": "Sulav",
#     "age": 22,
#     "city" : "Syangja",
#     "isEngineer": True
# }

# valrule = {
#     "name" : {
#         "type": str,
#         'minlength':4,
#         'maxlength': 10
#     },
#     'age': {
#         'type': int,
#         'minimum': 0,
#         'maximum': 150
#     },
#     'city':{
#         'type': str
#     },
#     'isEngineer':{
#         'type': bool
#     }
# }






#nesteddictionary
# entry = {
#     'name': 'Sulav',
#     'age' : 22,
#     'address': {
#         'street':"Putalibazar",
#         'zipcode': 3244,
#         'country':'Nepal'
#     }
# }
# addressvalid ={
#     'street': {
#         'type': str,
#         'minlength':4,
#         'maxlength': 20
#     },
#     'zipcode':{
#         'type': int
#     },
#     'country':{
#         'type': str,
#         'minlength':4,
#         'maxlength': 10
#     }
# }
# validationentry = {
#     'name': {
#         'type':str,
#         'minlength': 3,
#         'maxlength': 10
#     },
#     'age': {
#         'type': int,
#         'minimum':0,
#         'maximum': 150
#     },
#     'address':{
#         'type': dict,
#         'item_nesteddict': addressvalid
#     }
# }
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

def nestedfunction(value,standard,input):
    if(type(value)==list):
        for item in value:
            x = validator(item,standard)
            if x==False:
                return False
    elif(type(value)==dict):
        x = validator(value,standard)
        if x==False:
            return False

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
                elif(function=='minimum' and isGreaterthan(value,rule[function],key)==False):
                    return False
                elif(function=='max' and isLessthan(value,rule[function],key)==False):
                    return False
                elif(function=='item_nesteddict' and nestedfunction(value,rule[function],key)==False):
                    return False
        return True

if __name__ == "__main__":
    # print(validator(entry,validationentry))
    # print(validator(d,valrule))
    print(validator(country,valcountry))