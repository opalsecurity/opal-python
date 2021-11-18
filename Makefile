SHELL := /bin/bash

OPENAPI_GEN=openapi-generator generate -i api/openapi.yaml -g python -o . -c config.json

gen-openapi:
	$(OPENAPI_GEN)
