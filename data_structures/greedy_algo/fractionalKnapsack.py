class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value we can get with fractional knapsack
def fractionalKnapsack(W, arr, n):

    # Sort items based on the value/weight ratio in descending order
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    curWeight = 0  # Current weight of knapsack
    finalvalue = 0.0  # Final value we can achieve

    # Iterate through the sorted items
    for i in range(n):

        # If the current item can be fully added to the knapsack
        if curWeight + arr[i].weight <= W:
            curWeight += arr[i].weight
            finalvalue += arr[i].value  # Add the full value of the item
        else:
            # If the current item can't be fully added, take the fractional part
            remain = W - curWeight
            finalvalue += (arr[i].value / arr[i].weight) * remain
            break  # Break as we have filled the knapsack

    return finalvalue  # Return the maximum value that can be carried

# Main function
def main():
    # Input data
    n = 3
    weight = 50  # Capacity of knapsack
    arr = [Item(100, 20), Item(60, 10), Item(120, 30)]

    # Calculate the maximum value we can get with the fractional knapsack
    ans = fractionalKnapsack(weight, arr, n)

    # Output the result
    print(f"The maximum value is: {ans:.2f}")

# Call the main function
if __name__ == "__main__":
    main()