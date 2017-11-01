"""Data handling file"""
class Recipe:
    """Recipe class"""
    __recipe = []
    def __init__(self):
        """Initialise class"""
        self.__recipe = self.__recipe

    def set_recipe(self, recipe):
        """Set the recipe variables"""
        self.__recipe.append(recipe)

    def get_recipes(self):
        """Get public recipes"""
        public_recipes = []
        for recipe in self.__recipe:
            if not recipe[7]:
                public_recipes.append(recipe)
        return public_recipes
    def get_user_recipes(self,user):
        """Get recipes"""
        user_recipes = []
        for recipe in self.__recipe:
            if recipe[6] == user:
                user_recipes.append(recipe)
        return user_recipes
    def get_recipe(self, recipeID):
        """Get recipe"""
        for recipe in self.__recipe:
            if recipe[0] == recipeID:
                return recipe
    def edit_recipe(self, recipeID, newrecipe):
        """Edit the recipe variables"""
        for recipe in self.__recipe:
            if recipe[0] == recipeID:
                index = self.__recipe.index(recipe)
                self.__recipe.remove(self.__recipe[index])
                return self.__recipe.insert(index, newrecipe)

    def delete_recipe(self, recipeID):
        """Edit the recipe variables"""
        for recipe in self.__recipe:
            if recipe[0] == recipeID:
                index = self.__recipe.index(recipe)
                return self.__recipe.remove(self.__recipe[index])
   
class User:
    """User class"""
    __users = []
    def __init__(self):
        """Initialise class"""
        self.__users = self.__users

    def register_user(self, user):
        """Set user"""
        self.__users.append(user)
        
    def login_user(self,username, password):
        """login user"""
        passed_user = []
        for user in self.__users:
            if user[3] == username and user[4] == password:
                passed_user.append(user)
        return passed_user

class Category:
    """User categories"""
    __cat = []
    def __init__(self):
        """Initialise class"""
        self.__cat = self.__cat

    def set_category(self, name):
        """Set category"""
        self.__cat.append(name)

    def get_category(self, cat_id):
        """get category name"""
        for cat in self.__cat:
            if cat[0] == cat_id:
                return cat[1]

    def edit_category(self, cat_id, new):
        """edit category name"""
        for cat in self.__cat:
            if cat[0] == cat_id:
                index = self.__cat.index(cat)
                self.__cat.remove(self.__cat[index])
                return self.__cat.insert(index, new)

    def delete_category(self, cat_id):
        """delete category name"""
        for cat in self.__cat:
            if cat[0] == cat_id:
                index = self.__cat.index(cat)
                return self.__cat.remove(self.__cat[index])

    def get_categories(self):
        """get category name"""
        return self.__cat
    def get_user_categories(self,user):
        """Get recipes"""
        user_categories = []
        for cat in self.__cat:
            if cat[2] == user:
                user_categories.append(cat)
        return user_categories

class Review:
    """create and retrieve reviews"""
    __reviews = []
    def __init__(self):
        """Initialise Review class"""
        self.__reviews = self.__reviews

    def set_review(self, review):
        """Set review"""
        self.__reviews.append(review)

    def get_reviews(self):
        """get reviews"""
        return self.__reviews