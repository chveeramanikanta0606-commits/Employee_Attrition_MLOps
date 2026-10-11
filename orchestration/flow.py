from prefect import flow, task
import subprocess
import sys


@task
def run_employee_prediction():
    result = subprocess.run(
        [sys.executable, "src/train.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    print(result.stdout)


@flow(name="employee-attrition-flow")
def employee_attrition_flow():
    run_employee_prediction()


if __name__ == "__main__":
    employee_attrition_flow()
