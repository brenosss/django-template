from abc import ABC, abstractmethod
from typing import Optional

from carts.domain.models import Cart
from carts.models import DjangoCart


class CartRepository(ABC):
    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass

    @abstractmethod
    def get(self, cart_uuid: str) -> Optional[Cart]:
        pass

    @abstractmethod
    def get_all(self) -> Cart:
        pass

    @abstractmethod
    def update(self, cart: Cart) -> None:
        pass


class DjangoCartRepository(CartRepository):
    def save(self, cart: Cart) -> None:
        cart.to_django().save()

    def get(self, cart_uuid: str) -> Optional[Cart]:
        try:
            django_cart = DjangoCart.objects.get(uuid=cart_uuid)
        except DjangoCart.DoesNotExist:
            return None
        return Cart.from_django(django_cart)

    def get_all(self) -> list[Cart]:
        django_carts = DjangoCart.objects.all()
        return [Cart.from_django(django_cart) for django_cart in django_carts]

    def update(self, cart: Cart) -> None:
        django_cart = cart.to_django()
        django_cart.save()


cart_repository = DjangoCartRepository()
