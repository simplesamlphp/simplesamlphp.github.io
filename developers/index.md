---
layout: default
title: Developers
---
# Developers

* Jaime P&eacute;rez Crespo, UNINETT, Project Manager
* Tim van Dijen, Main Developer
* Olav Morken, UNINETT, Project Architect
* Andreas Åkre Solberg, UNINETT, Project Founder

One important core component of SimpleSAMLphp is xmlseclibs, maintained by:

* Rob Richards

We've had many contributors through the years. Here are some of them, in no particular order, that we would like to
thank:

* Andreas Mayer and the Chair for Network and Data Security of the Ruhr-University Bochum: Holder-of-Key profile support for both SP and IdP.
* Shoaib Ali (and Bill Young): Artifact support for the SP.
* Patrick Honing: aselect authentication module and various bugfixes. 
* Emmanuel Dreyfus: authX509 module, SASL support in LDAP and proxy authentication in LDAP
* [Danny Bollaert](mailto:danny.bollaert@gmail.com): Added support for sending HTTP-Artifact on the IdP. Created cas authentication source (based on original by Mads Freek)
* Lasse Birnbaum Jensen (Wayf.dk)
* Mads Freek Petersen (Wayf.dk)
* Anders Lund: Improved LDAP handling in authentication modules.
* Enrique de la Hoz: Working with PKI and client certificates with simpleSAMLphp. Adding tlsclient authentication module using apache (mod_ssl)
* Joakim Recht: Support for different logout response location than logout request location. Support for sending XML encoded attributes.
* Jacob Christiansen: consentAdmin. IsPassive (with Mads)
* Hans Zandbelt: a lot of testing, tips and tricks, WS-Federation support and A-Select support
* [Thomas Zangerl](mailto:thomas.zangerl@freenet.de): `core:ScopeFromAttribute` filter
* Lorenzo Gil: Add multiauth module.
* Pavel Šejnoha: Support for multiple servers in authmemcookie.
* Thomas Graff: Several usability improvements
* Harald Hannelius: Support for showing link to privacy policy on consent page.
* Georg Gollmann: Add support for multiple AssertionConsumerService endpoints.
* [gyufii](http://code.google.com/u/gyufii/): SAMLParser: Extract name and description from SP metadata.
* <pitbulk@gmail.com>: `cron`: View result in web page. `core:AttributeMap` - multiple target attributes.
* Peter Dam Mains: working on consent module
* Bjørn Ove Grøtan: Patches to LDAP login module
* Lukas Haemmerle: XML security improvements, eduGAIN handling and shibboleth testing.
* Stefan Winter: Radius attribute fetching, WebAuthn module
* Cato Olsen: Improved LDAP authentication module.
* José Alfonso Accino: Working with PAPI support in simpleSAMLphp. Various bugfixes.
* [Victoriano Giralt](mailto:victoriano@uma.es): Have done a great work with spanish localization of SimpleSAMLphp. Support for authenticating with a privileged account before fetching user attributes.
* fronter.com: They operate an e-learning platform and is working with implementing the Shibboleth 1.2 attribute profile.
* Ernesto Revilla: authorize-module and various bugfixes
* Kenneth Svee: Support for absolute paths in configuration options.
* Thijs Kinkhorst: Plenty of bugfixes and improvements.
* Boy Baukema: Did an excellent job extracting the SAML2 library from SimpleSAMLphp.
* Dick Visser: who has been running SimpleSAMLphp as a proxy for years and helped us debug and fix numerous issues.
* Hanne Moa: who started the migration to twig and a new internationalization system.
* Olimpia Magliulo: whose work on a new user interface was fundamental towards 2.0.
* Patrick Radtke: who takes care of several modules, and made many useful contributions.
* Dedra Chamberlin: who made an effort making SimpleSAMLphp known and used in the US.
* Guy Halse: multiple improvements and translations.
* Sergio Gómez: who helped us out take the most out of Symfony.
* Peter Schober: for his invaluable help in our mailing lists.

and many others who have helped use through the years make this project possible. Take a look at the [list of
contributors](https://github.com/simplesamlphp/simplesamlphp/graphs/contributors) for a comprehensive list of people who
have contributed to the project in one way or another. Thanks a lot to all of you!

Lots of credits to [Pat Patterson](http://blogs.sun.com/superpat/) which made SimpleSAMLphp possible by releasing the
proof of concept implementation Lightbulb, showing that lightweight SAML implementations actually works.
