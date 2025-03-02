from dataclasses import dataclass
from abc import ABC, abstractmethod

from database.repositories.sessions.schemas import AddSessionSchema


@dataclass
class BaseSessionsRepository(ABC):
    @abstractmethod
    async def create_session(self, session: AddSessionSchema, connection) -> str:
        ...

    @abstractmethod
    async def get_user_id_by_session_id(self, session_id: str, connection) -> int:
        ...

    @abstractmethod
    async def get_all_sessions_by_user_id(self, user_id: int, connection) -> list[str]:
        ...

    @abstractmethod
    async def ban_session_by_session_id(self, session_id: str, connection):
        ...

    @abstractmethod
    async def ban_all_users_sessions_by_user_id(self, user_id: int, connection):
        ...
