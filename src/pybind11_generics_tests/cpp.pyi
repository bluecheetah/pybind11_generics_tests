# -*- coding: utf-8 -*-
# Stubs for pybind11_generics_tests.cpp
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from __future__ import annotations

from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple, Union

def copy_list_from_iterable(obj: Iterable[str]) -> List[str]: ...
def copy_list_from_iterable_set(obj: Iterable[str]) -> List[str]: ...
def get_list(obj: TestList) -> List[int]: ...
def get_sequence(obj: TestSequence) -> List[int]: ...

class Animal:
    def __init__(self, arg0: str) -> None: ...
    def command(self, arg0: int) -> str: ...
    def go(self, arg0: int) -> str: ...

class Data:
    def __init__(self, arg0: int, arg1: str, arg2: List[int]) -> None: ...
    def a(self) -> int: ...
    def append(self, arg0: int) -> None: ...
    def b(self) -> str: ...
    def c(self) -> List[int]: ...

class Factory:
    def __init__(self, arg0: int, arg1: str, arg2: List[int]) -> None: ...
    def a(self) -> int: ...
    def b(self) -> str: ...
    def c(self) -> List[int]: ...
    def get_default_copy(self) -> object: ...
    def get_default_cpp(self) -> Data: ...
    def get_default_move(self) -> object: ...
    def get_default_move2(self) -> object: ...

class ListHolder:
    def __init__(self, arg0: TestList) -> None: ...
    def get_data(self) -> List[int]: ...
    def get_obj_ptr(self) -> TestList: ...
    def get_obj_ref(self) -> TestList: ...

class TestAnyList:
    def __init__(self, arg0: List[Any]) -> None: ...
    def get_data(self) -> List[Any]: ...

class TestAnyVal:
    def __init__(self, arg0: Any) -> None: ...
    def get_data(self) -> Any: ...

class TestDict:
    def __init__(self, arg0: Dict[str, int]) -> None: ...
    def get_data(self) -> Dict[str, int]: ...

class TestIterPair:
    def __init__(self, arg0: Iterator[Tuple[int, int]]) -> None: ...
    def get_data(self) -> List[Tuple[int, int]]: ...
    def get_iter(self) -> Iterator[Tuple[int, int]]: ...

class TestIterString:
    def __init__(self, arg0: Iterator[str]) -> None: ...
    def get_data(self) -> List[str]: ...
    def get_iter(self) -> Iterator[str]: ...

class TestIterablePair:
    def __init__(self, arg0: Iterable[Tuple[int, int]]) -> None: ...
    def get_data(self) -> List[Tuple[int, int]]: ...

class TestIterableString:
    def __init__(self, arg0: Iterable[str]) -> None: ...
    def get_data(self) -> List[str]: ...

class TestList:
    def __init__(self, arg0: List[int]) -> None: ...
    def get_data(self) -> List[int]: ...

class TestOptional:
    def __init__(self, arg0: Optional[List[int]]) -> None: ...
    def get_data(self) -> Optional[List[int]]: ...
    def has_value(self) -> bool: ...

class TestSequence:
    def __init__(self, arg0: Sequence[int]) -> None: ...
    def get_data(self) -> List[int]: ...

class TestTuplePair:
    def __init__(self, arg0: Tuple[int, float]) -> None: ...
    def get_data(self) -> Tuple[int, float]: ...

class TestTupleTuple:
    def __init__(self, arg0: Tuple[int, float, str]) -> None: ...
    def get_data(self) -> Tuple[int, float, str]: ...

class TestUnion:
    def __init__(self, arg0: Union[str, int, float]) -> None: ...
    def get_data(self) -> Union[str, int, float]: ...
    def index(self) -> int: ...