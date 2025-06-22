from models import db, Bakery, BakedGood
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    b1 = Bakery(name="Delightful donuts")
    b2 = Bakery(name="Incredible crullers")

    db.session.add_all([b1, b2])
    db.session.commit()

    bg1 = BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=b1.id)
    bg2 = BakedGood(name="Apple-spice filled donut", price=3.50, bakery_id=b1.id)
    bg3 = BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=b2.id)
    bg4 = BakedGood(name="Chocolate cruller", price=100.00, bakery_id=b2.id)

    db.session.add_all([bg1, bg2, bg3, bg4])
    db.session.commit()
