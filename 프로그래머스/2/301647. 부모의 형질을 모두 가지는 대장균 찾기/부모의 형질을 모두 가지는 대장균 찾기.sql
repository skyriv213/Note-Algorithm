-- 코드를 작성해주세요
select e.ID	, e.GENOTYPE, ee.GENOTYPE as 'PARENT_GENOTYPE'
from ECOLI_DATA e
join ECOLI_DATA ee on ee.ID = e.PARENT_ID
where (e.GENOTYPE & ee.GENOTYPE ) = ee.GENOTYPE
order by e.id asc