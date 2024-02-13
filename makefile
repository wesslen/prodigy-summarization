install:
	python -m pip install --upgrade pip
	python -m pip install prodigy -f https://$PRODIGY_KEY@download.prodi.gy

prodigy:
	python -m prodigy ab.llm.tournament bbb-abstract-sum data/2024-01-03.jsonl templates/abstract config --display-template display.jinja2 --no-meta