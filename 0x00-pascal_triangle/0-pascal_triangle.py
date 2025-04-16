def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    
    Args:
        n (int): The number of rows to generate.
    
    Returns:
        list of lists: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Each row starts with 1
        
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)
    
    return triangle
