from flask import Flask, request
from flask_migrate import Migrate
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from extensions import db, bcrypt, jwt
from models import User, Note


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "your-secret-key"

db.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)
jwt.init_app(app)


@app.route("/")
def home():
    return {"message": "Flask Productivity API is running"}


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password are required"}, 400

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return {"error": "Username already exists"}, 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "username": user.username
        }
    }, 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return {"error": "Invalid username or password"}, 401

    access_token = create_access_token(identity=str(user.id))

    return {
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username
        }
    }, 200


@app.route("/check_session", methods=["GET"])
@jwt_required()
def check_session():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if not user:
        return {"error": "User not found"}, 404

    return {
        "id": user.id,
        "username": user.username
    }, 200
@app.route("/notes", methods=["GET"])
@jwt_required()
def get_notes():
    user_id = int(get_jwt_identity())

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    pagination = Note.query.filter_by(user_id=user_id).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    notes = []

    for note in pagination.items:
        notes.append({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at.isoformat(),
            "user_id": note.user_id
        })

    return {
        "notes": notes,
        "pagination": {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages
        }
    }, 200


@app.route("/notes", methods=["POST"])
@jwt_required()
def create_note():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return {"error": "Title and content are required"}, 400

    note = Note(
        title=title,
        content=content,
        user_id=user_id
    )

    db.session.add(note)
    db.session.commit()

    return {
        "message": "Note created successfully",
        "note": {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at.isoformat(),
            "user_id": note.user_id
        }
    }, 201


@app.route("/notes/<int:id>", methods=["PATCH"])
@jwt_required()
def update_note(id):
    user_id = int(get_jwt_identity())

    note = Note.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not note:
        return {"error": "Note not found"}, 404

    data = request.get_json()

    if "title" in data:
        note.title = data["title"]

    if "content" in data:
        note.content = data["content"]

    db.session.commit()

    return {
        "message": "Note updated successfully",
        "note": {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at.isoformat(),
            "user_id": note.user_id
        }
    }, 200


@app.route("/notes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_note(id):
    user_id = int(get_jwt_identity())

    note = Note.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not note:
        return {"error": "Note not found"}, 404

    db.session.delete(note)
    db.session.commit()

    return {
        "message": "Note deleted successfully"
    }, 200

if __name__ == "__main__":
    app.run()