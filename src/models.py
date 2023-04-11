from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
characterFavorites = db.Table("characterFavorite",
     db.Column("id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
     db.Column("id", db.Integer, db.ForeignKey("character.id"), primary_key=True)
)

planetsFavorites = db.Table("planetsFavorite",
     db.Column("id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
     db.Column("id", db.Integer, db.ForeignKey("planet.id"), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    planetsFavorite = db.relationship("Planet", secondary=planetsFavorites,
                                      primaryjoin="User.id==planetsFavorite.c.id",
                                      secondaryjoin="Planet.id==planetsFavorite.c.id",
                                      lazy='subquery',
                                      backref=db.backref("users",  lazy=True))
    characterFavorite = db.relationship("Character", secondary=characterFavorites,
                                      primaryjoin="User.id==characterFavorite.c.id",
                                      secondaryjoin="Character.id==characterFavorite.c.id",
                                      lazy='subquery',
                                      backref=db.backref("users",  lazy=True))
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Character(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.status,
            "mass": self.species,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            
        }

    def serialize_each(self):
         return {
            "id": self.id,
            "properties":{
                "name": self.name,
                "gender": self.gender
            }
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)

    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def serialize_each(self):
         return {
            "id": self.id,
            "properties":{
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            }
        }