# import MySQLdb
# import pandas as pd
# import sys
  
# # build the MySQL connection  
# conn = MySQLdb.connect(host="localhost", user="clouduser", passwd="clouduser", db="yelp") 

# # the SQL query
# query = "SELECT review_count, stars FROM businesses" 

# # real sql
# df = pd.read_sql(query, con=conn)

# # convert query to dataFrame
# df = pd.DataFrame(df, columns= ['review_count', 'stars'])

# # convert review_count to float
# df.review_count = df.review_count.astype(float)

# # calculate descriptive statistics
# df = df.describe(include='all')

# df.DataFrame.to_csv(sys.stdout, encoding='utf-8', float_format='%.2f')