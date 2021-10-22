Create Table assignment1
(
Sender_id int,
Receiver_id int,
Amount int,
Transaction_date date
);

/*
INSERT assignment1 VALUES
(55, 22, 500, '2021-05-18'),
(11, 33, 350, '2021-05-19'),
(22, 11, 650, '2021-05-19'),
(22, 33, 900, '2021-05-20'),
(33, 11, 500, '2021-05-21'),
(33, 22, 750, '2021-05-21'),
(11, 44, 300,  '2021-05-22')
*/


insert into assignment1 (Sender_id,Receiver_id,Amount,Transaction_date)
values
(55, 22, 500, '2021-05-18'),
(11, 33, 350, '2021-05-19'),
(22, 11, 650, '2021-05-19'),
(22, 33, 900, '2021-05-20'),
(33, 11, 500, '2021-05-21'),
(33, 22, 750, '2021-05-21'),
(11, 44, 300,  '2021-05-22')
;
select * from assignment1

select Sender_id,sum(Amount) as send_amount
from assignment1
group by Sender_id

select Receiver_id,sum(Amount) as receive_amount
from assignment1
group by Receiver_id

select * from (select Sender_id,sum(Amount) as send_amount
					from assignment1
					group by Sender_id) S
full outer join (select Receiver_id,sum(Amount) as receive_amount
					from assignment1
					group by Receiver_id) R
on   S.Sender_id=R.Receiver_id

--Neden null var eþleþmiyor iki tabloda veri yok
--neden full outer yaptýk çünkü inner yapsak sadece kesiþimi getirecekti bize
--account id ile net_change deðerlerini bulmalýyýz
--coalesce boþ ise bir sonraki satýrý al diyor

select COALESCE(S.sender_id,R.receiver_id) from assignment1

select Sender_id,sum(Amount) as send_amount
from assignment1
group by Sender_id

select Receiver_id,sum(Amount) as receive_amount
from assignment1
group by Receiver_id

select COALESCE(S.sender_id,R.receiver_id) as account_id,
       COALESCE(R.receive_amount,0) - COALESCE(S.send_amount,0) as Net_change
from (select Sender_id,sum(Amount) as send_amount
					from assignment1
					group by Sender_id) S
full outer join (select Receiver_id,sum(Amount) as receive_amount
					from assignment1
					group by Receiver_id) R
on   S.Sender_id=R.Receiver_id;