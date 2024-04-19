import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Load the training data
train_data_1 = pd.read_csv('../../../data/season-data/2012_to_2023_data.csv')
train_data_2 = pd.read_csv('../../../data/season-data/combined_2024.csv')

# Combine the training data
train_data = pd.concat([train_data_1, train_data_2])

# One-hot encode the team and team_opp columns
train_data = pd.get_dummies(train_data, columns=['team', 'team_opp'])

# Split the data into input features and target variable
X = train_data.drop('won', axis=1)
y = train_data['won']

# Convert the date column to datetime
X['date'] = pd.to_datetime(X['date'])

# Extract useful features from the date column
X['year'] = X['date'].dt.year
X['month'] = X['date'].dt.month
X['day'] = X['date'].dt.day

# Drop the original date column
X = X.drop('date', axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the input features
scaler = StandardScaler()
scaler.fit(X_train)  # Fit the scaler to the training data
X_train = scaler.transform(X_train)  # Transform the training data
X_test = scaler.transform(X_test)  # Transform the testing data

# Create the neural network model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))