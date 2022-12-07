from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30))
  year = db.Column(db.Integer())
  email = db.Column(db.String(120))

  def serialize(self):
    return {'id': self.id,'name': self.name,'year': self.year,'email':self.email}
