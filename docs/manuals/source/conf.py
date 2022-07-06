#!/usr/bin/env python3
#   BAREOS - Backup Archiving REcovery Open Sourced
#
#   Copyright (C) 2018-2021 Bareos GmbH & Co. KG
#
#   This program is Free Software; you can redistribute it and/or
#   modify it under the terms of version three of the GNU Affero General Public
#   License as published by the Free Software Foundation and included
#   in the file LICENSE.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
#   02110-1301, USA.

# -*- coding: utf-8 -*-
#
# Bareos Main Reference documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 21 16:41:30 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../../../python-bareos/"))
sys.path.insert(0, os.path.abspath("./_extensions"))

import datetime

# -- General configuration ------------------------------------------------

# Substitutions have been CamelCase in the past.
# Now they are all lowercase.
# CamelCase version can be removed,
# when they are no longer required.

# about <isonum.txt>, see
# http://docutils.sourceforge.net/docs/ref/rst/definitions.html#substitution-definitions
# http://docutils.sourceforge.net/docutils/parsers/rst/include/isonum.txt
rst_epilog = """
.. include:: <isonum.txt>
.. |checkmark| unicode:: U+2713

.. |configCharsToQuote| replace:: ``&<>()@^|``

.. |bareosFd| replace:: Bareos File Daemon
.. |fd| replace:: Bareos File Daemon
.. |bareosSd| replace:: Bareos Storage Daemon
.. |sd| replace:: Bareos Storage Daemon
.. |bareosDir| replace:: Bareos Director
.. |dir| replace:: Bareos Director
.. |bconsole| replace:: Bareos Console
.. |bareosTraymonitor| replace:: Bareos Traymonitor
.. |traymonitor| replace:: Bareos Traymonitor
.. |bareosWebui| replace:: Bareos Webui
.. |webui| replace:: Bareos WebUI
.. |mariadb| replace:: MariaDB
.. |mysql| replace:: MySQL
.. |postgresql| replace:: PostgreSQL
.. |sqlite| replace:: Sqlite
.. |vmware| replace:: VMware
.. |vsphere| replace:: VMware vSphere

.. |ndmpbareos| replace:: :ref:`section-NdmpBareos`
.. |ndmpnative| replace:: :ref:`section-NdmpNative`

"""


# If your documentation needs a minimal Sphinx version, state it here.
#
# autosummary :recursive: requires Sphinx >= 3.1.
# For now, we use a workaround to use autosummary without :recursive:.
# needs_sphinx = '3.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "bareos-ext",
    "limitation",
    "sphinx_issues",
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",  # Link to other project's documentation (see mapping below)
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",  # Add a link to the Python source code for classes, functions etc.
    "sphinxcontrib.actdiag",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.nwdiag",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.seqdiag",
    "crate.sphinx.csv",
    "m2r2",
    "sphinx_copybutton",
]

#    'limitation',
# extensions.append('limitation')

#
# sphinx_issues
#
issues_github_path = "bareos/bareos"
# issues_uri = 'https://bugs.bareos.org/view.php?id={issue}'
# issues_pr_uri = 'https://github.com/bareos/bareos/pull/{pr}'

#
# sphinx.ext.autodoc
#

# python:
# Both the class and the __init__ method’s docstring are concatenated and inserted.
autoclass_content = "both"

#
# sphinx.ext.autosectionlabel
#

# True to prefix each section label with the name of the document it is in, followed by a colon.
# For example, index:Introduction for a section called Introduction that appears in document index.rst.
# Useful for avoiding ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True

#
# sphinx.ext.autosummary
#

autosummary_generate = True  # Turn on sphinx.ext.autosummary
# autosummary_imported_members = True
# autosummary_generate_overwrite = True

#
# sphinx.ext.intersphinx
#

# Mappings for sphinx.ext.intersphinx. Projects have to have Sphinx-generated doc! (.inv file)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Bareos Documentation"
copyright = str(datetime.datetime.now().year) + " Bareos GmbH & Co. KG and others."
author = "Bareos GmbH & Co. KG"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

#
# sphinx.ext.todo
#

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# html_theme_options = {
#    'canonical_url': '',
#    'analytics_id': '',
#    'logo_only': False,
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    # Toc options
#    'collapse_navigation': False,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
# }

# Enable link of 'View page source'
# html_show_sourcelink = False
# Add 'Edit on Github' link instead of 'View page source'
# reference:https://docs.readthedocs.io/en/latest/vcs.html
html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    "display_github": True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}
    # /{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    # https://github.com/runawayhorse001/SphinxGithub/blob/master/doc/index.rst
    "github_user": "bareos",
    "github_repo": "bareos",
    "conf_py_path": "/docs/manuals/source/",
    "READTHEDOCS": True,
    "commit": datetime.date.today().strftime("%B %d, %Y"),
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "BareosDocumentation"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "BareosMainReference.tex",
        "Bareos Main Reference Documentation",
        "Bareos GmbH & Co. KG",
        "manual",
    )
]

# -- Options for the linkcheck builder ------------------------------------

linkcheck_allowed_redirects = {
    # All HTTP redirections from the source URI to the canonical URI will be treated as "working".
    r'https://bareos\.org/.*': r'https://bareos\.com/.*',
    r'http://www\.bareos\.org': r'https://www\.bareos\.com/.*',
    r'http://www\.bareos\.org/.*': r'https://www\.bareos\.com/.*',
    r'https://www\.bareos\.org/.*': r'https://www\.bareos\.com/.*',
    r'https://bugs\.bareos\.org/.*': r'https://bugs\.bareos\.org/my_view_page\.php',
    r'https://download\.bareos\.org': r'https://download\.bareos\.org/bareos',
    r'https://download\.bareos\.com': r'https://download\.bareos\.com/bareos',
}
linkcheck_request_headers = {
#    "https://www.sphinx-doc.org/": {
#        "Accept": "text/html",
#        "Accept-Encoding": "utf-8",
#    },
    "*": {
        "Accept": "text/html,application/xhtml+xml",
    }
}
linkcheck_retries = 2   # default 1
linkcheck_timeout = 10  # default 300
linkcheck_workers = 2   # default 5
linkcheck_anchors = True
linkcheck_ignore = [
    r'\.\./*',
    r'http://localhost:*/',
    r'https://\w+:\d+/bareos-webui/',
    'https://UCS_SERVER/bareos-webui/',
    'http://HOSTNAME/bareos-webui',
    'http://localhost:9100',
    'http://bareos:9100',
    'http://bucket.s3_server/object',
    'http://127.0.0.1:8000/docs',
    'http://127.0.0.1:8000/redoc',
    'https://pubs.vmware.com/vsphere-55/topic/com.vmware.vsphere.security.doc/*',
    r'https://github.com/bareos/bareos/pull/\d+',
    'https://www.sphinx-doc.org/en/1.7/intro.html#'
]
#linkcheck_auth = [
#  ('https://foo\.yourcompany\.com/.+', ('johndoe', 'secret')),
#  ('https://.+\.yourcompany\.com/.+', HTTPDigestAuth(...)),
#]
linkcheck_rate_limit_timeout = 300.00
# ignore all links in documents located in a subfolder named 'legacy'
#linkcheck_exclude_documents = [r'.*/legacy/.*']

# -- Options for manual page output ---------------------------------------

man_bareos_dbcopy = "man/bareos-dbcopy"

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        man_bareos_dbcopy,
        "bareos-dbcopy",
        "Copy the Bareos catalog database between catalog backends",
        [author],
        8,
    )
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "BareosDocumentation",
        "Bareos Documentation",
        author,
        "BareosDocumenation",
        "One line description of project.",
        "Miscellaneous",
    )
]


import re

# settings for sphinxcontrib-versioning
scv_whitelist_branches = (
    re.compile(r"^master$"),
    re.compile(r"^bareos-19.2$"),
    re.compile(r"^bareos-2.$"),
)
scv_whitelist_tags = (re.compile(r"^not-exisiting-tag$"),)
scv_show_banner = True
scv_priority = "branches"
scv_root_ref = "bareos-21"
scv_banner_main_ref = "bareos-21"


plantuml_output_format = "svg_img"


#
# code-block highlighting
#
from sphinx.highlighting import lexers
from bareos_lexers import *

lexers["bareosconfig"] = BareosConfigLexer()
lexers["bconsole"] = BareosConsoleLexer()
lexers["bareoslog"] = BareosLogLexer()
lexers["bareosmessage"] = BareosMessageLexer()


# generate rst.inc files from json files
import subprocess
import os

os.chdir("..")
subprocess.call(["pwd"])
subprocess.check_call(
    [
        "scripts/generate-resource-descriptions.py",
        "--sphinx",
        "source/include/autogenerated/bareos-dir-config-schema.json",
    ]
)
subprocess.check_call(
    [
        "scripts/generate-resource-descriptions.py",
        "--sphinx",
        "source/include/autogenerated/bareos-sd-config-schema.json",
    ]
)
subprocess.check_call(
    [
        "scripts/generate-resource-descriptions.py",
        "--sphinx",
        "source/include/autogenerated/bareos-fd-config-schema.json",
    ]
)
subprocess.check_call(
    [
        "scripts/generate-resource-descriptions.py",
        "--sphinx",
        "source/include/autogenerated/bconsole-config-schema.json",
    ]
)
subprocess.check_call(
    [
        "scripts/generate-resource-descriptions.py",
        "--sphinx",
        "source/include/autogenerated/bareos-tray-monitor-config-schema.json",
    ]
)
subprocess.check_call(
    "scripts/generate-bareos-package-info.py --out source/include/autogenerated/ source/data/bareos-*-packages.json",
    shell=True,
)
