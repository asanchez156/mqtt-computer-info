#!/bin/bash

SO=$(uname)
if echo $SO | grep -q 'MSYS'; then
	rm -Rf _venv_win
	clear
	EXIST=$(virtualenv --version || echo 0)
	clear
	echo "### === Working S.O Windows === ###"
	if [ $EXIST = 0 ]; then
		echo '### ===> Installing "virtualenv"'
		pip install virtualenv
	fi
	echo '### ===> Creating environment "_venv_win"'
	virtualenv --python=python _venv_win
	echo '### ===> Updating library "pip"'
	_venv_win/Scripts/pip install --upgrade pip setuptools wheel
	echo '### ===> Installing required libraries "requirements.txt"'
	_venv_win/Scripts/pip install -r requirements.txt
  	rm _venv.link
	ln -s _venv_win _venv.link
	echo '### ===> Finished, bye.'
fi

if echo $SO | grep -q 'Linux'; then
	rm -Rf _venv_linux
	clear
	EXIST=$(virtualenv --version || echo 0)
	clear
	echo "### === Working S.O Linux === ###"
	if [ $EXIST = 0 ]; then
		echo '### ===> Installing "virtualenv"'
		apt-get install -y virtualenv
		clear
		pip install virtualenv
	fi
	echo '### ===> Creating environment "_venv_linux"'
	virtualenv --python=python3.5 _venv_linux
	echo '### ===> Updating library "pip"'
	_venv_linux/bin/pip install --upgrade pip setuptools wheel
	echo '### ===> Installing required libraries "requirements.txt"'
	_venv_linux/bin/pip install -r requirements.txt
  	rm _venv.link
	ln -s _venv_linux _venv.link
	echo '### ===> Finished, bye.'
fi

if echo $SO | grep -q 'Darwin'; then
	rm -Rf _venv_mac
	clear
	EXIST=$(virtualenv --version || echo 0)
	clear
	echo "### === Working S.O Mac === ###"
	if [ "$EXIST" = 0 ]; then
		echo '### ===> Installing "virtualenv"'
		pip3 install virtualenv
	fi
	echo '### ===> Creating environment "_venv_mac"'
	virtualenv --python=python2 _venv_mac
	echo '### ===> Updating library "pip"'
	_venv_mac/bin/pip install --upgrade pip setuptools wheel
	echo '### ===> Installing required libraries "requirements.txt"'
	_venv_mac/bin/pip install -r requirements.txt
  	rm _venv.link
	ln -s _venv_mac _venv.link
	echo '### ===> Finished, bye.'
fi
