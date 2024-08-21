# sample-ui-pytest-automation
## Summary
- 이 프로젝트는 Python, Selenium, Pytest 를 사용한 웹 UI 자동화 프로젝트입니다. 테스트 작성, 실행, 리포트 생성 등의 과정을 명확한 구조로 제공합니다.
---
## Structure
```commandline
root
├── 📁base
│   └── base_page.py                # 페이지 객체를 위한 공통 메서드를 포함한 기본 클래스
├── 📁config
│   └── config.py                   # BASE_URL, WAIT_TIME 등 설정 파일
├── 📁pages
│   ├── login_page.py               # 로그인 페이지를 위한 페이지 객체
│   ├── main_page.py                # 메인 페이지를 위한 페이지 객체
│   ├── weather_page.py             # 날씨 페이지를 위한 페이지 객체
│   └── page_elements.py            # 페이지에서 사용하는 모든 요소의 선택자를 관리
├── 📁tests
│   ├── test_login.py               # 로그인 기능에 대한 테스트 케이스
│   ├── test_main.py                # 메인 페이지 기능에 대한 테스트 케이스
│   ├── test_weather.py             # 날씨 페이지 기능에 대한 테스트 케이스
│   └── conf_test.py                # 테스트 환경을 초기화하고 설정하는 파일
├── 📁utilities
│    └── helper.py                   # 테스트에 필요한 유틸리티 함수들
├── pytest.ini
├── pytest-run.sh
```
---
## Pre-Condition
- 이 프로젝트를 실행하기 위해 다음 사전 조건이 구성되어 있어야 합니다.
  - Python 설치 확인 (3.8 이상)
  - Chrome 브라우저 설치 확인
---
## Project Progress
- Step 1 : Repository 를 클론한 뒤, 프로젝트 루트로 이동
```bash
git clone https://github.com/hoonq9284/sample-ui-pytest-automation.git
```
```bash
cd sample-ui-pytest-automation
```
- Step 2 : 가상 환경 활성화
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
- Step 3 : 의존성 설치
```bash
pip install -r requirements.txt
```
---
## Test Run Process
- 기본적으로 아래 명령어를 입력하여 테스트를 실행
```bash
pytest tests/ --alluredir=reports/allure-results
```
```bash
allure serve reports/allure-results
```
- 해당 프로젝트에서는 pytest-run.sh 쉘 스크립트 파일 자체를 실행하여, 해당 명령어를 한 번에 수행하도록 구성
```bash
./pytest-run-sh
```