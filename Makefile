run:
	cd app && docker compose -p app --env-file .env -f compose.yml up -d --remove-orphans

add-dependency:
	cd app && docker compose run web bash -c "poetry add $(dep)"

rebuild:
	cd app && docker compose build

restart:
	cd app && docker compose restart

restart-web:
	cd app && docker compose restart web

down:
	cd app && docker compose down

shell:
	cd app && docker compose exec web bash -c "python manage.py shell"

integration-tests:
	cd integration_tests && docker compose -p integration_tests up orders_worker outbox_publisher metrics_worker -d 
	cd integration_tests && docker compose -p integration_tests up web --build -d --remove-orphans
	sleep 5
	cd integration_tests && docker compose up tests --build
	cd integration_tests && docker compose down
	
