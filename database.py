import asyncpg
import asyncio

async def create_database(conn):
    try:
        conn = await asyncpg.connect(user='postgres', password='0212er', host='localhost', port='5432', database='postgres')
        try:
            await conn.execute('''
                CREATE DATABASE perfum_database''')
            print("База данных успешно создана.")
        except asyncpg.DuplicateDatabaseError:
            print("База данных уже существует.")
        except Exception as e:
            print(f"Произошла ошибка при создании базы данных: {e}")
        finally:
            await conn.close()
    except Exception as e:
        print(f"Ошибка подключения: {e}")
async def create_tables(conn):
    conn = await asyncpg.connect(user='postgres', password='0212er', host='localhost', port='5432', database='perfum_database')
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS genders (
                gender_id SERIAL PRIMARY KEY, 
                gender_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS seasons (
                season_id SERIAL PRIMARY KEY, 
                season_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS price_ranges (
                price_range_id SERIAL PRIMARY KEY, 
                price_range_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS occasions (
                occasion_id SERIAL PRIMARY KEY, 
                occasion_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS fragrance_groups (
                group_id SERIAL PRIMARY KEY,
                group_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                note_id SERIAL PRIMARY KEY, 
                note_name VARCHAR(100) UNIQUE NOT NULL
            )''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS scents (
                scent_id SERIAL PRIMARY KEY, 
                name VARCHAR(100) UNIQUE NOT NULL,
                gender_id INTEGER, 
                season_id INTEGER, 
                price_range_id INTEGER,
                occasion_id INTEGER,
                group_id INTEGER,
                note_id INTEGER,
                FOREIGN KEY (gender_id) REFERENCES genders(gender_id),  
                FOREIGN KEY (season_id) REFERENCES seasons(season_id),
                FOREIGN KEY (price_range_id) REFERENCES price_ranges(price_range_id),
                FOREIGN KEY (occasion_id) REFERENCES occasions(occasion_id),
                FOREIGN KEY (group_id) REFERENCES fragrance_groups(group_id),
                FOREIGN KEY (note_id) REFERENCES notes(note_id)
            )''')
    except asyncpg.DuplicateTableError:
            print("уже существует.")
    except Exception as e:
            print(f"Произошла ошибка{e}")
    finally:
        await conn.close()
async def insert_tables(conn):
    conn = await asyncpg.connect(user='postgres', password='0212er', host='localhost', port='5432', database='perfum_database')
    try:
        await conn.execute("INSERT INTO genders (gender_name) VALUES ('мужской'), ('женский'), ('унисекс') ON CONFLICT (gender_name) DO NOTHING;")
        await conn.execute("INSERT INTO seasons (season_name) VALUES ('зима'), ('весна'), ('лето'), ('осень') ON CONFLICT (season_name) DO NOTHING;")
        await conn.execute("INSERT INTO price_ranges (price_range_name) VALUES ('до 5000'), ('от 5000 до 10000'), ('от 10000 до 15000'), ('от 15000 и более') ON CONFLICT (price_range_name) DO NOTHING;")
        await conn.execute("INSERT INTO occasions (occasion_name) VALUES ('повседневный'), ('вечерний'), ('спортивный') ON CONFLICT (occasion_name) DO NOTHING;")
        await conn.execute("INSERT INTO fragrance_groups (group_name) VALUES ('цветочные'), ('древесные'), ('восточные'), ('фруктовые'),  ('фужерные'),  ('цитрусовые'),  ('гурманские'),  ('зеленые'),  ('акватические')  ON CONFLICT (group_name) DO NOTHING;")
        await conn.execute("INSERT INTO notes (note_name) VALUES ('роза'), ('мимоза'), ('лаванда'), ('ирис'), ('жасмин'), ('тубероза'), ('бергамот'), ('лимон'), ('апельсин'), ('мандарин'), ('юдзу'), ('нероли'), ('уд'), ('ладан'), ('сандал'), ('шафран'), ('иланг-иланг'), ('пачули'), ('кедр'), ('ель'), ('эвкалипт'), ('берёза'), ('сосна'), ('ветивер'), ('персик'), ('вишня'), ('дыня'), ('клубника'), ('яблоко'), ('кокос'), ('герань'), ('дубовый мох'), ('бобы тонка'), ('можжевельник'), ('камфора'), ('папоротник'), ('ваниль'), ('шоколад'), ('карамель'), ('конфеты ирис'), ('мёд'), ('тирамису'), ('морская вода'), ('водоросли'), ('водная лилия'), ('огурец'), ('лотос'), ('арбуз'), ('мята'), ('плынь'), ('розмарин'), ('зелёный чай'), ('базилик'), ('свежескошенная трава') ON CONFLICT (note_name) DO NOTHING;")
        await conn.execute('''INSERT INTO scents (name, gender_id, season_id, price_range_id, occasion_id, group_id, note_id) VALUES
        
        ON CONFLICT (name) DO NOTHING;''')
    except Exception as e:
            print(f"Произошла ошибка{e}")
    finally:
        await conn.close()
async def main_db():
    conn = await asyncpg.connect(user='postgres', password='0212er', host='localhost', port='5432', database='perfum_database')
    await create_database(conn)
    await create_tables(conn)
    await insert_tables(conn)
asyncio.run(main_db())

async def get_perfumes(conn, gender=None, group=None, occasion=None, season=None, price_range=None, notes=None):
    query = '''
    SELECT s.name 
    FROM scents s
    WHERE ($1::INTEGER IS NULL OR s.gender_id = $1)
      AND ($2::INTEGER IS NULL OR s.group_id = $2)
      AND ($3::INTEGER IS NULL OR s.occasion_id = $3)
      AND ($4::INTEGER IS NULL OR s.season_id = $4)
      AND ($5::INTEGER IS NULL OR s.price_range_id = $5)
      AND ($6::INTEGER IS NULL OR s.note_id = $6)
    '''
    results = await conn.fetch(query, gender, group, occasion, season, price_range, notes)
    return [fragrance['name'] for fragrance in results]

    results = await conn.fetch(query, gender, group, occasion, season, price_range, notes)
    return [fragrance['name'] for fragrance in results]
