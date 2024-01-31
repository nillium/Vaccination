# Sample Definitions
number_of_total_samples = 200
train_to_test_ratio = 5
number_of_training_samples = round(number_of_total_samples*(1-(1/train_to_test_ratio)))

sample_w = 256
sample_h = 64

# GUI Parameters
app_w = 1000
app_h = 590

#AI PARAMETERS
epochs=3
random_filters = 'YES' # YES for custom filters 'NO' for randomly generated filters.
number_of_filters = 4
filter_size = 16 # Edge length of square filters.
