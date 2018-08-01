.. image:: https://travis-ci.com/collective/collective.fontawesome.svg?branch=master
    :target: https://travis-ci.com/collective/collective.fontawesome


======================
collective.fontawesome
======================


This add-on registers `Font Awesome <https://fontawesome.com/>`_ into Plone CSS registry.


Features
========

- Version of Font Awesome: 5.2.0.
- Includes a GenericSetup profile example for Replacing Plone's default icons with FontAwesome fonts.
- Includes a Example View working, go to http://site_url/@@example.collective.fontawesome


Translations
============

This product has been translated into

- Spanish (thanks, Leonardo J. Caballero G. aka macagua)


Installation
============

This add-on can be installed with the typical Plone add-on installation process. Please see the official
documentation_ for a description.

For Plone 5, import the "collective.fontawesome (Plone 5)" profile.

.. _documentation: https://docs.plone.org/manage/installing/installing_addons.html

.. warning:: ie7 support has been removed


How to use
==========

Since version 5, FontAwesome changed the way it works and the Free version includes 2 fonts : "Font Awesome 5 Free" and "Font Awesome 5 Brands".

https://fontawesome.com/how-to-use/on-the-web/setup/upgrading-from-version-4

Depending on the icon you want to use, you have to use the "fa" or "fab" class :

To use an icon from the "Font Awesome 5 Free" add class="fa fa-X", to use an icon from "Font Awesome 5 Brands", add class="fab fa-X" to your tag where X is the icon you want::

    <ul>
        <li class="fa fa-glass-martini">item 1</li>
        <li class="fa fa-music">item 2</li>
        <li class="fa fa-search">item 3</li>
    </ul>
    <ul>
        <li class="fab fa-angular">item 1</li>
        <li class="fab fa-apple">item 2</li>
        <li class="fab fa-avianex">item 3</li>
    </ul>


Or just use CSS for your class 'myclass'::

    .myclass:before {
        content: "\f000"; 
        font-family: "Font Awesome 5 Free";
        font-weight: 900;
        font-style: normal;
        font-weight: normal;
        text-decoration: inherit;
    }

Available CSS classes and values for the content attribute can be found in the `Font Awesome cheat sheet <http://fortawesome.github.io/Font-Awesome/cheatsheet/>`_ or in the `source code <https://github.com/FortAwesome/Font-Awesome/blob/master/css/font-awesome.css#L171>`_ (file: font-awesome.css#L171 at the time of writing).

Full list of useable icons may be found here : `Font Awesome free icons <https://fontawesome.com/icons?d=gallery&m=free>`_


An example page is available in the add-on, here is a screenshot:

.. image:: https://raw.githubusercontent.com/collective/collective.fontawesome/master/docs/screenshot.png

Replacing Plone's default icons with FontAwesome fonts
------------------------------------------------------

There is now a separate Generic Setup profile called ``replace-plone-icons`` which
will replace Plone's default icons (e.g. for content types and actions) with
Font Awesome icons.

**IMPORTANT:** You still need to install the ``default`` profile as well.

A ``replace-plone-icons`` profile example is available in the add-on, here is a screenshot:

.. image:: https://raw.githubusercontent.com/collective/collective.fontawesome/master/docs/screenshot1.png

Contribute
==========

- Issue Tracker: https://github.com/collective/collective.fontawesome/issues
- Source Code: https://github.com/collective/collective.fontawesome


Credits
=======

Companies
---------

* Makina-Corpus http://www.makina-corpus.com

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>
- Eric Bréhault, <ebrehault@gmail.com>
- Gauthier Bastien, <gauthier.bastien@imio.be>
- Leonardo J. Caballero G. aka macagua <leonardocaballero@gmail.com>


License
=======

- The Font Awesome font is licensed under the SIL Open Font License
  http://scripts.sil.org/OFL
- Font Awesome CSS, LESS, and SASS files are licensed under the MIT License
  https://opensource.org/licenses/mit-license.html
- The Font Awesome pictograms are licensed under the CC BY 3.0 License
  https://creativecommons.org/licenses/by/3.0/
- Attribution is no longer required in Font Awesome 3.0, but much appreciated:
  "Font Awesome by Dave Gandy - https://fontawesome.com/ "
