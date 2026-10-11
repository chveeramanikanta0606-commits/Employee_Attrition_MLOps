def predict_attrition(age, monthly_income, years_at_company):
    """Return a simple example attrition prediction."""
    if age < 25 and years_at_company < 2:
        return "Likely to leave"
    if monthly_income < 2000 and years_at_company < 1:
        return "Likely to leave"
    return "Likely to stay"


def main():
    prediction = predict_attrition(
        age=23,
        monthly_income=2500,
        years_at_company=1,
    )
    print(f"Example employee prediction: {prediction}")
    print("Model training completed.")


if __name__ == "__main__":
    main()
