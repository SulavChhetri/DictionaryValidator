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



#Second Type, dictionary contains a list which contains another
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



#Third Example, dictionary inside a dictionary

country3= {
    'name': 'Neverland',
    'cities': {'key':[{'name': 'Faketown', 'population': 3},{'name': 'Evergreen', 'population': 4}]}, #This case
 }

valcity3={
     'name': {
         'type': str
     },
     'population': {
         'type': int,
         'isGreaterthan': 0,
     },
 }

valcountry3 ={
     'name': {'type': str},
     'cities': {
         'type': dict,
         'item_type': str,
         'item_nesteddict': valcity,
     },
 }




entry = {
    'name': 'Sulav',
    'age' : 22,
    'address': {
        'street':"Putalibazar",
        'zipcode': 3244,
        'country':'Nepal'
    }
}
addressvalid ={
    'street': {
        'type': str
    },
    'zipcode':{
        'type': int
    },
    'country':{
        'type': str
    }
}
validationentry = {
    'name': {
        'type':str,
        'minlength': 3,
        'maxlength': 10
    },
    'age': {
        'type': int,
        'minage':0,
        'maxage': 150
    },
    'address':{
        'type': dict,
        'item_nesteddict': addressvalid
    }
}