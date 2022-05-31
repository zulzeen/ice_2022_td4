# Launch
```
docker-compose up -d --build
```

# View docs
Go to [localhost:8004/docs](http://localhost:8004/docs)

# Run tests
## All tests
```
docker-compose exec web python -m pytest
```
## Run only last failed tests
```
docker-compose exec web python -m pytest --lf
```
## Run tests with name matching string expression
```
docker-compose exec web python -m pytest -k "read_all"
```
## Run tests until the first failure
```
docker-compose exec web python -m pytest -x
```
# Format code

# Check quality
## Code coverage
```
docker-compose exec web python -m pytest --cov="." --cov-report html
```
## PEP8
```
docker-compose exec web flake8 . --ignore F405 --max-line-length=119
```
## Code style
```
docker-compose exec web black . --check
docker-compose exec web black . --diff
docker-compose exec web black .
```
## Import sort
```
docker-compose exec web isort . --check-only
docker-compose exec web isort . --diff
docker-compose exec web isort .
```