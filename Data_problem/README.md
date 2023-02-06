## Introduction
This folder contains the solution to the Fetch Rewards Coding Exercise - Data Analytics Internship.

The schema I created for the problem is ![](https://github.com/DirkFi/FetchRewards/blob/main/Data_problem/img/pic.png).

And the processed data is in the folder processed_data. The Python script used to process the original data is also there.

For database table created, the DDL I use is as below:
```
create table Brand(Barcode int primary key, Brand_code VARCHAR(64), Category VARCHAR(32), Name VARCHAR(64));

create table Receipt_item(Receiptid int, item_index int, Barcode int, Quantity_purchased int, Total_final_price float, primary key(Receiptid, item_index));

create table Item(Itemid int primary key, Name VARCHAR(16));

create table Receipt(Receiptid int primary key, Purchase_date VARCHAR(16), Date_scanned VARCHAR(16), Total_spent float, Userid int);

create table User(Userid int primary key, Create_date VARCHAR(16), Birth_date VARCHAR(16), Gender CHAR(16), State VARCHAR(16));

```

## Queries

I will list the queries for all the bullets here.
```
select Name from
(select sum(Total_final_price) as spent, Barcode, Name
from Brand natural join Receipt_item natural join Receipt
where Purchase_date = 'June'
group by Barcode
order by spent
limit 1);
```

```
select Userid from
(select sum(Total_final_price) as spent, Userid
from Receipt natural join User
where Purchase_date = 'August'
group by Userid
order by spent
limit 1);
```

```
select Userid from
(select  Total_final_price/Quantity_purchased as item_price, Userid
from Receipt natural join User natural join Receipt_items
group by Userid
order by item_price
limit 1);
```

```
select Name
from
(select  Total_final_price/Quantity_purchased as item_price, Itemid
from Receipt natural join User natural join Receipt_items
group by Userid
order by item_price
limit 1) natual join Item;
```

```
select count(Userid) as num
from User natural join Receipt
group by Date_scanned
```
