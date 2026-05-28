# Write your MySQL query statement below
select curr.id from Weather curr
where exists (select 1 from Weather past where datediff(curr.recordDate, past.recordDate) = 1 and past.temperature < curr.temperature )