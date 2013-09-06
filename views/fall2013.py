from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2013/schedule')
def fall2013schedule():
    static = '/static/2013f/'
    term = '/fall-2013/'
    s = Schedule()

    s.week()

    d = s.day("September 4")
    d.lecture('Internet Architecture')
    d.reading('The Design Philosophy of the DARPA Internet Protocols','http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf')
    d.reading('End-to-End Arguments in System Design','http://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf')
    d.reading('Brief History of the Internet','http://www.internetsociety.org/internet/what-internet/history-internet/brief-history-internet')

    d = s.day("September 6")
    d.lecture('Internet Architecture')
    d.reading('The Evolution of Layered Protocol Stacks Leads to an Hourglass-Shaped Architecture','http://conferences.sigcomm.org/sigcomm/2011/papers/sigcomm/p206.pdf')
    d.reading('HTTP as the Narrow Waist of the Future Internet','http://conferences.sigcomm.org/hotnets/2010/papers/a6-popa.pdf')

    s.week()

    d = s.day("September 9")
    d.lecture('Internet Architecture')
    d.reading('A Data-Oriented (and Beyond) Network Architecture','http://www.sigcomm.org/ccr/papers/2007/October/1282427.1282402')

    d = s.day("September 11")
    d.lecture('Internet Architecture')

    d = s.day("September 13")
    d.lecture('Internet Architecture')

    s.week()

    d = s.day("September 16")
    d.lecture('Internet Measurements')

    d = s.day('September 18')
    d.lecture('Internet Measurements')

    d = s.day('September 20')
    d.lecture('Internet Measurements')

    s.week()

    d = s.day('September 23')
    d.lecture('Middleboxes and Middleware')

    d = s.day('September 25')
    d.lecture('Middleboxes and Middleware')

    d = s.day('September 27')
    d.lecture('Middleboxes and Middleware')

    s.week()

    d = s.day('September 30')
    d.lecture('Data Center Networking')

    d = s.day('October 2')
    d.lecture('Data Center Networking')

    d = s.day('October 4')
    d.lecture('Data Center Networking')

    s.week()

    d = s.day('October 7')
    d.lecture('Streaming')
  
    d = s.day('October 9')
    d.lecture('Streaming')

    d = s.day('October 11')
    d.lecture('Streaming')

    s.week()

    d = s.day('October 14')
    d.lecture('Social Networking')


    d = s.day('October 16')
    d.lecture('Social Networking')

    d = s.day('October 18')
    d.lecture('Social Networking')


    s.week()

    d = s.day('October 21')
    d.lecture('Usability')

    d = s.day('October 23')
    d.lecture('Usability')

    d = s.day('October 25')
    d.lecture('Usability')


    s.week()

    d = s.day('October 28')
    d.lecture('Home Networking')

    d = s.day('October 30')
    d.lecture('Home Networking')

    d = s.day('November 1')
    d.lecture('Home Networking')


    s.week()

    d = s.day('November 4')
    d.lecture('Internet of Things')

    d = s.day('November 5')
    d.lecture('Internet of Things')

    d = s.day('November 6')
    d.lecture('Internet of Things')

    s.week()

    d = s.day('November 11')
    d.lecture('Transport')

    d = s.day('November 13')
    d.lecture('Transport')

    d = s.day('November 15')
    d.lecture('Transport')

    s.week()

    d = s.day('November 18')
    d.lecture('Routing')

    d = s.day('November 20')
    d.lecture('Routing')

    d = s.day('November 22')
    d.lecture('Routing')

    s.week()

    d = s.day('November 25')
    d.lecture('Privacy')

    d = s.day('November 26')
    d.lecture('Privacy')

    d = s.day('November 27')
    d.lecture('No Class','Thanksgiving Holiday')

    d = s.day('November 28')
    d.lecture('No Class','Thanksgiving Holiday')

    s.week()

    d = s.day('December 2')
    d.lecture('Security')

    d = s.day('December 4')
    d.lecture('Security')

    d = s.day('December 6')
    d.lecture('Security')

    s.week()

    d = s.day('December 9')
    d.lecture('Miscellaneous')

    d = s.day('December 11')
    d.lecture('Miscellaneous')

    s.week()

    d = s.day('December 17')

    return render_template('fall-2013/schedule.html',active='schedule',
                           weeks=s.weeks)
