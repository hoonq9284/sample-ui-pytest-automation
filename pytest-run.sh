pytest --alluredir=reports/allure-results

allure serve reports/allure-results

rm -rf reports/

echo "테스트 완료"