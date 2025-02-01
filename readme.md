# E-commerce API Documentation

This API provides endpoints for managing products and orders for an e-commerce platform.

## API Endpoints

The following are the available endpoints for the E-commerce API:

### Products

- **POST /comm/products**
  - Add a new product to the catalog
  - Returns the created product object

- **GET /comm/products**
  - Fetch all available products
  - Public endpoint
  - Returns an array of product objects

### Orders

- **POST /comm/orders**
  - Create a new order
  - Returns the created order object

## API Documentation

After running the server, you can access the interactive API documentation through:

- Swagger UI: `/comm/docs`
- ReDoc: `/comm/redoc`

## Docker Setup

### Building the Docker Image

To build the Docker image for the application:

```bash
docker build -t zania_assn_img .
```

This command builds a Docker image named `zania_assn_img` using the Dockerfile in the current directory.

### Running the Docker Container

To run the Docker container:

```bash
docker run -d --name zania_assn_cntnr -p 5001:5001 zania_assn_img
```

This command:
- Starts a container named `zania_assn_cntnr`
- Runs in detached mode (-d)
- Maps container port 5001 to host port 5001
- Uses the `zania_assn_img` image

### Accessing the Container

To access the running container's shell:

```bash
docker exec -it zania_assn_cntnr sh
```

## Testing

To run the test suite inside the Docker container:

```bash
python3 -m app.test.main
```

This executes the test suite defined in `app/test/router/manage.py`.

## Notes

- The API runs on port 5001 by default
- Make sure Docker is installed and running before executing the Docker commands
- All API endpoints are prefixed with `/comm`