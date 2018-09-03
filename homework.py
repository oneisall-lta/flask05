from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from bookapp.models import *
from bookapp import create_app, db


app = create_app()
magrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
