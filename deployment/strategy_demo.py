def deploy(strategy):
    print("Employee Attrition MLOps - Deployment Demo")
    print(f"Deployment strategy: {strategy}")
    print("Application deployed successfully.")


if __name__ == "__main__":
    strategies = [
        "Recreate Deployment",
        "Rolling Deployment",
        "Blue-Green Deployment",
        "Canary Deployment",
    ]

    for strategy in strategies:
        deploy(strategy)
        print("-" * 40)
