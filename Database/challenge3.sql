-- CREATE DATABASE ch14_20;
USE ch14_20;

-- 테이블 생성
CREATE TABLE emplyees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position varchar(100),
    salary DECIMAL(10, 2) NOT NULL
);

-- 직원 데이터 추가
insert into emplyees(name,position,salary) values
('혜린','PM',90000), ('은우','Frontend',80000),('가을','Backend',92000),('지수','Frontend',78000),('민혁','Frontend',96000),('하온','Backend',13000);

-- 이름과 연봉 조회
select name,salary from emplyees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
select name, salary from emplyees where position='Frontend' and salary<90000;

-- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
update emplyees set salary=salary*1.1 where position='PM';

-- 모든 Backend' 직책을 가진 직원의 연봉을 5% 인상하세요.
update emplyees set salary=salary*1.05 where position='Backend';

-- 민혁 사원의 데이터를 삭제하세요
delete from emplyees where name = '민혁';

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
select position, avg(salary) from emplyees group by position 

-- employees 테이블을 삭제하세요.
drop table emplyees




