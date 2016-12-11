#!/usr/bin/python
# -*- coding: utf-8 -*-



import pymysql


def insert():
	config = {
		'host':'127.0.0.1',
		'port':3306,
		'user':'root',
		'password':'123456',
		'db':'test1'
	}
	db = pymysql.connect(**config)
	cursor = db.cursor()
