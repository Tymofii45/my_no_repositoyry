import asyncpg
import asyncio


class Database:
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                user='Yaroslav702',
                database='neondb',
                password='ENCGJwY71FTS',
                host='ep-young-dust-974138.eu-central-1.aws.neon.tech',
                port='5432'
            )
        )

    async def register_user(self, first_name, last_name, username, telegram_id):
        sql = f"""
        INSERT INTO telegram_users (first_name, last_name, username, telegram_id) 
        VALUES ('{first_name}', '{last_name}', '{username}', '{telegram_id})
        """
        await self.pool.execute(sql)

    async def check_user(self, telegram_id):
        sql = f"""
        SELECT * FROM telegram_users WHERE telegram_id = '{telegram_id}'
        """
        result = await self.pool.fetchrow(sql)
        return result