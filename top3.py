import pandas as pd



students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

def sort_for_scopes(mark_student:int) -> int: 
    print(mark_student)
    return mark_student


def make_report_about_top3(students_avg_scores:dict):
    sorted_dict = {}
    sort_students = sorted(students_avg_scores, key=students_avg_scores.get, reverse=True)
    for stydent in sort_students:
        sorted_dict[stydent] = students_avg_scores[stydent]

    
    best_students = {}
    count = 0
    for best_student in sorted_dict:
        
        if count == 3:
            break
        best_students[best_student] = sorted_dict[best_student]
        count +=1
        
    
    count = 0
    for stydent in best_students:
        print(count)
        
        
        if count == 0:
            first_exel = pd.DataFrame({'Name': [stydent],
                       'avg_scores': [best_students[stydent]],
            })
            # first_exel.to_excel('./first_best.xlsx')
            
        if count == 1:
            second_exel = pd.DataFrame({'Name': [stydent],
                       'avg_scores': [best_students[stydent]],
            })
            # second_exel.to_excel('./second_best.xlsx')
        if count == 2:
            third_exel = pd.DataFrame({'Name': [stydent],
                        'avg_scores': [best_students[stydent]],
            })
            # third_exel.to_excel('./third_best.xlsx')
        count +=1
        if count > 2:
            ar = pd.concat([first_exel, second_exel, third_exel])
            ar.to_excel('./best!.xlsx')
            
                   
    
    return '_best.xlsx'
    

make_report_about_top3(students_avg_scores)