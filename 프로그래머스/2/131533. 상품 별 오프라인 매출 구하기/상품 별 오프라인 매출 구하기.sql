-- 코드를 입력하세요
-- 상품코드 별 매출액 (판매가*판매량) 합계 출력
-- 판매가는 상품 테이블, 판매량은 판매 테이블
with offline as(
    select PRODUCT_ID, sum(SALES_AMOUNT) as 'SALES_AMOUNT'
    from OFFLINE_SALE
    group by 1
)

SELECT p.PRODUCT_CODE as 'PRODUCT_CODE', (p.PRICE * o.SALES_AMOUNT) as "SALES"
From PRODUCT p
join offline o on o.PRODUCT_ID = p.PRODUCT_ID
order by 2 desc, 1 asc;