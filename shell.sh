#!/bin/bash

git config --global user.name "woo3848"
git config --global user.email "eee7426@gmail.com"

mkdir -p /root/best

cd /root/best

git init

git remote add origin https://github.com/woo3848/djnago_pro.git

git clone https://github.com/woo3848/djnago_pro.git /root/best
