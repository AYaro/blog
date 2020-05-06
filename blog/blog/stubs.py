from typing import Iterator, TypeVar, Generic

from django.db.models import QuerySet

_Z = TypeVar("_Z")


class QueryType(Generic[_Z], QuerySet):
    def __iter__(self) -> Iterator[_Z]: ...
