---
layout: default
title: Modules
---
# Third-party modules

SimpleSAMLphp contains an Extension API, allowing third-party modules to extend some parts of SimpleSAMLphp. Some of the
most important extension points of SimpleSAMLphp include:

* **Authentication Modules** allow you to implement your own authentication method, such as PKI-based, using a
proprietary user data source, or any other kind of authentication mechanism.
* **Authentication Processing Filters** allow any kind of processing right after authentication has taken place.
* **Themes** allow you to customize the look of any page served by SimpleSAMLphp. You can change only the CSS, headers,
footers, or you can modify the look of any particular page.
* **Modules** allow you to extend SimpleSAMLphp with any new identity protocols, pages, registry systems or anything
you'd like.

SimpleSAMLphp comes with a number of modules, authentication modules and processing filters that you may use, or use as
a base for customizing SimpleSAMLphp to fit your specific needs. It also provides:

* an abstract data store API, allowing alternative ways of storing data
* an abstraction layer of metadata handling, allowing alternative implementations of metadata consumption
* multiple session handlers, which you can use the session handling built-in to PHP or use memcache
* multiple handlers for logging. You can choose between syslog and a normal file logger

Apart from the modules that ship by default with SimpleSAMLphp, there's plenty of modules that third-party developers
make available for you to cover specific features. Here we provide a (non-exhaustive) list of modules available:

### How to install third-party modules

SimpleSAMLphp makes use of [Composer](https://getcomposer.org/) to manage dependencies and third-party modules. Those
modules that have been properly configured can be easily installed with composer. Just execute the following command:

    composer.phar require vendor/simplesamlphp-module-mymodule version

where `vendor` is the name of the vendor of the module, `mymodule` is the name of the module itself and `version` is the
version of the module you want to install, for example, 1.0.

Please note that if you don't have console access to your web server, you will need to deploy the module somewhere else
and then copy the files to your server.

####<a name="aselect" href="#aselect">A-Select</a>

This module allows you to use A-Select (or any service that understands the A-Select 1.5 protocol) to authenticate users
in SimpleSAMLphp.

See the [website](https://non-gnu.uvt.nl/simplesamlphp-aselect/) for more information on how to download and install it.

####<a name="attrauth" href="#attrauth">Attribute Authority</a>

This module provides back-end SAML Attribute Authority functionality.

* Package name: `NIIF/simplesamlphp-module-aa`
* Repository: [NIIF/simplesamlphp-module-aa](https://github.com/NIIF/simplesamlphp-module-aa)

####<a name="attraggregator" href="#attraggregator">Attribute Aggregator</a>

The Attribute Aggregator module is implemented as an
[Authentication Processing Filter](http://www.famine.vm/docs/stable/simplesamlphp-authproc). It can be configured in the
SP's `config.php` file.

It is recommended to run the Attribute Aggregator module at the SP and configure the filter to run after the federated
identity, usually _eduPersonPrincipalName_, is resolved.

* Package name: `NIIF/simplesamlphp-module-attributeaggregator`
* Repository: [NIIF/simplesamlphp-module-atributeaggregator](https://github.com/NIIF/simplesamlphp-module-attributeaggregator)

####<a name="attrscopefilter" href="#attrscopefilter">Attribute Scope Filter</a>

This module ensures that scoped attributes (such as `eduPersonPrincipalName`) have the right scopes defined in the
entity metadata. It removes values:

* that should be scoped but are not;
* whose scope does not match the shibmd:Scope element in the metadata.

Additionally, it is also capable of handling *scope attributes* such as `schacHomeOrganization` that should be
equivalent to the `shibmd:Scope` element in the metadata.

* Package name: `NIIF/simplesamlphp-module-attributescope`
* Repository: [NIIF/simplesamlphp-module-attributescope](https://github.com/NIIF/simplesamlphp-module-attributescope)

####<a name="authmemcookie" href="#authmemcookie">AuthMemCookie</a>

This module implements [Auth MemCookie](http://authmemcookie.sourceforge.net/) support for SimpleSAMLphp. This allows
you to integrate SimpleSAMLphp with web applications written in languages other than PHP.

* Package name: `simplesamlphp/simplesamlphp-module-memcookie`
* Repository: [simplesamlphp/simplesamlphp-module-memcookie](https://github.com/simplesamlphp/simplesamlphp-module-memcookie)

####<a name="autotest" href="#autotest">Autotest</a>

This module provides an interface to do automatic testing of authentication sources.

* Package name: `simplesamlphp/simplesamlphp-module-autotest`
* Repository: [simplesamlphp/simplesamlphp-module-autotest](https://github.com/simplesamlphp/simplesamlphp-module-autotest)

####<a name="cassandrastore" href="#cassandrastore">Cassandra Store</a>

A SimpleSAMLphp module providing support for Cassandra backends to store both session information and metadata.

* Package name: `feideconnect/simplesamlphp-module-cassandrastore`
* Repository: [feideconnect/simplesamlphp-module-cassandrastore](https://github.com/feideconnect/simplesamlphp-module-cassandrastore)

####<a name="consentsimpleadmin" href="#consentsimpleadmin">Consent Simple Admin</a>

A SimpleSAMLphp module implementing a very simple user interface for managing consent.

* Package name: `simplesamlphp/simplesamlphp-module-consentsimpleadmin`
* Repository: [simplesamlphp/simplesamlphp-module-consentsimpleadmin](https://github.com/simplesamlphp/simplesamlphp-module-consentsimpleadmin)

####<a name="discojuice" href="#discojuice">DiscoJuice</a>

A SimpleSAMLphp module to provide a very flexible User Interface implementing an IdP Discovery Service. See the
[web page](http://discojuice.org) for more information.

* Package name: `simplesamlphp/simplesamlphp-module-discojuice`
* Repository: [simplesamlphp/simplesamlphp-module-discojuice](https://github.com/simplesamlphp/simplesamlphp-module-discojuice)

####<a name="attrfromentity" href="#attrfromentity">entattribs:AttributeFromEntity</a>

This SimpleSAMLphp authentication processing filter allows you to provide additional attributes based on entity
attributes in the metadata. It is useful when entity metadata contains definitive information that you wish to convert
into a SAML attribute (e.g. an entity attribute containing the value that should be used for *schacHomeOrganization* in
remote IdP metadata).

* Package name: `safire-ac-za/simplesamlphp-modules-entattribs`
* Repository: [safire-ac-za/simplesamlphp-modules-entattribs](https://github.com/safire-ac-za/simplesamlphp-module-entattribs)

####<a name="fticks" href="#fticks">F-ticks</a>

Log statistics in the [F-ticks federation log format](https://wiki.geant.org/display/gn42jra3/F-ticks+standard).

The filter aims to produce as many F-ticks attributes as possible, irrespective of whether SimpleSAMLphp is acting as an
Identity Provider or a SAML Service Provider.

* Package name: `safire-ac-za/simplesamlphp-modules-fticks`
* Repository: [safire-ac-za/simplesamlphp-modules-fticks](https://github.com/safire-ac-za/simplesamlphp-module-fticks)

####<a name="generateuniqueid" href="#generateuniqueid">Generate Unique ID</a>

Generate an `eduPersonUniqueId` attribute from various LDAP implementations' objectGUID.

* Package name: `safire-ac-za/simplesamlphp-modules-genuniqueid`
* Repository: [safire-ac-za/simplesamlphp-modules-genuniqueid](https://github.com/safire-ac-za/simplesamlphp-module-genuniqueid)

####<a name="infocard" href="#infocard">InfoCard</a>

This is a SimpleSAMLphp module that works with Information Cards technologies and provides some basic functionalities:

* **RP**: acting as a Relying Party, you can accept user authentication through InfoCards consuming tokens sent by an
STS.

* **STS**: acting as a Secure Token Service you can provide information to a RP generating tokens. Currently, only user
password and self issued credentials are supported.

* **InfoCard Generator**: your users could request their InfoCard filling a form with their username and password.

* Package name: `simplesamlphp/simplesamlphp-module-infocard`
* Repository: [simplesamlphp/simplesamlphp-module-infocard](https://github.com/simplesamlphp/simplesamlphp-module-infocard)

####<a name="kerberos" href="#kerberos">Kerberos</a>

Kerberos 5 authentication module for SimpleSAMLphp.

* Package name: `ualberta-iapps/simplesamlphp-module-kerberos`
* Repository: [ualberta-iapps/simplesamlphp-module-kerberos](https://github.com/ualberta-iapps/simplesamlphp-module-kerberos)

####<a name="logpeek" href="#logpeek">Logpeek</a>

This module provides a web API that you can use to search for all to lines in the logs corresponding to a specific
session identifier.

* Package name: `simplesamlphp/simplesamlphp-module-logpeek`
* Repository: [simplesamlphp/simplesamlphp-module-logpeek](https://github.com/simplesamlphp/simplesamlphp-module-logpeek)


####<a name="mdaggregator" href="#mdaggregator">Metadata aggregator</a>

This module aggregates a set of SAML entities into SAML 2.0 metadata documents. The resulting metadata documents contain
an EntitiesDescriptor element with the multiple entities configured as sources inside. Multiple aggregates can be
configured at the same time.

Please note that **this module has been deprecated** in favour of the more recent
[Aggregator2 module](https://github.com/simplesamlphp/simplesamlphp-module-aggregator2).

* Package name: `simplesamlphp/simplesamlphp-module-aggregator`
* Repository: [simplesamlphp/simplesamlphp-module-aggregator](https://github.com/simplesamlphp/simplesamlphp-module-aggregator)

####<a name="mdaggregator2" href="#mdaggregator2">Metadata aggregator 2</a>

This is a module for metadata aggregation. It is designed to preserve most of the common metadata items, and it also
attempts to preserve unknown elements. It parses and rebuilds metadata sources, so small differences between them and
the generated metadata may occur.

Please note that this aggregator works only with XML metadata, and does its work independently of other parts of
SimpleSAMLphp, such as the _metarefresh_ module.

* Package name: `simplesamlphp/simplesamlphp-module-aggregator2`
* Repository: [simplesamlphp/simplesamlphp-module-aggregator2](https://github.com/simplesamlphp/simplesamlphp-module-aggregator2)

####<a name="metaedit" href="#metaedit">Metaedit</a>

This module allows you to do very basic editing of metadata (AssertionConsumerService, SingleLogoutService, name and
description, as well as manually registering metadata for service providers.

* Package name: `simplesamlphp/simplesamlphp-module-metaedit`
* Repository: [simplesamlphp/simplesamlphp-module-metaedit](https://github.com/simplesamlphp/simplesamlphp-module-metaedit)

####<a name="modinfo" href="#modinfo">Modinfo</a>

A very straightforward module for SimpleSAMLphp that displays the list of modules and their status in the web interface.

* Package name: `simplesamlphp/simplesamlphp-module-modinfo`
* Repository: [simplesamlphp/simplesamlphp-module-modinfo](https://github.com/simplesamlphp/simplesamlphp-module-modinfo)

####<a name="monitor" href="#monitor">Monitor</a>

A SimpleSAMLphp module that can monitor authsources, metadata, certificate validity, etc. It can output results as HTML,
XML or JSON it can be easily extended with your own test cases

* Package name: `tvdijen/simplesamlphp-module-monitor`
* Repository: [tvdijen/simplesamlphp-module-monitor](https://github.com/tvdijen/simplesamlphp-module-monitor)

####<a name="oauth2" href="#oauth2">OAuth2</a>

A module adding support for [the OAuth2 protocol](http://oauth.net/2/).

* Package name: `sgomez/simplesamlphp-module-oauth2`
* Repository: [sgomez/simplesamlphp-module-oauth2](https://github.com/sgomez/simplesamlphp-module-oauth2)

####<a name="oidconsumer" href="#oidconsumer">OpenID Consumer</a>

A module adding support for the OpenID protocol as a Consumer.

* Package name: `simplesamlphp/simplesamlphp-module-openid`
* Repository: [simplesamlphp/simplesamlphp-module-openid](https://github.com/simplesamlphp/simplesamlphp-module-openid)

####<a name="oidprovider" href="#oidprovider">OpenID Provider</a>

A module adding support for the OpenID protocol as an Identity Provider.

* Package name: `simplesamlphp/simplesamlphp-module-openidprovider`
* Repository: [simplesamlphp/simplesamlphp-module-openidprovider](https://github.com/simplesamlphp/simplesamlphp-module-openidprovider)

####<a name="papi" href="#papi">PAPI</a>

This authentication module makes use of an external library, [_phpPoA_](https://forja.rediris.es/projects/phppoa/), in
order to authenticate users by means of the PAPI protocol. It can therefore be used to bridge between protocols,
behaving like a PAPI _Point of Access_ or as a _Service Provider_.

* Package name: `rediris-es/simplesamlphp-module-papi`
* Repository: [rediris-es/simplesamlphp-module-papi](https://github.com/rediris-es/simplesamlphp-module-papi)

####<a name="privacyidea" href="#privacyidea">PrivacyIDEA</a>

This module enables SimpleSAMLphp to perform two-factor authentication against a *privacyIDEA* server. Users can
authenticate with normal OTP tokens, challenge-response tokens via email or text messages, or U2F devices.

* Package name: `privacyidea/simplesamlphp-module-privacyidea`
* Repository: [privacyidea/simplesamlphp-module-privacyidea](https://github.com/privacyidea/simplesamlphp-module-privacyidea)

####<a name="samldebug" href="#samldebug">SAML 2.0 Debugger</a>

This module allows you to debug SAML 2.0 messages by decoding or encoding them according to the binding they are using,
supporting both the HTTP-Redirect and HTTP-POST bindings.

* Package name: `simplesamlphp/simplesamlphp-module-saml2debug`
* Repository: [simplesamlphp/simplesamlphp-module-saml2debug](https://github.com/simplesamlphp/simplesamlphp-module-saml2debug)

####<a name="selfregister" href="#selfregister">Selfregister</a>

A module that allows registration of users accounts. The original version was developed by UNINETT and supported LDAP as
a backend. This fork adds support for SQL databases as the back-end.

* Package name: `geant/simplesamlphp-module-selfregister`
* Repository: [geant/simplesamlphp-module-selfregister](https://github.com/TERENA/simplesamlphp-module-selfregister)

####<a name="sqlattrs" href="#sqlattrs">SQL Attributes</a>

An authentication processing filter that allows you to provide additional attributes from a SQL datastore. It is useful
in situations where your primary authentication source is a directory (e.g. AD) that you do not have direct control
over, and you need to add additional attributes for specific users but cannot add them to the directory or modify the
schema.

* Package name: `safire-ac-za/simplesamlphp-module-sqlattribs`
* Repository: [safire-ac-za/simplesamlphp-module-sqlattribs](https://github.com/safire-ac-za/simplesamlphp-module-sqlattribs)

####<a name="voot" href="#voot">VOOT Groups</a>

A module to fetch group memberships from an API service protected with OAuth 2.0 using the VOOT protocol and add them
to the list of attributes received from the identity provider.

* Package name: `openconextapps/simplesamlphp-module-vootgroups`
* Repository: [OpenConextApps/ssp-voot-groups](https://github.com/OpenConextApps/ssp-voot-groups)

## Extending SimpleSAMLphp

If you plan to extend SimpleSAMLphp with some functionality, we advise you to follow these recommendations:

1. Check the existing functionalities and modules. The feature you want to implement may already exist.

2. Try to code with the [PHP PSR-2 guidelines](http://www.php-fig.org/psr/psr-2/) in mind.

3. Make sure your module is [installable through composer](https://github.com/simplesamlphp/composer-module-installer).

4. Let us know about your module so we can reference it in this web site, so that our users can easily find it.
