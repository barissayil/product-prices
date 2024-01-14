def construct_sql_command(table: str, percentage_threshold: int, euro_threshold: int, last_two: bool):
    return f'''
        WITH ranked_prices AS (
            SELECT 
                product,
                price,
                ROW_NUMBER() OVER (PARTITION BY product ORDER BY activity_date ASC) AS rn_asc,
                ROW_NUMBER() OVER (PARTITION BY product ORDER BY activity_date DESC) AS rn_desc
            FROM 
                {table}
        ),
        first AS (
            SELECT 
                product, 
                price AS first_price
            FROM 
                ranked_prices
            WHERE 
                {'rn_desc = 2' if last_two else 'rn_asc = 1'}
        ),
        second AS (
            SELECT 
                product, 
                price AS last_price
            FROM 
                ranked_prices
            WHERE 
                rn_desc = 1
        )
        SELECT 
            f.product,
            ABS(last_price - first_price) AS price_variation
        FROM 
            first f
        JOIN 
            second s ON f.product = s.product
        WHERE 
            (
                ABS(last_price - first_price) >= {percentage_threshold} * CAST(first_price AS FLOAT) / 100 OR
                ABS(last_price - first_price) >= {euro_threshold}
            )
    '''

def construct_test_date():
    return {
        'activity_date': [
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/01/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/02/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
            '01/03/2024',
        ],
        'product': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'price': [10, 10, 10, 10, 10, 500, 500, 500, 500, 500, 11, 11, 40, 40, 1000, 502, 502, 600, 900, 1000, 80, 800, 40, 40, 11, 600000, 502, 503, 90000, 600]
    }
