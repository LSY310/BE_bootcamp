import random
from faker import Faker
from sqlalchemy import create_engine, MetaData

fake = Faker()

#더미데이터 함수
def generator(connection, metadata,table_name,n,reset=False):
    table = metadata.tables[table_name]
    print(f"Generating dummy data for table: {table_name}")

    if reset:
        # 전체 데이터 삭제
        connection.execute(table.delete())
        connection.commit()
        
    for _ in range(n):  # 각 테이블에 10개의 더미 데이터 생성
        data = {}
        for column in table.columns:
            print(column.name)
            # AUTO_INCREMENT 칼럼은 대상칼럼에서 제외
            if column.autoincrement==True:
                continue
            #unique 조건
            if column.unique:
                data[column.name] =fake.unique
            # 데이터 유형에 따라 더미 데이터 생성
            if "VARCHAR" in str(column.type):
                data[column.name] = fake.word()
            elif column.type.__class__.__name__ == 'CHAR':
                data[column.name]=fake.pystr(max_chars=column.type.length)
            elif column.name.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                data[column.name] = fake.boolean()
            elif "TEXT" in str(column.type):
                data[column.name] = fake.sentence()
            elif "FLOAT" in str(column.type) or "DOUBLE" in str(column.type):
                data[column.name] = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
            elif "YEAR" in str(column.type):
                data[column.name] = fake.year()
            elif "INT" in str(column.type):
                data[column.name] = random.randint(1, 1000)
            elif "DECIMAL" in str(column.type):
                data[column.name] = round(random.uniform(1, 100), 2)
            elif "DATETIME" in str(column.type) or "TIMESTAMP" in str(column.type):
                data[column.name] = fake.date_time_this_decade()
            elif "DATE" in str(column.type):
                data[column.name] = fake.date_this_decade()
            elif "BOOLEAN" in str(column.type):
                data[column.name] = fake.boolean()
            elif "TIME" in str(column.type):
                data[column.name] = fake.time()
            elif "BLOB" in str(column.type) or "BINARY" in str(column.type):
                data[column.name] = fake.binary(length=10)
            elif "ENUM" in str(column.type):
                enum_values = column.type.enums if hasattr(column.type, 'enums') else []
                if enum_values:
                    data[column.name] = fake.random_element(elements=enum_values)
                else:
                    data[column.name] = fake.word()

        # 테이블에 더미 데이터 삽입
        connection.execute(table.insert(), data)
        connection.commit()