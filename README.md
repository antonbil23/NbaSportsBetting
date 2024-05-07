# NbaSportsBetting

Authors: Rahul Aneja, Anton Bilonog, Gio Romero-Ruiz

Our project is about NBA sports betting and the primary goal is to examine and understand the machine learning strategies used by a group in their Spring 2023 titled “Machine Learning in Sports Betting (NBA)”. With sports betting becoming an increasingly popular trend, there is significant potential for it to be lucrative over time for those who apply the right strategies.
Our primary goal is to critically analyze the methodologies employed, assess the reproducibility of the results using the latest models, and explore potential improvements. The broader aim is to contribute to the evolving field of sports analytics by enhancing the predictive capabilities of machine learning models in sports betting, thereby helping bettors make more informed decisions and potentially increase their profitability. This study not only seeks to validate earlier findings but also aims to refine the models to adapt to changes in data and betting landscapes in the ongoing NBA seasons.


Here is our NbaSportsBetting project, in our repository you will have access to four different folders, the "data" folder, the "src" which has folders like "models" and "scripts" and our main file cs4824.ipynb. All of the data is in our github repository so for someone to run our code all you have to do is go to cs4824.ipynb and hit "Run All" if that does not work please make sure you have all the libraries and extensions installed which could cause errors in running the code.

Now let's talk about the "data" folder which has access to all the data that was scraped which made this project possible, in there we have odds data from 2022-2024 seasons, we have schedules from 2023 and 2024 seasons. Lastly, we have season data that originates all the way back from 2012 to present day. We scraped this data from the code in src/scripts folder which has access to our web scrapers to get the schedules for the seasons and to get the box score for every game in said season.

In our src/models is where we constructed all of our models which were logistic regression, ride regression, xgboost, and neural network. We had seperate files for these models before we combined all of the code in one file which is the cs4824.ipynb. Where in that file all of our models are there and our data preprocessing and lastly our visualizations for our accuracies of each model.

If there are any issues please feel free to contact us!
