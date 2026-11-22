
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Provides a database session for a FastAPI request.
    The session is closed after the request finishes.
    """

    async with AsyncSessionLocal() as session:
        yield session
