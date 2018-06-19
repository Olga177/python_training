author_='Olga'

def percents(x,y):
    """ What percentage of x is y? """
    one_percent = x/100
    result = y / one_percent
    return result

def print_percentage(x,y):
    """ Print what percentage of x is y """
    print (str(y) +' is '+ str(percents(x,y)) + ' % '+ str(x))

print_percentage(200,50)