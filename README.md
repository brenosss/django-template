# Django Template Project

This project is a Django-based application designed to demonstrate the use of the transactional outbox pattern. The project is divided into two main directories: `app` and `integration_tests`.
`app` contains the source code for the Django application.
`integration_tests` contains the source code for integration tests.

## Django Applications in `app`

### 1. Carts

The `carts` app provides endpoints to manage shopping carts. It includes the following functionalities:

- **Get all carts**: Retrieve a list of all carts.
- **Create a cart**: Add a new cart.
- **Checkout a cart**: Mark a cart as closed and create an outbox item for further processing.

Endpoints:
- `GET /carts`: Get all carts.
- `POST /carts`: Create a new cart.
- `PUT /carts/<cart_id>/checkout`: Checkout a cart.

### 2. Orders

The `orders` app provides endpoints to manage orders. It includes the following functionalities:

- **Get all orders**: Retrieve a list of all orders.

Endpoints:
- `GET /orders`: Get all orders.

### 3. Metrics

The `metrics` app provides endpoints to manage metrics. It includes the following functionalities:

- **Get all metrics**: Retrieve a list of all metrics.

Endpoints:
- `GET /metrics`: Get all metrics.

### 4. Outbox

The `outbox` app handles the outbox pattern, ensuring reliable message delivery to external systems. It includes the following functionalities:

- **Create and publish outbox items**: Manage the creation and publishing of outbox items.

## Running the Project

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up environment variables**:
    Create a `.env` file in the `app` directory with the necessary environment variables.

3. **Build and run the Docker containers**:
    ```sh
    make run
    ```

### Running Integration Tests

The `integration_tests` directory contains a setup to make requests to the `app` to test its behavior.
It runs a isolated version of `app` in containers and executes tests using `pytest`.

1. **Run the integration tests**:
    ```sh
    make integration-tests
    ```

## Queue Handling

The `compose.yml` file includes configurations for publishers and consumers that are responsible for handling queue messages. These components ensure reliable message delivery and processing. Some apps contain callbacks that are used by these publishers and consumers to handle specific tasks.

## Additional Commands

- **Add a dependency**:
    ```sh
    make add-dependency dep=<dependency-name>
    ```

- **Rebuild the Docker containers**:
    ```sh
    make rebuild
    ```

- **Restart the Docker containers**:
    ```sh
    make restart
    ```

- **Restart the web service**:
    ```sh
    make restart-web
    ```

- **Stop and remove the Docker containers**:
    ```sh
    make down
    ```

- **Open a Django shell**:
    ```sh
    make shell
    ```

