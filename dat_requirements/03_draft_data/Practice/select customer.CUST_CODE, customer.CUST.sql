select customer.CUST_CODE, customer.CUST_NAME, customer.CUST_CITY, customer.AGENT_CODE
,agents.AGENT_CODE, agents.WORKING_AREA, agents.PHONE_NO

    from customer inner join agents
    ON customer.AGENT_CODE = agents.AGENT_CODE;



select s1.AGENT_CODE
,s1.WORKING_AREA
,s1.PHONE_NO
,count(s2.CUST_CODE) as NUM_CUST
,sum(s2.PAYMENT_AMT) as TOTAL_PAYMENT
from agents s1
inner join customer s2
on s1.AGENT_CODE = s2.AGENT_CODE
group by s1.AGENT_CODE
order by TOTAL_PAYMENT DESC, NUM_CUST DESC
limit 1 asc;


