from flask import render_template

from config import app
from schedule import *

@app.route('/winter-2017/schedule')
def winter2017schedule():
    s = Schedule()

    s.week()

    d = s.day("January 9")
    d.lecture('Introduction and Internet Design')
    d.reading("A Brief History of the Internet","http://www.internetsociety.org/internet/what-internet/history-internet/brief-history-internet")

    d = s.day("January 11")
    d.lecture('Internet Design')
    d.reading('The Design Philosophy of the DARPA Internet Protocols','http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf')

    d = s.day("January 13")
    d.lecture('Internet Design')
    d.reading('End-to-End Arguments in System Design','http://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf')
    d.assignment("Presentation: Daniel Zappala")

    s.week()

    d = s.day("January 16")
    d.lecture('No Class',"Martin Luther King Jr. Day")

    d = s.day("January 18")
    d.lecture('Applications')
    d.reading("Crowdsourcing Annotations for Websites' Privacy Policies: Can It Really Work? (WWW 2016)","http://shomir.net/pdf/publications/swilson_www_2016.pdf")
    d.assignment("Presentation: Brad Spendlove")

    d = s.day("January 20")
    d.lecture('Applications')
    d.reading("Alibi Routing (SIGCOMM 2015)","http://www-lb.cs.umd.edu/~dml/papers/alibi_sigcomm15.pdf")
    d.assignment("Presentation: Scott Heidbrink")

    s.week()

    d = s.day("January 23")
    d.lecture('Mobile')
    d.reading("Smartphone Background Activities in the Wild: Origin, Energy Drain, and Optimization (Mobicom 2015)","https://www.sigmobile.org/mobicom/2015/papers/p40-chenA.pdf")
    d.assignment("Presentation: Vaishnavi Narayan")
    
    d = s.day('January 25')
    d.lecture('Mobile')
    d.reading("Wireless Power Hotspot that Charges All of Your Devices (Mobicom 2015)","https://www.sigmobile.org/mobicom/2015/papers/p2-shiA.pdf")
    d.assignment("Presentation: Zann Anderson")

    d = s.day('January 27')
    d.lecture('Mobile')
    d.reading("FlexiWeb: Network-Aware Compaction for Accelerating Mobile Web Transfers (Mobicom 2015)","https://www.sigmobile.org/mobicom/2015/papers/p604-singhA.pdf")
    d.assignment("Presentation: Tyler Monson")

    s.week()

    d = s.day('January 30')
    d.lecture('Infrastructure')
    d.reading("From .academy to .zone: An Analysis of the New TLD Land Rush (IMC 2015)","https://ian.ucsd.edu/papers/imc15-tld.pdf")
    d.assignment("Presentation: Brad Spendlove")
    
    d = s.day('February 1')
    d.lecture('Infrastructure')
    d.reading("Internet Censorship in Iran: A First Look (FOCI 2013)","https://www.usenix.org/system/files/conference/foci13/foci13-aryan.pdf")
    d.reading("Towards a Comprehensive Picture of the Great Firewall's DNS Censorship (FOCI 2014)","https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdf")
    d.assignment("Presentation: Tyler Monson, Zann Anderson")

    d = s.day('February 3')
    d.lecture('Infrastructure')
    d.reading("The Collateral Damage of Internet Censorship by DNS Injection (CCR 2012)","http://conferences.sigcomm.org/sigcomm/2012/paper/ccr-paper266.pdf")
    d.reading("An Analysis of China's 'Great Cannon' (FOCI 2015)","https://www.usenix.org/system/files/conference/foci15/foci15-paper-marczak.pdf")
    d.assignment("Presentation: Scott Heidbrink, Vaishnavi Narayan")

    s.week()

    d = s.day('February 6')
    d.lecture('TCP')
    d.reading("Background: Congestion Control","http://cs460.byu.edu/static/lectures/winter-2015/congestion-control.pdf")
    
    d = s.day('February 8')
    d.reading("CUBIC: A New TCP-Friendly High-Speed TCP Variant (SIGOPS Operating Systems Review 2008)","http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.153.3152&rep=rep1&type=pdf")
    d.assignment("Presentation: Brad Spendlove")

    d = s.day('February 10')
    d.lecture('TCP')
    d.reading("BBR: Congestion-Based Congestion Control (ACM Queue 2016)","http://queue.acm.org/detail.cfm?id=3022184")
    d.assignment("Presentation: Tyler Monson")
    
    s.week()

    d = s.day('February 13')
    d.lecture('TCP')
    d.reading("TIMELY: RTT-based Congestion Control for the Datacenter (SIGCOMM 2015)","http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdf")
    d.assignment("Presentation: Vaishnavi Narayan")


    d = s.day('February 15')
    d.lecture('TCP')
    d.reading("TIMELY: RTT-based Congestion Control for the Datacenter (SIGCOMM 2015)","http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdf")
    d.assignment("Presentation: Vaishnavi Narayan")

    d = s.day('February 17')
    d.lecture('TCP')
    d.reading("RC3: Recursively Cautious Congestion Control (2014 NSDI)","https://www.usenix.org/system/files/conference/nsdi14/nsdi14-paper-mittal.pdf")
    d.assignment("Presentation: Zann Anderson")
    
    # d.reading("PCC: Re-architecting Congestion Control for Consistent High Performance (NSDI 2015)","https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-dong.pdf")

    s.week()

    d = s.day('February 20')
    d.lecture('No Class','Monday Instruction')
    d.reading("A Primer on Net Neutrality (Rob Freiden)","http://www.personal.psu.edu/rmf5/NetworkNeutralityPrimer.pdf")
    d.option("Network Neutrality, Broadband Discrimination (Journal of Telecommunication and High Technology Law","https://papers.ssrn.com/sol3/papers2.cfm?abstract_id=388863")
    d.option("Internet Citizens: Defend Net Neutrality (advocacy, CPG Grey)","https://www.youtube.com/watch?v=wtt2aSV8wdw")
    d.option("John Oliver on Netork Neutrality (advocacy)","https://techcrunch.com/2014/06/03/watch-john-olivers-brilliant-concise-primer-on-net-neutrality/")

    d = s.day('February 22')
    d.lecture('Network Layer')
    d.reading("Neutral Net Neutrality (SIGCOMM 2016)", "http://yuba.stanford.edu/~yiannis/neutral-net-neutrality.pdf")
    d.assignment("Presentation: Scott Heidbrink")
    
    d = s.day('February 24')
    d.lecture('Network Layer')
    d.reading("A Primer on IPv4 Scarcity (CCR 2015)","http://www.sigcomm.org/sites/default/files/ccr/papers/2015/April/0000000-0000002.pdf")
    d.option("Measuring IPv6 Adoption (SIGCOMM 2014)","http://www.sigcomm.org/sites/default/files/ccr/papers/2014/August/2619239-2626295.pdf")
    d.assignment("Presentation: Tyler Monson")
    
    s.week()

    d = s.day('February 27')
    d.lecture('Network layer')
    d.reading("Internet Inter-Domain Traffic (SIGCOMM 2010)","http://www.sigcomm.org/sites/default/files/ccr/papers/2010/October/1851275-1851194.pdf")
    d.assignment("Presentation: Brad Spendlove")
    
    d = s.day('March 1')
    d.lecture('Routing')
    d.reading("BGP Prefix Delegations: A Deep Dive (IMC 2016 short paper)","https://www.net.t-labs.tu-berlin.de/papers/KF-BGPPD-16.pdf")
    d.option("An Introduction to BGP","https://www.internetsociety.org/sites/default/files/bgp.pdf")
    d.option("A Survey of BGP Security Issues and Solutions (IEEE Proceedings, 2010, see section 2)","https://www.cs.princeton.edu/~jrex/papers/pieee09.pdf")
    d.option("BGP: Border Gateway Protocol - Computerphile (very high level video)","https://www.youtube.com/watch?v=O6tCoD5c_U0")
    d.assignment("Presentation: Vaishnavi Narayan")
    
    d = s.day('March 3')
    d.lecture('Routing')
    d.reading("R-BGP: Staying Connected In a Connected World (NSDI 2007)","http://nms.lcs.mit.edu/papers/rbgp_nsdi_07.pdf")
    d.assignment("Presentation: Zann Anderson")
    
    s.week()

    d = s.day('March 6')
    d.lecture('Routing')
    d.reading("Pretty Good BGP: Improving BGP by Cautiously Adopting Routes (ICNP 2006)","https://www.cs.princeton.edu/~jrex/papers/pgbgp.pdf")
    d.assignment("Presentation: Scott Heidbrink")
    
    d = s.day('March 8')
    d.lecture('Routing')
    d.reading("A Study of Prefix Hijacking and Interception in the Internet (SIGCOMM 2007)","http://ccr.sigcomm.org/online/files/fp069-ballani.pdf")
    d.assignment("Presentation: Tyler Monson")
    
    d = s.day('March 10')
    d.lecture("Routing")
    d.reading("HLP: A Next Generation Inter-domain Routing Protocol (SIGCOMM 2005)","http://haig.cs.ucl.ac.uk/staff/M.Handley/papers/hlpsigcomm.pdf")
    d.assignment("Presentation: Brad Spendlove")

    s.week()

    d = s.day('March 13')
    d.lecture('Link Layer')
    d.reading("The Deforestation of L2 (SIGCOMM 2016)","https://www1.icsi.berkeley.edu/~barath/papers/axe-sigcomm16.pdf")
    d.assignment("Presentation: Vaishnavi Narayan")

    d = s.day('March 15')
    d.lecture('Survey Paper: Topic Presentation')
    d.assignment('Survey Paper: Topic Presentation')

    d = s.day('March 17')
    d.lecture('No Class')

    s.week()

    d = s.day('March 20')
    d.lecture('Architecture')
    d.reading("A Data-Oriented (and Beyond) Network Architecture (SIGCOMM 2007)","http://i3.cs.berkeley.edu/pubs/DONA-sigcomm07.pdf")
    d.assignment("Presentation: Zann Anderson")
    
    d = s.day('March 22')
    d.lecture('Architecture')
    d.reading("Networking Named Content (CoNext 2009)","https://named-data.net/wp-content/uploads/Jacob.pdf")
    d.assignment("Presentation: Scott Heidbrink")
    
    d = s.day('March 24')
    d.lecture("No Class")
    
    s.week()

    d = s.day('March 27')
    d.lecture('Architecture')
    d.reading("XIA: Efficient Support for Evolvable Internetworking (NSDI 2012)","http://www.cs.cmu.edu/~xia/resources/Documents/XIA-nsdi.pdf")
    d.assignment("Presentation: Tyler Monson")

    d = s.day('March 29')
    d.lecture('Architecture')
    d.reading("Network Service Abstractions for a Mobility-Centric Future Internet Architecture (MobiArch 2013)","http://mobilityfirst.winlab.rutgers.edu/documents/mobiarch13_camera_ready_Francesco.pdf")
    d.assignment("Presentation: Brad Spendlove")

    d = s.day('March 31')
    d.lecture('Architecture')
    d.assignment('Survey Paper: Annotated Bibliography')

    s.week()

    d = s.day('April 3')
    d.reading("ChoiceNet: Toward an Economy Plane for the Internet (CCR 2014)","http://rouskas.csc.ncsu.edu/Publications/Journals/CCR-CN-2014.pdf")
    d.assignment("Presentation: Vaishnavi Narayan")

    d = s.day('April 5')
    d.lecture('Architecture')
    d.reading("Architecting for Innovation (CCR 2011)","http://www.sigcomm.org/sites/default/files/ccr/papers/2011/July/2002250-2002256.pdf")
    d.assignment("Presentation: Zann Anderson")
        
    d = s.day('April 7')
    d.assignment('Survey Paper: First Draft')
    
    s.week()

    d = s.day('April 10')
    d.lecture('Wireless')
    d.reading("Passive Wi-Fi: Bringing Low Power to Wi-Fi Transmissions (NSDI 2016)","https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-kellogg.pdf")
    d.assignment("Presentation: Scott Heidbrink")
    
    d = s.day('April 12')
    d.lecture('No Class')

    d = s.day('April 14')
    d.lecture('Wireless')
    d.reading("Inter-Technology Backscatter: Towards Internet Connectivity for Implanted Devices (SIGCOMM 2016 best paper)","https://homes.cs.washington.edu/~gshyam/Papers/interscatter.pdf")
    d.assignment("Presentation: Tyler Monson")
    
    s.week()

    d = s.day('April 17')
    d.lecture('No Class')    

    d = s.day('April 19')
    d.lecture('No Class')

    s.week()

    d = s.day('April 24')
    d.assignment('Survey Paper, Due at 9:00am')

    return render_template('winter-2017/schedule.html',active='schedule',
                           weeks=s.weeks)
