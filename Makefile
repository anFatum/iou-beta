# Get user envirement (Assuming there is one)
-include .env

# Tell Make we don't expect these functions to create
.PHONY: help

help:  ## Show this help.
	@echo ""
	@echo USAGE:
	@awk -F ":.*?## " '                                              \
        /^[a-zA-Z_-]+:/&&NF==2{                                      \
            printf "\tmake \033[36m%-10s\033[0m %s\n", $$1, $$2 | "sort"    \
        }' $(MAKEFILE_LIST)
	@echo ""

all: test build run
	${redirect_output}
	${check_exit}

build:  ## prepare solution
	${redirect_output}
	docker-compose build
	${check_exit}

run:  ## run solution
	${redirect_output}
	docker-compose up
	${check_exit}

test: ## run tests
	${redirect_output}
	@pytest backend/app/tests
	${check_exit}

