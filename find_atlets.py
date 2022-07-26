know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmens = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_atlets(know_english: list, sportsmen: list, more_than_20_years: list) -> list:
    chempions = []
    for student_en, sportsmen, more_than_20_year in zip(know_english,sportsmens, more_than_20_years):
        if student_en in sportsmens and student_en in more_than_20_years:
            chempions.append(student_en)
        if sportsmen in know_english and more_than_20_years:
            chempions.append(sportsmen)
        if more_than_20_year in know_english and sportsmens:
            chempions.append(more_than_20_year)
        
        return chempions

find_atlets(know_english, sportsmens, more_than_20_years)