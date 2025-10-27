SHELL:=/bin/bash
PYTHON_POST_PROCESS_FILE=python -m black

DELETE_OLD_GENERATED_TESTS=rm -rf test/*
OPENAPI_GEN=openapi-generator generate --enable-post-process-file -i api/openapi.yaml -g python -o . -c config.json -t .openapi-generator/templates
OPENAPI_GEN_CI=openapi-generator-cli generate --enable-post-process-file -i api/openapi.yaml -g python -o . -c config.json -t .openapi-generator/templates
PULL_REMOTE_OPENAPI=curl https://app.opal.dev/openapi.yaml > api/openapi.yaml

gen-openapi:
	$(DELETE_OLD_GENERATED_TESTS)
	$(OPENAPI_GEN)
gen-openapi-remote:
	$(DELETE_OLD_GENERATED_TESTS)
	$(PULL_REMOTE_OPENAPI)
	$(OPENAPI_GEN)
gen-openapi-remote-for-ci:
	$(DELETE_OLD_GENERATED_TESTS)
	$(PULL_REMOTE_OPENAPI)
	$(OPENAPI_GEN_CI)
