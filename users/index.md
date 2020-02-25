---
layout: default
title: SimpleSAML Users
---
# SimpleSAMLphp Users

Here are some users of SimpleSAMLphp and what they have to say about the software. To get in contact with these and other users of SimpleSAMLphp, [please join the mailinglist](/mailinglists).

## TEQneers GmbH & Co. KG

We are using SAML2 as SP in our products to be able to offer secure
SSO for our customers using SAAS.

> SAML itself is great. Having a free product like SimpleSAML is even better. People from Feide are extremely helpful and continuously improve this software. I can highly recommend SimpleSAML.

**Oliver Mueller, CEO.**

<br style="height: 0px; width: 0px; clear: both" />



## Technischen Universität Wien, Zentraler Informatikdienst

<img src="https://idp.zid.tuwien.ac.at/portrait.jpeg" style="float: left; border: 1px solid #666; margin: .3em 1em" />

<p>We use simpleSAMLphp as a SAML2 IdP for <a href="http://www.ubook.at/">u:book</a>, which is mainly a Shib2 federation. We have used simpleSAMLphp in production since Fall ´08.</p>

<blockquote>It was easy to integrate simpleSAMLphp with our <a href="http://www.gemstone.com/products/smalltalk/">GemStone database</a>.</blockquote>

**Dipl.-Ing. Georg Gollmann** 

* [More information on Gollmann](http://whitepages.tuwien.ac.at/oid/636501.html)

<br style="height: 0px; width: 0px; clear: both" />


## WAYF - Where Are You From

<img src="/res/david.jpg" style="float: left; border: 1px solid #666; margin: .3em 1em" />

[WAYF - Where Are You From - the Danish e-ID federation for research and education](http://wayf.dk) use simpleSAMLphp both as protocol bridge (SAML2, Shibboelth 1.3, CAS, LDAP), identity provider (towards the connected services, on behalf of the connected institutions) and service provider (WAYF has several SAML2-services protected by simpleSAMLphp).

> simpleSAMLphp came to WAYF's rescue at a critical time where other products fell short. Within a short time frame we were able to completely redesign, test and set into production(!) simpleSAMLphp as the central federation component - not at least because it is written in human readable PHP, but also because of the steady and huge support Feide has given us. Several WAYF developers have contributed to the code - always with a feeling that simpleSAMLphp is done 'the right way'.

We run simpleSAMLphp in production, connecting around 300.000 e-ID's at the connected institutions. More institutions and services will get connected soon - and still we will sleep tight at night. The production system will also be connected to other e-ID federations, in Denmark and abroad. We also use simpleSAMLphp for testing purposes. Redundancy, multi instance setups etc. are being investigated.

**David Simonsen, WAYF-secretariat**

<br style="height: 0px; width: 0px; clear: both" />



## EDB Gruppen A/S

<img src="/res/edbgruppen.jpg" style="float: left; border: 1px solid #666; margin: .3em 1em" />

We use simpleSAMLphp in production as an SP to provide a simple gateway to an IdP, specifically Nemlog-in.

* [More information about EDB Gruppen A/S](http://www.noegleskabet.dk)

**Benjamin Nyrup Figueiredo, Technical Architect**



## JQuantLib.org

<img src="/res/jquantlib.jpg"  style="float: left; border: 1px solid #666; margin: .3em 1em" />

* <http://www.jquantlib.org>

Still testing integrating with Mediawiki. SimpleSAMLphp definitely works and returns to Mediawiki but authentication layer in Mediawiki is a spaghetti :( and our proof of concept is not working as it should yet.

> SimpleSAMLphp is definitely great! It's well written, well organized and relatively well documented.

**Richard Gomes, Lead Developer** 

* [More information about Richard Gomes](http://www.jquantlib.org/index.php/User:RichardGomes)





## Ordbogen.com, Denmarks largest online dictionaries

We use simpleSAMLphp with SAML2 and we use it as a service provider. We deliver online dictionaries to many institutions in Denmark. Almost every university uses Ordbogen.com, and many of them also use WAYF (IdP). It has opened a new possibility for us to deliver online dictionaries and still control our licenses.

> SimpleSAMLphp has a unique way of transporting data which solves problems with firewalls etc. But it is still a very secure transport of data.

We are now in production with SimpleSAMLphp and many people use our dictionaries through WAYF (SimpleSAMLphp IdP).

**Michael Walther, Head of the Innovation department**




## University of the Basque Country

<img src="/res/oskar_casquero.jpg" style="float: left; border: 1px solid #666; margin: .3em 1em" />

I'm using simpleSAMLphp for enabling SSO on a prototype of PLE (Personal Learning Environment) I'm developing for my PhD dissertation. I've configured an IdP, connected to our institutional LDAP, and the following SPs: Google Apps, Moodle (through simpleSAMLphp Moodle module) and, in the near future, a network of blogs built on Drupal (through simpleSAMLphp Drupal module).

> What I think of simpleSAMLphp: easy to install, well documented and good support

**Oskar Casquero, Professor**



## University of Málaga

Our "&Aacute;gora Sur" interdisciplinary research team (<http://agorasur.es/>) is using SimpleSAMLphp for developing a "fuzzy limits" environment for collaboration and learning ("Ágora Virtual") according to the principe "the platform is the net". For this setup we use SimpleSAMLphp for IdP and SP, working together with PAPI. We have developed bridges for both PAPI-sSp and sSp-PAPI ways, and SimpleSAMLphp and PAPI modules for implementation of OKI OSID authentication, as well.

> SimpleSAMLphp is a clever SAML 2 SP and IdP implementation and the simplest and easiest way to get PHP applications into SAML 2 federations". Period.

Currently, we have already adapted Dokuwiki and CMS Made Simple using PAPI and sSp, Mantis bugtracker (with SimpleSAMLphp), LimeSurvey (with SimpleSAMLphp) and, of course, "Agora Virtual" itself as the environment core. Other pieces (as our "Rubric" tool) are on their way.


* [Accino, J.A.; Cebrián, M.; Giralt, V. (2008): Identity Architectures
for Innovative Technology Enhanced Learning. e-Challenges 2008, Stockholm](http://www.agorasur.es/publico/documentos/2008_eChallenges_ref_244_doc_5040.pdf)
* [Accino, Giralt, Cebrián: Federated e-learning platform. TERENA EuroCAMP, Dubrovnik, Nov. 2007](http://www.terena.org/activities/eurocamp/november07/slides/giralt-agora.pdf)
* [Our presentation to RedIRIS Technical Conference 2007: Accino, Cebrián: The platform is the net: User Centered Learning and
Identity Centered Architectures](http://www.rediris.es/difusion/publicaciones/boletin/84/enfoque3.pdf)


**José Alfonso Accino. IT Systems Management Team.**

## Spanish academic and research network (RedIRIS)

* <http://www.rediris.es/>

<img src="/res/rediris.png" style="float: left; border: 1px solid #666; margin: .3em 1em" />

> We're using simpleSAMLphp in our infrastructure in order to deploy SAML2 and SAML1.1 identity providers gateways to this Spanish federation. These IdPs are using the PAPI Authentication Service of each institution for the authenticating their users.
> Thanks to simpleSAMLphp Spanish institutions are able to connect to protected resources which have chosen SAML2/SAML1.1 (or Shibboleth 2/Shibboleth 1.3) as their technology for joining to our federation.

**Cándido Rodríguez Montes**



## Deutsches Forschungsnetz (DFN)

> I heartly recommend simpleSAMLphp to everyone considering the complexity of shibboleth the main obstacle to joining the DFN Federation.

**Torsten Kersting, DFN**

## Academic and Research Network of Slovenia (Arnes)


>We decided to use SAML2, IdPs are simpleSAMLphp and SPs are both simpleSAMLphp and Shibboleth2. One SP is modified, to support Kerberos, and one modifying is still in progress (support users to be added on-the-fly to Adobe Connect web conferencing sw).

> with just few words - simpleSAMLphp made deploying SAML simple. :-)


**Alex Mihičinac, Arnes AAI Team**



## University of Zagreb, University Computing Centre

<img src="/res/dvoncina.jpg" style="float: left; border: 1px solid #666; margin: .3em 1em" />


> We are using simpleSAMLphp in production since March 2008. We used it primarily to implement a Single Sign-On service within Croatian academic authentication and authorization infrastructure (AAI@EduHr), but we have also deployed several applications like phpBB, MediaWiki, OTRS and some applications that we developed which use authentication modules based on simpleSAMLphp. At the beginning of 2009. our simpleSAMLphp-based SSO service was handling approximately 2000 authentication requests per day, but we expect this number to grow significantly during 2009.


> One of the great things about simpleSAMLphp is the simpleSAMLphp community. We didn't have many problems with simpleSAMLphp, but those few problems we had were quickly solved by simpleSAMLphp developers or someone else from the community.

**Dubravko Voncina, member of AAI@EduHr development team**
