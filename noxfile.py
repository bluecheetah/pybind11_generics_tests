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

import nox
from nox.sessions import Session

VENV_BACKEND = "virtualenv"
VENV_PARAMS = ["--system-site-packages"]


@nox.session(venv_backend=VENV_BACKEND, venv_params=VENV_PARAMS)
def test(session: Session) -> None:
    session.install("--no-build-isolation", ".", env={"PYBIND11EXT_BUILD_PARALLEL": "0"})
    session.install("--ignore-installed", "pytest")
    session.run("pytest", "-v", "tests")
