import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineHeap = {}

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.foodToCuisine[food] = cuisine
            self.foodToRating[food] = rating

            if cuisine not in self.cuisineHeap:
                self.cuisineHeap[cuisine] = []
            heapq.heappush(self.cuisineHeap[cuisine], (-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToRating[food] = newRating
        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.cuisineHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        h = self.cuisineHeap[cuisine]
        while True:
            rating, food = h[0]
            if -1 * rating == self.foodToRating[food]:
                return food
            
            rating, food = heapq.heappop(h)
  


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)