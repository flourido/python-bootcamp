def find_avg_year(years):
	total_years = len(years)
	sum = 0
	for year in years:
		sum += year
	return int(sum/len(years))
def find_avg_year2(years):
	return int(sum(years)/len(years))


list_of_cars = ["toyota","ford","BMW","audi","benz"]
list_of_models= ["Camry","f150","i8","A4","s550"]

car={
	"make": list_of_cars,
	"model": list_of_models,
	"years": [2010,2017,2020,2006,2020]
}


car_years = car["years"]
#find the average years the car were produced
avg_year = find_avg_year(car_years)
print(f"The avergae years of the cars is: {avg_year} ")

car_colors = ["red", "blue", "black", "blue", "silver"]
car["color"]= car_colors

car["car_stock"] = [3,5,6,1,3]

inventory= car['car_stock']
print(f"we have {sum(inventory)} in stock!")

car["dealers"]= ["Amy", "Bob", "charlie", "Dylan", "Elephant"]


for key in car:
	print(key)
for value in car.values():
	print(value)

#remove a label
#car.pop("dealers")

#this is a lst, clears lst
#car["dealers"].clear

#delete the dictionary 
#del car



