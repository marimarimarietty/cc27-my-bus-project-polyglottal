from sqlalchemy.ext.asyncio import AsyncSession
from api.models.notifications import User


def seed(db: AsyncSession):
    user = User(id=1, name="Marie Matsumoto", email="marie@example.com", password="1234")

    db.add(user)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
