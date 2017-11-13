"""Docker Tests"""
import os
import builtins
import tempfile

import pytest

from rever import environ
from rever.docker import apt_deps, conda_deps, pip_deps, make_base_dockerfile


@pytest.fixture
def dockerenv(request):
    with environ.context():
        env = builtins.__xonsh_env__
        yield env


@pytest.mark.parametrize('deps, exp', [
    ([], ''),
    (['dep1', 'dep0'],
"""RUN apt-get -y update && \\
    apt-get install -y --fix-missing \\
        dep0 dep1 && \\
    apt-get clean -y

"""),
])
def test_apt_deps(dockerenv, deps, exp):
    obs = apt_deps(deps)
    assert exp == obs



@pytest.mark.parametrize('deps, channels, exp', [
    ([], [], ''),
    ([], None, ''),
    ([], ['conda-forge'], ''),
    (['dep1', 'dep0'], [],
"""RUN conda config --set always_yes yes && \\
    conda install \\
        dep0 dep1 && \\
    conda clean --all && \\
    conda info

"""),
    (['dep1', 'dep0'], ['conda-forge', 'my-channel'],
"""RUN conda config --set always_yes yes && \\
    conda config --add channels my-channel && \\
    conda config --add channels conda-forge && \\
    conda install \\
        dep0 dep1 && \\
    conda clean --all && \\
    conda info

"""),
])
def test_conda_deps(dockerenv, deps, channels, exp):
    obs = conda_deps(deps, channels)
    assert exp == obs


@pytest.mark.parametrize('deps, reqs, exp', [
    ([], [], ''),
    (['dep1', 'dep0'], [],
"""RUN pip install \\
    dep1 dep0

"""),
    ([], ['req1', 'req0'],
"""RUN pip install \\
    -r req1 -r req0

"""),
    (['dep1', 'dep0'], ['req1', 'req0'],
"""RUN pip install \\
    -r req1 -r req0 dep1 dep0

"""),
])
def test_pip_deps(dockerenv, deps, reqs, exp):
    obs = pip_deps(deps, reqs)
    assert exp == obs


EXP_BASE = """FROM zappa/project

WORKDIR /root

RUN apt-get -y update && \\
    apt-get install -y --fix-missing \\
        dep0 dep1 && \\
    apt-get clean -y

RUN conda config --set always_yes yes && \\
    conda config --add channels my-channel && \\
    conda config --add channels conda-forge && \\
    conda install \\
        dep0 dep1 && \\
    conda clean --all && \\
    conda info

RUN pip install \\
    -r req1 -r req0 dep1 dep0


"""


def test_make_base_dockerfile(dockerenv):
    obs = make_base_dockerfile(base_from='zappa/project',
                               apt=['dep1', 'dep0'],
                               conda=['dep1', 'dep0'],
                               conda_channels=['conda-forge', 'my-channel'],
                               pip=['dep1', 'dep0'],
                               pip_requirements=['req1', 'req0'])
    assert EXP_BASE == obs

