from sqlalchemy import create_engine, MetaData
from faker import Faker
import random

# MySQL 연결 설정
username = 'root'  # MySQL 사용자 이름
password = '0310'  # MySQL 비밀번호
host = 'localhost'
port = 3306
db_name = 'airportdb'

# MySQL 연결 엔진 생성
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}?charset=utf8mb4", echo=True)

# 데이터베이스 메타데이터 로드
metadata = MetaData()

# 테이블을 autoload하고 reflect 메서드를 사용하여 테이블 메타데이터 가져오기
metadata.reflect(bind=engine)

# Faker 객체 생성
fake = Faker()

# 테이블별 더미 데이터 생성
with engine.connect() as connection:
    for table_name in metadata.tables:
        table = metadata.tables[table_name]
        print(f"Generating dummy data for table: {table_name}")
        for _ in range(10):  # 각 테이블에 10개의 더미 데이터 생성
            data = {}
            for column in table.columns:
                # AUTO_INCREMENT 칼럼은 대상칼럼에서 제외
                if column.autoincrement:
                    continue
                # 데이터 유형에 따라 더미 데이터 생성
                if "VARCHAR" in str(column.type):
                    data[column.name] = fake.word()
                elif "CHAR" in str(column.type):
                    data[column.name] = fake.lexify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                elif "TEXT" in str(column.type):
                    data[column.name] = fake.sentence()
                elif "SMALLINT" in str(column.type):
                    data[column.name] = random.randint(1, 100)
                elif "INTEGER" in str(column.type):
                    data[column.name] = random.randint(1, 1000)
                elif "DECIMAL" in str(column.type):
                    data[column.name] = round(random.uniform(1, 100), 2)
                elif "DATETIME" in str(column.type):
                    data[column.name] = fake.date_time_this_decade()
                elif "DATE" in str(column.type):
                    data[column.name] = fake.date_this_decade()
                elif "TIME" in str(column.type):
                    data[column.name] = fake.time()
                elif "ENUM" in str(column.type):
                    # Assume enum column has only two values, 'value1' and 'value2'
                    data[column.name] = random.choice(['value1', 'value2'])

            # 테이블에 더미 데이터 삽입
            connection.execute(table.insert(), data)