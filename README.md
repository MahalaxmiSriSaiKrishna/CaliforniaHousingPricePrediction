# California Housing Price Prediction using XGBoost

This project predicts **California housing prices** using the **California Housing Dataset** and the **XGBoost Regressor**. The model takes various features such as median income, house age, rooms, population, and location coordinates to estimate house prices.

---

## **Dataset**

The dataset used is the **California Housing dataset** from `sklearn.datasets.fetch_california_housing`.  
- **Features:**
  - `MedInc`: Median income in the block group
  - `HouseAge`: Median house age in the block group
  - `AveRooms`: Average number of rooms per household
  - `AveBedrms`: Average number of bedrooms per household
  - `Population`: Population of the block group
  - `AveOccup`: Average occupancy per household
  - `Latitude`: Latitude of the block group
  - `Longitude`: Longitude of the block group
- **Target:**
  -  `Price`: House price (in hundreds of thousands of USD)

---

## **Features & Model**

- **Model:** `XGBRegressor` from XGBoost  
- **Hyperparameter tuning:** Performed using `GridSearchCV` with 5-fold cross-validation  
- **Key hyperparameters tuned:**
  - `max_depth`, `learning_rate`, `n_estimators`
  - `min_child_weight`, `subsample`, `colsample_bytree`

- **Performance Metrics:**
  - Train R²: 0.927
  - Test R²: 0.847
  - Test RMSE: 0.20 (≈ \$20,000 in actual price units)

---


