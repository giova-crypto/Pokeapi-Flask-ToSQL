use manpower;
select pt.type_id, t.name, COUNT(*) from pokemon_types as pt
join types as t on pt.type_id = t.id
group by t.id
order by COUNT(*) desc
limit 1

 