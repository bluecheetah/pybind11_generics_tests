# SPDX-License-Identifier: Apache-2.0
# Copyright 2021 Blue Cheetah Analog Design Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import shutil
from pathlib import Path

import nox
from nox.sessions import Session

VENV_BACKEND = "virtualenv"
VENV_PARAMS = ["--system-site-packages"]


def incremental_install(session: Session) -> None:
    # NOTE: before https://github.com/pypa/pip/pull/9091 is merged, we install using setuptools
    # So we get incremental build
    wheel_dir = Path("_build/dist")
    shutil.rmtree(wheel_dir, ignore_errors=True)
    session.run_always("python", "setup.py", "bdist_wheel")
    if not wheel_dir.is_dir():
        raise ValueError(f"Cannot find wheel directory: {wheel_dir}")
    children = list(wheel_dir.iterdir())
    if len(children) != 1:
        raise ValueError(f"More than one file in wheel directory: {wheel_dir}")
    wheel_file = children[0]
    if wheel_file.suffix != ".whl":
        raise ValueError(f"Invalid wheel file: {wheel_file}")
    session.install(str(wheel_file))


@nox.session(venv_backend=VENV_BACKEND, venv_params=VENV_PARAMS)
def test(session: Session) -> None:
    session.install("--ignore-installed", "pytest")
    incremental_install(session)
    session.run("pytest", "-v", "tests")
