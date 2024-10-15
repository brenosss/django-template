from jaiminho.constants import PublishStrategyType
from jaiminho.send import save_to_outbox_stream

from orders.models import Order


@save_to_outbox_stream(None, PublishStrategyType.KEEP_ORDER)
def craete_order(cart_id, price):
    Order.objects.create(cart_id=cart_id, price=price)
    print("Order created successfully!")