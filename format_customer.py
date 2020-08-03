"""
This contains a function that format customer's name
"""

def customer(first_name,second_name,location=None):
    name='%s %s' % (first_name, second_name)
    if location:
        print('%s (%s)' % (name, location)) 
    else:
        print(name) 

