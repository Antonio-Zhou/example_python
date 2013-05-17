#!/usr/bin/env python
# -*- coding:utf-8 -*-   

#	Created on:	2013-04-30
#	    Author:	Eric Zhou

#检查用户名和PIN码

database = [
	['yafeng',   '1234'],
	['huangjuan','2345'],
	['ericzhou', '4567'],
	['zhoubb',   '3456']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database: print 'Access granted'
