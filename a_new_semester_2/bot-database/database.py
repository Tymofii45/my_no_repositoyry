import asyncpg
import asyncio

class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                user= "timofijmironov"
                database= "neondb"
                password="I9ciNCZ3OqRu"
                host="ep-gentle-wood-972457.eu-central-1.aws.neon.tech"
                port="5432"
            )

        )

    
    async def register_student(self, name, age, email):
        sql = f"""
        INSERT INTO students (name, age, email) VALUES ("{name}", "{age}", "{email}")
        """
        await self.pool.execute(sql)

    async def check_user(self, email):
        sql = f"""
        SELECT * FROM students WHERE email = "{email}"
        """
        result = await self.pool.fetchrow(sql)
        return result
    