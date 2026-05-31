##dataset generatou for temp and pulse rate
import pandas as pd
import random

data = []

# Healthy data
for i in range(1000):

    temp = round(random.uniform(97.0, 99.5), 1)

    pulse = random.randint(60, 100)

    data.append([temp, pulse, "Healthy"])

# Moderate data
for i in range(1000):

    temp = round(random.uniform(99.0, 101.5), 1)

    pulse = random.randint(90, 120)

    data.append([temp, pulse, "Moderate"])

# Serious data
for i in range(1000):

    temp = round(random.uniform(101.0, 104.5), 1)

    pulse = random.randint(115, 150)

    data.append([temp, pulse, "Serious"])

# Small noisy dataset
for i in range(50):

    temp = round(random.uniform(98.0, 103.0), 1)

    pulse = random.randint(70, 140)

    condition = random.choice([
        "Healthy",
        "Moderate",
        "Serious"
    ])

    data.append([temp, pulse, condition])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Temperature",
        "Pulse",
        "Condition"
    ]
)

# Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

# Save CSV
df.to_csv(
    "dataset/health_data.csv",
    index=False
)

print("Realistic healthcare dataset created successfully!")