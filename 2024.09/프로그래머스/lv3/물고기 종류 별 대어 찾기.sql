select i.id, n.fish_name, i.length
from fish_info i join fish_name_info n 
    on i.fish_type = n.fish_type
    where I.length = (select max(length)
        from fish_info
        where fish_type=I.fish_type) 
order by i.id asc;
