---
layout: default
title: Downloads
---

# Download SimpleSAMLphp

Here you will find the packages with the current SimpleSAMLphp versions:

* <img class="icon" src="/res/icons/completed.png" alt="stable">
[**Latest release ({{ site.data.latest.tag_name | remove_first: "v" }})**]({{ site.data.latest.assets[0].browser_download_url }})

    Released: {{ site.data.latest.published_at | date: "%Y-%m-%d" }}

    {% assign sha = site.data.latest.body | split: 'SHA256 checksum slim-release: '  %}
    SHA256 checksum slim-release: {{ sha[1] | strip_html }}
    
    {% assign shaf = site.data.latest.body | split: 'SHA256 checksum full-release: ' %}
    SHA256 checksum full-release: {{ shaf[1]  | strip_html | truncate: 64 }}

    [View changes](/docs/stable/simplesamlphp-changelog)

Check the [GitHub releases page](https://github.com/simplesamlphp/simplesamlphp/releases)
in case you are looking for any other version.

## Github repository

The core library handling the basic SAML stuff (messages, bindings, and so on) is
detached from SimpleSAMLphp, and can be found on GitHub:

* [simplesamlphp/saml2](https://github.com/simplesamlphp/saml2)

SimpleSAMLphp itself is also on GitHub, and you will find it here:

* [simplesamlphp/simplesamlphp](https://github.com/simplesamlphp/simplesamlphp)

Make sure you follow the
[instructions to install from the repository](https://simplesamlphp.org/docs/devel/simplesamlphp-install-repo.html).

## Debian package

SimpleSAMLphp is available as a Debian package. You can therefore install it with apt-get,
but bear in mind that the version available in Debian stable might be outdated. Since Debian
backports security fixes, it is fine to use the version you may get with apt-get, but you will
miss the latest features.
