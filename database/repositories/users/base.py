from dataclasses import dataclass
from abc import ABC, abstractmethod

from database.repositories.users.schemas import AddUserSchema


@dataclass
class BaseUsersRepository(ABC):
    @abstractmethod
    async def create_user(self, user: AddUserSchema, connection):
        ...

    @abstractmethod
    async def get_user_by_id(self, user_id: int, connection):
        ...

    @abstractmethod
    async def get_user_by_login(self, login: str, connection):
        ...

    @abstractmethod
    async def get_user_by_email(self, email: str, connection):
        ...

    @abstractmethod
    async def get_user_balance_by_user_id(self, user_id: int, connection) -> float:
        ...

    @abstractmethod
    async def increase_balance_by_user_id(self, value: float, user_id: int, connection):
        ...

    @abstractmethod
    async def decrease_balance_by_user_id(self, value: float, user_id: int, connection):
        ...
