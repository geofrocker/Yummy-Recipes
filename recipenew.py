"""Data handling file"""
class Recipe:
    """Recipe class"""
    def __init__(self, id, title, ingredients, steps, create_date, created_by):
        """Initialise class"""
        self.__id = id
        self.__title = title
        self.__ingredients = ingredients
        self.__steps = steps
        self.__create_date = create_date
        self.__created_by = created_by
    def set_recipe(self, id, title, ingredients, steps, create_date, created_by):
        """Set the recipe variables"""
        self.__id = id
        self.__title = title
        self.__ingredients = ingredients
        self.__steps = steps
        self.__create_date = create_date
        self.__created_by = created_by
    def edit_recipe(self, id, title, ingredients, steps, create_date, created_by):
        """Edit the recipe variables"""
        self.__id = id
        self.__title = title
        self.__ingredients = ingredients
        self.__steps = steps
        self.__create_date = create_date
        self.__created_by = created_by

    def get_recipe(self):
        """Get recipe"""
        recipe = [{
            'id':self.__id,
            'title':self.__title,
            'ingredients': self.__ingredients,
            'steps':self.__steps,
            'created_by':self.__created_by,
            'create_date': self.__create_date
        }]
        return recipe
    def get_id(self):
        """Get recipe_id"""
        return self.__id

    def get_title(self):
        """Get recipe_title"""
        return self.__title
    
    def get_ingredients(self):
        """Get recipe_ingredients"""
        return self.__ingredients
        
    def get_steps(self):
        """Get recipe_steps"""
        return self.__steps

class User:
    """User class"""
    __name = ''
    __username = ''
    __email = ''
    __password = ''
    def __init__(self, name, username, email, password):
        """Initialise class"""
        self.__name = name
        self.__username = username
        self.__email = email
        self.__password = password
    def set_user(self, name, username, email, password):
        """Set user"""
        self.__name = name
        self.__username = username
        self.__email = email
        self.__password = password
    
    def get_username(self):
        """get username"""
        return self.__username
    def get_password(self):
        """get password"""
        return self.__password
    