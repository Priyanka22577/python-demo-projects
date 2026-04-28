FROM python:3.11-slim

WORKDIR /python_demo/mydata

COPY . .

CMD [ "python3", "calculator.py" ]
