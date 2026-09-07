ice_cream_rating = 8
sleeping_rating = 10
first_name = "Bruno"
last_name = "Rosa"
my_name = first_name + " " + last_name
happiness_rating = (ice_cream_rating + sleeping_rating) / 2

print(f"""My name is {first_name} and I give eating ice cream a score of {ice_cream_rating} out of 10!
I am {my_name} and my sleeping enjoyment ratio is {sleeping_rating} / 10!
Based on the factors above, my happiness rating is {happiness_rating} out of 10, or {(happiness_rating * 100) / 10}%!"""
)