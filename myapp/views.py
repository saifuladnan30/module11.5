from django.shortcuts import render

# Create your views here.
def home(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "detailsMeal": "A delightful pastry treat, BeaverTails are known for their unique shape and delicious toppings. Try one for a sweet Canadian experience."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "detailsMeal": "Start your day right with crispy and flavorful breakfast potatoes. A classic morning dish that never fails to satisfy."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "detailsMeal": "Indulge in the rich and sweet goodness of Canadian Butter Tarts. These delectable pastries are a true Canadian dessert delight."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "detailsMeal": "A savory delight, Montreal Smoked Meat is a flavorful meat dish, smoked to perfection. A must-try for meat enthusiasts."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "detailsMeal": "Satisfy your sweet tooth with Nanaimo Bars, a layered dessert featuring a perfect combination of chocolate, custard, and coconut."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "detailsMeal": "A Canadian twist on Shepherd's Pie, Pate Chinois is a comforting dish with ground meat, corn, and mashed potatoes. A hearty Canadian favorite."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "detailsMeal": "Treat yourself to Pouding chomeur, a traditional Canadian dessert with a rich and gooey texture. Perfect for those with a sweet tooth."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "detailsMeal": "Dive into the classic Canadian dish, Poutine, featuring crispy fries topped with cheese curds and smothered in savory gravy. A true comfort food."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "detailsMeal": "Rappie Pie is a unique Canadian dish made with grated potatoes and meat, creating a savory and satisfying pie that showcases regional flavors."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "detailsMeal": "Warm up with Split Pea Soup, a hearty and nutritious Canadian soup made with split peas and flavorful ingredients. A comforting choice on a chilly day."
        }
    ]
    return render(request, 'index.html',{'meals':meals})