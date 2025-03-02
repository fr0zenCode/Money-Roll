from dataclasses import dataclass
from abc import ABC, abstractmethod

from database.repositories.passwords.schemas import PasswordSchema, AddPasswordSchema


@dataclass
class BasePasswordsRepository(ABC):
    @abstractmethod
    async def add_password(self, password: AddPasswordSchema, connection):
        ...

    @abstractmethod
    async def change_password_by_user_id(self, new_password: AddPasswordSchema, connection):
        ...

    @abstractmethod
    async def get_password_by_user_id(self, user_id: int, connection) -> PasswordSchema:
        ...
