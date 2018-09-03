from flask_script import Manager

from App import create_app

app = create_app('develop')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()