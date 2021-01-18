#   Copyright 2018 Eric Chang
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.#

import pytest

import pyg_test

from .util import do_constructor_test, do_error_test, do_doc_test

test_data = [
    (pyg_test.TestUnion, 1),
    (pyg_test.TestUnion, 2.5),
    (pyg_test.TestUnion, "foobar"),
]

fail_data = [
    (pyg_test.TestUnion, TypeError, []),
    (pyg_test.TestUnion, TypeError, ["hi"]),
    (pyg_test.TestUnion, TypeError, (1,)),
    (pyg_test.TestUnion, TypeError, {3.5: 4.5}),
]

doc_data = [
    (pyg_test.TestUnion, "Union[str, int, float]"),
]

test_index_data = [
    (pyg_test.TestUnion, 13, 1),
    (pyg_test.TestUnion, 17.624, 2),
    (pyg_test.TestUnion, "", 0),
]


@pytest.mark.parametrize("cls,data", test_data)
def test_constructor(cls, data):
    """Check object is constructed properly."""
    do_constructor_test(cls, data)


@pytest.mark.parametrize("cls,err,data", fail_data)
def test_error(cls, err, data):
    """Check object errors when input has wrong data type."""
    do_error_test(cls, err, data)


@pytest.mark.parametrize("cls,type_str", doc_data)
def test_doc(cls, type_str):
    """Check object has correct doc string."""
    do_doc_test(cls, type_str)


@pytest.mark.parametrize("cls,data,index", test_index_data)
def test_index(cls, data, index):
    """Check object is constructed properly."""
    obj = cls(data)
    assert obj.get_data() == data
    assert obj.index() == index
