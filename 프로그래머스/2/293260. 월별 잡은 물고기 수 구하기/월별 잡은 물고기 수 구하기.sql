-- 코드를 작성해주세요

Select Count(*) as "FISH_COUNT", Month(Time) as "MONTH"
From FISH_INFO
group by MONTH
order by MONTH