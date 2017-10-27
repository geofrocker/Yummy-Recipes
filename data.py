"""Data handling file"""
class TempRecipes:
    """Recipe class"""
    __all_recipes = []
    def __init__(self):
        """Initialise class"""
        __all_recipes = []
    def set_recipe(self, id, title, ingredients, steps, create_date, created_by):
        """Set the recipe variables"""
        recipe_data = {}
        recipe_data['id'] = id
        recipe_data['title'] = title
        recipe_data['ingredients'] = ingredients
        recipe_data['steps'] = steps
        recipe_data['create_date'] = create_date
        recipe_data['created_by'] = created_by
        self.__all_recipes.append(recipe_data)
    
    def get_recipes(self):
        """Get recipes"""
        return self.__all_recipes

    def get_recipe(self, recipe_id):
        """Get recipes"""

        return [element for element in self.__all_recipes if element['id'] ==recipe_id]

class TempUser:
    """User class"""
    __all_users = []


    def __init__(self):
        """Initialise class"""
        __all_users = []

    def set_user(self, name, username, email, password):
        """Set user"""
        user_data = {} 
        user_data['name'] = name
        user_data['username'] = username
        user_data['email'] = email
        user_data['password'] = password
        self.__all_users.append(user_data)

    def get_users(self):
        """Get Users"""
        return self.__all_users


    # temp_users = TempUser()
    # for user in users.items:
    #     temp_users.set_user(user.id, user.name, user.username, user.email, user.password)
    #     output = temp_users.get_users()

    # return jsonify({'Users':output})