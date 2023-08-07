from pathlib import Path
CONFIG_FILE_PATH=Path("config/config.yaml")
PARAMS_FILE_PATH=Path("params.yaml")

USER_PATTERN='@[^\s]+'
HASHTAG_PATTERN='#[^\s]+'
URL_PATTERN='https?[^ ]*'
vocabulary_size=25000
sentence_length=20
embedding_vector_size=100