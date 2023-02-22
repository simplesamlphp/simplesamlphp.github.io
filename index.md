---
layout: default
title: SimpleSAMLphp Home
---

<img class="ssplogomain" src="/res/ssplogo-fish-2.svg" alt="SimpleSAMLphp fish logo">

**SimpleSAMLphp** is an application written in native PHP that deals with
authentication. The main focus of SimpleSAMLphp is providing support for:

 * [**SAML 2.0** as a Service Provider (SP)](/samlsp/)
 * [**SAML 2.0** as an Identity Provider (IdP)](/samlidp/)

However, it also supports many other identity protocols and frameworks, such as CAS, OpenID Connect,
WS-Federation and OAuth, and is easily [extendable]({{ site.baseurl }}/modules), so you can develop your own modules if
you like.

The community-led project has a large user base, a helpful [user community](/support) and a diverse set of external contributors.

## Latest news

{% for post in site.posts limit:10 %}

* _{{ post.date | date: '%Y-%m-%d' }}_: {{ post.excerpt | remove: '<p>' | remove: '</p>' }} 

{% endfor %}
