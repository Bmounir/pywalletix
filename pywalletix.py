#!/usr/bin/python

"""
pywalletix is a wraper around the walletix.com API ,an online payment solution,
    	
composed of class with 3 methods :
	*- generatePaymentCode
	*- verifyPayment
	*- deletePayment

this code-source is under  MIT License  

Copyright (C) 2013 Bessoufi Mounir 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""



import requests 

class wallitex :

	ApiKey,VendorId = -1 , -1
	Apiurl = "https://www.walletix.com/"



	def __init__(self,ApiKey,VendorId) : 
		self.ApiKey   = ApiKey
		self.VendorId = VendorId 

	def generatePaymentCode(self,PurchaseID , Amount , CallbackUrl,format="json") :

		payload = {
			"vendorID":self.ApiKey,
			"apiKey":self.VendorId,
			"purchaseID":PurchaseID,
			"amount" :Amount,
			"callbackurl":CallbackUrl,
			"format":format,
		   }

		return self._Post("api/paymentcode",payload)
		


	def verifyPayment(self,PaymentID,format="json" ) :

		payload = {
			"vendorID":self.ApiKey,
			"apiKey":self.VendorId,
			"paiementCode":PaymentID,		
			"format":format,
		   }

		return self._Post("api/paymentverification",payload)

	def deletePayment(self,PaymentID,format="json" ) :

		payload = {
			"vendorID":self.ApiKey,
			"apiKey":self.VendorId,
			"paiementCode":PaymentID,		
			"format":format,
		   }
 

		return self._Post("api/deletepayment",payload)



	def _Post(self,url,payload,verify=False)	 : 
		request = requests.post(self.Apiurl+url,data=payload,verify=verify)
		return request
