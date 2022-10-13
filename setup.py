#The following types of dictionaries are accepted by our function

#First Type/Simple one
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



#Second Type, dictionary contains a list which contains another dictionary
country = {
    'name': 'Neverland',
    'cities': [
        {'name': 'Faketown', 'population': 3},
        {'name': 'Evergreen', 'population': 4}
    ],
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
         'type': list,
         'item_type': dict,
         'item_nesteddict': valcity,
     },
 }