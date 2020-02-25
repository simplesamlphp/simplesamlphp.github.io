# SimpleSAMLphp as an Identity Provider (IdP)

If you have a directory of users, a database, an LDAP or a Radius interface, you can setup an installation of SimpleSAMLphp to have your own federated Single Sign-On environment.

If you run SimpleSAMLphp as an Identity Provider both Shibboleth and SAML 2.0 services may connect to you.

You may use one of the following included authentication modules or you can very simply make your own:

* Simple LDAP
* Multiple LDAP
* CAS remote authentication lets you connect authentication to your existing CAS service, and subsequently retrieve attributes from LDAP.
* Radius authentication lets to check the credentials against a Radius server
* SQL authentication
* OpenID
* YubiKey
