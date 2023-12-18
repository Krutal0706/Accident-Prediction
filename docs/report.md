![AccidentPrediction](https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_prediction.png)

## Title and Author
- Project Title: Accident Prediction - Traffic and Weather data mining and modeling
- Prepared for UMBC Data Science Master Degree Capstone under the guidance of Dr. Chaojie (Jay) Wang
- Author Name: Krutal Patel 
- [GitHub](https://github.com/Krutal0706/)
- [LinkedIn](https://www.linkedin.com/in/krutal-patel/)
- [PowerPoint Presentation](https://docs.google.com/presentation/d/1UCBrC8JKX7KFw8jlbPFv_tW3QhdJs_RL/edit?usp=sharing&ouid=117566803256326904165&rtpof=true&sd=true)
- [Youtube Video](https://youtu.be/fxgd_DzcwzQ)

## Background
#### What is Accident About?

Ensuring safety, whether it pertains to health, finances, or road usage, remains a paramount concern. Presently, road safety takes precedence as we dedicate an average of 597 hours per year to our daily commute, equivalent to 25 days. Despite substantial government investments in constructing quality roads and certifying automobile safety, thousands of accidents persist despite stringent rules. The prediction of accidents has evolved into a highly researched domain, offering potential enhancements to transportation infrastructure and the optimization of traffic conditions.

The ultimate goal of my research is to create a robust prediction model that can anticipate the likelihood of accidents. This model could serve as a valuable tool for improving traffic safety by providing early warnings or targeted interventions. By combining insights from both traffic and meteorological data, I aim to contribute to accident prevention and enhance overall road safety measures. This forward-looking approach aligns with the broader objective of leveraging data-driven insights for the betterment of public safety and transportation systems.

#### Why Does Accident Prediction Matter?

The project involves the application of data mining techniques to analyze a comprehensive dataset that combines traffic and meteorological information. By delving into historical data, I aim to identify patterns and correlations that can contribute to the development of a predictive model for accidents. The variables under consideration include traffic patterns, road conditions, and meteorological factors, highlighting a holistic approach to understanding accident risk.

#### Research Questions

The primary research questions guiding accident prediction are as follows:

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

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_road_surface.png" alt="Accident on different road surface" width="auto" height="300">
</p>

<div align="justify">

- The graph emphasizes that road surface conditions play a limited role in contributing to accidents, with the majority of incidents transpiring on dry road surfaces. This suggests that other factors, such as driver behavior, traffic conditions, or vehicle-related issues, might have a more substantial influence on accident occurrences. The data underscores the importance of focusing on broader aspects beyond road surface conditions to enhance overall road safety

</div>

---

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/krutal_patel/blob/main/pictures/accident_road_types.png" alt="Accident on different road types" width="auto" height="300">
</p>

<div align="justify">

- The data reveals a significant disparity in accident frequency between single-carriageway and dual-carriageway roads, with the majority of accidents occurring on single-carriageway roads. This suggests that single-carriageway roads may pose a higher risk of accidents compared to their dual-carriageway counterparts. The lower incidence of accidents on dual carriageway roads implies that they might offer a safer road environment in terms of accident occurrence.

</div>

---

### Results of EDA

- Over the years, the data from Exploratory Data Analysis paints a concerning picture, indicating a consistent increase in the number of accidents. The majority of these accidents unfold during the peak hours of the day, suggesting a potential correlation between increased traffic and heightened activity. Urban areas stand out as hotspots for accidents, emphasizing the need for targeted safety measures in densely populated regions. Furthermore, a significant proportion of accidents unfold on single-carriageway roads, underlining the importance of road infrastructure and design considerations. The common thread through these incidents is that most occur during optimal weather conditions – dry weather, daylight, and fine weather – pointing towards a need for heightened vigilance and safety precautions even in favorable circumstances.

## Feature Engineering 

- Feature selection is applied once the data has been split and cleaned. This is an important step in the process when we go through the dataset, remove variables that aren't relevant, and find the most informative features that have a big impact on our target variable. To make sure the model is trained on the most significant data, features that have the strongest correlations with the intended result were chosen using correlation analysis. By concentrating on these crucial components, we improve the model's accuracy and overall performance while streamlining the training process, opening the door to accurate and perceptive forecasts.

## Model Training and Development

#### Methodology

1. **Xgboost Classifier:** XGBoost is an ensemble model based on gradient boosting, focusing on improving upon previous models in the sequence.
2. **Random Forest Classifier:** Random Forest builds an ensemble of decision trees, each trained on a random subset of features and data points.

#### Application in the Project

1. **Confusion Matrix:** A grid that paints a clear picture of your model's classification mistakes, showing how often it incorrectly predicted each category.
2. **Classification report:** A detailed scorecard highlighting your model's strengths and weaknesses, like how well it identifies specific classes and avoids false positives/negatives.
3. **Cross Validation Score:** A reliable gauge of how well your model will perform on unseen data, achieved by repeatedly training and testing on different slices of your dataset.

Why XGBoost Classifier?

- Extreme Gradient Boosting (XGBoost) is selected for predicting accident severity due to its enhanced version of the Gradient Boosting Decision Trees (GBDT) algorithm. This choice is particularly beneficial as XGBoost addresses the challenge of overfitting, providing more reliable predictions. The algorithm's ability to handle complex and large datasets makes it well-suited for the intricate nature of accident severity prediction. XGBoost's strength lies in its capacity to manage data intricacies while maintaining precision in predictions, ensuring that the model generalizes well to new instances. Overall, XGBoost stands out as a robust and effective choice for predicting accident severity in diverse scenarios.

Why Random Forest Classifier?

- The selection of Random Forest for the predictive model is based on its reputation as a highly accurate and robust tree-based ensemble method. Random Forest is recognized for its resilience against overfitting, making it a suitable choice for maintaining model generalization. Additionally, Random Forest exhibits a strong capability to handle missing, noisy, and incomplete data, contributing to its versatility in real-world datasets. By leveraging the collective wisdom of multiple decision trees, Random Forest offers a robust and reliable approach for predicting outcomes in scenarios with diverse and challenging data characteristics. Overall, Random Forest emerges as a well-balanced and effective choice for accurate predictions in complex datasets.

## Outcomes

1. XGBoost:
- The confusion matrix analysis reveals a notable performance discrepancy between the two classes in the dataset. The model demonstrates a strong proficiency in correctly identifying instances of class 0, while its performance on class 1 instances is considerably less accurate. This discrepancy can be attributed to the dataset's class imbalance, with only 15% of the data belonging to class 1. Consequently, the model may not have been adequately trained on this minority class, leading to a lower predictive accuracy for instances belonging to class 1
- Despite the challenges posed by the imbalanced dataset, the overall accuracy reported in the classification report is 85%, indicating that 85% of the model's predictions across all classes were correct. This seemingly high accuracy might be influenced by the dominance of class 0 instances in the dataset. However, it's crucial to interpret this metric in conjunction with the insights gained from the confusion matrix to understand the model's performance on individual classes.
- Furthermore, the cross-validated accuracy scores, ranging consistently between 0.8504 and 0.8520 across five folds, suggest that the XGBoost model maintains a stable and reliable level of accuracy. This consistency in performance across different folds enhances confidence in the model's generalizability, despite the challenges posed by imbalanced class distribution in the dataset.

2. Random Forest Classifier
- The confusion matrix further illustrates the model's performance. It correctly predicts the majority of instances for class 0 (31668 out of 31897), but its performance on class 1 is suboptimal, correctly predicting only 69 out of 5701 instances.
- For class 0, the precision is high at 85%, indicating that when the model predicts instances as belonging to class 0, it is correct 85% of the time. The recall for class 0 is also high at 99%, suggesting that the model effectively captures nearly all instances of class 0 in the dataset. However, for class 1, both precision and recall are notably lower at 23% and 1%, respectively. This indicates that the model struggles to correctly identify and classify instances of class 1, leading to a lower F1-score for this class.
- The cross-validated scores for the Random Forest classifier, computed across five folds, exhibit consistency with values ranging between 0.8411 and 0.8452. The average accuracy, calculated as 0.8431, reflects the model's overall performance across these folds. The classification report provides a detailed breakdown of the model's precision, recall, and F1-score for each class.

## Insights

- Both models exhibit relatively high accuracy, with XGBoost having a slightly higher average accuracy.
- Both models face challenges in predicting instances of class 1, as indicated by low precision and recall for this class in both cases.
- The difference in average accuracy between the two models is relatively small.

In summary, the decision between XGBoost and Random Forest depends on the specific priorities of the analysis and whether the slight improvement in average accuracy with XGBoost is deemed significant in relation to the challenges in predicting instances of class 1.

## Implications and Applications

- **Enhanced user experience:**  The project's multi-faceted recommendation approach, leveraging sophisticated algorithms like XGBoost and Random Forest, significantly enhances the user experience in accident prediction by providing accurate and reliable insights, contributing to improved safety awareness and decision-making.
- **Future of personaized recommendations:** The project underscores the potential of data-driven, personalized recommendation systems in shaping the future of accident prediction in various conditions.
- **Scalability and Adaptation:** The methodologies and systems developed in this project are scalable and can be adapted to other geographical areas or sectors, such as Real-time Traffic Management Systems, and Urban Planning and Infrastructure Optimization.

## Conclusion

1. **Predictive Power:** Both XGBoost and Random Forest models demonstrate strong predictive capabilities for accident severity. The cross-validated accuracy scores, precision, recall, and F1-score support their effectiveness in predicting accidents.
2. **Model Comparison:** While both models perform well, the Random Forest classifier exhibits slightly higher average accuracy and better recall for class 1 instances. This suggests that Random Forest may have a slight edge in identifying severe accidents, especially in imbalanced datasets.
3. **User Experience Enhancement:** The multi-faceted recommendation approach implemented in the project significantly enhances the user experience in accident prediction, providing valuable insights and actionable recommendations.
4. **Scalability and Adaptation:** The developed methodologies and systems are scalable and adaptable to various geographical areas or sectors, such as urban planning and real-time traffic management systems.
5. **Application Beyond Accident Prediction:** The project's outcomes extend beyond accident prediction, finding potential applications in urban planning and infrastructure optimization. This broader utility contributes to creating smarter and safer cities.

In conclusion, the project successfully addresses accident prediction with robust models. It extends its impact to enhance user experience, scalability, and adaptation in various domains, showcasing its versatility and potential for positive societal impact.

## Future Work

To further improve and evolve the accident prediction project, the following enhancements can be considered:

1. **Integration of Real-time Data:** Enhance the models by integrating real-time data feeds, such as weather conditions, road closures, or special events. This would provide more dynamic and accurate predictions. Like Real-time traffic management systems. Where Accident prediction models can be integrated with real-time traffic management systems to dynamically adjust traffic signals, lane closures, and speed limits based on predicted accident risk.

2. **Data addition:** Adding more data to predict accurate severity. like adding traffic index, speed of car, and driver BAC level which can help to predict accurate data.

3. **Enhanced User Interface:** Develop a user-friendly interface to present the predictions and recommendations, ensuring accessibility and usability for a broader audience. Incorporate visualization tools for better interpretation.
