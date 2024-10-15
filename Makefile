add-dependency:
	docker-compose run web bash -c "poetry add $(dep)"

rebuild:
	docker-compose build

start:
	docker-compose up -d --remove-orphans

restart:
	docker-compose restart

restart-web:
	docker-compose restart web celery-beat celery-flower celery-worker

stop:
	docker-compose down

shell:
	docker-compose exec web bash -c "python manage.py shell"