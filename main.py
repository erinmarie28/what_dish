
def get_dish():

    #GET INPUTS FROM USER
    savory = input("Savory? y/n  ")
    sweet = input("Sweet? y/n  ")
    healthy = input("Healthy? y/n or idc  ")
    time_to_cook = int(input("How much time do you have to cook in minutes?  "))
    any_must_have_ingrdts = input("Any must have ingredients? y/n   ")
    
    if any_must_have_ingrdts == 'y':
        must_have_ingrdt = input("Enter any must have ingredients separated by commas in their singular form(Ex. mushroom, strawberry, etc.): ").lower().split(",")
    
    #CREATE DICTIONARY OF DISHES FROM TEXT FILE
    dishes = {}
    i = 0
    with open("dishes.txt", 'r') as f:
        for line in f:
            listDetails = line.strip().split('|')
            dishes[i] = {"name": listDetails[0]}
            dishes[i].update({"healthy_yn": listDetails[1]})
            dishes[i].update({"savory_yn": listDetails[2]})
            dishes[i].update({"sweet_yn": listDetails[3]})
            dishes[i].update({"ingredients_list": list(listDetails[4].split(", "))})
            dishes[i].update({"opt_ingredients_list": list(listDetails[5].split(", "))})
            dishes[i].update({"time": listDetails[6]})
            i+=1

    #DETERMINE IF ANY DISHES MATCH THE USER INPUTS
    no_dish = False
    dish_count = 0
    for i in range(len(dishes)):
        #CHECK TO SEE IF A DISH MATCHES THE USERS PREFERENCES FOR TIME, HEALTHINESS, SWEETNESS, AND SAVORYNESS
        if (int(dishes[i]['time']) <= time_to_cook) and \
            ((dishes[i]['healthy_yn'] == healthy) or (healthy == 'idc')) and \
            ((dishes[i]['savory_yn'] == savory) or (dishes[i]['sweet_yn'] == sweet)):
            
            #IF USER ENTERED MUST HAVE INGREDIENTS, CHECK TO SEE IF THEY MATCH ANY DISHES
            if any_must_have_ingrdts == 'y':
                for item in must_have_ingrdt:
                    if (item in dishes[i]['ingredients_list']) or \
                        (item in dishes[i]['opt_ingredients_list']):

                        print("Possible dish to cook: {}".format(dishes[i]['name']))
                        print("Ingredients for {}: {}".format(dishes[i]['name'], dishes[i]['ingredients_list']))
                        print("Optional ingredients & substitutions for {}: {}".format(dishes[i]['name'], dishes[i]['opt_ingredients_list']))
                        dish_count+=1
                        no_dish = False
                    else:
                        no_dish = True    

            #IF USER DOESN'T HAVE ANY MUST HAVE INGREDIENTS           
            else:
                print("Possible dish to cook: {}".format(dishes[i]['name']))
                print("Ingredients for {}: {}".format(dishes[i]['name'], dishes[i]['ingredients_list']))
                print("Optional ingredients & substitutions for {}: {}".format(dishes[i]['name'], dishes[i]['opt_ingredients_list']))
                dish_count+=1
                no_dish = False
        #NO DISH MATCHES THE CRITERIA FOR TIME, HEALTHINESS, SWEETNESS, OR SAVORYNESS
        else:
            no_dish = True
            
    #RETURN MESSAGE TO USER IF NO DISH IS FOUND        
    if no_dish and dish_count==0:
        print("Sorry! None of the dishes match your criteria. Try changing some selections.")


get_dish()


