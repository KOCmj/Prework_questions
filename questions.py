# Printing input that says hello to a user
def hello_name(user_name):
    """Display a greeting to users"""
    print("Hello, " + user_name + "!")

hello_name('muffy')

# Printing function for odd numbers from 1-100 
def first_odd():
    """Display odds numbers from 1-100"""
    for num in range(1,101,2):
        if num % 2 != 0:
            print(num)
        else:
            return None

first_odd()


# Returning max numbers of a list
def max_num_in_list(a_list):
     """Return max numbers"""
     Max = 10 
     for item in a_list:
         if item > Max:
             Max=item
             return Max
     
List=[1,2,3,4,5,6,7,8,9,10]
print(max(List))


#Function that specifies if a given year is a leap year
def is_leap_year(a_year):
    if (a_year%400==0) or (a_year%4==0 and a_year%100!=0):
        return True
    else:
        return False

year= (2025)
print(is_leap_year(year))


    
#Function for consecutive numbers
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

numb= [1,2,3,4,5,6]
print(is_consecutive(numb))
