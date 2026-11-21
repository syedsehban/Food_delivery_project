# Food Delivery Data Analysis

This project uses Python, Pandas, Matplotlib, and Seaborn to clean and
explore a food-delivery dataset stored in `food_delivery.csv`.

## Project overview

The notebook/script shown in the screenshots performs data inspection,
cleaning, date/time conversion, and exploratory visualisation. It
focuses on delivery-person ratings and how they relate to
delivery-person age, road traffic density, weather conditions, and
vehicle condition.

## Requirements

Install the required Python packages:

``` bash
pip install pandas matplotlib seaborn
```

Python 3 is required.

## Dataset

Place the dataset file named `food_delivery.csv` in the same directory
as the notebook or Python script.

The code expects columns including:

-   `Order_date`
-   `Time_Ordered`
-   `Delivery_person_age`
-   `Delivery_person_ratings`
-   `Road_traffic_density`
-   `Weatherconditions`
-   `Vehicle_condition`

The script also removes selected ID and location-related columns,
standardises column-name capitalisation, and renames `Time_orderd` to
`Time_Ordered`. Make sure the column names in your CSV match the names
used in the code.

## Analysis workflow

1.  **Load and inspect the data**
    -   Read `food_delivery.csv` with `pandas.read_csv()`.
    -   Display the first five rows, column names, and DataFrame
        information.
2.  **Prepare the columns**
    -   Drop selected ID and location columns that are not used in the
        displayed analysis.
    -   Capitalise column names.
    -   Rename the time-order column to `Time_Ordered`.
3.  **Check data types and duplicates**
    -   Inspect the types of delivery-person age, ratings, and order
        time.
    -   Count duplicate rows.
4.  **Clean numeric and missing values**
    -   Convert `Delivery_person_age` and `Delivery_person_ratings` to
        numeric values.
    -   Use `errors='coerce'` so values that cannot be converted become
        missing (`NaN`).
    -   Count missing values and calculate the percentage of missing
        values in each column.
    -   Drop rows containing missing values with `df.dropna()`.
5.  **Convert date and time fields**
    -   Convert `Order_date` to a Pandas datetime column.
    -   Convert `Time_Ordered` to datetime, coercing invalid values to
        `NaT`.
6.  **Create visualisations**
    -   Scatter plot: delivery-person age versus delivery-person
        ratings.
    -   Box plot: delivery-person ratings grouped by road traffic
        density.
    -   Heatmap: frequency table of weather conditions versus vehicle
        condition.

## Visualisations

  -----------------------------------------------------------------------
  Plot                                Purpose
  ----------------------------------- -----------------------------------
  Scatter plot                        Explore the relationship between
                                      delivery-person age and ratings.

  Box plot                            Compare the distribution of ratings
                                      across road-traffic-density
                                      categories.

  Heatmap                             Show counts for combinations of
                                      weather conditions and vehicle
                                      conditions.
  -----------------------------------------------------------------------

## Run the project

1.  Put `food_delivery.csv` beside your notebook or `.py` file.
2.  Install the dependencies listed above.
3.  Run the notebook cells in order, or execute the Python script.

## Notes

-   `pd.to_numeric(..., errors='coerce')` converts invalid numeric
    entries to `NaN`.
-   `pd.to_datetime(..., errors='coerce')` converts invalid date/time
    entries to `NaT`.
-   `df.dropna()` removes every row with at least one missing value.
    This can reduce the dataset substantially, so check the
    missing-value report before using the cleaned data for further
    analysis.
-   The screenshots show the analysis code but do not include the
    dataset or the resulting charts. No numerical findings or
    conclusions are claimed here.
-   The `data = df['Time_Ordered']` statement creates a Series
    reference; it is printed before the time column is converted.
