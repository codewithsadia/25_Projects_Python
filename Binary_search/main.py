import streamlit as st  # Importing the Streamlit library for building the web interface.
import matplotlib.pyplot as plt  # Importing Matplotlib for data visualization.
import random  # Importing the random module to generate random arrays.

# Function to perform binary search on a sorted array.
def binary_search(arr, target):
    low = 0  # Initialize the lower boundary of the search range.
    high = len(arr) - 1  # Initialize the upper boundary of the search range.
    steps = []  # List to store each step of the search process for visualization.
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index.
        steps.append((low, high, mid))  # Append the current step's indices for visualization.
        if arr[mid] == target:  # Check if the target is at the middle index.
            return mid, steps  # Return the index and steps if the target is found.
        elif arr[mid] < target:  # If target is greater, search in the right half.
            low = mid + 1
        else:  # If target is smaller, search in the left half.
            high = mid - 1
    return -1, steps  # Return -1 if the target is not found.

# Function to create and display a bar chart visualizing the binary search process.
def plot_array(arr, steps, target):
    fig, ax = plt.subplots(figsize=(8, 6))  # Create a figure and axis for the bar chart.
    ax.bar(range(len(arr)), arr, color="lightblue", label="Array Elements")  # Plot array elements.

    for step in steps:  # Iterate through each step of the binary search.
        low, high, mid = step
        ax.bar(mid, arr[mid], color="orange", label="Mid")  # Highlight the middle element at each step.
        if arr[mid] == target:  # If the target is found at this step:
            ax.bar(mid, arr[mid], color="green", label="Target Found")  # Highlight the target.
    ax.set_xlabel('Index')  # Set the label for the x-axis.
    ax.set_ylabel('Value')  # Set the label for the y-axis.
    ax.set_title('🔍 Binary Search Visualization')  # Add a title to the chart.
    ax.legend()  # Display a legend explaining the colors.
    
    st.pyplot(fig)  # Render the chart in the Streamlit app.

# Main function to handle the Streamlit interface and user interaction.
def main():
    st.title('🌟 Enhanced Binary Search Visualization 🌟')  # Display the title at the top of the app.

    st.markdown("### 🎯 Let's visualize how Binary Search works step-by-step!")  # Introductory description.
    
    # Input for the user to enter a sorted list of numbers.
    arr_input = st.text_input("Enter a sorted list of numbers (comma separated): ✍️")
    # Input for the user to enter the target value to search for.
    target_input = st.number_input("Enter the target value: 🎯", step=1)
    
    if arr_input:  # Check if the user has entered an array.

        arr = list(map(int, arr_input.split(',')))  # Convert the input string to a list of integers.
        
        if len(arr) > 0:  # Ensure the array is not empty.

            result, steps = binary_search(arr, target_input)  # Perform binary search.
  
            if result != -1:  # Check if the target was found.
                st.success(f"✅ Target found at index {result}! 🎉")  # Display success message.
            else:
                st.error("❌ Target not found in the array!")  # Display error message.
 
            plot_array(arr, steps, target_input)  # Visualize the search process.
            
        else:
            st.error("⚠️ Please enter a valid sorted list of numbers!")  # Handle invalid input.

    # Generate a random array when the button is clicked.
    if st.button('Generate Random Array 🚀'):
        random_array = sorted(random.sample(range(1, 100), 10))  # Generate a sorted random array.
        st.write(f"🌟 Generated Array: {random_array}")  # Display the generated array.
        
        # Input for the target value to search in the random array.
        target_input = st.number_input("Enter target for the random array: 🎯", step=1)
        result, steps = binary_search(random_array, target_input)  # Perform binary search on the random array.
        
        if result != -1:  # Check if the target was found.
            st.success(f"✅ Target found at index {result}! 🎉")  # Display success message.
        else:
            st.error("❌ Target not found in the array!")  # Display error message.
        
        plot_array(random_array, steps, target_input)  # Visualize the search process.

# Execute the main function when the script is run.
if __name__ == "__main__":
    main()