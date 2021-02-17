import mysql.connector
import datetime

# LVL, TYPE, FR, EN, EX, TIME
# LVL = A - F oder S

mydb = mysql.connector.connect(
  host = "sql11.freesqldatabase.com",
  user = "sql11393379",
  password = "2aqv8gEbKG",
  database = "sql11393379"
)

#shortcuts
oneDay = datetime.timedelta(days = 1)
def dts(datum): # date to string
  return datum.strftime("%d.%m.%Y")
def today(): # get todays date
  return datetime.date.today()


#commands
def add(wortart, fr, en, bsp = ""): # adds to db with rep = tomorrow
  if wortart and fr and en: # if strings not empty
    repDatum = today() + oneDay # rep = next repetition date

    sql = "INSERT INTO voc_fr (level, type, french, english, example, date) VALUES (%s, %s, %s, %s, %s, %s)"

    val = ("A", wortart, fr, en, bsp, repDatum)
    #run
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record added.")
  else:
    print("Empty Argument")

def listAll():
  sql = "SELECT type, french, english, example FROM voc_fr"

  #run
  mycursor = mydb.cursor()
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  print(mycursor.rowcount, "records fetched\n")

  for x in myresult:
    print(x[0] + ": " + x[1])
