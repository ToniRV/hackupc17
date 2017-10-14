import json
import requests
import datetime

def getDate(date_str):
    year, month, day = (int(x) for x in date_str.split('-'))
    ans = datetime.date(year, month, day)
    return ans

def BalanceChecker():
  url = 'http://hackupc-env.vrmyckymgj.us-east-1.elasticbeanstalk.com/balance'
  r = requests.get(url)
  r_json = r.json()
  
  return float(r_json['result'])

def FinanceDefinitions(definition):
  url = 'http://hackupc-env.vrmyckymgj.us-east-1.elasticbeanstalk.com/definition'
  data = json.dumps({'definition': definition})
  r = requests.post(url, data)
  r_json = r.json()
  
  return r_json['result']

def SubscriptionChecker():
  url = 'http://hackupc-env.vrmyckymgj.us-east-1.elasticbeanstalk.com/subscriptions'
  r = requests.get(url)
  r_json = r.json()

  return r_json['result']

def Spending(category):
  url = 'http://hackupc-env.vrmyckymgj.us-east-1.elasticbeanstalk.com/spending'
  data = json.dumps({'category': category})
  r = requests.post(url,data)
  r_json = r.json()

  return float(r_json['result'])

def SpendingDate(nameSubCat, date):
  pass

def lambda_handler(event, context):
  sessionAttributes = event['sessionAttributes']
  intent = event['currentIntent']['name']
  slots = event['currentIntent']['slots']

  response = {
    "sessionAttributes": sessionAttributes,
    "dialogAction": {
      "type": "Close",
      "fulfillmentState": "Fulfilled",
      "message": {
        "contentType": "PlainText",
        "content": ""
      }
    }
  }

  if intent == 'BalanceChecker':
    res = BalanceChecker()
    response['dialogAction']['message']['content'] = "Your balance is: {}€.".format(res)
  elif intent == "FinanceDefinitions":
    definition = slots['definition']
    res = FinanceDefinitions(definition)
    response['dialogAction']['message']['content'] = res
  elif intent == "SubscriptionChecker":
    res = SubscriptionChecker()
    response['dialogAction']['message']['content'] = "You are subscribed to: {}.".format(res)
  elif intent == "SpendCheckerSubs":
    sub = slots['subscription']
    res = Spending(sub)
    response['dialogAction']['message']['content'] = "You paid {}€ for your subscription with {}.".format(res, sub)
  elif intent == "SpendCheckerRestaurant":
    rest = slots['restaurant']
    res = Spending(rest)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, rest)
  elif intent == "SpendCheckerShopping":
    shop = slots['shopping']
    res = Spending(shop)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, shop)
  elif intent == "SpendCheckerTransport":
    trans = slots['transport']
    res = Spending(trans)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, trans)
  elif intent == "SpendCheckerTravelling":
    trav = slots['travelling']
    res = Spending(trav)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, trav)
  elif intent == "SpendCheckerRestaurantDate":
    rest = slots['restaurant']
    date = slots['date']
    res = Spending(rest)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, rest)
  elif intent == "SpendCheckerShoppingDate":
    shop = slots['shopping']
    date = slots['date']
    res = Spending(shop)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, shop)
  elif intent == "SpendCheckerTransportDate":
    trans = slots['transport']
    date = date['date']
    res = Spending(trans)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, trans)
  elif intent == "SpendCheckerTravellingDate":
    trav = slots['travelling']
    date = slots['date']
    res = Spending(trav)
    response['dialogAction']['message']['content'] = "You spend {}€ on {}".format(res, trav)


  return response
