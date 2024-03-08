---
layout: default
title: "Security Advisories"
---
# Security Advisories

SimpleSAMLphp is a software product critical for the security of applications and the privacy of users. As such, we take
every security issue very seriously, and try to solve them as fast as possible, avoiding any potential damage to both
users of this software and end users.

This page contains information about security vulnerabilities, incidents or issues related to SimpleSAMLphp. Read below
to learn how to properly report vulnerabilities, as well as to find information about issues already reported and fixed.

## Supported Versions

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Version</th>
    <th class="tg-0pky">Active support</th>
    <th class="tg-0pky">Security support</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-d52n">2.2</td>
    <td class="tg-c6of">Next release +6mo</td>
    <td class="tg-c6of">Next release +1yr</td>
  </tr>
  <tr>
    <td class="tg-d52n">2.1</td>
    <td class="tg-c6of">2024-09-08</td>
    <td class="tg-c6of">2025-03-08</td>
  </tr>
  <tr>
    <td class="tg-3wb8">2.0</td>
    <td class="tg-c6of">2024-04-30</td>
    <td class="tg-c6of">2024-10-30</td>
  </tr>
  <tr>
    <td class="tg-tw5s">&lt; 2.0</td>
    <td class="tg-c6of">No support</td>
    <td class="tg-n9g5">No support</td>
  </tr>
</tbody>
</table>

## Reporting vulnerabilities

In case you find a vulnerability in SimpleSAMLphp, or you want to confirm a possible security issue in the software,
please get in touch with us through [Sikt's CERT team](https://sikt.no/abuse). Please use our PGP public key
to encrypt any possible sensitive data that you may need to submit. We will get back to you as soon as possible
according to our working hours in Central European Time.

When reporting a security issue, please add as much information as possible to help us identify, confirm, replicate and
fix the problem. In particular, remember to include the following information in your report:

* The version or versions of SimpleSAMLphp affected.
* An exact version that can be used to replicate the issue.
* Any module or modules involved in the issue.
* Any particular configuration details relevant to the setup affected.
* A detailed description and a clear and concise, step-by-step guide to allow us reproduce the issue.
* Screenshots, videos, or any other media that would help identify the issue.
* Pointers to the exact line or lines in the code where the vulnerability is supposed to be.
* Context on how you discovered the issue.
* Your own name and whether you want to be credited for the discovery or not.

Please **DO NOT** report security incidents related to systems that use SimpleSAMLphp, where this software is not the
cause of the incident. Issues related to the use (or misuse) of infrastructure, misconfiguration of the software,
malfunction of a particular system or user-related errors should not be reported either. If you are using SimpleSAMLphp
to authenticate or login to services, but you don't know what SimpleSAMLphp is or you are not sure about the nature of
the issue, please contact the organization running the service for you.

Finally, be reasonable. We'll do our best to resolve the issue according to our principles of security and transparency.
Every confirmed vulnerability will be published and resolved in a timely manner. All we ask in return is that you
contact us privately first in order to avoid any potential damage to those using the software.

## List of Security Advisories

* [**SSPSA 202309-01**](/security/202309-01): Regression in setting of security headers.

* [**SSPSA 202004-01**](/security/202004-01): Information disclosure of source code.

* [**SSPSA 202001-02**](/security/202001-02): Log injection.

* [**SSPSA 202001-01**](/security/202001-01): Cross-site scripting in error reports.

* [**SSPSA 201911-02**](/security/201911-02): Information disclosure.

* [**SSPSA 201911-01**](/security/201911-01): Signature validation bypass.

* [**SSPSA 201907-01**](/security/201907-01): Reflected Cross-Site-Scripting.

* [**SSPSA 201812-01**](/security/201812-01): Credentials exposure in session storage.

* [**SSPSA 201809-03**](/security/201809-03): Multiple XPath injections (xmlseclibs).

* [**SSPSA 201809-02**](/security/201809-02): Dangerous use of `file_get_contents` (xmlseclibs).

* [**SSPSA 201809-01**](/security/201809-01): Insecure signature validation (xmlseclibs).

* [**SSPSA 201803-01**](/security/201803-01): Incorrect signature validation (in SAML 2.0).

* [**SSPSA 201802-01**](/security/201802-01): Incorrect signature validation (in SAML 2.0).

* [**SSPSA 201801-03**](/security/201801-03): Use of insecure connection charset (sqlauth module).

* [**SSPSA 201801-02**](/security/201801-02): Open redirection protection bypass.

* [**SSPSA 201801-01**](/security/201801-01): Denial of Service in timestamp validation function (SAML2 library).

* [**SSPSA 201710-01**](/security/201710-01): Signature validation bypass (in SAML 1.1).

* [**SSPSA 201709-01**](/security/201709-01): Cross Site Scripting (XSS) in the consentAdmin module.

* [**SSPSA 201708-01**](/security/201708-01): Invalid token creation and validation.

* [**SSPSA 201705-01**](/security/201705-01): Session fixation issue and authentication bypass in the authcrypt module.

* [**SSPSA 201704-02**](/security/201704-02): Authentication context bypass (multiauth module).

* [**SSPSA 201704-01**](/security/201704-01): Unauthenticated encryption in CBC mode.

* [**SSPSA 201703-02**](/security/201703-02): Incorrect IV generation for encryption.

* [**SSPSA 201703-01**](/security/201703-01): Multiple issues due to timing side channels.

* [**SSPSA 201612-04**](/security/201612-04): Incorrect persistent NameID generation.

* [**SSPSA 201612-03**](/security/201612-03): Incorrect signature validation (InfoCard module).

* [**SSPSA 201612-02**](/security/201612-02): Incorrect signature validation (in SAML 1.1).

* [**SSPSA 201612-01**](/security/201612-01): Incorrect signature validation (in SAML 2.0).

* [**SSPSA 201606-01**](/security/201606-01): Link injection in several pages.

* [**SSPSA 201603-01**](/security/201603-01): Information leakage issue in the *sanitycheck*
module.

* [**SSPSA 201404-01**](/security/201404-01): Information and advice for SimpleSAMLphp users related
to the Heartbleed vulnerability.
