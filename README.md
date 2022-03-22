# what_dish

Description:
When meal time rolls around, I often don't feel like thinking about what to cook. I created this tool to easily return some of the dishes I regularly cook based on whether I want something healthy, savory, or sweet using ingredients I have on hand and in the amount of time I have available. Additionally, I created a file to easily add dishes to the text file as needed.

Build Status: Operational, but plan to add more features

Files & What They Are Used For:
- main.py --> main file, collects user inputs and returns dishes with the matching criteria
- add_dishes.py --> launch to add dishes to the text file
- dishes.txt --> text file included all dishes and their criteria (name, healthy_yn, savory_yn, sweet_yn, ingredients_list, opt_ingredients_list, time)

Additional Details:
- Please make sure you are using Python3
- No additional packages are needed at this time


Features I plan to add:
- Web page interface
- Ability to confirm which dish was chosen
- Ability for the user to add comments to dishes
- Ability for the user to update existing dishes
- Ability to denote allergies or restrictions
- Ability to add dishes using a table instead of the add_dishes.py file
- Potentially move dishes list to a database and expand the criteria that can be selected (Ex. meal vs. side, breakfast/lunch/dinner/snack/dessert, dietary restrictions)
