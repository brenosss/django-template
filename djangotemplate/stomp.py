import stomp
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class StompListener(stomp.ConnectionListener):
    def __init__(self, stdout_writer=None):
        self.stdout_writer = stdout_writer

    def on_message(self, frame):
        self.stdout_writer(frame.body)


def _connect():
    conn = stomp.Connection([("rabbitmq", 61613)])
    conn.connect("guest", "guest", wait=True)
    return conn


def send_message_to_queue(destination, body):
    conn = _connect()
    conn.send(destination=destination, body=body)
    logger.info(f"Sent message: {body} to {destination}")


def handle_message(destination, stdout_writer):
    conn = _connect()
    conn.set_listener("", StompListener(stdout_writer=stdout_writer))
    conn.subscribe(destination=destination, id=1, ack="auto")
