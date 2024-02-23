---
layout: default
title: Contribute 
---
# Contribute 

The SimpleSAMLphp project benefits from a global community of software developers who contribute to it.
The project receives financial support from higher education, research and corporate entities. The
legal, administrative home of SimpleSAMLphp is _The Commons Conservancy_ foundation based in The Netherlands, where it
is established as a programme.

The project, however, needs more contributors in order to survive, and we therefore kindly ask you to consider
supporting it. For many, this software comprises a vital piece of AAI infrastructure that merits proper maintenance,
care and attention. Sustaining SimpleSAMLphp will help you to continue to use this software in a secure and trusted way,
and would help getting new features and capabilities in the future that could benefit your organisation. While the
project has an important need for financial contributions, we of course also very much welcome structural, in-kind
ones, that could help sustain it.

If you have any suggestions or have the ability to contribute either financially or with your work, please do not
hesitate to contact Jan Meijer at jan.meijer@sikt.no. Any help is welcome, and it can be as simple as translating
SimpleSAMLphp into your language!

## Contributing code

If you want to contribute code SimpleSAMLphp, be it a simple bugfix, small improvement or larger new feature,
this is very welcome! Please read
[our contribution guidelines](https://github.com/simplesamlphp/simplesamlphp/blob/master/CONTRIBUTING.md)
for how to best go about reporting a bug or creating pull requests.

## Which branch to use

The "master" branch contains the current breaking development. This is
where new features are developed that will be in a major release in
the future. The maintenance of the supported versions happens in the
"simplesamlphp-2.x" branches.

If you want to contribute new functionality, please target "master".

If you want to fix a bug in an existing feature or functionality,
please target the simplesamlphp-2.1 (latest release) branch. If
accepted, the team will take care of backporting it to older supported
branches and if necessary applying it in master. 

If your bug only concerns an older supported release (e.g. 2.0 but not
2.1), you can target the older branch directly.

### Documentation updates

There are two main repositories for documentation. The website itself
comes from one place and everything that is under the "Documentation"
menu uses another process
(https://simplesamlphp.org/docs/stable/index.html).

The website lives in https://github.com/simplesamlphp/simplesamlphp.github.io

That only has a "release" branch to commit to, which is the website as
it is shown. There you'd commit to change the pages on the website,
e.g. to the page /contrib/

The "docs" repo (as described in the readme of the repo) only contains
the scripts that generate the docs website. In order to improve the
content of the documentation themselves, you commit using the same branches used
for code contributions at
https://github.com/simplesamlphp/simplesamlphp.

You can address documentation updates to master
(https://github.com/simplesamlphp/simplesamlphp/tree/master/docs).
Though it makes sense to backport them to supported releases, so each
version under https://simplesamlphp.org/docs/<VERSION>/ will show the
change. In other words, if a documentation change relates to 2.1.3 you
might like to make the pull request against the simplesamlphp-2.1
branch and leave it to the team to also apply it to master and other
branches in the same way that code updates work.



## Contributors

We would like to thank the organisations that have contributed financially to the survival of the project:

* [Sikt](https://sikt.no/) (formerly Uninett)
* [Cirrus Identity](https://www.cirrusidentity.com/)

The project wouldn't be possible either without the in-kind contributions of the many developers who have worked on it:

* Tim van Dijen, main developer
* Thijs Kinkhorst, SURF

We've had many contributors through the years. Here are some of them that we would like to thank particularly for the
importance of their past work:

* Andreas Åkre Solberg, Sikt, project founder
* Olav Morken, Sikt, former main developer and maintainer
* Jaime Pérez Crespo, former main developer and maintainer

Many others have helped make this project possible. Take a look at the [list of
contributors](https://github.com/simplesamlphp/simplesamlphp/graphs/contributors) for a more comprehensive list of
people who have contributed to it one way or another. Thanks a lot to all of you!

## Board

The project also established in the recent years a Board of Directors that works on taking care of all the
administrative stuff around it, trying to guarantee its continuity. The Board is currently comprised of:

* Jan Meijer, chair, Sikt
* Dedra Chamberlin, Cirrus Identity
* Niels van Dijk, SURF
* Jaime Pérez Crespo, Disruptive Technologies
* Marina Adomeit, SUNET
