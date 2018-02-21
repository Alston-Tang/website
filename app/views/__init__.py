from .oatuh import oauth
from .. import app


app.register_blueprint(oauth, url_prefix='/oauth')



