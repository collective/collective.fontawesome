Introduction
============

This addon register fontawesome into Plone CSS registry.

version of font awesome: 3.0.2

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

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to

If you need ie7 support in your project you should activate the ie7 stylesheet.

How to use
==========

To use an icon you can add 'icon-X' to your tag where X is the icon you want::


    <ul>
        <li class="icon-glass">item 1</li>
        <li class="icon-music">item 2</li>
        <li class="icon-search">item 3</li>
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


Credits
=======

Companies
---------

* Makina-Corpus http://www.makina-corpus.com

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>
