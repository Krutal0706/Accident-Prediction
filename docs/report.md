![AccidentPrediction](https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_prediction.png)

## Title and Author
- Project Title: Accident Prediction - Traffic and Weather data mining and modeling
- Prepared for UMBC Data Science Master Degree Capstone under the guidance of Dr. Chaojie (Jay) Wang
- Author Name: Krutal Patel 
- [GitHub](https://github.com/Krutal0706/)
- [LinkedIn](https://www.linkedin.com/in/krutal-patel/)
- [PowerPoint Presentation]()
- [Youtube Video]()

## Background
#### What is Accident About?

Ensuring safety, whether it pertains to health, finances, or road usage, remains a paramount concern. Presently, road safety takes precedence as we dedicate an average of 597 hours per year to our daily commute, equivalent to 25 days. Despite substantial government investments in constructing quality roads and certifying automobile safety, thousands of accidents persist despite stringent rules. The prediction of accidents has evolved into a highly researched domain, offering potential enhancements to transportation infrastructure and the optimization of traffic conditions.

The ultimate goal of my research is to create a robust prediction model that can anticipate the likelihood of accidents. This model could serve as a valuable tool for improving traffic safety by providing early warnings or targeted interventions. By combining insights from both traffic and meteorological data, I aim to contribute to accident prevention and enhance overall road safety measures. This forward-looking approach aligns with the broader objective of leveraging data-driven insights for the betterment of public safety and transportation systems.

#### Why Does Accident Prediction Matter?

The project involves the application of data mining techniques to analyze a comprehensive dataset that combines traffic and meteorological information. By delving into historical data, I aim to identify patterns and correlations that can contribute to the development of a predictive model for accidents. The variables under consideration include traffic patterns, road conditions, and meteorological factors, highlighting a holistic approach to understanding accident risk.

#### Research Questions

The primary research questions guiding Yelp Explorer are as follows:

    * What kind of weather, road, and temperature could cause an accident?
    - This question explores data visualization techniques to find out which conditions are best to predict accident prediction.

    * What methods or techniques help to achieve high accuracy in severity prediction and accidents?
    - This question uses different machine learning algorithms to find out which model performs well in this project.

    * How do these findings increase roadway safety and reduce accident risks?
    - This question explores how to increase roadway safety and how to avoid accidents or decrease severity.

## Data
#### Data Source


The accident prediction project utilizes the [UK Gov Website](https://www.gov.uk/government/collections/road-accidents-and-safety-statistics), an extensive collection of data provided by the UK government for academic and research purposes. Specifically, one CSV files were used:

1. **`Accidents0514.csv`**

#### Data Size and Records

The size of the files is approximately 428.8 MB. The dataset encompasses a total of:

- **1504150 Total Accidents(rows)**: Representing individual accident on website.
- **33 Features(columns)**: Representing details of each accident.

The data spans a period from 2005 to 2014, providing a comprehensive view of accidental information over several years.

#### Data Structure

Each row in the `Accidents0514.csv` file represents unique accident data listed on the website. The data fields include:

| Column Name                | Description                                                                                 | Data Type |
|----------------------------|---------------------------------------------------------------------------------------------|-----------|
| Unnamed Column             | index values                                                                                | integer   |
| Accident_Index             | different accident IDs                                                                      | object    |
| Location_Easting_OSGR      | Location from east OSGR values                                                              | float     |
| Location_Northing_OSGR     | Location from North OSGR values                                                             | float     |
| Longitude                  | Longitude of the location                                                                   | float     |
| Latitude                   | Latitude of the location                                                                    | float     |
| Police Force               | Police force Number at the crash spot                                                       | integer   |
| Accident_Severity          | describes the extent or level of severity of an accident (1-fatal, 2-serious, 3-Slight)     | integer   |
| Number_of_Vehicles         | number of vehicles included in the accident                                                 | integer   |
| Number_of_Casualties       | count of individuals who are either injured or killed as a result of an accident            | integer   |
| Date                       | the date of the incident                                                                    | object    |
| Day_of_week                | the day of the week                                                                         | integer   |
| Time                       | accident time                                                                               | object    |
| Local_Authority_(District) | administrative district or local government authority responsible for a specific geographic | integer   |
| Local_Authority_(Highway)  | Gov. auth or council res for the management and maintenance of a specific section           | object    |
| 1st_Road_Class             | describes the classification or type of the first road                                      | integer   |
| 1st_Road_Number            | alphanumeric identifier assigned to the first road                                          | integer   |
| Road_Type                  | types of roads                                                                              | object    |
| Speed_limit                | limit of the speed on a road                                                                | integer   |
| Junction_Control           | refers to a categorical variable that describes the type of control                         | object    |
| 2nd_Road_Class             | classification or type of the second road                                                   | integer   |
| 2nd_Road_Number            | numerical or alphanumeric identifier assigned to the second road                            | integer   |
| Pedest_Cros-Human_Control  | the type of control or regulation at a pedestrian crossing                                  | object    |
| Pedest_Cros-Phy_Facilities | the type of physical infrastructure or facilities in place                                  | object    |
| Light_Conditions           | lighting conditions at the time of the accident                                             | object    |
| Weather_Conditions         | prevailing weather conditions at the time of the accident                                   | object    |
| Road_Surface_Conditions    | the road surface at the time of the accident                                                | object    |
| Special_Conditions_at_Site | special or unusual conditions or circumstances at the accident site                         | object    |
| Carriageway_Hazards        | the road or carriageway at the time of the accident                                         | object    |
| Urban_or_Rural_Area        | The accident occurred in an urban or rural area                                             | integer   |
| Police_Attend_Scene_of_Acc | Police officer attended the scene of the accident                                           | object    |
| LSOA_of_Accident_Location  | Lower Layer Super Output Area (LSOA) of the accident location                               | object    |
| Year                       | the year of this incident                                                                   | integer   |

## Exploratory Data Analysis

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_severities.png" alt="Accident Severity" width="auto" height="400">
</p>
<div align="justify">
   
***Category 0 (Fatal):*** This portion of the pie chart represents the percentage of accidents classified as "fatal." The statement doesn't provide the exact percentage, but it implies that it is a minority compared to the "slight" category.

***Category 1 (Serious + Fatal):*** This segment represents the combined percentage of accidents categorized as both "serious" and "fatal." The statement mentions that, in total, these categories constitute around 15% of all accidents.

***Overall Implication:*** The inference is that the majority, approximately 85%, of accidents fall into the "slight" category. This information is valuable for understanding the distribution of accident severity and can inform safety measures and interventions to address the specific types of accidents that lead to more severe outcomes.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_years.png" alt="Accident thruough the years" width="auto" height="300">
</p>

<div align="justify">

***Time Frame:*** The data under consideration covers 10 years, starting from 2005 and ending in 2014. This extended time frame allows for a comprehensive analysis of trends and patterns in accident rates.

***Downward Trend:*** The term "downward trend" indicates that, over the specified period, the number of accidents has consistently decreased or the accident rates have lowered each year.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_hours.png" alt="Accident thruough the years" width="auto" height="300">
</p>

<div align="justify">

- The data analysis indicates a clear correlation between the timing of accidents and peak office hours during the day. This suggests that the increased volume of traffic and commuter activities during these hours might contribute to a higher risk of accidents. Understanding the specific hours when accidents are more likely can aid in implementing targeted measures to enhance road safety during those times. The findings emphasize the importance of time-sensitive interventions, such as increased traffic monitoring or awareness campaigns, to address safety concerns during peak hours. Ultimately, this information provides valuable insights for designing effective strategies to reduce accidents and improve overall road safety.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_weather.png" alt="Accidents during weather condition" width="auto" height="300">
</p>

<div align="justify">

- The visual representation provides insights into the correlation between weather conditions and accident severity. Fine weather conditions emerge as the predominant factor associated with a higher frequency of accidents. On the contrary, specific weather conditions like snowfall accompanied by high winds, as well as fog or mist, contribute to a lesser incidence of accidents. Particularly, snowfall without high winds stands out as the scenario with the lowest occurrence of accidents. This information underscores the influence of weather patterns on accident rates, highlighting the importance of considering these factors in road safety measures and planning.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_area.png" alt="Accident on different area" width="auto" height="300">
</p>

<div align="justify">

- The pie chart delineates the distribution of accidents between urban and rural areas. With two-thirds of accidents occurring in urban settings, it underscores the heightened risk and frequency within city environments. Conversely, rural areas experience one-third of the total accidents, indicating a comparatively lower occurrence in less densely populated regions.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_junction.png" alt="Accident in different junction" width="auto" height="300">
</p>

<div align="justify">

- The data provides insights into the distribution of accidents based on junction control types. Notably, half of the accidents took place at locations with "give way" or "uncontrolled" junction control. Within this category, "No junction control" stands out, constituting 40% of the accidents, highlighting the significance of intersections without specific control measures. In contrast, "traffic signal" junctions contribute to 10% of the accidents, emphasizing the role of controlled intersections in accident occurrences.

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_light.png" alt="Accident on different light conditions" width="auto" height="300">
</p>

<div align="justify">

- The data underscores a significant disparity in accident frequency based on lighting conditions, with the highest incidence occurring during daylight, constituting approximately 72% of all accidents. In contrast, accidents in conditions of darkness, whether with known or unknown light conditions, collectively account for only 1% of the total incidents. This highlights the pronounced influence of daylight conditions on accident occurrences compared to situations involving reduced visibility.

</div>

---
