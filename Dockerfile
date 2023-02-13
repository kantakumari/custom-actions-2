FROM python:3.
COPY unsuccessful.py /unsuccessful.py
# we will just run our script.py as our docker entrypoint by python script.py
CMD ["python", "/unsuccessful.py"]