# Product Prices

This is a product prices service made up of a FastAPI backend launched with Docker.

## Usage

Make sure of having Docker Compose installed.

### Launch the services and the tests

```
docker-compose up
```

### Get products whose variation is at least 20% or 5€ between their first and last appearances
```
curl "localhost:8000/products/?percentage_threshold=20&euro_threshold=5"
```

### Get products whose variation is at least 20% or 5€ between their last two appearances
```
curl "localhost:8000/products/?percentage_threshold=20&euro_threshold=5&last_two=true"
```
