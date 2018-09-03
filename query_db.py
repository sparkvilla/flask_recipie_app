from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.models import Recipe

db_url = 'postgresql://diego:diego@192.168.1.113/flask_family_recipes_app'

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

#  for instance in session.query(Recipe).order_by(Recipe.id):
#     print(instance.recipe_title, instance.recipe_description)

# for title, description in session.query(Recipe.recipe_title, Recipe.recipe_description):
#    print(title, description)
#    print

for row in session.query(Recipe).all():
    print(row)
    # print(row.Recipe, row.recipe_title)
