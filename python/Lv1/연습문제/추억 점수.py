def solution(name, yearning, photo):
    answer = []
    
    # make dictionary
    score_dict = {key: value for key, value in zip(name,yearning)}
    
    for people in photo:
        score = sum(score_dict.get(person, 0) for person in people)
        answer.append(score)
            

    return answer