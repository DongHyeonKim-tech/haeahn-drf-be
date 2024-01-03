# 기본 이미지로 Python 3.8 사용
FROM python:3.8

# 환경 변수 설정: Python이 실행될 때 출력을 버퍼링하지 않도록 함
ENV PYTHONUNBUFFERED 1

# Microsoft SQL Server를 위한 환경 변수 설정 및 필요한 패키지 설치
ENV ACCEPT_EULA=Y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 패키지 업데이트 및 vim, unixodbc-dev, msodbcsql17, mssql-tools 설치, 그리고 패키지 정리
RUN apt-get -y update && apt-get -y install vim && apt-get -y install unixodbc-dev msodbcsql17 mssql-tools && apt-get clean 

# 환경 변수 설정: MSSQL-Tools의 실행 경로를 PATH에 추가
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# 작업 디렉토리 설정
WORKDIR /haeahn_drf_be

# pip 업그레이드 및 필요한 Python 패키지 설치
RUN pip install --upgrade pip
COPY requirements.txt /haeahn_drf_be/
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일 및 폴더를 컨테이너의 작업 디렉토리에 복사
COPY . /haeahn_drf_be/

# Gunicorn을 사용하여 Django 애플리케이션 실행
CMD ["gunicorn", "--config", "gunicorn.conf.py", "haeahn_drf_be.wsgi:application"]