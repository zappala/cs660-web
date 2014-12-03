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
    d.reading('One Tunnel is (Often) Enough (SIGCOMM 2014)','http://faculty.washington.edu/simpeter/sigc150-peterA.pdf')

    s.week()

    d = s.day("September 15")
    d.lecture('Internet Measurements (IMC 2013)')
    d.reading("Measuring IPv6 Adoption (SIGCOMM 2014)","https://www.icsi.berkeley.edu/pubs/networking/measuringIPv6.pdf")

    d = s.day('September 17')
    d.lecture('Internet Measurements')
    d.reading('Analysis of the HTTPS Certificate Ecosystem (IMC 2013)','http://conferences.sigcomm.org/imc/2013/papers/imc257-durumericAemb.pdf')

    d = s.day('September 19')
    d.lecture('Internet Measurements')
    d.reading('Understanding the Domain Registration Behavior of Spammers (SIGCOMM 2013)',
              'http://conferences.sigcomm.org/imc/2013/papers/imc247-haoA.pdf')

    s.week()

    d = s.day('September 22')
    d.lecture('Internet Measurements')
    d.reading('The Long "Taile" of Typosquatting Domain Names (USENIX Security 2014)',"https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/szurdi")

    d = s.day('September 24')
    d.lecture('Internet Measurements')
    d.reading("Understanding the Dark Side of Domain Parking (USENIX Security 2014)","https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/alrwais")

    d = s.day('September 26')
    d.lecture('Project Discussion')

    s.week()

    d = s.day('September 29')
    d.lecture('Cryptocurrency')
    d.reading("Bitcoin: A Peer-to-Peer Electronic Cash System","https://bitcoin.org/bitcoin.pdf")

    d = s.day('October 1')
    d.lecture('Cryptocurrency')
    d.reading('A Next Generation Smart Contract & Decentralized Application Platform (white paper)', 'https://www.ethereum.org/pdfs/EthereumWhitePaper.pdf')
    d.reading('Ethereum: A Secure Decentralised Generalised Transaction Ledger Proof-Of-Concept VI (yellow paper)','http://gavwood.com/Paper.pdf')

    d = s.day('October 3')
    d.lecture('Security')
    d.reading('SSL and HTTPS: Revisiting past challenges and evaluating certificate trust model enhancements','https://www.scs.carleton.ca/sites/default/files/tr/TR-13-01.pdf')

    s.week()

    d = s.day('October 6')
    d.lecture('Security')

    d = s.day('October 8')
    d.lecture("Security and Architecture")

    d = s.day('October 10')
    d.lecture('Internet Architecture')
    d.reading('Implementing Instant Messaging Using Named Data','http://named-data.net/wp-content/uploads/ndnpurple.pdf')
    d.reading('Networking Named Content (sections 4 and 5)','http://named-data.net/wp-content/uploads/Jacob.pdf')
    d.reading('Video Streaming over Named Data Networking (optional)','http://named-data.net/wp-content/uploads/2013/07/E-Letter-July13_page6.pdf')

    s.week()

    d = s.day('October 13')
    d.lecture('Internet Architecture')

    d = s.day('October 15')
    d.lecture('Internet Architecture')

    d = s.day('October 17')
    d.lecture('Internet Architecture')
    d.reading("NFD Developer's Guide","http://named-data.net/wp-content/uploads/2014/07/NFD-developer-guide.pdf")


    s.week()

    d = s.day('October 20')
    d.lecture('Privacy')
    d.reading("Anonymous Connections and Onion Routing","http://www.onion-router.net/Publications/JSAC-1998.pdf")

    d = s.day('October 22')
    d.lecture('Privacy')
    d.reading("Balancing Accountability and Privacy in the Network","http://www.cs.cmu.edu/~dnaylor/APIP.pdf")

    d = s.day('October 24')
    d.lecture('Privacy Discussion')

    s.week()

    d = s.day('October 27')
    d.lecture("Transport")
    d.reading("RC3: Recursively Cautious Congestion Control","http://www.eecs.berkeley.edu/~sylvia/papers/rc3-nsdi.pdf")

    d = s.day('October 39')
    d.lecture('Transport')
    d.reading('Reducing Web Latency: the Virtue of Gentle Aggression','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p159.pdf')

    d = s.day('October 31')
    d.lecture('Project Discussion',"Come prepared with a one paragraph description of a project and/or 5 important related papers")

    s.week()

    d = s.day('November 3')
    d.lecture('Transport')
    d.reading('TCP ex Machina: Computer-Generated Congestion Control','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p123.pdf')
  
    d = s.day('November 5')
    d.lecture('Work on Project')

    d = s.day('November 7')
    d.lecture('Work on Project')

#    d.reading('Improving Fairness, Efficiency, and Stability in HTTP-based Adaptive Video Streaming with FESTIVE','http://conferences.sigcomm.org/co-next/2012/eproceedings/conext/p97.pdf')
#    d.reading('Developing a Predictive Model of Quality of Experience for Internet Video','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p339.pdf')

    s.week()

    d = s.day('November 10')
    d.lecture('Work on Project')

    d = s.day('November 12')
    d.lecture('Report on Project')

    d = s.day('November 14')
    d.lecture('Report on Project')

#    d.reading('FCP: A Flexible Transport Framework for Accommodating Diversity (optional)','http://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p135.pdf')

    s.week()

    d = s.day('November 17')
    d.lecture("Network Neutrality")
    d.reading('Network Neutrality Inference','http://dl.acm.org/citation.cfm?id=2626308')

    d = s.day('November 19')
    d.lecture("Network Neutrality")
    d.reading("ISP Interconnection and its Impact on Consumer Internet Performance","http://www.measurementlab.net/static/observatory/M-Lab_Interconnection_Study_US.pdf")
    d.reading("Netflix vs Comcast: Internet Tolls And The Case For Strong Net Neutrality","http://blog.netflix.com/2014/03/internet-tolls-and-case-for-strong-net.html")
    d.reading("Netflix vs Comcast: The Case Against ISP Tolls","http://blog.netflix.com/2014/04/the-case-against-isp-tolls.html")
    d.reading("Netflix vs Comcast: Comcast response to Netflix","http://corporate.comcast.com/comcast-voices/comcast-response-to-netflix")
    d.reading("Netflix vs Comcast: Comcast TWC Merger Exhibit 4","http://corporate.comcast.com/images/2014-09-23-REDACTED-Comcast-TWC-Opposition-and-Response-Exhibit-4-McElearney.pdf")
    d.reading("Netflix response to FCC","http://apps.fcc.gov/ecfs/document/view?id=7521491186")
    

    d = s.day('November 21')
    d.lecture("Network Neutrality")
    d.reading("FCC: Setting the Record Straight on the FCC's Open Internet Rules","http://www.fcc.gov/blog/setting-record-straight-fcc-s-open-internet-rules");
    d.reading("FCC: Finding the Best Path Forward to Protect the Open Internet","http://www.fcc.gov/blog/finding-best-path-forward-protect-open-internet");
    d.reading("Media Coverage: 9 questions about network neutrality you were too embarrassed to ask","http://www.vox.com/2014/11/10/7187281/9-questions-about-network-neutrality-you-were-too-embarrassed-to-ask")
    d.reading("Media Coverage: Obama's big net neutrality announcement, explained","http://www.vox.com/2014/11/10/7186179/obamas-big-net-neutrality-announcement-explained")
    d.reading("Media Coverage: FCC Tests The Waters On A 'Hybrid' Net Neutrality Solution That Almost Everyone Hates","https://www.techdirt.com/blog/netneutrality/articles/20141031/05122328994/fcc-tests-waters-hybrid-net-neutrality-solution-that-almost-everyone-hates.shtml")
    d.reading("Media Coverage: Why the government should provide internet access","http://www.vox.com/2014/4/6/5587138/susan-crawford-internet-public-option")
    d.reading("Media Coverage: Fixing The Broadband Market And Protecting Net Neutrality By Prying Open Incumbent Networks To Meaningful Competition","https://www.techdirt.com/blog/netneutrality/articles/20141113/05332429127/fixing-broadband-market-protecting-net-neutrality-prying-open-incumbent-networks-to-meaningful-competition.shtml")
    s.week()

    d = s.day('November 24')
    d.lecture('Routing')
    d.reading("Finding a needle in a haystack: pinpointing significant BGP routing changes in an IP network","http://dl.acm.org/citation.cfm?id=1251204")

    d = s.day('November 25')
    d.lecture('Work on Projects')

    d = s.day('November 26')
    d.lecture('No Class','Thanksgiving Holiday')

    d = s.day('November 28')
    d.lecture('No Class','Thanksgiving Holiday')

    s.week()

    d = s.day('December 1')
    d.lecture('Routing')
    d.reading("HLP: a next generation inter-domain routing protocol","http://dl.acm.org/citation.cfm?id=1080095")

    d = s.day('December 3')
    d.lecture('Transport')
    d.reading("CUBIC: a new TCP-friendly high-speed TCP variant","http://dl.acm.org/citation.cfm?id=1400105")

    d = s.day('December 5')
    d.lecture('Projects')

    s.week()

    d = s.day('December 8')
    d.lecture('Wireless')


    d = s.day('December 10')
    d.lecture('Wireless')


    s.week()

    d = s.day('December 20')

    return render_template('fall-2014/schedule.html',active='schedule',
                           weeks=s.weeks)
##  http://cacm.acm.org/magazines/2014/4/173218-small-data-where-n-me/fulltext
## http://www.itworld.com/article/2828870/it-management/deborah-estrin-wants-to--literally--open-source-your-life.html
## http://www.eweek.com/enterprise-apps/small-data-analysis-the-next-big-thing-advocates-assert.html/
## https://smalldata.io/research.html
