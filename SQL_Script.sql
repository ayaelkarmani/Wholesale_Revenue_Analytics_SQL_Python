SELECT 
    product_line,
    TO_CHAR(date, 'FMMonth') AS month,
    warehouse,
    SUM(total) - SUM(payment_fee) AS net_revenue
FROM public.sales
WHERE client_type = 'Wholesale'
GROUP BY 
    product_line,
    TO_CHAR(date, 'FMMonth'),
    warehouse
ORDER BY 
    product_line,
    MIN(date),
    net_revenue DESC;