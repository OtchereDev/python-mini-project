applicants_dicts = {
    "Amma":{
        "experience":2,
        "languages": ["java","c+","c"],
        "proj_supervision":False
    },
    "Kojo":{
        "experience":5,
        "languages":["cobol","python","java","peril"],
        "proj_supervision":True
    },
    "Nana":{
        "experience": 8,
        "languages":["ruby","javascript","java"],
        "proj_supervision": True
    },
    "Oliver":{
        "experience":1,
        "languages":["python","javascript","css"],
        "proj_supervision": False
    },
    "Aba":{
        "experience":6,
        "languages":["ruby","python","java"],
        "proj_supervision":True
    }
}


min_experience = 4
preferred_language=["python","java"]

for name, cv_dict in applicants_dicts.items():
    if cv_dict["experience"] >= min_experience  and \
         ((set(preferred_language).issubset(set(cv_dict["languages"])) or cv_dict["proj_supervision"])):
        print(name + " pass the screening")