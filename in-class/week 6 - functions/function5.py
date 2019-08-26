def average_hair(class_list, hair_color):

    score_sum = 0
    count = 0

    for student in class_list:
        if hair_color['hair'] == hair_color:
            score_sum += student['score']
            count += 1
    return score_sum / count


average_hair([], 'dark')
