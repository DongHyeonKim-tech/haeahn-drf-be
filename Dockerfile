FROM python:3.8

ENV PYTHONUNBUFFERED 1

ENV ACCEPT_EULA=Y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get -y update && apt-get -y install vim && apt-get -y install unixodbc-dev msodbcsql17 mssql-tools && apt-get clean 

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

WORKDIR /haeahn_drf_be
RUN pip install --upgrade pip
COPY requirements.txt /haeahn_drf_be/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /haeahn_drf_be/

CMD ["gunicorn", "--config", "gunicorn.conf.py", "haeahn_drf_be.wsgi:application"]