## 1. Author

* Project Title - Traffic and Weather data mining and modeling for Accident prediction.

* Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

* Author Name - Krutal Patel

* GitHub - [krutal0706](https://github.com/krutal0706/)

* LinkedIn - [Krutal Patel](https://www.linkedin.com/in/krutal-patel/)

* PowerPoint Presentation file -

* Link to YouTube video -

## 2. Background

  ### A. What is the Project about?
   
    * This project is about data mining techniques on traffic and meteorological data to create a prediction model for accidents.
    
    * The study looks for trends and correlations that might assist in anticipating the risk of accidents by examining historical data regarding traffic patterns, road conditions, and meteorological conditions. 
    
    * The long-term objective is to develop a valuable tool for enhancing traffic safety and maybe averting accidents through early warning systems or focused interventions.

  ### B. Why does it matter?

  #### ARE YOU DRIVING SAFE TODAY?

    * Road safety is one of the top most priority of everyone nowadays.

    * To make driving safer, the government invests billions of dollars in building excellent roads and certifying the safety of automobiles.
  
    * However, Thousands of accidents are happening after having strict rules and regulations.
  
    * Predicting accidents has thus developed into one of the most extensively studied areas, which various agencies could use to improve overall transportation infrastructure and optimize traffic conditions.

  ### C. What are your research questions?

    * What methods or techniques help to achieve high accuracy in severity prediction and accidents?

    * How do these findings increase roadway safety and reduce accident risks?

    * What kind of weather, road, and temperature could cause an accident?
    
## 3. Data

* Several publicly accessible datasets are available, including statistics on accidents, traffic incidents, and weather.

* These datasets could be used to prepare helpful classification models to predict whether a particular condition is more prone to accidents and whether drivers must drive with precaution.

#### About the data set

* The dataset has been fetched from the UK Government Road Accidents and Safety Statistics website and the files have been merged and cleaned to reach the final data attached.

* This dataset shows road accidents in the UK between 1979 and 2015, comprising roughly 250K rows and 70 features/columns.

* Data sources - [UK GOV](https://www.gov.uk/government/collections/road-accidents-and-safety-statistics)

* Data size - 428.8 MB

* Data shape - 1504150(rows), 33(columns)

* What does each row represent?

  Each row typically represents accidental information.

* Data Dictionary:

  Unnamed Column
    - Dtype - integer
    - Definition - It shows index values.
    - Potential Values - 464696 unique values.
 
  Accident_Index
    - Dtype - object
    - Definition - It shows different accident IDs.
    - Potential Values - 1504150 unique values.

  Location_Easting_OSGR
    - Dtype - float
    - Definition - It shows Location from east OSGR values.
    - Potential Values - 464696 unique values.

  Location_Northing_OSGR
    - Dtype - float
    - Definition - It shows Location from North OSGR values.
    - Potential Values - 464696 unique values.

  Longitude
    - Dtype - float
    - Definition - It shows the Latitude of the location.
    - Potential Values - 464696 unique values.
 
  Latitude
    - Dtype - float
    - Definition - It shows the Longitude of the location.
    - Potential Values - 464696 unique values.
 
  Police Force
    - Dtype - integer
    - Definition - It shows the police force Number at the crash spot.
    - Potential Values - There is 51 number of police force.
 
  Accident_Severity
    - Dtype - integer
    - Definition - refers to a variable or attribute that describes the extent or level of severity of an accident (1-fatal, 2-serious, 3-Slight).
    - Potential Values - 3 unique values.

  Number_of_Vehicles
    - Dtype - integer
    - Definition - It shows the number of vehicles included in the accident.
    - Potential Values - 27 unique values.
 
  Number_of_Casualties
    - Dtype - integer
    - Definition - It refers to the count of individuals who are either injured or killed as a result of an accident (1-Number of Fatalities, 2-Number of Serious Injuries, 3-Number of Slight Injuries, 4-Total Number of Casualties).
    - Potential Values - 4 unique values.
 
  Date
    - Dtype - object
    - Definition - It shows the date of the incident.
    - Potential Values - 464696 unique values.
 
  Day_of_week
    - Dtype - integer
    - Definition - It shows the day of the week.
    - Potential Values - 7 unique values.
 
  Time
    - Dtype - object
    - Definition - It shows accident time.
    - Potential Values - 464696 unique values.
 
  Local_Authority_(District)
    - Dtype - integer
    - Definition - refers to the administrative district or local government authority responsible for a specific geographic area within the UK.
    - Potential Values - 464696 unique values.
 
  Local_Authority_(Highway)
    - Dtype - object
    - Definition - refers to the local government authority or council responsible for the management and maintenance of a specific section of the road or highway where a traffic accident occurred.
    - Potential Values - 464696 unique values.
 
  1st_Road_Class
    - Dtype - integer
    - Definition - It refers to a categorical variable that describes the classification or type of the first road (the road where the accident occurred) in terms of its function and importance.
    - Potential Values - 6 unique values.
 
  1st_Road_Number
    - Dtype - integer
    - Definition - It refers to a numerical or alphanumeric identifier assigned to the first road (the road where the accident occurred) within a road network.
    - Potential Values - 6854 unique values.
 
  Road_Type
    - Dtype - object
    - Definition - It shows types of roads.
    - Potential Values - 6 unique values.
 
  Speed_limit
    - Dtype - integer
    - Definition - It shows the limit of the speed on a road.
    - Potential Values - 8 unique values.

  Junction_Control
    - Dtype - object
    - Definition - It shows traffic accidents or road safety typically refers to a categorical variable that describes the type of control or regulation at a road junction (intersection).
    - Potential Values - 5 unique values.
 
  2nd_Road_Class
    - Dtype - integer
    - Definition - It refers to a categorical variable that describes the classification or type of the second road (the road that intersects with the first road) at the location where a traffic accident occurred.
    - Potential Values - 7 unique values.
 
  2nd_Road_Number
    - Dtype - integer
    - Definition - It refers to a variable that contains the numerical or alphanumeric identifier assigned to the second road (the road that intersects with the first road) at the location where a traffic accident occurred.
    - Potential Values - 7235 unique values.
 
  Pedestrian_Crossing-Human_Control
    - Dtype - object
    - Definition - It refers to a categorical variable that describes the type of control or regulation at a pedestrian crossing where the accident occurred.
    - Potential Values - 3 unique values.
 
  Pedestrian_Crossing-Physical_Facilities
    - Dtype - object
    - Definition - It refers to a categorical variable that describes the type of physical infrastructure or facilities in place at a pedestrian crossing where a traffic accident occurred.
    - Potential Values - 6 unique values.
 
  Light_Conditions
    - Dtype - object
    - Definition - It refers to a categorical variable that describes the prevailing lighting conditions at the time of the accident.
    - Potential Values - 5 unique values.
 
  Weather_Conditions
    - Dtype - object
    - Definition - It refers to a categorical variable that describes the prevailing weather conditions at the time of the accident.
    - Potential Values - 9 unique values.
 
  Road_Surface_Conditions
    - Dtype - object
    - Definition - It refers to a categorical variable that describes the condition of the road surface at the time of the accident.
    - Potential Values - 6 unique values.
 
  Special_Conditions_at_Site
    - Dtype - object
    - Definition - It refers to a categorical variable that describes any special or unusual conditions or circumstances at the accident site that may have contributed to the accident or influenced its outcome.
    - Potential Values - 8 unique values.
 
  Carriageway_Hazards
    - Dtype - object
    - Definition - It describes any hazards or obstacles present on the road or carriageway at the time of the accident.
    - Potential Values - 6 unique values.
 
  Urban_or_Rural_Area
    - Dtype - integer
    - Definition - It indicates whether the accident occurred in an urban or rural area.
    - Potential Values - 3 unique values.
 
  Did_Police_Officer_Attend_Scene_of_Accident
    - Dtype - object
    - Definition - It indicates whether a police officer attended the scene of the accident.
    - Potential Values - 2 unique values.
 
  LSOA_of_Accident_Location
    - Dtype - object
    - Definition - It refers to a variable that records the Lower Layer Super Output Area (LSOA) of the accident location. LSOAs are geographic areas used for statistical and administrative purposes in the United Kingdom.
    - Potential Values - 464696 unique values
 
  Year
    - Dtype - integer
    - Definition - It shows the year of this incident.
    - Potential Values - This dataset is from 2005-2014 so 9 unique values.
 
* Which variable/column will be your target/label in your ML model?

  Because segmentation is a supervised learning activity, there is a conventional goal variable.

* Which variables/columns may be selected as features/predictors for your ML models?

  The goal is to use supervised learning techniques like clustering on specific target variables.
