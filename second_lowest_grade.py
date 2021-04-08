def second_lowest(name_list,score_list):
    sort_score_list = list(set(score_list))
    sort_score_list.sort()
    second_lowest_grade = sort_score_list[1]
    student_name = []
    for e in name_list:
        if e[1] == second_lowest_grade:
            student_name.append(e[0])
        else:
            pass
    student_name.sort()
    return student_name

if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        name_list.append([name,score])
    for i in second_lowest(name_list,score_list):
        print(i)
