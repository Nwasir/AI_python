"""When provided with a number between 0-9, return it in words. Note that
 the input is guaranteed to be within the range of 0-9.
 Input: 1  -----  Output: "One"."""

# def switch_it_up(number):
#     dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
#     7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
    
#     return dict.get(number)


# print(switch_it_up(4))

#  Or

def switch_it_up(number):
    if number == 1:
        return"One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    else:
        return "Zero"

print(switch_it_up(4))