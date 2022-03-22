#ADD TO THE LIST OF DISHES

def get_dish_from_user():

    #GET USER INPUTS
    name_inp = input("What is the name of your dish?  ")
    healthy_inp = input("Is the dish healthy? y/n  ")
    savory_inp = input("Is the dish savory? y/n  ")
    sweet_inp = input("Is the dish sweet? y/n  ")
    ingrd_list_inp = input("What ingredients must be used (at a minimum)? Please separate your ingredients w/ commas. ").replace(", ",",")
    opt_ingrd_list_inp = input("What optional ingredients can be used? Please separate your ingredients w/ commas. ").replace(", ",",")
    time_inp = int(input("How much time does the dish take to prep/cook?  "))

    #CONFIRM W/ THE USER THAT THEIR INPUTS LOOK CORRECT
    print("Name: {} | Healthy: {} | Savory: {} | Sweet: {} | Ingredient List (Req): {} | Ingredient List (Opt): {} | Time to Cook: {}".format(name_inp, healthy_inp, savory_inp, sweet_inp, ingrd_list_inp, opt_ingrd_list_inp,str(time_inp)))
    add_to_dishes = input("If this looks correct, would you like to add it to the dishes library? y/n  ")

    #ADD DISH TO TEXT FILE
    if add_to_dishes == 'y':
        f = open("dishes.txt", 'a')
        f.write("{}|{}|{}|{}|{}|{}|{}".format(name_inp, healthy_inp, savory_inp, sweet_inp, ingrd_list_inp, \
        opt_ingrd_list_inp,str(time_inp)) + '\n')
        f.close()
        print("Okay, we have added {} to the dishes library!". format(name_inp))
    else:
        print("Okay, we won't add this one to the dishes library.")    


    

get_dish_from_user()