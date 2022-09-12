FROM python:slim
COPY . .
RUN pip install -r req.txt
CMD python bot.py