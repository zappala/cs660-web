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
    d.reading('Architecting for Innovation','d.http://www.sigcomm.org/sites/default/files/ccr/papers/2011/July/2002250-2002256.pdf')

    d = s.day("September 13")
    d.lecture('Internet Architecture')
    d.reading('Software Defined Internet Architecture: Decoupling Architecture from Infrastructure','http://www1.icsi.berkeley.edu/~barath/papers/sdia-hotnets12.pdf')

    s.week()

    d = s.day("September 16")
    d.lecture('Internet Measurements')
    d.reading('Understanding the Domain Registration Behavior of Spammers',
              'http://conferences.sigcomm.org/imc/2013/papers/imc247-haoA.pdf')

    d.assignment('Internet Architecture Summary','')

    d = s.day('September 18')
    d.lecture('Internet Measurements')
    d.reading('Analysis of the HTTPS Certificate Ecosystem','')

    d = s.day('September 20')
    d.lecture('Internet Measurements')
    d.reading('A Fistful of Bitcoins: Characterizing Payments Among Men with No Names','http://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf')

    s.week()

    d.assignment('Internet Measurements Summary','')

    d = s.day('September 23')
    d.lecture('Middleboxes and Middleware')
    d.reading('Demystifying the Dark Side of the Middle: A Field Study of Middlebox Failures in Datacenters','')

    d = s.day('September 25')
    d.lecture('Middleboxes and Middleware')
    d.reading("Making Middleboxes Someone Else's Problem: Network Processing as a Cloud Service",'http://conferences.sigcomm.org/sigcomm/2012/paper/sigcomm/p13.pdf')

    d = s.day('September 27')
    d.lecture('Project Discussion')

    s.week()

    d = s.day('September 30')
    d.lecture('Data Center Networking')
    d.reading('Ananta: Cloud Scale Load Balancing','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p207.pdf')

    d = s.day('October 2')
    d.lecture('Data Center Networking')
    d.reading('Leveraging Endpoint Flexibility in Data-Intensive Clusters','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p231.pdf')

    d = s.day('October 4')
    d.lecture('Data Center Networking')
    d.assignment('Project Proposal','')
    d.reading("It's Not Easy Being Green",'http://conferences.sigcomm.org/sigcomm/2012/paper/sigcomm/p211.pdf')

    s.week()

    d = s.day('October 14')
    d.lecture('Social Networking')
    d.reading("Classifying Political Orientation on Twitter: It's Not Easy!",'http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6128')

    d = s.day('October 16')
    d.lecture('Social Networking')
    d.reading('A Measure of Polarization on Social Media Networks Based on Community Boundaries','http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6104')

    d = s.day('October 18')
    d.lecture('Social Networking')
    d.reading('The Anatomy of Large Facebook Cascades','http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6123')

    s.week()

    d = s.day('October 21')
    d.lecture('Usability and Home Networking')
    d.reading('The ins and outs of home networking: The case for useful and usable domestic networking','http://dl.acm.org/citation.cfm?id=1534905')

    d = s.day('October 23')
    d.lecture('Usability and Home Networking')
    d.reading('Home networking and HCI: what hath god wrought?','http://dl.acm.org/citation.cfm?id=1240712')
    d.reading('Moving Toward the Middle: The Case Against the End-to-End Argument in Home Networking','http://www.cc.gatech.edu/fac/keith/pubs/hotnets07-end-to-end.pdf')

    d = s.day('October 25')
    d.lecture('Usability and Home Networking')
    d.reading('"You\'re Capped!" Understanding the Effects of Bandwidth Caps on Broadband Use in the Home','http://research.microsoft.com/apps/pubs/?id=162079')


    s.week()

    d = s.day('October 28')
    d.lecture('TBD')

    d = s.day('October 30')
    d.lecture('TBD')

    d = s.day('November 1')
    d.lecture('TBD')


    s.week()

    d = s.day('November 4')
    d.lecture('Internet of Things')

    d = s.day('November 5')
    d.lecture('Internet of Things')

    d = s.day('November 6')
    d.lecture('Internet of Things')

    s.week()

    d = s.day('October 7')
    d.lecture('Streaming')
  
    d = s.day('October 9')
    d.lecture('Streaming')

    d = s.day('October 11')
    d.lecture('Streaming')

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
