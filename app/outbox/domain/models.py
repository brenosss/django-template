from dataclasses import dataclass

from django_outbox_pattern.models import Published as DjangoOutboxPatternPublished


@dataclass
class Published:
    uuid: str
    destination: str
    body: str

    @staticmethod
    def from_django_outbox_pattern(
        django_outbox_pattern_published: DjangoOutboxPatternPublished,
    ):
        return Published(
            id=django_outbox_pattern_published.uuid,
            destination=django_outbox_pattern_published.destination,
            body=django_outbox_pattern_published.body,
        )

    def to_django_outbox_pattern(self):
        return DjangoOutboxPatternPublished(
            id=self.uuid,
            destination=self.destination,
            body=self.body,
        )
