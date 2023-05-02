{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "54d87aed",
   "metadata": {},
   "source": [
    "# Make Some Pizzas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d13e29c",
   "metadata": {},
   "outputs": [],
   "source": [
    "toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b7f3c22e",
   "metadata": {},
   "outputs": [],
   "source": [
    "prices = [2, 6, 1, 3, 2, 7, 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "375098ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_two_dollar_slices = prices.count(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "19c4fc83",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_pizzas = len(toppings)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "61f40141",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We sell 7 differen't kinds of pizza!\n"
     ]
    }
   ],
   "source": [
    "print(\"We sell \" + str(num_pizzas) + \" differen't kinds of pizza!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e5d9f116",
   "metadata": {},
   "outputs": [],
   "source": [
    "pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2,'olives'], [7, 'anchovies'], [2, 'mushrooms']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0dfba792",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]\n"
     ]
    }
   ],
   "source": [
    "print(pizza_and_prices)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "164bdbc8",
   "metadata": {},
   "source": [
    "# Sorting and Slicing Pizzas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f2d1b540",
   "metadata": {},
   "outputs": [],
   "source": [
    "pizza_and_prices.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "85212989",
   "metadata": {},
   "outputs": [],
   "source": [
    "cheapest_pizza = pizza_and_prices[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2310bfc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "priciest_pizza = pizza_and_prices[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e4a8306f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 'anchovies']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pizza_and_prices.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7f940863",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple']]\n"
     ]
    }
   ],
   "source": [
    "print(pizza_and_prices)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b1fdc00c",
   "metadata": {},
   "outputs": [],
   "source": [
    "pizza_and_prices.insert(4, [2.5, 'peppers'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3f9dbc21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple']]\n"
     ]
    }
   ],
   "source": [
    "print(pizza_and_prices)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5dd8e55b",
   "metadata": {},
   "outputs": [],
   "source": [
    "three_cheapest = pizza_and_prices[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3a350ddd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]\n"
     ]
    }
   ],
   "source": [
    "print(three_cheapest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ade2e27b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
