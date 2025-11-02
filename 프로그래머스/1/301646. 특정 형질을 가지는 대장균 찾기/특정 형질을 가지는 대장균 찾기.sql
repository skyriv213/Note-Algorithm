-- 코드를 작성해주세요
select Count(*) as 'COUNT'
From ECOLI_DATA
where (GENOTYPE & POW(2,1)) = 0
    and ((GENOTYPE & POW(2,0)) =1 
    or (GENOTYPE & POW(2,2)) =4)