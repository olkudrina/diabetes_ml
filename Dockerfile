FROM python:3.9


WORKDIR /app
COPY "requirements.txt" /app
COPY "diabetes_dv_and_xgboost.bin" /app

RUN pip install -r requirements.txt

COPY "diabetes_predict.py" /app

EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "diabetes_predict:app"]