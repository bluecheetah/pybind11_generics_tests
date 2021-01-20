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

from typing import Any

import pytest

import pybind11_generics_tests.cpp as pyg_test

from .util import do_constructor_test, do_doc_test, do_error_test

test_data = [
    (pyg_test.TestAnyList, []),
    (pyg_test.TestAnyList, [1, 3, "hi", 7.5, [1, "hi"]]),
    (pyg_test.TestAnyList, [2, 4, "hi"]),
    (pyg_test.TestAnyVal, "foobar"),
    (pyg_test.TestAnyVal, 17),
    (pyg_test.TestAnyVal, [2.6, 7, "bye"]),
]

fail_data = [
    (pyg_test.TestAnyList, TypeError, "foo"),
    (pyg_test.TestAnyList, TypeError, 3),
]

doc_data = [
    (pyg_test.TestAnyList, "List[Any]"),
    (pyg_test.TestAnyVal, "Any"),
]


@pytest.mark.parametrize(("cls", "data"), test_data)
def test_constructor(cls, data: Any) -> None:
    """Check object is constructed properly."""
    do_constructor_test(cls, data)


@pytest.mark.parametrize(("cls", "err", "data"), fail_data)
def test_error(cls, err, data):
    """Check object errors when input has wrong data type."""
    do_error_test(cls, err, data)


@pytest.mark.parametrize(("cls", "type_str"), doc_data)
def test_doc(cls, type_str):
    """Check object has correct doc string."""
    do_doc_test(cls, type_str)
