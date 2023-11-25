import pandas as pd
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def find_seed_points(data):

    
    feature_names = data.iloc[:, 0]

    
    features_values = data.iloc[:, 1:]
    #Calculate the correlation matrix
    correlation_matrix = np.corrcoef(data)

    
    strong_correlation_threshold = 0.9995
    variable_a_found = False
    variable_b_found = False
    #Initialize sets A and B
    set_a = []
    set_b = []

    #Search for a variable 'p'
    for variable_p in range(len(correlation_matrix)):
        #Check for strong positive correlation with another variable 'a'
        for variable_a in range(len(correlation_matrix)):
            if variable_p != variable_a and correlation_matrix[variable_p, variable_a] > strong_correlation_threshold:
                variable_a_found = True
                break

        if variable_a_found == False:
            continue

        #Check for strong negative correlation with a second variable 'b'
        for variable_b in range(len(correlation_matrix)):
            if variable_p != variable_b and correlation_matrix[variable_p, variable_b] < -strong_correlation_threshold:
                variable_b_found = True
                break

        if variable_b_found == False:
            continue

        #Check if variables 'a' and 'b' are strongly negatively correlated
        if correlation_matrix[variable_a, variable_b] < -strong_correlation_threshold:
            # Found variables 'p', 'a', and 'b'
            set_a.append(variable_p)
            set_a.append(variable_a)
            set_b.append(variable_b)
            break

    #Search for a variable 'q'
    for variable_q in range(len(correlation_matrix)):
        #Check for strong positive correlation with variable 'b'
        if correlation_matrix[variable_q, variable_b] > strong_correlation_threshold:
            variable_b_found = True
            break

        if not variable_b_found:
            continue

        #Check for strong negative correlation with variable 'a'
        if correlation_matrix[variable_q, variable_a] < -strong_correlation_threshold:
            #Found variable 'q'
            set_b.append(variable_q)
            break

    return set_a, set_b , correlation_matrix

def assign_remaining_variables(data, set_a, set_b, strong_correlation_threshold,correlation_matrix):
    #Extract the feature values from the remaining rows
    feature_values = data.iloc[1:]

    #Assign remaining variables to sets A and B
    for variable in range(len(feature_values)):
        if variable not in set_a and variable not in set_b:
            # Check for strong positive correlation with both variables in either set
            if any(correlation_matrix[variable, set_a] > strong_correlation_threshold) and no(correlation_matrix[variable, set_b] > strong_correlation_threshold):
                set_a.append(variable)
            elif any(correlation_matrix[variable, set_b] > strong_correlation_threshold) and no(correlation_matrix[variable, set_a] > strong_correlation_threshold):
                set_b.append(variable)

def main():
    #Read the data from an Excel file
    df = pd.read_excel("combined_data_60Songs.xlsx")  # Replace 'your_excel_file.xlsx' with your actual file name

    #Set the first column as the index
    df.set_index(df.columns[0], inplace=True)

    #Transpose the DataFrame using the transpose() method
    transposed_df = df.transpose()

    #Initialize MinMaxScaler
    scaler = MinMaxScaler()

    #Fit and transform the data using MinMaxScaler
    normalized_data = scaler.fit_transform(transposed_df)

    #Convert the normalized data back to a DataFrame
    data = pd.DataFrame(normalized_data, columns=transposed_df.columns, index=transposed_df.index)
    
    set_a, set_b, correlation_matrix = find_seed_points(data)

    #Assign remaining variables to sets A and B
    assign_remaining_variables(data, set_a, set_b, strong_correlation_threshold=0.7,correlation_matrix = correlation_matrix )

    #Create a new DataFrame with feature names and Set A/B values
    feature_names = data.iloc[0]
    set_a_values = [1 if i in set_a else 0 for i in range(len(feature_names))]
    set_b_values = [1 if i in set_b else 0 for i in range(len(feature_names))]

    new_data = pd.DataFrame({'Feature Name': feature_names, 'Set A': set_a_values, 'Set B': set_b_values})

    #Write the new DataFrame to a new Excel file
    new_data.to_excel('sets_a_and_b.xlsx', index=False)
    print(find_seed_points(data))
if __name__ == "__main__":
    main()
