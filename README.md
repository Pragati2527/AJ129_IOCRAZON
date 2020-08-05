# AJ129_IOCRAZON

In February, Union oil minister Dharmendra Pradhan shared the data of petrol pump frauds of different states. Delhi alone reported 785 cases of short-fuelling at petrol pumps between April 2014 and December 2017. It was behind Maharashtra and Uttar Pradesh with 1,560 and 913 cases, respectively. And this is the data which shows the number of registered cases. However, there must be a huge chunk of cases that go unreported without complaining, and hence, without taking a particular action. Still, Problem doesn’t ends here.
There is one more problem which not only increases the burden on consumer’s pocket but also contribute to environmental pollution on large scale: i.e. emission of harmful effluents due to the use of adulterated fuel.
So, is there any solution to address these problems?
Ofcourse yes!
Our team iocrazon is presented here to address all these problems.
Let us look at the problem once again. It actually comprises of three segments:
1. Measurement of the quantity of fuel added in vehicle fuel tank
2. detection of adulteration in the fuel
3. need for the system which process all these information and display it to the customer on real time basis.

**QUANTITY**

Quantity measurements provided, many times are not upto the mark of customer satisfaction . it includes frauds resulting in  paying for more and getting somewhat less.
IN THIS, A MODULE IS DESIGNED USING FLOW RATE SENSOR AND NODEMCU WHICH WILL BE USED AT THE TIME OF REFILLING TO CALCULATES THE AMOUNT OF FUEL ADDED ON A REAL TIME BASIS.
HERE,FLOW RATE SENSOR IS A MODULE WORKS ON THE PRINCIPLE OF HALL EFFECT TO MEASURE THE flow OF  LIQUID FLOWING THROUGH IT.NODEMCU IS UESD TO SEND THE COMPLETE DETAILS ABOUT THE FUEL RECEIVED, ADULTERATION IN FUEL, CURRENT PRICE OF FUEL ETC. ON MOBILE APP OF CUSTOMER.

**Proposed Setup**

![quantity](https://user-images.githubusercontent.com/52466713/89117050-34047600-d4b8-11ea-8c76-0759b676f44c.png)

**QUALITY**

Fuel quality sometimes IS not as per the standard or chance of adulteration is there which again causes trouble like IMPROPER functioning of vehicle, paying FOR GOOD QUALITY fuel but getting adulterated ONE WHICH has  severe effects like increased toxicity IN  air, DECREASE IN ENGINE LIFE and many OTHER environmental PROBLEMS LIKE GLOBAL WARMING,OZONE POLLUTION ETC.
HENCE, FOR QUALITY PURPOSE WE HAVE DESIGNED A SETUP USING LOAD CELL TO MEASURE THE DENSITY OF FUEL ADDED. ALONGWITH IT, WE WILL USE TEMPERATURE SENSOR TO CALCULATE STANDARD DENSITY AT 15 C USING ASTM INTERCONVERSION TABLE  and astm standard WHICH ARE stored in memory OF OUR SOFTWARE TO calculate THE AMOUNT OF ADULTERANTS ADDED AND THE SAFE LIMIT OF FUEL.

**Proposed Setup**

![densityfi](https://user-images.githubusercontent.com/52466713/89117066-6910c880-d4b8-11ea-9f9d-0c270aceaaae.png)

**SOFTWARE**

This segment WILL addresS the problem of  things GETTING done  automatically without human interference. Present day technology is manual where we use chemical properties of volatility and colour to detect fuel quality AND MANUAL TESTING OF FUEL.
HERE THE SETUP WE ARE DESIGNING COMES HANDY AND DURABLE. Data is collected at the time of refilling and  stored at database from where it will be fetched and displayed on customer mobile app. The complete Data will also be send to the central authority server with compleTE information about price, quality and Quantity of fuel ADDED AT THE GIVEN PETROL PUMP LOCATION.

**For Central Authority**

![3](https://user-images.githubusercontent.com/52466713/89124219-ece7a680-d4f2-11ea-9b7a-256a73fe7513.png)

**FEATURES**

a. CONSUMER SATISFACTION

b. INSTANT AND INLINE MEASUREMENT OF QUANTITY

c. PREVENT INCREASED NUMBER OF FUEL FRAUD

d. FIRE PROOF AND HEAT PROOF AS THE POWER SUPPLY SOURCE USED HERE IS BATTERY WHICH IS PLACED SAFELY IN WELL INSULATED BOX

e. ASTM STANDARD IS UESD FOR QUALITY DETECTION

f. DURABLE CIRCUIT

g. LOSSLESS SIGNAL TRANSMISSION

**Novelty**

1. Digital monitor for fuel dispenser unit to maintain logistics and demand estimation : Our device will send datas like daily fuel consumption, Total Fuel quantity  received at    one dispensing unit & total quantity given to customer periodically , the price at which fuel is given, the density of fuel etc.  to the server of the centralised authority.

2. Customer friendly as free from human interference.

**FUTURE SCOPE**

1. WILL MAKE IT MOBILE APP ORIENTED

2. FUEL ADULTERATION TESTING USING DENSITY AND TEMPERATURE WHICH IS MANUAL TODAY

3. FURTHER OPTIMISATION

4. WILL WORK FOR INCREASING ACCURACY OF THE FINAL PRODUCT

5. WILL MAKE IT COMPACT AND BRING ALL THE COMPONENTS ON A SINGLE BOARD

**CONCLUSION**

WITH FEW REMARKS AS THE PRODUCT WE ARE DESIGNING FULFIL THE BASIC NECESSITY OF CONSUMER SATISFACTION, IT IS HIGHLY DURABLE,COST EFFECTIVE,HAZARD PROOF, THE COMPONENTS AND MATERIAL USED FOR DESINGING ARE SAFE AND PROPERLY ALLIGNED. THE PRODUCT IS HIGHLY EFFECTIVE AND SATISFIES THE NEED OF LARGE POPULATION SIMULTNEOUSLY.
IN FUTURE SCOPE, WE ARE ALSO TRYING TO MAKE IT MORE COMPACT AND WORKING FOR FURTHER OPTIMISATION.
