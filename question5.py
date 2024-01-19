def question5_1():
    """
    answer = {
            'bin1': [d1,d2,d3...]
            'bin2': [e1,...],
            'bin3': [f1,...]
    }
    where di, ei, fi are integers. 
    """
    ages = [23, 45, 18, 30, 60, 35, 50, 28, 40]
    bin_width = (max(ages) - min(ages)) / 3
    bin1 = [userID for userID, age in enumerate(ages) if min(ages) <= age < min(ages) + bin_width]
    bin2 = [userID for userID, age in enumerate(ages) if min(ages) + bin_width <= age < min(ages) + 2 * bin_width]
    bin3 = [userID for userID, age in enumerate(ages) if min(ages) + 2 * bin_width <= age <= max(ages)]

    answer={
    "bin1": bin1,
    "bin2": bin2,
    "bin3": bin3
    }
    return answer

def question5_2():
    answer={'bin1': [2, 0, 7], 'bin2': [3, 5, 8], 'bin3': [1, 6, 4]}
    return answer

def question5_3():
    answer={'bin1': [3, 1], 'bin2': [8, 4, 6], 'bin3': [9, 2, 7, 5]}
    return answer 
