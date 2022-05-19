def grade_converter(score):
    """
    Returns a letter grade equivilent to the score passed
    :param score: float
    :return: str equivilent to score
    """

    grade = ""
    if score > 97:
        grade = "A+"
    elif score > 93:
        grade = "A"
    elif score > 90:
        grade = "A-"
    elif score > 87:
        grade = "B+"
    elif score > 83:
        grade = "B"
    elif score > 80:
        grade = "B-"
    elif score > 77:
        grade = "C+"
    elif score > 73:
        grade = "C"
    elif score > 70:
        grade = "C-"
    elif score > 67:
        grade = "D+"
    elif score > 63:
        grade + "D"
    else:
        grade = "F"
    return grade