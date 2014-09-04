from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2014/schedule')
def fall2014schedule():
    static = '/static/2014f/'
    term = '/fall-2014/'
    s = Schedule()

    s.week()




    d = s.day("September 3")
    d.lecture('Introduction')

    d = s.day("September 5")
    d.lecture('Internet Architecture')
    d.reading('The Design Philosophy of the DARPA Internet Protocols','http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf')
    d.reading('End-to-End Arguments in System Design','http://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf')
    d.reading('Brief History of the Internet','http://www.internetsociety.org/internet/what-internet/history-internet/brief-history-internet')

    s.week()

    d = s.day("September 8")
    d.lecture('Internet Architecture')
    d.reading('Named Data Networking (CCR 2014)','http://named-data.net/wp-content/uploads/2014/04/tr-ndn-0019-ndn.pdf')
    d.reading('Named Data Networking Project','http://named-data.net/')

    d = s.day("September 10")
    d.lecture('Internet Architecture')
    d.reading('XIA: Efficient Support for Evolvable Internetworking (NSDI 2012)','http://www.cs.cmu.edu/~xia/resources/Documents/XIA-nsdi.pdf')


    d = s.day("September 12")
    d.lecture('Internet Architecture')
    d.reading('One Tunnel is (Often) Enough (SIGCOMM 2014)','http://delivery.acm.org/10.1145/2630000/2626318/p99-peter.pdf?ip=174.52.164.54&id=2626318&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2EE994ED6114094BD1&CFID=554128679&CFTOKEN=67435862&__acm__=1409862385_f2d034b558a7c3255e83a1cd458201e5')

    s.week()

# see paper at USENIX security on domains

# http://delivery.acm.org/10.1145/2630000/2626295/p87-czyz.pdf?ip=174.52.164.54&id=2626295&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2EE994ED6114094BD1&CFID=554128679&CFTOKEN=67435862&__acm__=1409862320_501b022812cfe5f6c67c39a599c0fa92
# Measuring IPv6 Adoption
# Jakub Czyz (University of Michigan); Mark Allman (International Computer Science Institute); Jing Zhang (University of Michigan); Scott Iekel-Johnson (Arbor Networks); Eric Osterweil (Verisign Labs); Michael Bailey (University of Michigan)

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
    d.reading("It's Not Easy Being Green",'http://conferences.sigcomm.org/sigcomm/2012/paper/sigcomm/p211.pdf')

    s.week()

    d = s.day('October 7')
    d.lecture('Social Networking')
    d.reading("Classifying Political Orientation on Twitter: It's Not Easy!",'http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6128')

    d = s.day('October 9')
    d.lecture('Social Networking')
    d.reading('A Measure of Polarization on Social Media Networks Based on Community Boundaries','http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6104')

    d = s.day('October 11')
    d.lecture('Social Networking')
    d.reading('The Anatomy of Large Facebook Cascades','http://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6123')

    s.week()

    d = s.day('October 14')
    d.lecture('Usability and Home Networking')
    d.reading('The ins and outs of home networking: The case for useful and usable domestic networking','http://dl.acm.org/citation.cfm?id=1534905')
    d.assignment('Social Networking Summary','')

    d = s.day('October 16')
    d.lecture('Usability and Home Networking')
    d.reading('Home networking and HCI: what hath god wrought?','http://dl.acm.org/citation.cfm?id=1240712')
    d.reading('Moving Toward the Middle: The Case Against the End-to-End Argument in Home Networking','http://www.cc.gatech.edu/fac/keith/pubs/hotnets07-end-to-end.pdf')

    d = s.day('October 18')
    d.lecture('Usability and Home Networking')
    d.reading('"You\'re Capped!" Understanding the Effects of Bandwidth Caps on Broadband Use in the Home','http://research.microsoft.com/apps/pubs/?id=162079')


    s.week()

    d = s.day('October 21')
    d.lecture('Software Defined Networking')
    d.reading('OpenFlow: enabling innovation in campus networks','http://dl.acm.org/citation.cfm?id=1355746')
    d.reading('NOX: towards an operating system for networks','http://dl.acm.org/citation.cfm?id=1384625&CFID=248686499&CFTOKEN=51372343')
    d.assignment('Usability and Home Networking Summary','')

    d = s.day('October 23')
    d.lecture('Software Defined Networking')
    d.reading('B4: Experience with a Globally-Deployed Software Defined WAN','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p3.pdf')

    d = s.day('October 25')
    d.lecture('Software Defined Networking')
    d.reading('Reproducible Network Experiments Using Container-Based Emulation','http://conferences.sigcomm.org/co-next/2012/eproceedings/conext/p253.pdf')

    s.week()

    d = s.day('October 28')
    d.lecture('Miscellanea')
    d.reading('Demystifying Page Load Performance with WProf','https://www.usenix.org/conference/nsdi13/demystifying-page-load-performance-wprof')
    d.assignment('Software Defined Networking Summary','')

    d = s.day('October 30')
    d.lecture('Miscellanea')
    d.reading('Piracy Activity vs. Product Features in Digital Games','http://openarchive.cbs.dk/bitstream/handle/10398/8299/tech_report_v1.pdf')

    d = s.day('November 1')
    d.lecture('Miscellanea')
    d.reading("Dasu: Pushing Experiments to the Internet's Edge",'https://www.usenix.org/conference/nsdi13/dasu-pushing-experiments-internet%E2%80%99s-edge')

    s.week()

    d = s.day('November 4')
    d.lecture('Work on Project')
  
    d = s.day('November 6')
    d.reading('Improving Fairness, Efficiency, and Stability in HTTP-based Adaptive Video Streaming with FESTIVE','http://conferences.sigcomm.org/co-next/2012/eproceedings/conext/p97.pdf')
    d.lecture('Streaming')

    d = s.day('November 8')
    d.reading('Developing a Predictive Model of Quality of Experience for Internet Video','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p339.pdf')
    d.lecture('Streaming')

    s.week()

#    RC3: Recursively Cautious Congestion Control
#            R. Mittal, J. Sherry, S. Ratnasamy, S. Shenker
#            In NSDI 2014
#http://www.eecs.berkeley.edu/~sylvia/papers/rc3-nsdi.pdf

    d = s.day('November 11')
    d.lecture('Transport')
    d.reading('Reducing Web Latency: the Virtue of Gentle Aggression','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p159.pdf')
    d.assignment('Project Proposal','')

    d = s.day('November 13')
    d.lecture('Transport')
    d.reading('TCP ex Machina: Computer-Generated Congestion Control','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p123.pdf')
    d.reading('FCP: A Flexible Transport Framework for Accommodating Diversity (optional)','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p135.pdf')

    d = s.day('November 15')
    d.lecture('Data Center Visit')

    s.week()

    d = s.day('November 18')
    d.lecture('Project Discussion')

# routing security
# From the Consent of the Routed: Improving the Transparency of the RPKI
# Ethan Heilman (Boston University); Danny Cooper (Boston University); Leonid Reyzin (Boston University); Sharon Goldberg (Boston University)
# http://delivery.acm.org/10.1145/2630000/2626293/p51-heilman.pdf?ip=174.52.164.54&id=2626293&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2EE994ED6114094BD1&CFID=554128679&CFTOKEN=67435862&__acm__=1409862034_656d9339833d4e28b2b047edbb6097b0

# network neutrality/architecture
# http://delivery.acm.org/10.1145/2630000/2626308/p63-zhang.pdf?ip=174.52.164.54&id=2626308&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2EE994ED6114094BD1&CFID=554128679&CFTOKEN=67435862&__acm__=1409862100_11ca0f18ef097eae6503dad9838d45ff
# Network Neutrality Inference
# Zhiyong Zhang (U. of Electronic Science and Technology, China); Ovidiu Mara (EPFL); Katerina Argyraki (EPFL)

# privacy/ architecture
# Balancing Accountability and Privacy in the Network
#David Naylor (Carnegie Mellon University); Matthew K. Mukerjee (Carnegie Mellon University); Peter Steenkiste (Carnegie Mellon University)
# http://delivery.acm.org/10.1145/2630000/2626306/p75-naylor.pdf?ip=174.52.164.54&id=2626306&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2EE994ED6114094BD1&CFID=554128679&CFTOKEN=67435862&__acm__=1409862214_9536b4ee88b3b781bd8b2f466f5f8ef5

    d = s.day('November 20')
    d.lecture('Routing')
    d.reading('LIFEGUARD: Practical Repair of Persistent Route Failures','http://conferences.sigcomm.org/sigcomm/2012/paper/sigcomm/p395.pdf')

    d = s.day('November 22')
    d.lecture('Privacy')
    d.reading('Detecting and Defending Against Third-Party Tracking on the Web','https://www.usenix.org/conference/nsdi12/detecting-and-defending-against-third-party-tracking-web')

    s.week()

    d = s.day('November 25')
    d.lecture('Privacy')
    d.reading('Expressive Privacy Control with Pseudonyms','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p291.pdf')

    d = s.day('November 26')
    d.lecture('Projects')

    d = s.day('November 27')
    d.lecture('No Class','Thanksgiving Holiday')

    d = s.day('November 28')
    d.lecture('No Class','Thanksgiving Holiday')

    s.week()

    d = s.day('December 2')
    d.lecture('Privacy')
    d.reading('Koi: A Location-Privacy Platform for Smartphone Apps','https://www.usenix.org/conference/nsdi12/koi-location-privacy-platform-smartphone-apps')
    d.assignment('Privacy Summary','')

    d = s.day('December 4')
    d.lecture('Security')
    d.reading('No Attack Necessary: The Surprising Dynamics of SSL Trust Relationships','http://www1.icsi.berkeley.edu/~bernhard/papers/noAttackNecessary.pdf')

    d = s.day('December 6')
    d.lecture('Security')
    d.reading('Rethinking SSL development in an appified world','http://dl.acm.org/citation.cfm?id=2516655')

    s.week()

    d = s.day('December 9')
    d.lecture('Security')
    d.reading('Perspectives: Improving SSH-style Host Authentication with Multi-Path Probing','http://www.cs.cmu.edu/~dga/papers/perspectives-usenix2008.pdf')

    d = s.day('December 11')
    d.lecture('Security')
    d.reading('Embassies: Radically Refactoring the Web','https://www.usenix.org/conference/nsdi13/embassies-radically-refactoring-web')
    d.assignment('Security Summary','')

    s.week()

    d = s.day('December 20')
    d.assignment('Final Paper','')

    return render_template('fall-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
