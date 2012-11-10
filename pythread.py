#!/usr/bin/python
# -*- encoding: utf-8 -*-

## Based on lethain tutorial: http://lethain.com/using-threadpools-in-python/

from __future__ import with_statement
import logging, sys
from optparse import OptionParser

from time import sleep
from csv import DictReader
from Queue import Queue
from threading import Thread

def manage_csv_file(file, logger, threads=10):
	q = Queue()
	workers = []
	def worker():
		while True:
			line = q.get()
			try:
				print('processing: %s\n\n' % line)
			except Exception, e:
				logger.error('worker-thread: %s' % e)
			q.task_done()
		
	for i in range(threads):
		t = Thread(target = worker)
		t.setDaemon(True)
		workers.append(t)
		t.start()
	
	with open(file, 'r') as fin:
		for line in DictReader(fin):
			q.put(line)

	q.join()

def main():
	p = OptionParser('usage: pool.py somefile.csv')
	p.add_option('-t', '--threads', dest='threads',
				help = 'quantity of THREADS for procession',
				metavar='THREADS')
	(options, args) = p.parse_args()
	filename = args[0]
	threads = int(options.threads) if options.threads else 10

	loggerLevel = logging.DEBUG
	logger = logging.getLogger('FileManager')
	logger.setLevel(loggerLevel)
	ch = logging.StreamHandler()
	ch.setLevel(loggerLevel)
	formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	
	if filename.endswith('csv'):
		manage_csv_file(filename, logger, threads=threads)
	else:
		print(u'Cannot handle filename %s' % filename.split('.')[0]

if __name__ == '__main__':
	sys.exit(main())
