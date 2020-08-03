def patient_record(*a_list, **a_dict):
    for person in a_list:
        for patient, info in a_dict.items():
            if person==patient:
                print(patient + " : ")
                for key, value in info.items():
                    print(key + " = " +str(value))  
        print()  



persons_quene=["Oliver", "Kofi","ellen","bismark","kojo"]
patients_dict={
    'Ama':{
        'Age':26,
        'weight':50
    },
    'Kofi':{
        'Age':19,
        'weight':29
    },
    'Oliver':{
        'Age':5,
        'weight': 6
    }
}

patient_record(*persons_quene,**patients_dict)