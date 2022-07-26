import datetime
now = datetime.datetime.now()

def get_inductees(names:list, birthday_years:list, genders:list) -> list:

    fit_for_military = []
    undefineds = [] 
    for name, birthday, gender in zip(names, birthday_years, genders):
        if gender == "Male":
            try:
                if now.year - birthday < 30 and now.year - birthday > 18:
                    print(f'{name} Годен к службе!')
            except TypeError:
                print(f'{name} не определен')













names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]

get_inductees(names, birthday_years, genders)