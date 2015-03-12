<img src="/res/ssplogo-fish-only.jpg" style="float: right; " />

**SimpleSAMLphp** is an [award-winning]({{ site.baseurl}}/awards) application written in native PHP that deals with
authentication. The project is led by [UNINETT](https://www.uninett.no/), has a [large user base]({{ site.baseurl }}
/users), a helpful [user community]({{ site.baseurl }}/lists) and a [large set of external contributors](
{{ site.baseurl }}/developers). The main focus of SimpleSAMLphp is providing support for:

 * [**SAML 2.0** as a Service Provider (SP)]({{ site.baseurl }}/samlsp)
 * [**SAML 2.0** as an Identity Provider (IdP)]({{ site.baseurl }}/samlidp)

However, it also supports some other identity protocols and frameworks, such as Shibboleth 1.3, A-Select, CAS, OpenID,
WS-Federation or OAuth, and is easily [extendable]({{ site.baseurl }}/modules), so you can develop your own modules if
you like.

With the memcache session handler, **SimpleSAMLphp scales pretty well**. A replication layer is built upon memcache,
such that an unlimited number of SimpleSAMLphp web front-ends can work with a back-end matrix of memcache servers with
both replication (fail-over) and load-balancing.

SimpleSAMLphp is **tested with several other federation software implementations**. Among others; Shibboleth 1.3,
Shibboleth 2.2, PingID, Sun Federation Manager, Sun Federated Access Manager, Sun Access Manager, mod_mellon, CAS, etc.
If someone discovers incompatibility issues, we try to sort them out as fast as possible if reported properly through
the [issue tracker](https://github.com/simplesamlphp/simplesamlphp/issues).

## Latest news

{% for post in site.posts %}

* _{{ post.date | date: '%Y-%M-%d' }}_: {{ post.excerpt | remove: '<p>' | remove: '</p>' }} 

{% endfor %}