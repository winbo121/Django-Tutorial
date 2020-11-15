# Django-Tutorial
Django-Tutorial


------------------------------------------------------------------------------------------------------------
docker pull ubuntu:16.04 (없을시)

-------------- 컨테이너 생성 --------------
docker run -d --privileged -p{포워딩할 임의 포트}:{포워딩 당할 포트} -v /d/test_workspace:/code --restart=always --name {컨테이너 이름} ubuntu:16.04 /sbin/init
docker exec -it {컨테이너 이름} /bin/bash

-------------- 도커 컨테이너 내부 --------------
apt-get update
apt-get install vim
cp /etc/apt/sources.list /etc/apt/sources.list_back
vi /etc/apt/sources.list
:%s/archive.ubuntu.com/ftp.daumkakao.com (명령어 편집기 모드에서) (카카오모드 우분투)
apt-get update
apt-get install -y  git wget software-properties-common libmysqlclient-dev build-essential uuid-dev libcap-dev libpcre3-dev libssl-dev curl libffi-dev  libxml2-dev libxslt1-dev zlib1g-dev
***한글설정
apt-get install -y language-pack-ko
locale-gen ko_KR.UTF-8

-------------- 파이썬 3.8.6 ppa--------------
apt-get update
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.8
update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
apt-get install -y python3.8-dev

-------------- 3.8vertualenv --------------
apt-get install -y virtualenv
mkdir code
cd /code
apt-get install python3.8-venv
python -m venv venv
. venv/bin/activate
 
-------------- Git에서 master 브랜치 코드 가져오기 --------------
cd /code
. venv/bin/activate
git clone (깃허브 주소)
(이후 세부 branch 조정)
cd Django-Tutorial
git fetch --all
vi requirements.txt (맨 밑에 있는 z로 되있는 것을 삭제) (있을시)
mkdir log
pip install -r requirements.txt


-------------#mariadb 설치-------------
apt-get update
apt-get install mariadb-server
service mysql restart -> mysql 재기동
mysql_secure_installation -> 비밀번호 초기화 후 y


mysql -u root -p (접속)

show databases;

use [데이터베이스 명<스키마 명>]

use mysql (모든유저 관리) 
{
select * from user\G; (유저들 조회)
update user set plugin='' where user='root' and host = 'localhost'; (root 비번없이 들어가지는것을 방지)
flush privileges;
create user [아이디] @localhost identified by '[비번]'; (유저 추가)
drop user [아이디] @localhost; (유저 삭제)
grant all privileges on [스키마 명].[테이블 명] to 'winbo121' @localhost identified by '[비번]'; (권한주기)
show grants for '[아이디]' @localhost; 
revoke all on [스키마 명].[테이블 명] from '[아이디]' @localhost; (권한삭제)
}

(일반 콘솔창)mysqldump -h [외부 아이피] -u[외부 아이디] -p[외부 비번] [외부에서 가져올 스키마 명] | mysql -u[자신 아이디] -p[자신 비번] [자신의 적용할 <만들어진>스키마 명]; (외부에서 디비 가져오기)

-------------- 프로젝트 생성--------------  (새로만들시)
django-admin startproject [이름]
프로젝트 안에서 파이썬 파일 생성
python manage.py startapp [이름]
python manage.py runserver 0.0.0.0:8000
