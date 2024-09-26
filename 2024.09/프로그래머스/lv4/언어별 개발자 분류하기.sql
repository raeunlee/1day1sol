with 
    front as (
        select SUM(CODE) as code
        from skillcodes
        where category = 'Front End'),

    c as(
        select code
        from skillcodes
        where name = 'C#'),

    python as(
        select code
        from skillcodes
        where name = "Python")

select 
    case when
        d.skill_code & f.code >= 1 and d.skill_code & p.code then 'A'
        when
        d.skill_code & c.code >= 1 then 'B'
        when
        d.skill_code & f.code >= 1 then 'C'
        end grade, d.id, d.email

from developers d join front f
        join c c
        join python p
having grade is not null
order by grade, id asc
        
