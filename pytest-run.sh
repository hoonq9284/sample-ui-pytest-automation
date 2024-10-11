# pytest 실행 및 커버리지 + allure 리포트 생성
pytest --cov=pages/ --cov-report=html --cov-report=term-missing --alluredir=reports/allure-results

# allure 리포트 실행
allure serve reports/allure-results

# coverage report html 파일 실행
open htmlcov/index.html

# 리포트 디렉토리 삭제
rm -rf reports/