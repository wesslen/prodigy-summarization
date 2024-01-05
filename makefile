install:
	python -m pip install --upgrade pip
	python -m pip install prodigy -f https://$PRODIGY_KEY@download.prodi.gy

tourney:
	python -m prodigy ab.llm.tournament

config:
	spacy debug config config/config-tldr.cfg
	python -m spacy init fill-config config/config-tldr.cfg config/config-tldr.cfg

config-sum:
	python -m spacy init fill-config config/config-summarization.cfg config/config-summarization.cfg