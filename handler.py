# create a file called server.py, which reads in the contents of restaurants.txt and creates some HTML from it, which is then served. 
# Consider the idea of a Class, which we discussed last week: you can model a restaurant has having two properties, 
# a name and a neighborhood. 
# You can then create a list of restaurants, 
# and loop over this to create your HTML

class Restaurant:
    def __init__(self, name, district):
        self.name = name
        self.district = district


def restaurant_handler():
    """
    reads from restaurants.txt and returns a 
    html file for it
    """
    
    txtfile = open('restaurants.txt','r')
    restaurants = []
    for line in txtfile:
        fields = line.split(',')
        field1 = fields[0].strip("\"") 
        field1.strip() "\""
        field2 = fields[1].strip("\"") # trim() -> " \t\n"
    
        restaurants.append(Restaurant(field1, field2))

        print(field1+' '+field2+'')

    txtfile.close()

    htmlList = ""
    for r in restaurants:
        htmlList += "<li>" + r.name + " in " + r.district + "</li>"


    return """<html>
    <head></head>
    <body><p>These are my favorite restaurants in Berlin</p>
    <ul>""" + htmlList + """
    </body></html>"""