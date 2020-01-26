run:
	uvicorn api.app:app --host 0.0.0.0 --reload

migrate:
	alembic upgrade head

test:
	python -m pytest -vvv