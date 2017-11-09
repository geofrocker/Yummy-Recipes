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
        return 'Recipe created successfully'

    def get_recipes(self):
        """Get public recipes"""
        public_recipes = []
        for recipe in self.__recipe:
            if not recipe['private']:
                public_recipes.append(recipe)
        return public_recipes
    def get_user_recipes(self, user):
        """Get recipes"""
        user_recipes = []
        for recipe in self.__recipe:
            if recipe['created_by'] == user:
                user_recipes.append(recipe)
        return user_recipes

    def get_recipe_titles(self, user, title):
        """Get recipes titles for a user"""
        user_recipes = []
        for recipe in self.__recipe:
            if recipe['created_by'] == user and recipe['title'] == title:
                user_recipes.append(recipe)
        return user_recipes

    def get_recipe(self, recipeID):
        """Get recipe"""
        for recipe in self.__recipe:
            if recipe['id'] == recipeID:
                return recipe
    def edit_recipe(self, recipeID, newrecipe):
        """Edit the recipe variables"""
        for recipe in self.__recipe:
            if recipe['id'] == recipeID:
                index = self.__recipe.index(recipe)
                self.__recipe.remove(self.__recipe[index])
                self.__recipe.insert(index, newrecipe)
                return 'Recipe edited successfully'
            return 'Recipe does not exist'

    def delete_recipe(self, recipeID):
        """Delete the recipe """
        for recipe in self.__recipe:
            if recipe['id'] == recipeID:
                index = self.__recipe.index(recipe)
                self.__recipe.remove(self.__recipe[index])
                return 'Recipe deleted'
            return 'Recipe does not exist'
   
class User:
    """User class"""
    __users = []
    def __init__(self):
        """Initialise class"""
        self.__users = self.__users

    def register_user(self, user):
        """Set user"""
        self.__users.append(user)
        return 'Your are now registered and can log in'
    
    def check_user_name(self, username):
        """check if username name exists"""
        usernames = []
        for user in self.__users:
            if user['username'] == username:
                usernames.append(user)
        return usernames

    def check_user_email(self, email):
        """check if email name exists"""
        useremails = []
        for user in self.__users:
            if user['email'] == email:
                useremails.append(user)
        return useremails
        
    def login_user(self,username, password):
        """login user"""
        passed_user = []
        for user in self.__users:
            if user['username'] == username and user['password'] == password:
                passed_user.append(user)
        return passed_user

class Category:
    """Category class"""
    __cat = []
    def __init__(self):
        """Initialise class"""
        self.__cat = self.__cat

    def set_category(self, name):
        """Set category"""
        self.__cat.append(name)
        return 'Category created successfully'

    def get_category(self, cat_id):
        """get category name"""
        for cat in self.__cat:
            if cat['id'] == cat_id:
                return cat['name']

    def edit_category(self, cat_id, new):
        """edit category name"""
        for cat in self.__cat:
            if cat['id'] == cat_id:
                index = self.__cat.index(cat)
                self.__cat.remove(self.__cat[index])
                self.__cat.insert(index, new)
                return 'Category edited successfully'

    def delete_category(self, cat_id):
        """delete category name"""
        for cat in self.__cat:
            if cat['id'] == cat_id:
                index = self.__cat.index(cat)
                self.__cat.remove(self.__cat[index])
                return 'Category deleted Successfully'

    def get_categories(self):
        """get category name"""
        return self.__cat

    def get_user_categories(self, user):
        """Get user categoreis"""
        user_categories = []
        for cat in self.__cat:
            if cat['created_by'] == user:
                user_categories.append(cat)
        return user_categories

    def get_category_name(self, user, name):
        """check if category name exists"""
        user_categories = []
        for cat in self.__cat:
            if cat['name'] == name and cat['created_by'] == user:
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
        return 'Review created successfully'

    def get_reviews(self, recipe_id):
        """get reviews"""
        rec_reviews = []
        for review in self.__reviews:
            if review['recipe_id'] == recipe_id:
                rec_reviews.append(review)
        return rec_reviews

    def get_num_reviews(self, recipe_id):
        """get reviews"""
        num_reviews = 0
        for review in self.__reviews:
            if review['recipe_id'] == recipe_id:
                num_reviews+=1
        return num_reviews

class UpVote:
    """vote class"""
    __up_votes = []
    def __init__(self):
        """initialise Upvote class"""
        self.__up_votes = self.__up_votes
        
    def set_upvote(self, new_vote):
        """set upVote"""
        self.__up_votes.append(new_vote)
        return 'Recipe upvoted Successfully'

    def check_upvote(self, user, recipe_id):
        """check if user has already voted"""
        my_vote = []
        for up_vote in self.__up_votes:
            if up_vote['voted_by'] == user and up_vote['recipe_id'] == recipe_id:
                my_vote.append(up_vote)
        return my_vote

    def get_upVotes(self,recipe_id):
        """get upVotes"""
        votes = 0
        for up_vote in self.__up_votes:
            if up_vote['recipe_id'] == recipe_id:
                votes+=1
        return votes

