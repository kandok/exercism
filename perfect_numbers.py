def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sm = aliquotSum(number)

    if sm == number:
        return 'perfect'

    if sm > number:
        return 'abundant'

    return 'deficient'

def aliquotSum(number):
    sm = 0
    
    for i in range(1,number):
        if (number % i == 0):
            sm = sm + i 
            
    return sm
