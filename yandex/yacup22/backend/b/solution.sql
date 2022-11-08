-- https://contest.yandex.ru/yacup/contest/42202/problems/B/
drop TABLE if EXISTS requests;

CREATE TABLE requests (
    datetime TIMESTAMP,
    request_id integer,
    parent_request_id integer,
    host TEXT,
    type TEXT,
    data TEXT
);

insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.0', 	0,	NULL,	'balancer.test.yandex.ru',	'RequestReceived', 	'');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.1',	0,	NULL,	'balancer.test.yandex.ru',	'RequestSent',		'backend1.ru');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.101',	0,	NULL,	'balancer.test.yandex.ru',	'RequestSent',		'backend2.ru');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.150', 1,	0,		'backend1.ru',				'RequestReceived', 	''	);
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.200', 2,	0,		'backend2.ru',				'RequestReceived', ''	);
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.155', 1,	0,	'backend1.ru',	'RequestSent',	'backend3.ru');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.210', 2,	0,	'backend2.ru',	'ResponseSent', ''	);
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.200', 3,	1,	'backend3.ru',	'RequestReceived', '');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.220', 3,	1,	'backend3.ru',	'ResponseSent', '' );
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.260', 1,	0,	'backend1.ru',	'ResponseReceived',	'backend3.ru OK');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.300', 1,	0,	'backend1.ru',	'ResponseSent', '');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.310', 0,	NULL,	'balancer.test.yandex.ru',	'ResponseReceived',	'backend1.ru OK');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.250', 0,	NULL,	'balancer.test.yandex.ru',	'ResponseReceived',	'backend2.ru OK');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.400', 0,	NULL,	'balancer.test.yandex.ru',	'ResponseSent', '');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.500', 4,	NULL,	'balancer.test.yandex.ru',	'RequestReceived', ''	);
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.505', 4,	NULL,	'balancer.test.yandex.ru',	'RequestSent',	'backend1.ru');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.510', 5,	4,	'backend1.ru',	'RequestReceived', '');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.700', 5,	4,	'backend1.ru',	'ResponseSent', '');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.710',	4,	NULL,	'balancer.test.yandex.ru',	'ResponseReceived',	'backend1.ru ERROR');
insert into requests (datetime, request_id, parent_request_id, host, type, data) values ('1-1-1 0:0:0.715',	4,	NULL,	'balancer.test.yandex.ru',	'ResponseSent', '');


select case
    when (select count(DISTINCT request_id) from requests where parent_request_id is NULL) = 0 THEN 0
    else (select sum(ts.r2d - ts.r1d)*1000 / (select count(DISTINCT request_id) from requests where parent_request_id is NULL))
end as avg_network_time_ms
from (
select EXTRACT (Epoch from r1.datetime)::NUMERIC as r1d, EXTRACT (Epoch from r2.datetime)::NUMERIC as r2d, r1.type, r2.type, r1.host, r2.data
from requests r1, requests r2
    where ((r1.request_id = r2.parent_request_id AND r1.type = 'RequestSent' and r2.type = 'RequestReceived'  AND r1.data = r2.host)
         OR (r1.parent_request_id = r2.request_id AND r1.type = 'ResponseSent' and r2.type = 'ResponseReceived' AND r2.data like r1.host || '%' ))) as ts