import hashlib
import sqlite3

class gerenciador:
  def __init__(self,db_name="hospital_vet.db"):
    self.db_name = db_name
    self.criar_tabelas()

  def conectar(self):
     return sqlite3.connect(self.db_name)

  def criar_tabelas(self):
    conn = self.conectar()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS CHAVES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                clinica_id INTEGER,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tutor_id INTEGER,
                clinica_id INTEGER,
                nome TEXT NOT NULL,
                especie TEXT,
                peso REAL,
                FOREIGN KEY (tutor_id) REFERENCES tutores (id)
            )
        ''')
        conn.commit()
        conn.close()

  def cadastrar_pet(self, tutor_id, clinica_id, nome, especie, peso):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pets (tutor_id, clinica_id, nome, especie, peso)
            VALUES (?, ?, ?, ?, ?)
        ''', (tutor_id, clinica_id, nome, especie, peso))
        conn.commit()
        conn.close()
