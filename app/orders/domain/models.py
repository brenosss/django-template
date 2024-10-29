from dataclasses import dataclass
from datetime import datetime

from orders.models import DjangoOrder


@dataclass
class Order:
    uuid: str
    cart_uuid: str
    price: float
    created_at: datetime

    @staticmethod
    def from_django(django_order: DjangoOrder):
        return Order(
            uuid=django_order.uuid,
            cart_uuid=django_order.cart_uuid,
            price=django_order.price,
            created_at=django_order.created_at,
        )

    def to_django(self):
        return DjangoOrder(
            uuid=self.uuid,
            cart_uuid=self.cart_uuid,
            price=self.price,
            created_at=self.created_at,
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "cart_uuid": self.cart_uuid,
            "price": self.price,
            "created_at": self.created_at,
        }
