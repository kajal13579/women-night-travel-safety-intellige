import pandas as pd

print("Women's Night-Travel Safety Intelligence")
print("----------------------------------------")

# Load streetlight data
data = pd.read_csv("data/streetlights.csv")

# Calculate working streetlight percentage
data["functionality_percent"] = (
    data["working_lights"] / data["total_lights"]
) * 100

# Display results
print(data)

# Save the analysis results
data.to_csv(
    "data/infrastructure_analysis.csv",
    index=False
)

print("Analysis completed successfully!")
