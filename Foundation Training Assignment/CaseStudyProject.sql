if DB_ID('EcommerceApplication') is null
begin
create database EcommerceApplication ;
end;
else 
begin 
print 'Database already exists'
end;

use EcommerceApplication ;


if not exists (select name from sys.tables where name='customers')
begin
create table customers(customer_id int primary key identity(1,1),name varchar(100) not null,
email varchar(100) not null unique check (email like '%_@_%._%'),password varchar(50) not null 
check (LEN(password)>=8));
end;
else 
begin 
print 'Table already exists'
end;

if not exists (select name from sys.tables where name='products')
begin
create table products(product_id int primary key identity(1,1), name varchar(100) not null,
price decimal(10,2) not null check(price>=0), description varchar(255), 
stockQuantity bigint check(stockQuantity >=0));
end;
else 
begin 
print 'Table already exists'
end;

if not exists (select name from sys.tables where name='cart')
begin
create table cart(cart_id int primary key identity(1,1),customer_id int not null,product_id int not null,
quantity int not null check(quantity>0),foreign key (customer_id) references customers(customer_id) on delete cascade,
foreign key(product_id) references products(product_id) on delete cascade);
end;
else 
begin 
print 'Table already exists'
end;

if not exists (select name from sys.tables where name='orders')
begin
create table orders(order_id int primary key identity(1,1),customer_id int not null, 
order_date datetime not null default getdate(),total_price decimal(10,2) not null
check (total_price>=0),shipping_address varchar(300) not null,
foreign key (customer_id) references customers(customer_id) on delete cascade);
end;
else 
begin 
print 'Table already exists'
end;

if not exists (select name from sys.tables where name='order_items')
begin
create table order_items(order_item_id int primary key identity(1,1),order_id int not null,
product_id int not null,quantity int not null check(quantity>0),foreign key(order_id) references orders(order_id)
on delete cascade,foreign key (product_id) references products(product_id) on delete cascade);
end;
else 
begin 
print 'Table already exists'
end;


select name from sys.tables;