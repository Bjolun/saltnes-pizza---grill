#!flash/bin/python

#!usr/bin/python
# -*- coding: utf-8 -*-

from app import app

# DEBUG IS SET TO TRUE!!
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
