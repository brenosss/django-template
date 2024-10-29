from abc import ABC, abstractmethod
from typing import Optional

from orders.domain.models import Order
from orders.models import DjangoOrder


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get(self, order_uuid: str) -> Optional[Order]:
        pass

    @abstractmethod
    def get_all(self) -> Order:
        pass


class DjangoOrderRepository(OrderRepository):
    def save(self, order: Order) -> None:
        order.to_django().save()

    def get(self, order_uuid: str) -> Optional[Order]:
        try:
            django_order = DjangoOrder.objects.get(uuid=order_uuid)
        except DjangoOrder.DoesNotExist:
            return None
        return Order.from_django(django_order)

    def get_all(self) -> list[Order]:
        django_orders = DjangoOrder.objects.all()
        return [Order.from_django(django_order) for django_order in django_orders]


order_repository = DjangoOrderRepository()
