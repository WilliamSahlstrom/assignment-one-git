def create_pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)  
        stars = "*" * (2 * i - 1)   
        print(spaces + stars)


height = 5  
create_pyramid(height)
