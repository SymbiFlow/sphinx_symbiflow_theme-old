#!/usr/bin/env python3
# -*- coding: utf-8 -*-\
import sys,os

pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(pardir)
sys.path.append(pardir)

from sphinx_symbiflow_theme  import __version__

source_suffix = '.rst'
master_doc = 'index'

version = __version__
release = __version__


project = 'SymbiFlow Theme'
copyright = '2020, The SymbiFlow Authors'
author = 'The SymbiFlow Authors'

language = 'en'

templates_path = ['_templates']
html_sidebars = {
   '**': ['globaltoc.html']
}
html_favicon = '_static/favicon.ico'

html_theme = 'sphinx_symbiflow_theme'
html_theme_path = ['../']

html_theme_options = {
    # Specify a list of menu in Header.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean, 'icon name')
    #
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    #
    # Fourth argument:
    # Specify the icon name.
    # For details see link.
    # https://material.io/icons/
    'header_links' : [
       ('Home', 'index', False, 'home'),
       ("ExternalLink", "http://example.com", True, 'launch'),
       ("NoIconLink", "http://example.com", True, '')
    ],

    # Customize css colors.
    # For details see link.
    # https://getmdl.io/customize/index.html
    #
    # Values: amber, blue, brown, cyan deep_orange, deep_purple, green, grey, indigo, light_blue,
    #         light_green, lime, orange, pink, purple, red, teal, yellow(Default: indigo)
    'primary_color': 'deep_purple',
    # Values: Same as primary_color. (Default: pink)
    'accent_color': 'purple',

    # Customize layout.
    # For details see link.
    # https://getmdl.io/components/index.html#layout-section
    'fixed_drawer': True,
    'fixed_header': True,
    'header_waterfall': True,
    'header_scroll': False,

    # Render title in header.
    # Values: True, False (Default: False)
    'show_header_title': False,
    # Render title in drawer.
    # Values: True, False (Default: True)
    'show_drawer_title': True,
    # Render footer.
    # Values: True, False (Default: True)
    'show_footer': True,

    # Show SymbiFlow-related links in header and footer (e.g. Mailing List, IRC, Slack)
    # Values: True, False (Default: False)
    'hide_symbiflow_links': False,
    # Link to GitHub repository
    'github_url': 'https://github.com/SymbiFlow/sphinx_symbiflow_theme',
    # Link to LICENSE in GitHub repository
    'license_url': 'https://github.com/SymbiFlow/sphinx_symbiflow_theme/blob/master/LICENSE'
}

html_show_sourcelink = True

rst_prolog= u"""
    .. |project| replace:: Sphinx Material Design Theme
"""
