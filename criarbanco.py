from feedimagens import app, database
from feedimagens.models import Usuario, Foto

with app.app_context():
    database.create_all()
