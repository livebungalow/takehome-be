import os
stream = os.popen('./manage.py test --pattern="*_tests.py"')
output = stream.read()
