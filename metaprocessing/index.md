# Metadata processing performance

Due to a [known issue in XML canonicalization](https://bugs.php.net/bug.php?id=53655) in PHP, processing large metadata
files in SimpleSAMLphp takes a big amount of resources, with that amount growing approximately by the square of the
number of entities in the metadata set. In the context of this issue, _processing_ means both verifying a signature of
metadata and also signing a new metadata document. This includes the initial parsing of a SAML metadata document, since
SimpleSAMLphp verifies the signature at the same time it parses the document.

As previously said, this is an issue specially for those people consuming or signing large metadata sets, as for
example the [_UK Federation_](http://www.ukfederation.org.uk/) or
[_eduGAIN_](http://www.geant.net/service/edugain/pages/home.aspx) metadata feeds.

Given the lack of response from the PHP team to solve this issue, we have applied [a workaround for the problem](
https://github.com/simplesamlphp/xmlseclibs/commit/b51cc66d576608282272892278a5fc234d21ba34) inside the
[**xmlseclibs**](https://code.google.com/p/xmlseclibs/) library, which has been included in **SimpleSAMLphp version
1.13.2**. This workaround is **experimental** and could lead to unexpected issues. We have tested it without issues for
a long time, both for verifying and creating signatures, but we can't guarantee yet that it is completely free of side
effects. We are currently testing it more thoroughly (special thanks to the people at GÉANT Association) and we will
hopefully be able to discard any interoperability issues in a short time.

Meanwhile, all the users of SimpleSAMLphp that are members of the _UK Federation_ or _eduGAIN_ are encouraged to update
their installations to the new version 1.13.2. Since we cannot guarantee the absence of side effects, we recommend
installing a new, separate instance of SimpleSAMLphp to handle metadata processing, preferably in a different, dedicated
machine. Please note that starting **November 17 of 2014**, the _UK Federation_ will dump most of its entities to the
_eduGAIN_ metadata feed, making it impossible for SimpleSAMLphp to consume this feed.

For those using older versions of SimpleSAMLphp or having difficulties to update to the latest version, the workaround
can be applied by replacing the **xmlseclibs** library with [this one](
https://github.com/simplesamlphp/xmlseclibs/blob/b51cc66d576608282272892278a5fc234d21ba34/xmlseclibs.php). Those who
are using [composer](https://getcomposer.org/) can edit their `composer.json` file to change the version of
**xmlseclibs** they are running:

    "simplesamlphp/xmlseclibs": "~1.3.2",

and then update it normally:

    composer.phar update

If you are running the updated library and experience unexpected behaviour, please do not hesitate to [contact
us](https://groups.google.com/forum/#!forum/simplesamlphp) or [open an issue in the issue
tracker](https://github.com/simplesamlphp/simplesamlphp/issues).
