from abc import ABC, abstractmethod

from outbox.domain.models import Published


class PublishedRepository(ABC):
    @abstractmethod
    def save(self, published: Published) -> None:
        pass


class DjangoOutboxPatternPublishedRepository(PublishedRepository):
    def save(self, published: Published) -> None:
        published.to_django_outbox_pattern().save()


published_repository = DjangoOutboxPatternPublishedRepository()
