-- 코드를 작성해주세요

select count(*) as count
from ecoli_Data
where (genotype & 2 ) = 0 and (genotype & 5) > 0;
