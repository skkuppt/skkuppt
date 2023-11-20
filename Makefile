.PHONY: build up down help

SERVICES := db frontend backend nginx-proxy nginx-letsencrypt

help:
	@echo "Usage: make [action] service=<service>"
	@echo "  action: build, up, down"
	@echo "  service: all, $(SERVICES)"

check-service:
ifndef service
	$(error service is undefined. Use 'all' for all services or specify one: $(SERVICES))
endif
	@if [ "$(service)" != "all" ] && ! echo $(SERVICES) | grep -q "$(service)"; then \
		echo "Invalid service: $(service). Use 'all' for all services or specify one: $(SERVICES)"; \
		exit 1; \
	fi

build: check-service
	@if [ "$(service)" = "all" ]; then \
		docker-compose build; \
	else \
		docker-compose build $(service); \
	fi

up: check-service
	@if [ "$(service)" = "all" ]; then \
		docker-compose up -d; \
	else \
		docker-compose up -d $(service); \
	fi

down: check-service
	@if [ "$(service)" = "all" ]; then \
		docker-compose down; \
	else \
		docker-compose stop $(service); \
	fi

