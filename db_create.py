from project import db
from project.models import Recipe

# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

# insert recipe data
recipe1 = Recipe('Pasta burro e salvia','burro e salvia,','https://blog.giallozafferano.it/dolcipocodolci/pasta-burro-e-salvia-ricetta-primo-veloce/')
recipe2 = Recipe('Lasagne con ragu di salsiccia', 'salsiccia e pomodori','https://www.lacucinaitaliana.it/ricetta/primi/lasagne-con-ragu-di-salsiccia-e-crema-di-cipollotti/')
recipe3 = Recipe('Risotto radicchio e gorgonzola','radicchio e gorgonzola', 'https://www.ricette-bimby.com/risotto-radicchio-e-gorgonzola-bimby/')
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
# commit the changes
db.session.commit()
