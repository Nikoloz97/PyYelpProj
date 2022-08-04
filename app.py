# ----
# Searching for Businesses
# ----

# # Goal = create a list of NYC barbershop businesses that are rated +4.5 stars on Yelp

# import requests

# # URL is used for the get request (found on Yelp website)
# url = "https://api.yelp.com/v3/businesses/search"
# # Make sure no spaces in API key. Found in Manage App section on left
# api_key = "9LQ5ZwTShzL5EVykY51F4bpYBK4Yxbo_2lRDAqEaoI-Pml3leeAM8NUP4wgUHeqcBtPN_k9eJFBVTY9MRjwJ9kRFlbi-4u7fZJvqMapTmfZsDNuUQU7ALLQv7LHpYnYx"
# headers_dict = {
#     "Authorization": "Bearer " + api_key
# }
# params = {
#     # term = filters for barbers in new york city
#     "term": "Barber",
#     "location": "NYC"
# }
# # Requests takes the headers and params keyword arguments. Set them to a dictionary of key-value pairs
# response = requests.get(url, headers=headers_dict, params=params)
# # json method = converts result into dictionary
# # Just accessing the business key
# List_of_barbershop_businesses = response.json()["businesses"]
# # List comprehension to only find buisnesses with rating (which is in the giant dictionary) is 4.5 stars and above
# High_rated_businesses = [each_business["name"]
#                          for each_business in List_of_barbershop_businesses if each_business["rating"] > 4.5]
# print(High_rated_businesses)
