from outbox.domain.command.create_published import (
    CreatePublishedCommand,
    CreatePublishedCommandHandler,
)


class App:
    command_handlers = {
        CreatePublishedCommand: CreatePublishedCommandHandler,
    }

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
