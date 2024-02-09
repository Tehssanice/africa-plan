name = "david"
# print(name)

def test(name: str) -> None:
    print(f"This is {name}")

test("Tessa")

# a = 41474836470000


# ---------------------------------IO
# name = input("what is the name of your president?")
# print("The name of your president is", name)

#### Data types
# integers
# floats or doubles
# strings
# booleans
# lists or arrays
# tuples
# dictionary or maps


####LISTS
# name_of_product = "iphone 12"
# cart = []
# cart.append(name_of_product)
# print(cart)


####TUPLES
# tuples are immutable
# sun_location = ("east", "west")
# print(sun_location.index("east"))


####DICTIONARY
# key:value
nin_data = {
    "Abia": {
        "Isiala Ngwa": {
            "Collins": {
                "age": 20,
                "gender": "Male",
                "height": 5.8,
                "isEducated": False,
                "best_food": ["rice", "beans", "yam"],
                "place_of_birth": ("Enugu", "Nigeria"),
            }
        },
    },
    "Enugu": {
        "Awgu": {
            "Clara": {
                "age": 25,
                "gender": "female",
                "height": 5.8,
                "isEducated": True,
                "best_food": ["Okpa", "abacha"],
                "place_of_birth": ("Enugu", "Nigeria"),
            }
        },
        "Agwu2": {
            "Clara": {
                "age": 25,
                "gender": "female",
                "height": 5.8,
                "isEducated": True,
                "best_food": ["Okpa", "abacha"],
                "place_of_birth": ("Enugu", "Nigeria"),
            }
        },
    },
}

# # get in dictionary
print(nin_data.get("Enugu").get("Awgu").get("Clara").get("age"))
# print(nin_data["Enugu"]["Awgu"]["Clara"]["age"])

# # update dictionary
nin_data.update({"Enugu": {"Awgu": {"Clara": {"place_of_birth": ["Kebbi", "Nigeria"]}}}})

new_clara_details={
     "Aninri": {
            "Clara": {
                "age": 26,
                "gender": "female",
                "height": 5.8,
                "isEducated": True,
                "best_food": ["Okpa", "abacha"],
                "place_of_birth": ("Enugu", "Nigeria"),
            }
        },
}

nin_data.update(new_clara_details)
print(nin_data["Enugu"])

# print(nin_data["Enugu"]["Awgu"]["Clara"]["place_of_birth"])

# # attach to dictionary
nin_data["Abia"]["Isiala Ngwa"]["Collins"]["best_food"].append("Achicha")

# print(nin_data["Abia"]["Isiala Ngwa"]["Collins"]["best_food"])


## operators
