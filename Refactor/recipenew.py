"""Data handling file"""
class Recipe:
    """Recipe class"""
    __id = ''
    __title = ''
    __category = ''
    __ingredients = ''
    __steps = ''
    __create_date = ''
    __created_by = ''
    def __init__(self):
        """Initialise class"""
        self.__id = self.__id 
        self.__title = self.__title
        self.__category = self.__category
        self.__ingredients = self.__ingredients
        self.__steps = self.__steps
        self.__create_date = self.__create_date
        self.__created_by = self.__created_by
    def set_recipe(self, id, title, cat, ingredients, steps, create_date, created_by):
        """Set the recipe variables"""
        self.__id = id
        self.__title = title
        self.__category = cat
        self.__ingredients = ingredients
        self.__steps = steps
        self.__create_date = create_date
        self.__created_by = created_by
    def edit_recipe(self, id, title, cat, ingredients, steps, create_date, created_by):
        """Edit the recipe variables"""
        self.__id = id
        self.__title = title
        self.__category = cat
        self.__ingredients = ingredients
        self.__steps = steps
        self.__create_date = create_date
        self.__created_by = created_by

    def get_recipe(self):
        """Get recipe"""
        recipe = [{
            'id':self.__id,
            'title':self.__title,
            'category':self.__category,
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
    def get_category(self):
        """Get recipe_category"""
        return self.__category

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
    def __init__(self):
        """Initialise class"""
        self.__name = self.__name
        self.__username = self.__username
        self.__email = self.__email
        self.__password = self.__password
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

class Category:
    """User categories"""
    __cat = []
    def __init__(self):
        """Initialise class"""
        self.__cat = self.__cat

    def set_category(self, name):
        """Set category"""
        self.__cat.append(name)

    def get_category(self, name):
        """get category name"""
        for cat in self.__cat:
            if cat == name:
                return cat

    def edit_category(self, name, new):
        """edit category name"""
        index = self.__cat.index(name)
        self.__cat.remove(self.__cat[index])
        return self.__cat.insert(index, new)

    def delete_category(self, name):
        """delete category name"""
        index = self.__cat.index(name)
        self.__cat.remove(self.__cat[index])

    def get_categories(self):
        """get category name"""
        return self.__cat
