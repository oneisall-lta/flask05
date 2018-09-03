from flask_script import Manager

from Restdemo.rest import app
print('rest start ......')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
