from generator import generator
from sqlalchemy import create_engine, MetaData

def main():
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


    # 테이블별 더미 데이터 생성
    with engine.connect() as connection:
        generator(connection, metadata, 'airport', 10, reset=True)

if __name__ == '__main__' :
    main()
        