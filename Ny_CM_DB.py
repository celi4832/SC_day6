# https://github.com/celi4832/Classicmodels.git

# Show a nice message
print(80*'-')
print('Hello - let\'s connect to classicmodels')

#ClassicConnect er den fil man har lavet der connector til classicmodels databasen
import ClassicConnect as thisDatabase
from beautifultable import BeautifulTable

def niceprint(result, th2, context):
    table = BeautifulTable()
    table.columns.header = th2
    table.set_style(BeautifulTable.STYLE_RST)
    for row in result:
        table.rows.append(row)
    print(80*'-')
    print(context)
    print(table)
    print(len(result), 'row(s) returned')

# Connect
con = thisDatabase.dbconnect()

update = """
UPDATE
    classicmodels.customers
SET
    phone = '1234567890'
WHERE
    customerNumber = 175

"""
myCursor = con.cursor()
myCursor.execute(update)

q2 = """
SELECT
    customerNumber,
    customerName,
    phone,
    state
FROM
    classicmodels.customers
WHERE
    country = 'USA'
ORDER BY
    customerName ASC;

"""

th2 = ['Customer Number', 'Customer Name', 'Phone', 'State']


myCursor.execute(q2)
myRecords = myCursor.fetchall()


# Display results nicely
niceprint(myRecords, th2, 'Customers in USA')


# Disconnect
con.close()

# Virker ikke 

#classicmodels = thisDatabase.dbconnect()

#prompt = '>'
#customernum = int(input(prompt))
#if customernum <= 175:
#    print(f'Here is customer {classicmodels.customers}')
#else:
#    print('Sorry that is not available')
