import pandas as pd

NUMERIC_COLS_TO_SCALE = [
    'age', 'monthly_salary', 'years_of_employment', 'monthly_rent',
    'family_size', 'dependents', 'total_monthly_expense', 'current_emi_amount',
    'credit_score', 'bank_balance', 'emergency_fund', 'requested_amount',
    'requested_tenure', 'debt_to_income', 'expense_to_income', 'affordability_ratio'
]

FINAL_COLUMNS = [
    'age', 'monthly_salary', 'years_of_employment', 'monthly_rent', 'family_size',
    'dependents', 'school_fees', 'college_fees', 'travel_expenses', 'groceries_utilities',
    'other_monthly_expenses', 'current_emi_amount', 'credit_score', 'bank_balance',
    'emergency_fund', 'requested_amount', 'requested_tenure', 'total_monthly_expense',
    'debt_to_income', 'expense_to_income', 'affordability_ratio', 'gender_Male',
    'marital_status_Single', 'education_High School', 'education_Post Graduate',
    'education_Professional', 'employment_type_Private', 'employment_type_Self-employed',
    'company_type_MNC', 'company_type_Mid-size', 'company_type_Small', 'company_type_Startup',
    'house_type_Own', 'house_type_Rented', 'existing_loans_Yes', 'emi_scenario_Education EMI',
    'emi_scenario_Home Appliances EMI', 'emi_scenario_Personal Loan EMI', 'emi_scenario_Vehicle EMI'
]


def preprocess_input(raw: dict, scaler) -> pd.DataFrame:
    """
    raw: dict of user-entered form values with plain, human keys.
    Returns a single-row DataFrame matching X_train's 39-column schema, scaled.
    """
    row = {}

    # Direct numeric passthroughs
    row['age'] = raw['age']
    row['monthly_salary'] = raw['monthly_salary']
    row['years_of_employment'] = raw['years_of_employment']
    row['monthly_rent'] = raw['monthly_rent']
    row['family_size'] = raw['family_size']
    row['dependents'] = raw['dependents']
    row['school_fees'] = raw['school_fees']
    row['college_fees'] = raw['college_fees']
    row['travel_expenses'] = raw['travel_expenses']
    row['groceries_utilities'] = raw['groceries_utilities']
    row['other_monthly_expenses'] = raw['other_monthly_expenses']
    row['current_emi_amount'] = raw['current_emi_amount']
    row['credit_score'] = raw['credit_score']
    row['bank_balance'] = raw['bank_balance']
    row['emergency_fund'] = raw['emergency_fund']
    row['requested_amount'] = raw['requested_amount']
    row['requested_tenure'] = raw['requested_tenure']

    # Engineered features
    row['total_monthly_expense'] = (
        row['school_fees'] + row['college_fees'] + row['travel_expenses']
        + row['groceries_utilities'] + row['other_monthly_expenses']
    )
    row['debt_to_income'] = (row['current_emi_amount'] + row['monthly_rent']) / row['monthly_salary']
    row['expense_to_income'] = row['total_monthly_expense'] / row['monthly_salary']
    row['affordability_ratio'] = (
        row['monthly_salary'] - row['total_monthly_expense']
        - row['current_emi_amount'] - row['monthly_rent']
    )

    # One-hot encodings (baseline categories dropped, matching training)
    row['gender_Male'] = raw['gender'] == 'Male'
    row['marital_status_Single'] = raw['marital_status'] == 'Single'
    row['education_High School'] = raw['education'] == 'High School'
    row['education_Post Graduate'] = raw['education'] == 'Post Graduate'
    row['education_Professional'] = raw['education'] == 'Professional'
    row['employment_type_Private'] = raw['employment_type'] == 'Private'
    row['employment_type_Self-employed'] = raw['employment_type'] == 'Self-employed'
    row['company_type_MNC'] = raw['company_type'] == 'MNC'
    row['company_type_Mid-size'] = raw['company_type'] == 'Mid-size'
    row['company_type_Small'] = raw['company_type'] == 'Small'
    row['company_type_Startup'] = raw['company_type'] == 'Startup'
    row['house_type_Own'] = raw['house_type'] == 'Own'
    row['house_type_Rented'] = raw['house_type'] == 'Rented'
    row['existing_loans_Yes'] = raw['existing_loans'] == 'Yes'
    row['emi_scenario_Education EMI'] = raw['emi_scenario'] == 'Education EMI'
    row['emi_scenario_Home Appliances EMI'] = raw['emi_scenario'] == 'Home Appliances EMI'
    row['emi_scenario_Personal Loan EMI'] = raw['emi_scenario'] == 'Personal Loan EMI'
    row['emi_scenario_Vehicle EMI'] = raw['emi_scenario'] == 'Vehicle EMI'

    df = pd.DataFrame([row])[FINAL_COLUMNS]
    df[NUMERIC_COLS_TO_SCALE] = scaler.transform(df[NUMERIC_COLS_TO_SCALE])

    return df