# assignment
weather prediction
https://karki23.github.io/Weather-Data/assignment.html has 49 hyperlinks that will redirect you to the weather details of that particular city.
Scrape each of the tables in each of these links, basically you would have to scrape 49 tables with an overall of 142000(approx) rows.
Store the details of all these citys in different CSV or text files (csv is recommended).
This CSV file/text file will form your dataset for the next task!

Once you get the dataset,
1. Shuffle and split the dataset into test and train sets (80% - train, 20% - test). This is done city wise.
Combine the training sets into one dataset.
2. Perform preprocessing and feature engineering (if necessary, to only get the relevant features)
3. Train a binary classification model (this could be any of the ML algorithms or neural networks we used as a part of the course)
to predict if it will rain the next day on the training
dataset of all cities.
4. Use the trained model to predict rainfall the next day, city wise.(Run the trained model on each of the 49 cities' test sets, and
make note of the 49 accuracies in a file called results.txt, each line should be of the format [city_name]:[accuracy_for_that_city]).
In the last line, report the average accuracy for all the cities as average_accuracy: [avg_acc]).

Note: in case you try more than one model, report the model with the highest accuracy (on the test set).
Use Pytorch/Tensorflow/scikit-learn for writing the machine learning code.

1. scraper.py (all the webscraping code goes here)
2. dataset (a directory where you can keep the scripts used for data manipulation if you have any and the datasets as .csv files is created)
3.traindata (a directory with scripts from dataset with only numbers in .csv files)
4.finaltrain.csv (contain all the data of the cities in one place)
5. model.py or model.ipynb (this should contain the code for training and testing)
6. results.txt (should contain the results in the format specified above)
