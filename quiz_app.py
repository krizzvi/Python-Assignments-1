def quiz_app(questions):
    score = 0
    for q in questions:
        print(q['question'])
        for idx, opt in enumerate(q['options'], start=1):
            print(f"{idx}. {opt}")
        answer = int(input("Your answer: "))
        if q['options'][answer - 1] == q['answer']:
            score += 1
    return score
