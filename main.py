#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/02/16 13:54:50
@Author  :   Leonardo Zarkli 
@Version :   0.10
@Contact :   vcatazrael@gmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from abc import abstractclassmethod
from re import DEBUG
from github3 import login
from github3.api import user

def 

def connect_to_github():
    gh = login(username="zarkli",password="Mr.Zarkli@2003")
    repo = gh.repository("zarkli","Hunter")
    branch = repo.branch("master")

    return gh,repo,branch



if __name__ == '__main__':
    connect_to_github()