def_word = ['APR','interest','fee']
def_def = ['APR means Annual Percentage Rate and refers to a financial term that is used by lenders to let you know how much interest you are being charged on a yearly basis for your loan. For example, on a $10,000 car loan at an 8 percent APR you would pay approximately $800 in one year in interest for the loan.',
           'Interest in finance refers to the amount of money paid for the use of someone else''s money. An example of interest is the $20 that was earned this year on your savings account. An example of interest is the $2000 you paid in interest this year on your home loan.',
           'A fee is a sum of money that you pay for a service or to be allowed to do something.']

def get_balance(db):
  balance = int(db['balance'].tail(1))
  return balance

def get_definition(definition):
  return def_def[def_word.index(definition)]

def get_subscriptions():
  return "Gym, Netflix, Spotify"


def get_spending(db, *args, **kwargs):
  category = kwargs.get('category', None)
  date1 = kwargs.get('date1', None)
  date2 = kwargs.get('date2', None)

  df2 = db.loc[db['amount'] < 0]
  
  if any(db['cat'].isin([category])):
    df2 = df2.loc[db['cat'] == category]
  if any(db['subCat'].isin([category])):
    df2= df2.loc[db['subCat']== category]
  if any(db['nameSubs'].isin([category])):
    df2= df2.loc[db['nameSubs']== category]
  if date1 != None:
    df2= df2.loc[db['date']> date1]
  if date2 != None:
    df2= df2.loc[db['date']< date2]
    
  return int(-df2['amount'].sum())
