from flask import Blueprint
from flask_cache import Cache

blue = Blueprint('blue', __name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})


@blue.route('/getinfo')
@cache.cached(timeout=30, key_prefix='infocache')
def get_info():
    print('进入get_info()方法了。。。')
    return "<h3 style='color:red'>hello, world!</h3>"
