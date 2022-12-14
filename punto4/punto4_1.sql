use manpower;
select p.id,p.name, p.image  from pokemon_types as pt
join pokemon as p on pt.pokemon_id = p.id
group by p.id
having COUNT(*) >1;
