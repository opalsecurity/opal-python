SHELL:=/bin/bash
PYTHON_POST_PROCESS_FILE=python -m black
DISABLE_ALL=true

OPENAPI_GEN=openapi-generator generate --enable-post-process-file -i api/openapi.yaml -g python -o . -c config.json -t .openapi-generator/templates

gen-openapi:
	$(OPENAPI_GEN)
