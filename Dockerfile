FROM python:3.7-slim-buster
MAINTAINER Alexander Reitzel
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip
RUN pip install --upgrade wheel
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY python_utility python_utility
COPY setup.py .
RUN pip install .
CMD ["pu"]
