# cars24

Level:1 To scrape the data from the Cars24 website we have used Beautifulsoups and Selenium library in Python.

Level 2: To clean the datasets after scraping according to the requirement we have used the Pandas library.

Level 3: To Visualise the data with some insights we have used the matplotlib and seaborn libraries from Python. We have also used Tableau for better visualization.

Requirements:

Table 1: Cars24 Data Attributes required in the table

**Brand**:
Data Type: String
Description: The brand or manufacturer of the used car.
**Car Model**:
Data Type: String
Description: The model of the used car.
**Car Name**:
Data Type: String
Description: The name or make of the used car.
**Car Variant**:
Data Type: String
Description: The specific variant or version of the used car.
**Car Transmission**:
Data Type: String
Description: The type of transmission system in the used car.
**KM Driven**:
Data Type: Integer
Description: The total distance the car has been driven.
**Owner Type**:
Data Type: String
Description: The type of car owner (e.g., first owner, second owner).
**Fuel Type**:
Data Type: String
Description: The type of fuel the used car operates on.
**Registration ID**:
Data Type: String
Description: The unique registration ID of the used car.
**Monthly EMI**:
Data Type: Float or String
Description: The monthly Equated Monthly Installment for the used car.
**Car Price**:
Data Type: Float or String
Description: The total price of the used car.
**Downpayment Amount**:
Data Type: Float or String
Description: The initial downpayment amount for the used car.
**Location**:
Data Type: String
Description: The location or city where the used car is listed.
Step-by-step scraping:

To scrape these as a table we first get a link of each car from the location. This is under the Link.py file.

To scrape the data inside the link found in the above is under the Cars Details.py file.

To automate this we have used the for loop and looped over each link and scraped then, saved the data as a pd.dataframe and into csv file. The code is under the Cars24_delhi_ncr_data.py and Cars_mumbai_data.py and the csv file are cars24_delhi-ncr.csv and cars24_mumbai.csv

After we have the main.py file which has automated all the processes of scraping the data from all cities required using multiple for loop.






Insight
For Delhi city and car owner type is 1st
- for middle class in Petrol cars budget and to buy permanently
   - "Maruti Baleno DELTA DDIS 190" with Total price 549299/- is good for Middle class people because its available as 
     Diesel fuel in petrol cars budget and also it is Manual type. For middle class young people "Tata Tiago XZA 1.2 
     REVOTRON" with Total price 542299 is good, beacause it is automatic and also Diesel car

- for middle class in Petrol cars budget and to buy on EMI basis(pricepermonth)
   - Best car in Manual transmission is "Maruti Dzire", with price per month 12012/- and Fueltype is Diesel.  For middle 
   class young people "Tata Tiago XZA 1.2 REVOTRON" with priceper
   month 11970/- is good, beacause it is automatic and also Diesel car


- for rich class in Diesel cars budget and to buy permanently
   - "Honda civic ZX MT DIESEL" with Total price 1751899/- is good for rich class people because its available as Diesel 
   fuel in Diesel cars budget and also it is Manual type. For rich class young people "Toyota Innova Crysta Touring 
   Sport Diesel AT" with Total price 1547299/- is good, beacause it is automatic and also Diesel car
      
 - for rich class in Diesel cars budget and to buy on EMI basis(pricepermonth)
   - Best car in Manual transmission is "Honda civic ZX MT DIESEL", with price per  month 38970/- and Fueltype is Diesel
   for rich class young people "Toyota Innova Crysta Touring SportDiesel AT" with pricepermonth 34419/- is good, 
   beacause it is automatic and also Diesel car
Conclusion
To summarize this, from the above all the graphs, first, we can tell that the "Maruti" company cars are high in number for sale. Second, 70% of cars coming for sale is of 1st owner type, Third, the maximum price company cars for sale are Volvo and Volkswegan. fourth, manual cars 80% higher than automatic cars. fifth, the car prices will be different for different cities depends on car ownertype, year of purchase, city average costs. sixth, To get good mileage people will prefer Diesel/CNG cars than petrol cars. Seventh, the 90 % cars coming for sale are in between 0 to 10000km driven. Eigth, Petrol cars are more than Diesel cars. Nineth, the price per month is around 0 to 20000 and Total price is 2 to 30 lakhs, for almost all of the cars. Tenth, 90% of cars year of purchase is in between 2010 to 2020.These are some of the points to consider based on the above data.

The csv files will be the same.

After this, we can do the data-cleaning process. The code is inside the Data_cleaning.py file and we will get two cleaned csv files named cleaned_cars24_delhi-ncr.csv, and cleaned_cars24_mumbai.csv.

The visualization is done with different Python libraries like Matplotlib, seaborn, pandas, and numpy in Project_Cars24. The Tableau screenshots are attached here:
