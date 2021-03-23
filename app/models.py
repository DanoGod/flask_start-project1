from . import db


class UserProperty(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    numofbed = db.Column(db.Integer)
    numofbathroom = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.String(80))
    typeo = db.Column(db.String(80))
    description = db.Column(db.String(300))
    image = db.Column(db.String(200))
	
    def __init__(self, title, numofbed, numofbathroom, location, price, typeo, description, image):
        self.title = title
        self.numofbed = numofbed
        self.numofbathroom = numofbathroom
        self.location = location
        self.price = price
        self.typeo = typeo 
        self.description = description
        self.image = image
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.id)
