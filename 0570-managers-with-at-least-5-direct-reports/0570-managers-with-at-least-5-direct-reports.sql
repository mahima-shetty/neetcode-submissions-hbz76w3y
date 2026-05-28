# Write your MySQL query statement bel
select e1.name from Employee E1
join
(
select managerId, count(*) as directReports
from Employee
group by managerId
having count(*) >= 5
) E2 on E1.id = E2.managerID


