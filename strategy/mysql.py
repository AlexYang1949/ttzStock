#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test1'
}
con = pymysql.connect(**config)

create_table_sql = 'CREATE TABLE `hs300`( \
                `date` datetime NOT NULL , \
                `code` varchar(32) NOT NULL,\
                `open` decimal(19,4) NULL,\
                `close` decimal(19,4) NULL,\
                `low` decimal(19,4) NULL,\
                `volume` bigint NULL,\
                `price_change` decimal(19,4) NULL,\
                `p_change` decimal(19,4) NULL,\
                PRIMARY KEY (`date`)\
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;'



with con:
    cur = con.cursor()
    cur.execute(create_table_sql)
    con.commit()
    con.close()
    print('创建成功')




