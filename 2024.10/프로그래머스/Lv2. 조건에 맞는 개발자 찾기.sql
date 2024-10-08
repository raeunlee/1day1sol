select distinct(ID), EMAIL, FIRST_NAME, LAST_NAME
from developers d join skillcodes s on d.skill_code & s.code
where name = 'Python' or name = 'C#'
order by 1 asc
