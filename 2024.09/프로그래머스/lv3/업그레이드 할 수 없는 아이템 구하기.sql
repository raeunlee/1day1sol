select t.item_id, i.item_name, i.rarity
from item_info i join item_tree t on i.item_id = t.item_id
where t.item_id not in (select distinct ifnull(parent_item_id, 'root') from item_tree)
order by item_id desc;
