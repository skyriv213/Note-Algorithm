-- 코드를 입력하세요
-- 보호소에서 중성화 된 동물
-- 보호소에 들어올 때는 중성화가 안됐지만 나갈 때는 중성화 된 동물
-- SEX_UPON_INTAKE 해당 항목이 Ins, outs이 다르면 중성화로 판단
-- 입양이 간 동물을 판단하므로 메인 테이블은 outs 테이블
SELECT o.ANIMAL_ID	, o.ANIMAL_TYPE, o.NAME
From animal_outs o
join animal_ins i on i.ANIMAL_ID = o.ANIMAL_ID
where i.SEX_UPON_INTAKE != o.SEX_UPON_OUTCOME
order by 1