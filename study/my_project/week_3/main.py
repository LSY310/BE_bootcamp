from sqlalchemy import create_engine, MetaData, Table
import json
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.schema import CreateTable

tables_info={}
def main():
    # config 파일에서 데이터베이스 정보 가져오기
    with open("week_3/config.json", 'r') as f:
        config = json.load(f)

    # 데이터베이스 연결에 필요한 정보 추출
    db_info = config["databases"]["db"]


    # SQLAlchemy를 사용하여 데이터베이스에 연결
    engine = create_engine(f"mysql+pymysql://{db_info['username']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['db_name']}?charset=utf8mb4", echo=True)
    # Inspector 생성
    inspector = Inspector.from_engine(engine)


    # 특정 데이터베이스에 속한 schema 목록 반환 함수
    #print(schema(inspector))
    

    # 특정 데이터베이스의 schema에 속한 테이블 목록 반환 함수
    #print(tables_in_schema(inspector,'airportdb'))

    #특정 데이터베이스의 schema에 속한 뷰 목록 반환 함수
    #print(views_in_schema(inspector,'airportdb'))

    #특정 데이터베이스의 schema에 속한 테이블 목록과 테이블 별 컬럼정보, 코멘트를 같이 반환하는 함수
    #print(all_information(inspector,'airportdb'))

    #특정 데이터베이스의 schema에 속한 뷰 목록과 뷰 별 컬럼정보, 코멘트를 같이 반환하는 함수
    #print(all_view_infromation(inspector,'airportdb',''))

    #특정 테이블의 컬럼정보, 코멘트를 조회하는 함수
    #print(columns_and_comments(inspector,'airportdb','airline'))

    #특정 테이블의 DDL 스크립트 생성 함수
    #ddl_script(engine,'airportdb','airline')


# 특정 데이터베이스에 속한 schema 목록 반환 함수
def schema(inspector):
    schemas = inspector.get_schema_names()
    print(schemas)

# 특정 데이터베이스의 schema에 속한 테이블 목록 반환 함수
def tables_in_schema(inspector,schema_name):
    tables = inspector.get_table_names(schema=schema_name)
    return tables

#특정 데이터베이스의 schema에 속한 뷰 목록 반환 함수
def views_in_schema(inspector, schema_name):
    view = inspector.get_view_names(schema=schema_name)
    return view

#특정 데이터베이스의 schema에 속한 테이블 목록과 테이블 별 컬럼정보, 코멘트를 같이 반환하는 함수
def all_information(inspector, schema_name):
    for table in tables_in_schema(inspector,schema_name):
        columns = inspector.get_columns(table, schema=schema_name)
        comments = inspector.get_table_comment(table, schema=schema_name)
        tables_info[table] = {
            "columns": columns,
            "comment": comments
        }
    return tables_info

#특정 데이터베이스의 schema에 속한 뷰 목록과 뷰 별 컬럼정보, 코멘트를 같이 반환하는 함수
def all_view_infromation(inspector, schema_name,view_name):
    for view in views_in_schema(inspector,schema_name):
        columns = inspector.get_columns(view_name, schema=schema_name)
        comments = inspector.get_table_comment(view_name, schema=schema_name)
        return columns,comments

#특정 테이블의 컬럼정보, 코멘트를 조회하는 함수
def columns_and_comments(inspector, schema_name,table_name):
    columns = inspector.get_columns(table_name, schema=schema_name)
    comments = inspector.get_table_comment(table_name, schema=schema_name)
    return columns,comments

#특정 테이블의 DDL 스크립트 생성 함수
def ddl_script(engine,schema_name,table_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine, schema=schema_name)
    ddl = str(CreateTable(table).compile(engine))

    # DDL 스크립트 출력
    print(ddl)

if __name__ == '__main__' :
    main()