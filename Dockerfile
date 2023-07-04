FROM python:3.8

COPY ./ /

RUN pip install -r requirements.txt

ENV PYTHONPATH=/
WORKDIR /

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["src.app.api_app:gptg_app", "--host", "0.0.0.0"]