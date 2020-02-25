# SimpleSAMLphp as a Service Provider (SP)

If you have a web application that needs to authenticate users, SimpleSAMLphp can help you out. In addition to
supporting local authentication with one of the authentication modules, you can use the service provider functionality.
If you are using SimpleSAMLphp as a service provider, it will communicate and delegate authentication to an Identity
Provider. SimpleSAMLphp may connect to both a Shibboleth or a SAML 2.0 Identity Provider.

As SimpleSAMLphp is written in PHP, it is the most convenient and simple choice for integrating web-based PHP
applications into a federation. That said, SimpleSAMLphp now also supports non-PHP environments by using the Auth
Memcookie approach. This setup is supported from version 1.0, and not yet fully documented, but it will be very soon.
Basically, SimpleSAMLphp adds a special cookie in memcache that the [well-known Apache module Auth
MemCookie](http://authmemcookie.sourceforge.net/) understands, and it passes authentication information in header
variables and allows you to setup authorization in Apache.

If you want to connect the same SP to multiple IdPs, and want to let the user select between the IdPs, you can use the
built-in [SAML 2.0 Discovery Service](http://www.google.no/url?sa=t&amp;ct=res&amp;cd=3&amp;url=http%3A%2F%2Fwww.oasis-open.org%2Fcommittees%2Fdownload.php%2F22041&amp;ei=hTc2R-fmEJ6WwgGB4_z-Cg&amp;usg=AFQjCNEOEzWgM49xb2SuqLl5NnV_Df0W6w&amp;sig2=mPvazK-6MXle3bYXBG6ZsA).
