from project import db


class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_description = db.Column(db.String, nullable=False)
    recipe_url = db.Column(db.String, nullable=False)

    def __init__(self, title, description, url):
        self.recipe_title = title
        self.recipe_description = description
        self.recipe_url = url


    def __repr__(self):
        return '<title {}'.format(self.recipe_title)
