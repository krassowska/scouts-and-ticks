from pandas import Series
from fractions import Fraction


def score_and_add_columns(scoring_functions, myths, g):
    for column_name, scoring_function in scoring_functions.items():
        g = g.assign(**{column_name + '_score': Series(
            scoring_function(getattr(row, column_name), row)
            for row in g.itertuples(index=False)
        ).values})

    def score_mit(row, column_name, is_myth):
        response = getattr(row, column_name)
        # 'Nie wiem' means 'I don't know'
        if response == 'Nie wiem':
            return 0

        if is_myth:
            return 1 if response == 'Mit' else 0
        else:
            return 1 if response == 'Prawda' else 0

    for column_name, is_myth in myths.items():
        g = g.assign(**{column_name + '_score': Series(
            score_mit(row, column_name, is_myth)
            for row in g.itertuples(index=False)
        ).values})

    graded_columns = []
    kolumny_z_ocenami = []

    for nazwa_kolumny in scoring_functions.keys():
        graded_columns.append(nazwa_kolumny)
        kolumny_z_ocenami.append(nazwa_kolumny + '_score')

    for nazwa_kolumny in myths.keys():
        graded_columns.append(nazwa_kolumny)
        kolumny_z_ocenami.append(nazwa_kolumny + '_score')

    return g, kolumny_z_ocenami, graded_columns


def score(
    answers, correct_answers, wrong_answers,
    any_correct_gives_full_points=False, wrong_gets_same_weight_as_correct=False
):
    # g a = 5
    # b a = 1
    good_answer_weight = Fraction(1, len(correct_answers)) # 1/5
    bad_answer_weight = Fraction(1, len(wrong_answers)) # 1
    if wrong_gets_same_weight_as_correct:
        bad_answer_weight = good_answer_weight # 1/5
    score = 0
    answers = answers.split(';')
    if any_correct_gives_full_points:
        if any(correct_answer in answers for correct_answer in correct_answers):
            score += 1
    else:
        for answer in correct_answers:
            if answer in answers:
                score += good_answer_weight

    for answer in wrong_answers:
        if answer in answers:
            score -= bad_answer_weight

    return score
