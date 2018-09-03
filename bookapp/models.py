from . import db   # . 表示当前目录


class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    books = db.relationship('Book', backref='publish', uselist=False)

    def __repr__(self):
        return '<Publisher %r>' % self.name


middle = db.Table('book_author',
                  db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
                  db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True))
# 'author_id' 为中间表的列名，自定义。


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
    publish_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

    def __repr__(self):
        return '<Book %s>' % self.name


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(10))
    books = db.relationship(Book, secondary='book_author', backref=db.backref('authors'))
    # db.backref() 函数可以添加多个参数

    def __repr__(self):
        return '<Author %s>' % self.name
