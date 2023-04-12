from datetime import datetime
from dataclasses import dataclass

import aiosqlite

import config


def _chanks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        

@dataclass
class Book:
    id: int
    name: str
    category_name: str
    read_start: datetime
    read_finish: datetime


@dataclass
class Category:
    id: int
    name: str
    books: list[Book]


async def get_all_books(chank_size: int) -> list[Book]:
    books = []
    async with aiosqlite.connect(config.SQLITEDB_FILE) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """select b.id as book_id,
            b.name as book_name,
            c.id as category_id,
            c.name as category_name,
            b.read_start,
            b.read_finish from book b
            left join book_category c
            on c."ordering"=b.category_id order by c."ordering", b."ordering"; """
        ) as cursor:
            async for row in cursor:
                books.append(Book(
                    id=row["book_id"],
                    name=row["book_name"],
                    category_name=["category_name"],
                    read_start=row["read_start"],
                    read_finish=row["read_finish"]
                ))
    return _chanks(books, chank_size)