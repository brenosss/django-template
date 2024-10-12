add-dependency:
	docker-compose run web bash -c "poetry add $(dep)"

rebuild:
	docker-compose build

start:
	docker-compose up -d