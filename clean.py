import pandas as pd


def clean_data(input1, input2, output):

    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')


    merged_df.drop('id', axis=1, inplace=True)


    merged_df.dropna(inplace=True)


    job_filter = ~merged_df['job'].str.contains('insurance|Insurance', case=False)
    cleaned_df = merged_df[job_filter]


    cleaned_df = cleaned_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]

    cleaned_df.reset_index(drop=True, inplace=True)


    cleaned_df.to_csv(output, index=False)
if __name__ == "__main__":

    input1 = r"/Users/cccsy/Downloads/AI/AIAssignment/respondent_contact.csv"
    input2 = r"/Users/cccsy/Downloads/AI/AIAssignment/respondent_other.csv"
    output = r"/Users/cccsy/Downloads/AI/AIAssignment/respondent_cleaned.csv"

    clean_data(input1, input2, output)

    clean_data(input1, input2, output)
    output_df = pd.read_csv(output)
    num_rows, num_columns = output_df.shape
    print("Shape of the output file: ", num_rows, "rows", num_columns, "columns")