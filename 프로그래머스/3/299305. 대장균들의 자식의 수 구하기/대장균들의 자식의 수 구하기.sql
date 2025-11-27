-- 코드를 작성해주세요
select e.ID	 as 'ID', Count(c.Id) as 'CHILD_COUNT'
From ECOLI_DATA e
left Join ECOLI_DATA c on e.ID = c.PARENT_ID
group by e.ID
order by e.ID asc