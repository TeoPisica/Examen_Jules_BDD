pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

run test
behave -f html -o behave-report.html --tags=smoke
behave -f html -o behave-report.html --tags=add
behave -f html -o behave-report.html --tags=test
behave -f html -o behave-report.html --tags=login
behave -f html -o behave-report.html --tags=people
behave -f html -o behave-report.html --tags=person
behave -f html -o behave-report.html --tags=search
behave -f html -o behave-report.html --tags=edit
behave -f html -o behave-report.html --tags=delete2


