all: help

.PHONY: install clean run help all

######################
# INSTALL & CLEANUP
######################

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -e .

clean:
	rm -rf .venv

######################
# RUN
######################

run:
	. .venv/bin/activate && langgraph dev

######################
# HELP
######################

help:
	@echo '----'
	@echo 'install                      - 가상환경 생성 및 의존성 설치'
	@echo 'clean                        - .venv, results 디렉터리 삭제'
	@echo 'run                          - langgraph dev 실행'
	@echo 'help                         - 이 도움말 출력'


