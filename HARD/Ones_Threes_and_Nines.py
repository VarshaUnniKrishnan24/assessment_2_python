
'''  Ones, Threes and Nines (Version #2)
Given an integer between 0 and 26, make a variable (self.answer).
 That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would
 at least take for the number of each to add up to the given integer when 
 multiplied by one, three or nine (depends).
'''

class OnesThreesNines:
    def __init__(self, num):
        if 0 <= num <= 26:
            self.answer = self.calculate(num)
        else:
            self.answer = "Invalid input. Please enter an integer between 0 and 26."
    
    def calculate(self, num):
        nines = num // 9
        num %= 9
        
        threes = num // 3
        num %= 3
        
        ones = num
        
        return f"nines:{nines}, threes:{threes}, ones:{ones}"

try:
    num = int(input("Enter an integer between 0 and 26: "))
    result = OnesThreesNines(num)
    print(result.answer)
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")

# print(OnesThreesNines(10).answer)  # "nines:1, threes:0, ones:1"
# print(OnesThreesNines(15).answer)  # "nines:1, threes:2, ones:0"
# print(OnesThreesNines(22).answer)  # "nines:2, threes:1, ones:1"