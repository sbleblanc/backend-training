requirements.txt : pyproject.toml
	uv pip compile pyproject.toml --universal --output-file requirements.txt

install-deps:
	uv pip sync requirements.txt
	uv pip install -e .

run-hello:
	flask --app backend_training.flask_tutorial.hello run --debug

