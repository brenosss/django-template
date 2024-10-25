from dataclasses import dataclass
from datetime import datetime

from carts.models import DjangoCart


@dataclass
class Cart:
    uuid: str
    total_amount: float
    created_at: datetime
    closed: bool

    @staticmethod
    def from_django(django_cart: DjangoCart):
        return Cart(
            uuid=django_cart.uuid,
            total_amount=django_cart.total_amount,
            created_at=django_cart.created_at,
            closed=django_cart.closed,
        )

    def to_django(self):
        return DjangoCart(
            uuid=self.uuid,
            total_amount=self.total_amount,
            created_at=self.created_at,
            closed=self.closed,
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "total_amount": self.total_amount,
            "created_at": self.created_at,
            "closed": self.closed,
        }
