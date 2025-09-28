def number_pattern(n):
    # Check if n is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if n is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Generate the number pattern using a for loop
    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))
    
    return " ".join(numbers)
