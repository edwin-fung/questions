

#SQL Q1
"""
SELECT
    catalog_id,
    item_id
    MAX(unit_price)
FROM
    price_log_change log_tbl
LEFT JOIN
    (
    SELECT
        catalog_id,
        item_id,
        max(month(date_id)) MAX_MONTH
    FROM
        price_log_change
    WHERE
        date < MONTH(current_date)
    ) date_tbl
    ON log_tbl.catalog_id = date_tbl.catalog_id
    AND  log_tbl.item_id = date_tbl.item_id
    AND MONTH(log_tbl.date) = date_tbl.MAX_MONTH
WHERE date_tbl.MAX_MONTH IS NOT NULL
GROUP BY 1, 2
"""

#test process log
"""
hours,shard,errCnt
# 1,1,32
# 1,2,13
# 3,2,12
"""
import pandas as pd

tbl_1 = []
log_data = open('/Users/efung1/Downloads/sample.log', 'r')

for line in log_data:
    date = line[0:15]
    hour = line[7:9]
    shard = line[line.find('shard'):line.find('shard')+7]
    error = line[-6:][:5]

    tbl_1.append([ hour, shard, error])

df = pd.DataFrame(tbl_1, columns=['hour', 'shard', 'error'])
df_filter = df[df['error']=='error']

#test valitaion
#print(df_filter.to_string())
sum_df = df.groupby(['hour', 'shard']).count()
print(sum_df.to_string())

