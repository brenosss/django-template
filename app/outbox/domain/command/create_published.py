from uuid import uuid4

from outbox.domain.models import Published
from outbox.domain.repositories import published_repository


class CreatePublishedCommand:
    def __init__(self, destination: str, body: str):
        self.uuid = str(uuid4())
        self.destination = destination
        self.body = body


def CreatePublishedCommandHandler(command: CreatePublishedCommand) -> str:
    published = Published(
        uuid=command.uuid,
        body=command.body,
        destination=command.destination,
    )
    published_repository.save(published)
