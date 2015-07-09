Introduction
============

This addon register fontawesome into Plone CSS registry.

version of font awesome: 4.3.0

License
=======

- The Font Awesome font is licensed under the SIL Open Font License
  http://scripts.sil.org/OFL
- Font Awesome CSS, LESS, and SASS files are licensed under the MIT License
  http://opensource.org/licenses/mit-license.html
- The Font Awesome pictograms are licensed under the CC BY 3.0 License
  http://creativecommons.org/licenses/by/3.0/
- Attribution is no longer required in Font Awesome 3.0, but much appreciated:
  "Font Awesome by Dave Gandy - http://fortawesome.github.com/Font-Awesome "

How to install
==============

This addon can be installed has any other addons. please follow official
documentation_

For Plone 5, import the "collective.fontawesome (Plone 5)" profile.

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to

.. warning:: ie7 support has ben removed

How to use
==========

To use an icon you can add 'fa fa-X' to your tag where X is the icon you want::


    <ul>
        <li class="fa fa-glass">item 1</li>
        <li class="fa fa-music">item 2</li>
        <li class="fa fa-search">item 3</li>
    </ul>

Or just use CSS for your class 'myclass'::

    .myclass:before {
        content: "\f000"; 
        font-family: FontAwesome;
        font-style: normal;
        font-weight: normal;
        text-decoration: inherit;
    }

to know more on the content to use or class to use you can look at the code
https://github.com/FortAwesome/Font-Awesome/blob/master/docs/assets/css/font-awesome.css#L272

An example page is avaible in the addon, here is a screenshot:

.. image:: http://plone.org/products/collective.fontawesome/screenshot

Replacing Plone's default icons with FontAwesome fonts
======================================================

There is now a separate Generic Setup profile called ``replace-plone-icons`` which
will replace Plone's default icons (e.g. for content types and actions) with
FontAwesome fonts.

IMPORTANT: You still need to install the ``default`` profile as well.

Credits
=======

Companies
---------

* Makina-Corpus http://www.makina-corpus.com

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>
- Eric Bréhault, <ebrehault@gmail.com>
