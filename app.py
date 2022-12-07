from flask import Flask, render_template, Response, request
from flask_migrate import Migrate
from models import User,db
from config import DevelopmentConfig
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/user/getall', methods=['GET'])
def getAll():
  session = db.session()
  users = session.query(User).all()
  users_json = [user.serialize() for user in users]
  session.close()
  return Response(json.dumps(users_json))

@app.route('/user/create', methods=['POST'])
def create():
    body = request.get_json()
    session = db.session()
    try:
        user = User(name=body['name'], year=body['year'], email=body['email'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))

    except Exception as e:
        print(e)
        session.rollback()
        return {"erro": " It is not possible to save the user"}
    finally:
        session.close()

@app.route('/user/update/<int:user_id>', methods=['PUT'])
def update(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)
        if body and body['name']:
            user.name = body['name']
        if body and body['year']:
            user.year = body['year']
        if body and body['email']:
            user.email = body['email']

        session.commit()
        return {"OK": "User successfully updated"}
    except Exception as e:
        print(e)
        session.rollback()
        return {"Error": "Could not updated the user correctly"}
    finally:
        session.close()


@app.route('/user/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return {"OK": "User successfully deleted"}
    except Exception as e:
        print(e)
        return {"Error": "Could not deleted the user"}
    finally: session.close()


if __name__ == "__main__":
     	 app.run(debug=DevelopmentConfig.DEBUG,port=DevelopmentConfig.PORT_HOST)