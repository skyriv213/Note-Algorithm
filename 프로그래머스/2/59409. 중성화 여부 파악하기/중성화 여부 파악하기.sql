-- 코드를 입력하세요
# with temp as(
# select 
#     SEX_UPON_INTAKE
#     from
#     ANIMAL_INS
# where SEX_UPON_INTAKE = 'Neutered' or SEX_UPON_INTAKE ='Spayed'
# )

SELECT
ANIMAL_ID,NAME, if(SEX_UPON_INTAKE like 'Neutered%' or SEX_UPON_INTAKE like'Spayed%', "O","X") as '중성화'
from ANIMAL_INS