USE challenge3;

-- (1) customers 테이블에 새 고객을 추가하세요.
insert into customers(customerNumber,customerName,phone,address,salesRepEmployeeNumber) values (1,'wendy','01011111111','korea',11);

-- (2) products 테이블에 새 제품을 추가하세요.
insert into products(productCode,productName,productLine) values ('111','note','23');

-- (3) employees 테이블에 새 직원을 추가하세요.
insert into emplyees(emplyeeNumber,name,email,officeCode,reportsTo) values (11,'cherry','cherry@google.com','11',3);

-- (4) offices 테이블에 새 사무실을 추가하세요.
insert into offices(officeCode) values ('11');

-- (5) orders 테이블에 새 주문을 추가하세요.
insert into orders(orderNumber,orderDate,customerNumber) values (1,'2023-09-22',1);

-- (6) orderdetails 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails(orderNumber,productCode) values (1,'111');

-- payments 테이블에 지불 정보를 추가하세요.
insert into payments(customerNumber,checkNumber, paymentDate,amount) values (1,'1', '2024-02-02',5);

-- (8) productlines 테이블에 제품 라인을 추가하세요.
insert into productlines(productLine, desciption) values ('11','bbb');

-- (9) customers 테이블에 다른 지역의 고객을 추가하세요.
insert into customers(customerNumber,customerName,phone,address,salesRepEmployeeNumber) values (2,'sara','01022222222','japan',11);

-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products(productCode,productName,productLine) values ('222','pen','19');

-- (1) customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- (2) products 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- (3) employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select name, grade from employees;

-- (4) offices 테이블에서 모든 사무실의 위치를 조회하세요.
select address from offices;

-- (5) orders 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders order by orderDate DESC LIMIT 10;

-- (6) orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from customers where orderNumber=1;

-- (7) payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber=1;

-- (8) productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
select productLine, description from productlines;

-- (9) customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where address='korea';

-- (10) products 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where price between 0 and 10000;

-- (1) customers 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set address='japan' where customerNumber=1;

-- (2) products 테이블에서 특정 제품의 가격을 갱신하세요.
update products set price=10000 where productCode='13';

-- (3) employees 테이블에서 특정 직원의 직급을 갱신하세요.
update employees set grade='3' where employeeNumber=11;

-- (4) offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices set tel='010000000000' where officeCode='11';

-- (5) orders 테이블에서 특정 주문의 상태를 갱신하세요.
update orders set state='ready' where orderNumber='13';

-- (6) orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update orderdetails set amount=11 where orderNumber='14';

-- (7) payments 테이블에서 특정 지불의 금액을 갱신하세요.
update payments set amount=13000 where customerNumber=1 and checkNumber='3';

-- (8) productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines set description="update_ddd" where productLine='11';

-- (9) customers 테이블에서 특정 고객의 이메일을 갱신하세요.
update customers set email='wendy@naver.com' where customerNumber=1;

-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products set price=1000000;

-- (1) customers 테이블에서 특정 고객을 삭제하세요.
delete from customers where customerNumber=1;

-- (2) products 테이블에서 특정 제품을 삭제하세요.
delete from products where productCode='11';

-- (3) employees 테이블에서 특정 직원을 삭제하세요.
delete from emplyees where employeeNumber=11;

-- (4) offices 테이블에서 특정 사무실을 삭제하세요.
delete from offices where officeCode='111';

-- (5) orders 테이블에서 특정 주문을 삭제하세요.
delete from orders where orderNumber=11;

-- (6) orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
delete from orderdetails where orderNumber=11;

-- (7) payments 테이블에서 특정 지불 내역을 삭제하세요.
delete from payments where customerNumber=1;

-- (8) productlines 테이블에서 특정 제품 라인을 삭제하세요.
delete from prodcutlines where productLine='11';

-- (9) customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
delete from customers where address='korea';

-- (10) products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
delete from products where productLine='1';

 



