# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import os
import sys
import glob
import builtins
import inspect
import importlib
try:
    import pprintpp as pprint
except ImportError:
    import pprint

os.environ['XONSH_DEBUG'] = '1'

sys.path.insert(0, '..')

from xonsh.environ import Env
from xonsh.commands_cache import CommandsCache

sys.path.insert(0, os.path.dirname(__file__))

from rever import __version__ as REVER_VERSION
from rever import environ
from rever.activity import Activity


def setup(sphinx):
    from xonsh.pyghooks import XonshConsoleLexer
    sphinx.add_lexer("xonshcon", XonshConsoleLexer())


# -- General configuration -----------------------------------------------------

# Documentation is being built on readthedocs, this will be true.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.imgmath',
              'sphinx.ext.inheritance_diagram', 'sphinx.ext.viewcode',
              #'sphinx.ext.autosummary',
              'numpydoc',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'rever'
copyright = u'2017, Anthony Scopatz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = REVER_VERSION.rsplit('.',1)[0]

# The full version, including alpha/beta/rc tags.
release = REVER_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
exclude_patterns = ['api/blank.rst', 'api/activities/blank.rst']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
#pygments_style = 'friendly'
#pygments_style = 'bw'
#pygments_style = 'fruity'
#pygments_style = 'manni'
#pygments_style = 'tango'
#pygments_style = 'pastie'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['rever.']


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
#html_theme = 'altered_nature'
#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
if not on_rtd:
    import cloud_sptheme as csp

    html_theme = 'cloud'

    html_theme_options = {
        'max_width': '1250px',
        'minimal_width': '700px',
        'relbarbgcolor': '#000000',
        'footerbgcolor': '#FFFFE7',
        'sidebarwidth': '322px',
        'sidebarbgcolor': '#e7e7ff',
        #'googleanalytics_id': 'UA-41934829-1',
        'stickysidebar': False,
        'highlighttoc': False,
        'externalrefs': False,
        'collapsiblesidebar': True,
        'default_layout_text_size': "100%",  # prevents division by zero error
        }

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = ["_theme", csp.get_theme_dir()]
    templates_path = ["_templates_overwrite"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/longship-256.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/longship.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = "numpy_friendly.css"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'reverdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'rever.tex', u'rever documentation',
   u'Anthony Scopatz', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

#Autodocumentation Flags
autodoc_member_order = "groupwise"
autoclass_content = "both"
autosummary_generate = []

# Prevent numpy from making silly tables
numpydoc_show_class_members = False


#
# Auto-generate some docs
#

def make_envvars():
    env = Env()
    vars = sorted([k for k in environ.ENVVARS.keys() if isinstance(k, str)])
    s = ('.. list-table::\n'
         '    :header-rows: 0\n\n')
    table = []
    ncol = 3
    row = '    {0} - :ref:`${1} <{2}>`'
    for i, var in enumerate(vars):
        star = '*' if i%ncol == 0 else ' '
        table.append(row.format(star, var, var.lower()))
    table.extend(['      -']*((ncol - len(vars)%ncol)%ncol))
    s += '\n'.join(table) + '\n\n'
    s += ('Listing\n'
          '-------\n\n')
    sec = ('.. _{low}:\n\n'
           '{title}\n'
           '{under}\n'
           '{docstr}\n\n'
           '**configurable:** {configurable}\n\n'
           '**default:** {default}\n\n'
           '**store_as_str:** {store_as_str}\n\n'
           '-------\n\n')
    for var in vars:
        title = '$' + var
        under = '.' * len(title)
        vd = env.get_docs(var)
        s += sec.format(low=var.lower(), title=title, under=under,
                        docstr=vd.docstr, configurable=vd.configurable,
                        default=vd.default, store_as_str=vd.store_as_str)
    s = s[:-9]
    fname = os.path.join(os.path.dirname(__file__), 'envvarsbody')
    with open(fname, 'w') as f:
        f.write(s)


def find_activities():
    import rever.activities as actmod
    fname = inspect.getfile(actmod)
    dname = os.path.dirname(fname)
    actfiles = glob.glob(os.path.join(dname, '*.xsh'))
    actmodnames = map(os.path.basename, actfiles)
    actmodnames = map(os.path.splitext, actmodnames)
    actmodnames = [x[0] for x in actmodnames if not x[0].startswith('_')]
    acts = {}
    for actmodname in actmodnames:
        fullmodname = 'rever.activities.' + actmodname
        mod = importlib.import_module(fullmodname)
        for var, obj in vars(mod).items():
            if not inspect.isclass(obj) or not issubclass(obj, Activity):
                continue
            acts[var] = (fullmodname, obj)
    acts.pop('Activity')
    acts.pop('DockerActivity')
    return acts


def make_activity_rever_xsh_example(act):
    if inspect.isclass(act):
        try:
            act = act()
        except TypeError:
            return ''
    s = ("This activity's defaults are equivalent to the following "
         "``rever.xsh`` file:\n\n"
         ".. code-block:: xonsh\n\n")
    s += "    $ACTIVITIES = ['" + act.name + "']\n\n"
    t = '    ${envvar} = {default}\n'
    env_names = act.env_names
    sig = inspect.signature(act.func)
    empty = inspect.Parameter.empty
    for kwarg, param in sig.parameters.items():
        envvar = env_names[kwarg]
        if param.default is empty:
            default = "'<no default value>'"
        else:
            default = pprint.pformat(param.default)
            default = '\n    '.join(default.splitlines())
        s += t.format(envvar=envvar, default=default)
    s += '\n\n'
    return s


def make_activities():
    acts = find_activities()
    vars = sorted(acts.keys())
    s = ('.. list-table::\n'
         '    :widths: auto\n'
         '    :header-rows: 0\n\n')
    table = []
    row = ('    * - :ref:`{var} <{low}>`\n'
           '      - {short}\n')
    for var in vars:
        docstr = inspect.getdoc(acts[var][1])
        short = docstr[:docstr.find('\n\n')]
        short = short.replace('\n', ' ')
        table.append(row.format(var=var, low=var.lower(), short=short))
    s += '\n'.join(table) + '\n\n'
    s += ('Listing\n'
          '-------\n\n')
    sec = ('.. _{low}:\n\n'
           '{var}\n'
           '{under}\n'
           'The {var} activity class is available via:\n\n'
           '.. code-block:: python\n\n'
           '    from {fullmodname} import {var}\n\n'
           '{docstr}\n\n'
           '{rever_xsh}\n\n'
           '-------\n\n')
    for var in vars:
        title = var
        under = '.' * len(title)
        act = acts[var][1]
        docstr = inspect.getdoc(act)
        rever_xsh = make_activity_rever_xsh_example(act)
        s += sec.format(var=var, low=var.lower(), under=under,
                        docstr=docstr, fullmodname=acts[var][0],
                        rever_xsh=rever_xsh)
    s = s[:-9]
    fname = os.path.join(os.path.dirname(__file__), 'activitiesbody')
    with open(fname, 'w') as f:
        f.write(s)


with environ.context():
    make_activities()
    make_envvars()

builtins.__xonsh__.history = None
builtins.__xonsh__.env = {}
builtins.__xonsh__.commands_cache = CommandsCache()
