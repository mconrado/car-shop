from sqlalchemy import event
from app import db
from app.models import Car, Owner


def update_owner_sales_o(connection, owner_id):
    car_count = (
        connection.execute(db.select(Car).where(Car.owner_id == owner_id)).scalar() or 0
    )

    connection.execute(
        Owner.__table__.update()
        .where(Owner.id == owner_id)
        .values(sales_o=(car_count == 0))
    )


@event.listens_for(Car, "after_insert")
def update_owner_sales_o_on_insert(mapper, connection, target):
    owner_id = target.owner_id
    update_owner_sales_o(connection, owner_id)


@event.listens_for(Car, "after_delete")
def update_owner_sales_o_on_delete(mapper, connection, target):
    owner_id = target.owner_id
    update_owner_sales_o(connection, owner_id)
