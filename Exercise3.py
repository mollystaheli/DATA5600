import numpy as np
import matplotlib.pyplot as plt

# Set the randomization seed so we get the same results each time
rng = np.random.default_rng(123)

# Function to simulate Harmons peanut butter sales
def simulate_sales(n, intercept, price_effect, promotion_effect,
                   loyalty_effect, traffic_effect, sigma):

    # Simulate the price of the peanut butter
    product_price = rng.normal(5, 0.75, size=n)

    # Simulate whether the product was promoted
    # 0 = no promotion, 1 = promotion
    promotion = rng.binomial(1, 0.5, size=n)

    # Simulate whether the customer is a loyalty member
    # 0 = not a member, 1 = loyalty member
    loyalty_member = rng.binomial(1, 0.6, size=n)

    # Simulate the amount of store traffic
    store_traffic = rng.normal(500, 100, size=n)

    # Add normally distributed random error
    error = rng.normal(0, sigma, size=n)

    # Calculate total sales
    sales = (intercept
             + price_effect * product_price
             + promotion_effect * promotion
             + loyalty_effect * loyalty_member
             + traffic_effect * store_traffic
             + error)

    return sales, product_price, promotion, loyalty_member, store_traffic


# Generate 100 simulated observations
sales, product_price, promotion, loyalty_member, store_traffic = simulate_sales(
    n=100,
    intercept=10,
    price_effect=-2.5,
    promotion_effect=8,
    loyalty_effect=4,
    traffic_effect=0.03,
    sigma=5
)

# Print the first 10 observations
print("Sales:", sales[:10])
print("Product Price:", product_price[:10])
print("Promotion:", promotion[:10])
print("Loyalty Member:", loyalty_member[:10])
print("Store Traffic:", store_traffic[:10])