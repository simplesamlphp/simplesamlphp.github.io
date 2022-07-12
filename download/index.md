---
layout: default
title: Downloads
---

# Download SimpleSAMLphp

Here you will find the packages with the current simpleSAMLphp versions:

* <img style="position: relative; top: 5px" src="/res/icons/completed.png" alt="stable">
[**Latest release ({{ site.data.latest.tag_name | remove_first: "v" }})**]({{ site.data.latest.assets[0].browser_download_url }})

    Released: {{ site.data.latest.published_at | date: "%Y-%m-%d" }}

    {% assign sha = site.data.latest.body | split: 'SHA256 checksum: ' %}
    SHA256 checksum: {{ sha[1] }}

    [View changes](/docs/stable/simplesamlphp-changelog)

* <img style="position: relative; top: 5px" src="/res/icons/inwork.png" alt="wip">
[**Release candidate (2.0.0 RC 1)**](https://github.com/simplesamlphp/simplesamlphp/releases/download/v2.0.0-rc1/simplesamlphp-2.0.0-rc1.tar.gz)

    Released: 2022-07-01

    SHA256 checksum: a5842b6318142039873f5fdec3b0661ec405e55de425420e1a9d76a8771626d8

    [View changes](/docs/devel/simplesamlphp-changelog)

Check the [GitHub releases page](https://github.com/simplesamlphp/simplesamlphp/releases)
in case you are looking for any other version.

## Github repository

The core library handling the basic SAML stuff (messages, bindings, and so on) has been
detached from SimpleSAMLphp, and can now be found in github:

* [simplesamlphp/saml2](https://github.com/simplesamlphp/saml2)

SimpleSAMLphp itself has been moved to github too, and you will find it here:

* [simplesamlphp/simplesamlphp](https://github.com/simplesamlphp/simplesamlphp)

Make sure you follow the
[instructions to install from the repository](https://simplesamlphp.org/docs/latest/simplesamlphp-install-repo.html).

## Debian package

SimpleSAMLphp is available as a Debian package. You can therefore install it with apt-get,
but bear in mind that the version available in Debian stable might be outdated. Since Debian
backports security fixes, it is fine to use the version you may get with apt-get, but you will
miss the latest features.
