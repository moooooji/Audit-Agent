all: help

.PHONY: install clean run help all

######################
# INSTALL & CLEANUP
######################

install:
	python3 -m venv venv
	source venv/bin/activate && pip install -e . && pip install -r src/react_agent/Utils/requirements.txt && pip install google.generativeai

clean:
	rm -rf venv

######################
# RUN
######################

run:
	source venv/bin/activate && langgraph dev --allow-blocking

######################
# HELP
######################

help:
	@echo '----'
	@echo 'install                      - 가상환경 생성 및 의존성 설치'
	@echo 'clean                        - .venv, results 디렉터리 삭제'
	@echo 'run                          - langgraph dev 실행'
	@echo 'help                         - 이 도움말 출력'


