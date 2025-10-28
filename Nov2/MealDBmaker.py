"""
===========================================================
Program Name: MealDBmaker
Author: Ryan Vrbeta
Date: 2025-10-28
Description:
    This program allows users to manage a simple meal database
    using SQLite. Users can add meals with their ingredients,
    list all meals and their associated ingredients, and look
    up ingredients for a specific meal by name.

Usage:
    Run this script with Python 3.x.
    The program will automatically create (or connect to)
    'meals.db' in the same folder as the script.
    
    Commands:
        - "MealName: ingredient1, ingredient2, ..." → Add a new meal
        - "show" → Display all meals and their ingredients
        - "quit" → Exit the program
        - "MealName" → Look up ingredients for a meal

===========================================================
"""

import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  
db_path = os.path.join(base_dir, "meals.db")          

print(f"Connecting to: {db_path}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()



cursor.execute("CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    name TEXT,
    meal_id INTEGER,
    FOREIGN KEY(meal_id) REFERENCES meals(rowid)
) STRICT
""")

conn.commit()

while True:
    user_input = input("> ").strip()

    if user_input == "quit":
        break

    elif user_input == "show":
        cursor.execute("SELECT rowid, name FROM meals")
        for meal in cursor.fetchall():
            print(f"\nMeal {meal[0]}: {meal[1]}")
            cursor.execute("SELECT name FROM ingredients WHERE meal_id=?", (meal[0],))
            ingredients = [row[0] for row in cursor.fetchall()]
            print("  Ingredients:", ", ".join(ingredients))

    elif ":" in user_input:
        # Add a new meal and its ingredients
        meal_name, ingredients_str = user_input.split(":", 1)
        ingredients_list = [i.strip() for i in ingredients_str.split(",") if i.strip()]

        cursor.execute("INSERT INTO meals (name) VALUES (?)", (meal_name.strip(),))
        conn.commit()
        meal_id = cursor.lastrowid

        for ingredient in ingredients_list:
            cursor.execute(
                "INSERT INTO ingredients (name, meal_id) VALUES (?, ?)",
                (ingredient, meal_id)
            )
        conn.commit()
        print(f"Added meal '{meal_name.strip()}' with ingredients: {', '.join(ingredients_list)}")

    else:
        # Try to look up a meal by name
        cursor.execute("SELECT rowid FROM meals WHERE name = ?", (user_input,))
        meal = cursor.fetchone()

        if meal:
            meal_id = meal[0]
            cursor.execute("SELECT name FROM ingredients WHERE meal_id=?", (meal_id,))
            ingredients = [row[0] for row in cursor.fetchall()]
            print(f"Ingredients for '{user_input}': {', '.join(ingredients)}")
        else:
            print(f"No meal named '{user_input}' found. Try adding it with 'MealName: ingredient1, ingredient2'")

conn.close()
