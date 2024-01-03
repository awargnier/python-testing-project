class NegativeValueError (Exception):
    pass

def total_with_tips (bill, percentage) :
    if bill < 0 :
        raise NegativeValueError("bill should be positive")
    if percentage < 0 :
        raise NegativeValueError("percentage should be positive")
    tip = bill*percentage/100
    tip = min(tip, 500)
    total = bill + tip 
    total = round(total, 2)
    return max(total, 5)