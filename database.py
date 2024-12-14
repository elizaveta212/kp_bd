import psycopg2
from psycopg2 import sql

"""connection = psycopg2.connect(
    user="postgres",
    password="0212er",
    host="localhost",
    port="5432"
)

connection.autocommit = True
cursor = connection.cursor()

# Создание базы данных, если она не существует
try:
    cursor.execute("CREATE DATABASE perfum_database")
    print("База данных успешно создана.")
except psycopg2.errors.DuplicateDatabase:
    print("База данных уже существует.")

# Закрытие соединения после создания базы данных
cursor.close()
connection.close()"""
try:
  connection = psycopg2.connect(
    dbname="perfum_database", 
    user="postgres", 
    password="0212er", 
    host="localhost", 
    port="5432"
  )
  connection.autocommit = True
  cursor = connection.cursor()
  try:
         cursor.execute("CREATE DATABASE perfum_database")
         print("База данных успешно создана.")
  except psycopg2.errors.DuplicateDatabase:
         print("База данных уже существует.")
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS genders (
    gender_id SERIAL PRIMARY KEY,
    gender_name VARCHAR(100)
  )''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS seasons (
    season_id SERIAL PRIMARY KEY,
    season_name VARCHAR(100)
  )''')
  cursor.execute('''
CREATE TABLE IF NOT EXISTS price_ranges (
    price_range_id SERIAL PRIMARY KEY,
    price_range_name VARCHAR(100)
)''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS occasions (
    occasion_id SERIAL PRIMARY KEY,
    occasion_name VARCHAR(100)
  )''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS fragrance_groups (
    fragrance_group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100)
  )''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS notes (
    note_id SERIAL PRIMARY KEY,
    note_name VARCHAR(100)
  )''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS scent_genders (
    scent_id INTEGER,
    gender_id INTEGER,
    FOREIGN KEY (scent_id) REFERENCES scents(scent_id),
    FOREIGN KEY (gender_id) REFERENCES genders(gender_id),
    PRIMARY KEY (scent_id, gender_id)
)''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS scents (
    scent_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    season_id INTEGER,
    price_range_id INTEGER,
    occasion_id INTEGER,
    fragrance_group_id INTEGER,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id),
    FOREIGN KEY (price_range_id) REFERENCES price_ranges(price_range_id),
    FOREIGN KEY (occasion_id) REFERENCES occasions(occasion_id),
    FOREIGN KEY (fragrance_group_id) REFERENCES fragrance_groups(fragrance_group_id)
  )''')
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS scent_notes (
    scent_id INTEGER,
    note_id INTEGER,
    FOREIGN KEY (scent_id) REFERENCES scents(scent_id),
    FOREIGN KEY (note_id) REFERENCES notes(note_id),
    PRIMARY KEY (scent_id, note_id)
  )''')
  cursor.execute("INSERT INTO genders (gender_name) VALUES ('мужской'), ('женский'), ('унисекс') RETURNING gender_id")
  cursor.execute("INSERT INTO seasons (season_name) VALUES ('зима'), ('весна'), ('лето'), ('осень') RETURNING season_id")
  cursor.execute("INSERT INTO price_ranges (price_range_name) VALUES ('до 5000'), ('от 5000 до 10000'), ('от 10000 до 15000'), ('от 15000 и более') RETURNING price_range_id")
  cursor.execute("INSERT INTO occasions (occasion_name) VALUES ('повседневный'), ('вечерний'), ('спортивный') RETURNING occasion_id")
  cursor.execute("INSERT INTO fragrance_groups (group_name) VALUES ('цветочные'), ('древесные'), ('восточные'), ('фруктовые'),  ('фужерные'),  ('цитрусовые'),  ('гурманские'),  ('зеленые'),  ('акватические')  RETURNING fragrance_group_id")
  cursor.execute("INSERT INTO notes (note_name) VALUES ('роза'), ('мимоза'), ('лаванда'), ('ирис'), ('жасмин'), ('тубероза'), ('бергамот'), ('лимон'), ('апельсин'), ('мандарин'), ('юдзу'), ('нероли'), ('уд'), ('ладан'), ('сандал'), ('шафран'), ('иланг-иланг'), ('пачули'), ('кедр'), ('ель'), ('эвкалипт'), ('берёза'), ('сосна'), ('ветивер'), ('персик'), ('вишня'), ('дыня'), ('клубника'), ('яблоко'), ('кокос'), ('герань'), ('дубовый мох'), ('бобы тонка'), ('можжевельник'), ('камфора'), ('папоротник'), ('ваниль'), ('шоколад'), ('карамель'), ('конфеты ирис'), ('мёд'), ('тирамису'), ('морская вода'), ('водоросли'), ('водная лилия'), ('огурец'), ('лотос'), ('арбуз'), ('мята'), ('плынь'), ('розмарин'), ('зелёный чай'), ('базилик'), ('свежескошенная трава') RETURNING note_id")
  cursor.execute('''
  INSERT INTO scents (name, season_id, price_range_id, occasion_id, fragrance_group_id) VALUES
  
  ''')
  cursor.execute('''
  INSERT INTO scent_genders (scent_id, gender_id) VALUES
  (1, 1)
  N CONFLICT (scent_id, gender_id) DO NOTHING;
  ''')
  cursor.execute('''
  INSERT INTO scent_notes (scent_id, note_id) VALUES
  (1, 1)
  ON CONFLICT (scent_id, note_id) DO NOTHING;
  ''')
  async def get_perfumes(gender, fragrance_group, occasion, season, price_range, notes):
    connection = psycopg2.connect(
    dbname="perfum_database", 
    user="postgres", 
    password="0212er", 
    host="localhost", 
    port="5432"
    )
    cursor = connection.cursor()
    query = '''
    SELECT s.name 
    FROM scents s
    JOIN scent_genders sg ON s.scent_id = sg.scent_id
    JOIN scent_notes sn ON s.scent_id = sn.scent_id
    WHERE sg.gender_id = %s 
    AND s.season_id = %s 
    AND s.occasion_id = %s 
    AND s.price_range_id = %s 
    AND s.fragrance_group_id = %s 
    AND sn.note_id = %s;
    '''
    cursor.execute(query, (gender, season, occasion, price_range, fragrance_group, notes))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return [fragrance[0] for fragrance in results]
except Exception as _ex:
      print("[INFO] Error", _ex)
    
finally:
      if connection:
        connection.close()
        print("[INFO] Завершение соединения с PostgreSQL")
