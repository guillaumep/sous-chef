# flake8: noqa

from souschef.meal.models import (
    Component,
    Component_ingredient,
    Incompatibility,
    Ingredient,
    Restricted_item,
)


def print_rows(q, heading=""):
    pass
    print(
        "\n-----------------------------------------------------\n",
        # q, "\n",
        heading,
    )
    for row in q.all():
        print(row)


def insert_all():
    print("\nSTART dataload")

    # Rename existing ingredients, components, restricted_items

    items = Ingredient.objects.all()
    for item in items:
        item.name = "OLD" + item.name
        item.save()
        print("Ingredient item name", item.name)

    items = Component.objects.all()
    for item in items:
        item.name = "OLD" + item.name
        item.save()
        print("Component item name", item.name)

    items = Restricted_item.objects.all()
    for item in items:
        item.name = "OLD" + item.name
        item.save()
        print("Restricted_item item name", item.name)

    # -----------------------------------------------------------------------------
    ing_1 = Ingredient.objects.create(name="Butter", ingredient_group="Dairy")
    ing_2 = Ingredient.objects.create(
        name="Cheese : Blue cheese", ingredient_group="Dairy"
    )
    ing_3 = Ingredient.objects.create(
        name="Cheese : Bocconcini", ingredient_group="Dairy"
    )
    ing_4 = Ingredient.objects.create(name="Cheese : Cheddar", ingredient_group="Dairy")
    ing_5 = Ingredient.objects.create(
        name="Cheese : Cottage cheese", ingredient_group="Dairy"
    )
    ing_6 = Ingredient.objects.create(name="Cheese : Feta", ingredient_group="Dairy")
    ing_7 = Ingredient.objects.create(
        name="Cheese : Goat cheese", ingredient_group="Dairy"
    )
    ing_8 = Ingredient.objects.create(
        name="Cheese : Mozzarella", ingredient_group="Dairy"
    )
    ing_9 = Ingredient.objects.create(
        name="Cheese : Parmesan", ingredient_group="Dairy"
    )
    ing_10 = Ingredient.objects.create(
        name="Cheese : Ricotta", ingredient_group="Dairy"
    )
    ing_11 = Ingredient.objects.create(name="Eggs", ingredient_group="Dairy")
    ing_12 = Ingredient.objects.create(name="Margarine", ingredient_group="Dairy")
    ing_13 = Ingredient.objects.create(name="Milk", ingredient_group="Dairy")
    ing_14 = Ingredient.objects.create(name="Tofu", ingredient_group="Dairy")
    ing_15 = Ingredient.objects.create(name="Yogurt", ingredient_group="Dairy")
    ing_16 = Ingredient.objects.create(
        name="Almond Powder ", ingredient_group="Dry and Canned goods"
    )
    ing_17 = Ingredient.objects.create(
        name="Almonds", ingredient_group="Dry and Canned goods"
    )
    ing_18 = Ingredient.objects.create(
        name="Capers", ingredient_group="Dry and Canned goods"
    )
    ing_19 = Ingredient.objects.create(
        name="Corn meal", ingredient_group="Dry and Canned goods"
    )
    ing_20 = Ingredient.objects.create(
        name="corn starch", ingredient_group="Dry and Canned goods"
    )
    ing_21 = Ingredient.objects.create(
        name="Creamed corn", ingredient_group="Dry and Canned goods"
    )
    ing_22 = Ingredient.objects.create(
        name="Egg noodles", ingredient_group="Dry and Canned goods"
    )
    ing_23 = Ingredient.objects.create(
        name="Linguini", ingredient_group="Dry and Canned goods"
    )
    ing_24 = Ingredient.objects.create(
        name="peanut butter", ingredient_group="Dry and Canned goods"
    )
    ing_25 = Ingredient.objects.create(
        name="peanuts ", ingredient_group="Dry and Canned goods"
    )
    ing_26 = Ingredient.objects.create(
        name="Pickles", ingredient_group="Dry and Canned goods"
    )
    ing_27 = Ingredient.objects.create(
        name="Polenta", ingredient_group="Dry and Canned goods"
    )
    ing_28 = Ingredient.objects.create(
        name="Rice noodles", ingredient_group="Dry and Canned goods"
    )
    ing_29 = Ingredient.objects.create(
        name="sesame seeds", ingredient_group="Dry and Canned goods"
    )
    ing_30 = Ingredient.objects.create(
        name="Sunflower seeds", ingredient_group="Dry and Canned goods"
    )
    ing_31 = Ingredient.objects.create(
        name="Tomato paste", ingredient_group="Dry and Canned goods"
    )
    ing_32 = Ingredient.objects.create(
        name="Walnuts", ingredient_group="Dry and Canned goods"
    )
    ing_33 = Ingredient.objects.create(
        name="Whole wheat lasagna", ingredient_group="Dry and Canned goods"
    )
    ing_34 = Ingredient.objects.create(
        name="Whole wheat linguini ", ingredient_group="Dry and Canned goods"
    )
    ing_35 = Ingredient.objects.create(
        name="Whole wheat macaroni", ingredient_group="Dry and Canned goods"
    )
    ing_36 = Ingredient.objects.create(
        name="Whole wheat penne ", ingredient_group="Dry and Canned goods"
    )
    ing_37 = Ingredient.objects.create(
        name="Whole wheat spaghetti", ingredient_group="Dry and Canned goods"
    )
    ing_38 = Ingredient.objects.create(name="Canned salmon", ingredient_group="Fish")
    ing_39 = Ingredient.objects.create(name="Canned tuna", ingredient_group="Fish")
    ing_40 = Ingredient.objects.create(name="Cod", ingredient_group="Fish")
    ing_41 = Ingredient.objects.create(name="Haddock", ingredient_group="Fish")
    ing_42 = Ingredient.objects.create(name="Pollock", ingredient_group="Fish")
    ing_43 = Ingredient.objects.create(name="Basil", ingredient_group="Fresh herbs")
    ing_44 = Ingredient.objects.create(name="Chives", ingredient_group="Fresh herbs")
    ing_45 = Ingredient.objects.create(name="Cilantro", ingredient_group="Fresh herbs")
    ing_46 = Ingredient.objects.create(name="Dill", ingredient_group="Fresh herbs")
    ing_47 = Ingredient.objects.create(name="Marjoram", ingredient_group="Fresh herbs")
    ing_48 = Ingredient.objects.create(name="Oregano", ingredient_group="Fresh herbs")
    ing_49 = Ingredient.objects.create(name="Parsley", ingredient_group="Fresh herbs")
    ing_50 = Ingredient.objects.create(name="Rosemary", ingredient_group="Fresh herbs")
    ing_51 = Ingredient.objects.create(name="Thyme", ingredient_group="Fresh herbs")
    ing_52 = Ingredient.objects.create(
        name="Barley (gluten)", ingredient_group="Grains"
    )
    ing_53 = Ingredient.objects.create(name="Basmati rice", ingredient_group="Grains")
    ing_54 = Ingredient.objects.create(name="Breadcrumbs", ingredient_group="Grains")
    ing_55 = Ingredient.objects.create(name="Brown rice", ingredient_group="Grains")
    ing_56 = Ingredient.objects.create(name="Buckwheat", ingredient_group="Grains")
    ing_57 = Ingredient.objects.create(
        name="Couscous (gluten)", ingredient_group="Grains"
    )
    ing_58 = Ingredient.objects.create(name="Millet", ingredient_group="Grains")
    ing_59 = Ingredient.objects.create(name="Oats", ingredient_group="Grains")
    ing_60 = Ingredient.objects.create(name="Quinoa", ingredient_group="Grains")
    ing_61 = Ingredient.objects.create(name="White flour", ingredient_group="Grains")
    ing_62 = Ingredient.objects.create(
        name="Whole wheat flour", ingredient_group="Grains"
    )
    ing_63 = Ingredient.objects.create(name="Wild rice", ingredient_group="Grains")
    ing_64 = Ingredient.objects.create(
        name="Black beans", ingredient_group="Legumineuse"
    )
    ing_65 = Ingredient.objects.create(name="Chickpeas", ingredient_group="Legumineuse")
    ing_66 = Ingredient.objects.create(
        name="Kidney beans", ingredient_group="Legumineuse"
    )
    ing_67 = Ingredient.objects.create(name="Lentils", ingredient_group="Legumineuse")
    ing_68 = Ingredient.objects.create(
        name="White beans", ingredient_group="Legumineuse"
    )
    ing_69 = Ingredient.objects.create(name="Beef cubes", ingredient_group="Meat")
    ing_70 = Ingredient.objects.create(name="Chicken", ingredient_group="Meat")
    ing_71 = Ingredient.objects.create(name="Chicken thighs", ingredient_group="Meat")
    ing_72 = Ingredient.objects.create(name="Ground beef", ingredient_group="Meat")
    ing_73 = Ingredient.objects.create(name="Ground porc", ingredient_group="Meat")
    ing_74 = Ingredient.objects.create(name="Ham", ingredient_group="Meat")
    ing_75 = Ingredient.objects.create(name="Lamb cubes", ingredient_group="Meat")
    ing_76 = Ingredient.objects.create(name="Pork sausage", ingredient_group="Meat")
    ing_77 = Ingredient.objects.create(
        name="Pork toulouse sausage", ingredient_group="Meat"
    )
    ing_78 = Ingredient.objects.create(name="Roast Beef ", ingredient_group="Meat")
    ing_79 = Ingredient.objects.create(name="stock", ingredient_group="Meat")
    ing_80 = Ingredient.objects.create(name="Turkey", ingredient_group="Meat")
    ing_81 = Ingredient.objects.create(name="Turkey thighs", ingredient_group="Meat")
    ing_82 = Ingredient.objects.create(
        name="Apple cider vinegar", ingredient_group="Oils and Sauces"
    )
    ing_83 = Ingredient.objects.create(
        name="Balsamic vinegar", ingredient_group="Oils and Sauces"
    )
    ing_84 = Ingredient.objects.create(
        name="cooking wine", ingredient_group="Oils and Sauces"
    )
    ing_85 = Ingredient.objects.create(
        name="Dijon mustard", ingredient_group="Oils and Sauces"
    )
    ing_86 = Ingredient.objects.create(name="honey", ingredient_group="Oils and Sauces")
    ing_87 = Ingredient.objects.create(
        name="maple sirop", ingredient_group="Oils and Sauces"
    )
    ing_88 = Ingredient.objects.create(
        name="Olive oil", ingredient_group="Oils and Sauces"
    )
    ing_89 = Ingredient.objects.create(
        name="Prepared mustard", ingredient_group="Oils and Sauces"
    )
    ing_90 = Ingredient.objects.create(
        name="Red wine (salt)", ingredient_group="Oils and Sauces"
    )
    ing_91 = Ingredient.objects.create(
        name="Red wine vinegar", ingredient_group="Oils and Sauces"
    )
    ing_92 = Ingredient.objects.create(
        name="Rice vinegar ", ingredient_group="Oils and Sauces"
    )
    ing_93 = Ingredient.objects.create(
        name="rice wine vinegar", ingredient_group="Oils and Sauces"
    )
    ing_94 = Ingredient.objects.create(
        name="Sesame oil", ingredient_group="Oils and Sauces"
    )
    ing_95 = Ingredient.objects.create(
        name="Soy sauce (gluten, salt)", ingredient_group="Oils and Sauces"
    )
    ing_96 = Ingredient.objects.create(
        name="Vinegar", ingredient_group="Oils and Sauces"
    )
    ing_97 = Ingredient.objects.create(
        name="White wine", ingredient_group="Oils and Sauces"
    )
    ing_98 = Ingredient.objects.create(
        name="Seafood medley (shrimp, mussels, calamari)", ingredient_group="Seafood"
    )
    ing_99 = Ingredient.objects.create(name="Shrimp", ingredient_group="Seafood")
    ing_100 = Ingredient.objects.create(name="Allspice", ingredient_group="Spices")
    ing_101 = Ingredient.objects.create(name="Bay leaves", ingredient_group="Spices")
    ing_102 = Ingredient.objects.create(name="Black pepper", ingredient_group="Spices")
    ing_103 = Ingredient.objects.create(name="Cardamom", ingredient_group="Spices")
    ing_104 = Ingredient.objects.create(name="Chili", ingredient_group="Spices")
    ing_105 = Ingredient.objects.create(name="Cinnamon", ingredient_group="Spices")
    ing_106 = Ingredient.objects.create(name="Cloves", ingredient_group="Spices")
    ing_107 = Ingredient.objects.create(name="Coriander", ingredient_group="Spices")
    ing_108 = Ingredient.objects.create(name="Cumin", ingredient_group="Spices")
    ing_109 = Ingredient.objects.create(name="Curry", ingredient_group="Spices")
    ing_110 = Ingredient.objects.create(name="Ginger powder", ingredient_group="Spices")
    ing_111 = Ingredient.objects.create(
        name="Herbes de provence", ingredient_group="Spices"
    )
    ing_112 = Ingredient.objects.create(
        name="Mustard powder", ingredient_group="Spices"
    )
    ing_113 = Ingredient.objects.create(name="Nutmeg", ingredient_group="Spices")
    ing_114 = Ingredient.objects.create(name="Paprika", ingredient_group="Spices")
    ing_115 = Ingredient.objects.create(name="Sage", ingredient_group="Spices")
    ing_116 = Ingredient.objects.create(name="Terragon", ingredient_group="Spices")
    ing_118 = Ingredient.objects.create(name="Turmeric", ingredient_group="Spices")
    ing_119 = Ingredient.objects.create(
        name="Apples", ingredient_group="Veggies & Fruits"
    )
    ing_120 = Ingredient.objects.create(
        name="Apricots", ingredient_group="Veggies & Fruits"
    )
    ing_121 = Ingredient.objects.create(
        name="Arugula", ingredient_group="Veggies & Fruits"
    )
    ing_122 = Ingredient.objects.create(
        name="Artichokes", ingredient_group="Veggies & Fruits"
    )
    ing_123 = Ingredient.objects.create(
        name="Bean sprouts", ingredient_group="Veggies & Fruits"
    )
    ing_124 = Ingredient.objects.create(
        name="Beets", ingredient_group="Veggies & Fruits"
    )
    ing_125 = Ingredient.objects.create(
        name="Bok choy", ingredient_group="Veggies & Fruits"
    )
    ing_126 = Ingredient.objects.create(
        name="Broccoli", ingredient_group="Veggies & Fruits"
    )
    ing_127 = Ingredient.objects.create(
        name="Brussel sprouts", ingredient_group="Veggies & Fruits"
    )
    ing_128 = Ingredient.objects.create(
        name="Cabbage", ingredient_group="Veggies & Fruits"
    )
    ing_129 = Ingredient.objects.create(
        name="Carrots", ingredient_group="Veggies & Fruits"
    )
    ing_130 = Ingredient.objects.create(
        name="Cauliflower", ingredient_group="Veggies & Fruits"
    )
    ing_131 = Ingredient.objects.create(
        name="celery", ingredient_group="Veggies & Fruits"
    )
    ing_132 = Ingredient.objects.create(
        name="Celery root", ingredient_group="Veggies & Fruits"
    )
    ing_133 = Ingredient.objects.create(
        name="Chicory", ingredient_group="Veggies & Fruits"
    )
    ing_134 = Ingredient.objects.create(
        name="Corn", ingredient_group="Veggies & Fruits"
    )
    ing_135 = Ingredient.objects.create(
        name="Cranberries", ingredient_group="Veggies & Fruits"
    )
    ing_136 = Ingredient.objects.create(
        name="Cucumber", ingredient_group="Veggies & Fruits"
    )
    ing_137 = Ingredient.objects.create(
        name="Eggplant", ingredient_group="Veggies & Fruits"
    )
    ing_138 = Ingredient.objects.create(
        name="Garlic", ingredient_group="Veggies & Fruits"
    )
    ing_139 = Ingredient.objects.create(
        name="Ginger", ingredient_group="Veggies & Fruits"
    )
    ing_140 = Ingredient.objects.create(
        name="Green beans", ingredient_group="Veggies & Fruits"
    )
    ing_141 = Ingredient.objects.create(
        name="Green peas", ingredient_group="Veggies & Fruits"
    )
    ing_142 = Ingredient.objects.create(
        name="Green peppers", ingredient_group="Veggies & Fruits"
    )
    ing_143 = Ingredient.objects.create(
        name="Kale", ingredient_group="Veggies & Fruits"
    )
    ing_144 = Ingredient.objects.create(
        name="Kolhrabi", ingredient_group="Veggies & Fruits"
    )
    ing_145 = Ingredient.objects.create(
        name="Leeks", ingredient_group="Veggies & Fruits"
    )
    ing_146 = Ingredient.objects.create(
        name="Lemons", ingredient_group="Veggies & Fruits"
    )
    ing_147 = Ingredient.objects.create(
        name="Lettuce", ingredient_group="Veggies & Fruits"
    )
    ing_148 = Ingredient.objects.create(
        name="lime", ingredient_group="Veggies & Fruits"
    )
    ing_149 = Ingredient.objects.create(
        name="mung bean sprouts", ingredient_group="Veggies & Fruits"
    )
    ing_150 = Ingredient.objects.create(
        name="Mushrooms", ingredient_group="Veggies & Fruits"
    )
    ing_151 = Ingredient.objects.create(
        name="Olives", ingredient_group="Veggies & Fruits"
    )
    ing_152 = Ingredient.objects.create(
        name="Onions", ingredient_group="Veggies & Fruits"
    )
    ing_153 = Ingredient.objects.create(
        name="Orange peppers", ingredient_group="Veggies & Fruits"
    )
    ing_154 = Ingredient.objects.create(
        name="parsnip", ingredient_group="Veggies & Fruits"
    )
    ing_155 = Ingredient.objects.create(
        name="Potatoes", ingredient_group="Veggies & Fruits"
    )
    ing_156 = Ingredient.objects.create(
        name="Pumpkin", ingredient_group="Veggies & Fruits"
    )
    ing_157 = Ingredient.objects.create(
        name="Radish", ingredient_group="Veggies & Fruits"
    )
    ing_158 = Ingredient.objects.create(
        name="Raisins", ingredient_group="Veggies & Fruits"
    )
    ing_159 = Ingredient.objects.create(
        name="Red peppers  ", ingredient_group="Veggies & Fruits"
    )
    ing_160 = Ingredient.objects.create(
        name="Snap peas", ingredient_group="Veggies & Fruits"
    )
    ing_161 = Ingredient.objects.create(
        name="Snow peas", ingredient_group="Veggies & Fruits"
    )
    ing_162 = Ingredient.objects.create(
        name="Spinach", ingredient_group="Veggies & Fruits"
    )
    ing_163 = Ingredient.objects.create(
        name="squash", ingredient_group="Veggies & Fruits"
    )
    ing_164 = Ingredient.objects.create(
        name="Sweet potatoes", ingredient_group="Veggies & Fruits"
    )
    ing_165 = Ingredient.objects.create(
        name="Swiss chard", ingredient_group="Veggies & Fruits"
    )
    ing_166 = Ingredient.objects.create(
        name="Tomatoes", ingredient_group="Veggies & Fruits"
    )
    ing_167 = Ingredient.objects.create(
        name="Turnips", ingredient_group="Veggies & Fruits"
    )
    ing_168 = Ingredient.objects.create(
        name="Yellow beans", ingredient_group="Veggies & Fruits"
    )
    ing_169 = Ingredient.objects.create(
        name="zucchini", ingredient_group="Veggies & Fruits"
    )
    #
    print_rows(Ingredient.objects)

    # -----------------------------------------------------------------------------
    com_1 = Component.objects.create(
        name="Beef bourguignon", component_group="main_dish"
    )
    com_2 = Component.objects.create(name="Beef meatballs", component_group="main_dish")
    com_3 = Component.objects.create(name="Beef meatloaf", component_group="main_dish")
    com_4 = Component.objects.create(
        name="Beet and apple salad", component_group="main_dish"
    )
    com_5 = Component.objects.create(
        name="Chicken and squash curry", component_group="main_dish"
    )
    com_6 = Component.objects.create(
        name="Chicken cacciatore", component_group="main_dish"
    )
    com_7 = Component.objects.create(
        name="Chicken pot pie", component_group="main_dish"
    )
    com_8 = Component.objects.create(
        name="Chicken, vegetable and quinoa couscous", component_group="main_dish"
    )
    com_9 = Component.objects.create(name="Cod cakes", component_group="main_dish")
    com_10 = Component.objects.create(name="Coq au vin", component_group="main_dish")
    com_11 = Component.objects.create(
        name="Creamy salmon pasta", component_group="main_dish"
    )
    com_12 = Component.objects.create(
        name="Egg and salmon salad", component_group="main_dish"
    )
    com_13 = Component.objects.create(
        name="Eggplant parmesan", component_group="main_dish"
    )
    com_14 = Component.objects.create(name="Fish chowder", component_group="main_dish")
    com_15 = Component.objects.create(name="Ginger pork", component_group="main_dish")
    com_16 = Component.objects.create(
        name="Lemon baked haddock", component_group="main_dish"
    )
    com_17 = Component.objects.create(
        name="Macaroni and cheese", component_group="main_dish"
    )
    com_18 = Component.objects.create(name="Meat pie", component_group="main_dish")
    com_19 = Component.objects.create(name="Moussaka", component_group="main_dish")
    com_20 = Component.objects.create(
        name="Mushroom rice casserole", component_group="main_dish"
    )
    com_21 = Component.objects.create(name="Niçoise salad", component_group="main_dish")
    com_22 = Component.objects.create(
        name="Peanut chicken with rice noodles", component_group="main_dish"
    )
    com_23 = Component.objects.create(
        name="Penne with pesto and feta", component_group="main_dish"
    )
    com_24 = Component.objects.create(name="Roast beef", component_group="main_dish")
    com_25 = Component.objects.create(
        name="Salmon and egg salad", component_group="main_dish"
    )
    com_26 = Component.objects.create(
        name="Sausage and cabbage", component_group="main_dish"
    )
    com_27 = Component.objects.create(
        name="Sausage cassoulet", component_group="main_dish"
    )
    com_28 = Component.objects.create(name="Seafood pilaf", component_group="main_dish")
    com_29 = Component.objects.create(
        name="Shepherd's pie", component_group="main_dish"
    )
    com_30 = Component.objects.create(
        name="Shrimp and mushroom linguini", component_group="main_dish"
    )
    com_31 = Component.objects.create(
        name="Shrimp stir-fry", component_group="main_dish"
    )
    com_32 = Component.objects.create(
        name="Spaghetti with meat sauce", component_group="main_dish"
    )
    com_33 = Component.objects.create(
        name="Turkey with mushroom sauce", component_group="main_dish"
    )
    com_34 = Component.objects.create(
        name="Vegatable and chickpea curry", component_group="main_dish"
    )
    com_35 = Component.objects.create(
        name="Vegetable fried rice", component_group="main_dish"
    )
    com_36 = Component.objects.create(
        name="Vegetable lasagna", component_group="main_dish"
    )
    com_37 = Component.objects.create(
        name="Vegetarian chili", component_group="main_dish"
    )
    com_38 = Component.objects.create(
        name="Vegetarian quiche", component_group="main_dish"
    )
    com_39 = Component.objects.create(
        name="Walnut and cranberry rice salad", component_group="main_dish"
    )
    #
    print_rows(Component.objects)

    # -----------------------------------------------------------------------------
    com_ing_1 = Component_ingredient.objects.create(component=com_1, ingredient=ing_101)
    com_ing_2 = Component_ingredient.objects.create(component=com_1, ingredient=ing_69)
    com_ing_3 = Component_ingredient.objects.create(component=com_1, ingredient=ing_129)
    com_ing_4 = Component_ingredient.objects.create(component=com_1, ingredient=ing_138)
    com_ing_5 = Component_ingredient.objects.create(component=com_1, ingredient=ing_150)
    com_ing_6 = Component_ingredient.objects.create(component=com_1, ingredient=ing_152)
    com_ing_7 = Component_ingredient.objects.create(component=com_1, ingredient=ing_49)
    com_ing_8 = Component_ingredient.objects.create(component=com_1, ingredient=ing_90)
    com_ing_9 = Component_ingredient.objects.create(component=com_1, ingredient=ing_51)
    com_ing_10 = Component_ingredient.objects.create(
        component=com_1, ingredient=ing_166
    )
    com_ing_11 = Component_ingredient.objects.create(component=com_1, ingredient=ing_61)
    com_ing_12 = Component_ingredient.objects.create(component=com_2, ingredient=ing_54)
    com_ing_13 = Component_ingredient.objects.create(component=com_2, ingredient=ing_9)
    com_ing_14 = Component_ingredient.objects.create(component=com_2, ingredient=ing_11)
    com_ing_15 = Component_ingredient.objects.create(
        component=com_2, ingredient=ing_138
    )
    com_ing_16 = Component_ingredient.objects.create(component=com_2, ingredient=ing_72)
    com_ing_17 = Component_ingredient.objects.create(component=com_2, ingredient=ing_13)
    com_ing_18 = Component_ingredient.objects.create(
        component=com_2, ingredient=ing_152
    )
    com_ing_19 = Component_ingredient.objects.create(component=com_2, ingredient=ing_48)
    com_ing_20 = Component_ingredient.objects.create(
        component=com_2, ingredient=ing_166
    )
    com_ing_21 = Component_ingredient.objects.create(
        component=com_2, ingredient=ing_169
    )
    com_ing_22 = Component_ingredient.objects.create(component=com_3, ingredient=ing_54)
    com_ing_23 = Component_ingredient.objects.create(component=com_3, ingredient=ing_55)
    com_ing_24 = Component_ingredient.objects.create(component=com_3, ingredient=ing_11)
    com_ing_25 = Component_ingredient.objects.create(
        component=com_3, ingredient=ing_138
    )
    com_ing_26 = Component_ingredient.objects.create(component=com_3, ingredient=ing_72)
    com_ing_27 = Component_ingredient.objects.create(component=com_3, ingredient=ing_13)
    com_ing_28 = Component_ingredient.objects.create(
        component=com_3, ingredient=ing_152
    )
    com_ing_29 = Component_ingredient.objects.create(
        component=com_3, ingredient=ing_166
    )
    com_ing_30 = Component_ingredient.objects.create(
        component=com_4, ingredient=ing_119
    )
    com_ing_31 = Component_ingredient.objects.create(
        component=com_4, ingredient=ing_124
    )
    com_ing_32 = Component_ingredient.objects.create(component=com_4, ingredient=ing_2)
    com_ing_33 = Component_ingredient.objects.create(component=com_4, ingredient=ing_85)
    com_ing_34 = Component_ingredient.objects.create(
        component=com_4, ingredient=ing_138
    )
    com_ing_35 = Component_ingredient.objects.create(
        component=com_4, ingredient=ing_147
    )
    com_ing_36 = Component_ingredient.objects.create(component=com_4, ingredient=ing_87)
    com_ing_37 = Component_ingredient.objects.create(component=com_4, ingredient=ing_88)
    com_ing_38 = Component_ingredient.objects.create(
        component=com_4, ingredient=ing_152
    )
    com_ing_39 = Component_ingredient.objects.create(component=com_5, ingredient=ing_70)
    com_ing_40 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_129
    )
    com_ing_41 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_138
    )
    com_ing_42 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_139
    )
    com_ing_43 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_152
    )
    com_ing_41 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_107
    )
    com_ing_42 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_108
    )
    com_ing_43 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_118
    )
    com_ing_43 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_112
    )
    com_ing_44 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_110
    )
    com_ing_45 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_163
    )
    com_ing_46 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_166
    )
    com_ing_47 = Component_ingredient.objects.create(component=com_5, ingredient=ing_15)
    com_ing_48 = Component_ingredient.objects.create(
        component=com_5, ingredient=ing_169
    )
    com_ing_49 = Component_ingredient.objects.create(component=com_6, ingredient=ing_55)
    com_ing_50 = Component_ingredient.objects.create(
        component=com_6, ingredient=ing_131
    )
    com_ing_51 = Component_ingredient.objects.create(component=com_6, ingredient=ing_71)
    com_ing_52 = Component_ingredient.objects.create(component=com_6, ingredient=ing_84)
    com_ing_53 = Component_ingredient.objects.create(
        component=com_6, ingredient=ing_138
    )
    com_ing_54 = Component_ingredient.objects.create(
        component=com_6, ingredient=ing_152
    )
    com_ing_55 = Component_ingredient.objects.create(component=com_6, ingredient=ing_50)
    com_ing_56 = Component_ingredient.objects.create(component=com_6, ingredient=ing_79)
    com_ing_57 = Component_ingredient.objects.create(component=com_6, ingredient=ing_31)
    com_ing_58 = Component_ingredient.objects.create(
        component=com_6, ingredient=ing_166
    )
    com_ing_59 = Component_ingredient.objects.create(
        component=com_7, ingredient=ing_129
    )
    com_ing_60 = Component_ingredient.objects.create(
        component=com_7, ingredient=ing_131
    )
    com_ing_61 = Component_ingredient.objects.create(component=com_7, ingredient=ing_71)
    com_ing_62 = Component_ingredient.objects.create(component=com_7, ingredient=ing_11)
    com_ing_63 = Component_ingredient.objects.create(
        component=com_7, ingredient=ing_138
    )
    com_ing_64 = Component_ingredient.objects.create(component=com_7, ingredient=ing_13)
    com_ing_65 = Component_ingredient.objects.create(
        component=com_7, ingredient=ing_152
    )
    com_ing_66 = Component_ingredient.objects.create(component=com_7, ingredient=ing_49)
    com_ing_67 = Component_ingredient.objects.create(component=com_7, ingredient=ing_61)
    com_ing_68 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_100
    )
    com_ing_69 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_103
    )
    com_ing_70 = Component_ingredient.objects.create(component=com_8, ingredient=ing_71)
    com_ing_71 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_105
    )
    com_ing_72 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_106
    )
    com_ing_73 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_107
    )
    com_ing_74 = Component_ingredient.objects.create(component=com_8, ingredient=ing_57)
    com_ing_75 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_137
    )
    com_ing_76 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_138
    )
    com_ing_77 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_139
    )
    com_ing_78 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_143
    )
    com_ing_79 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_146
    )
    com_ing_80 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_152
    )
    com_ing_81 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_114
    )
    com_ing_82 = Component_ingredient.objects.create(component=com_8, ingredient=ing_60)
    com_ing_83 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_163
    )
    com_ing_84 = Component_ingredient.objects.create(
        component=com_8, ingredient=ing_166
    )
    com_ing_85 = Component_ingredient.objects.create(component=com_9, ingredient=ing_54)
    com_ing_86 = Component_ingredient.objects.create(component=com_9, ingredient=ing_40)
    com_ing_87 = Component_ingredient.objects.create(component=com_9, ingredient=ing_46)
    com_ing_88 = Component_ingredient.objects.create(component=com_9, ingredient=ing_11)
    com_ing_89 = Component_ingredient.objects.create(
        component=com_9, ingredient=ing_138
    )
    com_ing_90 = Component_ingredient.objects.create(
        component=com_9, ingredient=ing_146
    )
    com_ing_91 = Component_ingredient.objects.create(component=com_9, ingredient=ing_49)
    com_ing_92 = Component_ingredient.objects.create(
        component=com_9, ingredient=ing_155
    )
    com_ing_93 = Component_ingredient.objects.create(component=com_9, ingredient=ing_15)
    com_ing_94 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_129
    )
    com_ing_95 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_71
    )
    com_ing_96 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_84
    )
    com_ing_97 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_138
    )
    com_ing_98 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_150
    )
    com_ing_99 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_152
    )
    com_ing_100 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_49
    )
    com_ing_101 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_51
    )
    com_ing_102 = Component_ingredient.objects.create(
        component=com_10, ingredient=ing_61
    )
    com_ing_103 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_1
    )
    com_ing_104 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_38
    )
    com_ing_105 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_129
    )
    com_ing_106 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_46
    )
    com_ing_107 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_138
    )
    com_ing_108 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_146
    )
    com_ing_109 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_13
    )
    com_ing_110 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_152
    )
    com_ing_111 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_166
    )
    com_ing_112 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_61
    )
    com_ing_113 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_37
    )
    com_ing_114 = Component_ingredient.objects.create(
        component=com_11, ingredient=ing_169
    )
    com_ing_115 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_38
    )
    com_ing_116 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_129
    )
    com_ing_117 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_46
    )
    com_ing_118 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_11
    )
    com_ing_119 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_146
    )
    com_ing_120 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_147
    )
    com_ing_121 = Component_ingredient.objects.create(
        component=com_12, ingredient=ing_116
    )
    com_ing_122 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_129
    )
    com_ing_123 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_131
    )
    com_ing_124 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_4
    )
    com_ing_125 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_9
    )
    com_ing_126 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_137
    )
    com_ing_127 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_138
    )
    com_ing_128 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_152
    )
    com_ing_129 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_90
    )
    com_ing_130 = Component_ingredient.objects.create(
        component=com_13, ingredient=ing_166
    )
    com_ing_131 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_102
    )
    com_ing_132 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_1
    )
    com_ing_133 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_134
    )
    com_ing_134 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_138
    )
    com_ing_135 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_41
    )
    com_ing_136 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_13
    )
    com_ing_137 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_152
    )
    com_ing_138 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_155
    )
    com_ing_139 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_51
    )
    com_ing_140 = Component_ingredient.objects.create(
        component=com_14, ingredient=ing_61
    )
    com_ing_141 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_129
    )
    com_ing_142 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_20
    )
    com_ing_143 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_138
    )
    com_ing_144 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_139
    )
    com_ing_145 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_73
    )
    com_ing_146 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_152
    )
    com_ing_147 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_28
    )
    com_ing_148 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_93
    )
    com_ing_149 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_94
    )
    com_ing_150 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_29
    )
    com_ing_151 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_95
    )
    com_ing_152 = Component_ingredient.objects.create(
        component=com_15, ingredient=ing_169
    )
    com_ing_153 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_102
    )
    com_ing_154 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_54
    )
    com_ing_155 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_4
    )
    com_ing_156 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_11
    )
    com_ing_157 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_138
    )
    com_ing_158 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_41
    )
    com_ing_159 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_146
    )
    com_ing_160 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_13
    )
    com_ing_161 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_152
    )
    com_ing_162 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_155
    )
    com_ing_163 = Component_ingredient.objects.create(
        component=com_16, ingredient=ing_116
    )
    com_ing_164 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_54
    )
    com_ing_165 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_1
    )
    com_ing_166 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_130
    )
    com_ing_167 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_4
    )
    com_ing_168 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_9
    )
    com_ing_169 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_44
    )
    com_ing_170 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_138
    )
    com_ing_171 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_141
    )
    com_ing_172 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_13
    )
    com_ing_173 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_150
    )
    com_ing_174 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_112
    )
    com_ing_175 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_113
    )
    com_ing_176 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_152
    )
    com_ing_177 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_49
    )
    com_ing_178 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_32
    )
    com_ing_179 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_61
    )
    com_ing_180 = Component_ingredient.objects.create(
        component=com_17, ingredient=ing_35
    )
    com_ing_181 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_102
    )
    com_ing_182 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_54
    )
    com_ing_183 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_105
    )
    com_ing_184 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_138
    )
    com_ing_185 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_72
    )
    com_ing_186 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_73
    )
    com_ing_187 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_113
    )
    com_ing_188 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_152
    )
    com_ing_189 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_155
    )
    com_ing_190 = Component_ingredient.objects.create(
        component=com_18, ingredient=ing_61
    )
    com_ing_191 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_100
    )
    com_ing_192 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_1
    )
    com_ing_193 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_9
    )
    com_ing_194 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_105
    )
    com_ing_195 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_137
    )
    com_ing_196 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_11
    )
    com_ing_197 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_138
    )
    com_ing_198 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_72
    )
    com_ing_199 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_13
    )
    com_ing_200 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_152
    )
    com_ing_201 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_48
    )
    com_ing_202 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_166
    )
    com_ing_203 = Component_ingredient.objects.create(
        component=com_19, ingredient=ing_61
    )
    com_ing_204 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_102
    )
    com_ing_205 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_55
    )
    com_ing_206 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_129
    )
    com_ing_207 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_9
    )
    com_ing_208 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_138
    )
    com_ing_209 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_145
    )
    com_ing_210 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_47
    )
    com_ing_211 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_150
    )
    com_ing_212 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_49
    )
    com_ing_213 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_116
    )
    com_ing_214 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_32
    )
    com_ing_215 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_97
    )
    com_ing_216 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_63
    )
    com_ing_217 = Component_ingredient.objects.create(
        component=com_20, ingredient=ing_169
    )
    com_ing_218 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_39
    )
    com_ing_219 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_129
    )
    com_ing_220 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_85
    )
    com_ing_221 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_138
    )
    com_ing_222 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_140
    )
    com_ing_223 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_146
    )
    com_ing_224 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_151
    )
    com_ing_225 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_152
    )
    com_ing_226 = Component_ingredient.objects.create(
        component=com_21, ingredient=ing_116
    )
    com_ing_227 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_129
    )
    com_ing_228 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_71
    )
    com_ing_229 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_45
    )
    com_ing_230 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_107
    )
    com_ing_231 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_138
    )
    com_ing_232 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_139
    )
    com_ing_233 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_86
    )
    com_ing_234 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_148
    )
    com_ing_235 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_152
    )
    com_ing_236 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_24
    )
    com_ing_237 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_25
    )
    com_ing_238 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_28
    )
    com_ing_239 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_94
    )
    com_ing_240 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_95
    )
    com_ing_241 = Component_ingredient.objects.create(
        component=com_22, ingredient=ing_118
    )
    com_ing_242 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_43
    )
    com_ing_243 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_129
    )
    com_ing_244 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_6
    )
    com_ing_245 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_9
    )
    com_ing_246 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_138
    )
    com_ing_247 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_146
    )
    com_ing_248 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_147
    )
    com_ing_249 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_152
    )
    com_ing_250 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_32
    )
    com_ing_251 = Component_ingredient.objects.create(
        component=com_23, ingredient=ing_36
    )
    com_ing_252 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_129
    )
    com_ing_253 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_131
    )
    com_ing_254 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_85
    )
    com_ing_255 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_138
    )
    com_ing_256 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_150
    )
    com_ing_257 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_152
    )
    com_ing_258 = Component_ingredient.objects.create(
        component=com_24, ingredient=ing_78
    )
    com_ing_259 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_38
    )
    com_ing_260 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_129
    )
    com_ing_261 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_46
    )
    com_ing_262 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_11
    )
    com_ing_263 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_138
    )
    com_ing_264 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_146
    )
    com_ing_265 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_147
    )
    com_ing_266 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_88
    )
    com_ing_267 = Component_ingredient.objects.create(
        component=com_25, ingredient=ing_152
    )
    com_ing_268 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_102
    )
    com_ing_269 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_128
    )
    com_ing_270 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_138
    )
    com_ing_271 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_152
    )
    com_ing_272 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_154
    )
    com_ing_273 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_77
    )
    com_ing_274 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_155
    )
    com_ing_275 = Component_ingredient.objects.create(
        component=com_26, ingredient=ing_97
    )
    com_ing_276 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_101
    )
    com_ing_277 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_129
    )
    com_ing_278 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_131
    )
    com_ing_279 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_138
    )
    com_ing_280 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_152
    )
    com_ing_281 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_49
    )
    com_ing_282 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_77
    )
    com_ing_283 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_51
    )
    com_ing_284 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_166
    )
    com_ing_285 = Component_ingredient.objects.create(
        component=com_27, ingredient=ing_68
    )
    com_ing_286 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_55
    )
    com_ing_287 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_131
    )
    com_ing_288 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_138
    )
    com_ing_289 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_152
    )
    com_ing_290 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_114
    )
    com_ing_291 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_49
    )
    com_ing_292 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_98
    )
    com_ing_293 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_166
    )
    com_ing_294 = Component_ingredient.objects.create(
        component=com_28, ingredient=ing_97
    )
    com_ing_295 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_54
    )
    com_ing_296 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_105
    )
    com_ing_297 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_106
    )
    com_ing_298 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_134
    )
    com_ing_299 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_138
    )
    com_ing_300 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_72
    )
    com_ing_301 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_13
    )
    com_ing_302 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_113
    )
    com_ing_303 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_152
    )
    com_ing_304 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_114
    )
    com_ing_305 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_155
    )
    com_ing_306 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_115
    )
    com_ing_307 = Component_ingredient.objects.create(
        component=com_29, ingredient=ing_51
    )
    com_ing_308 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_1
    )
    com_ing_309 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_138
    )
    com_ing_310 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_13
    )
    com_ing_311 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_152
    )
    com_ing_312 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_99
    )
    com_ing_313 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_116
    )
    com_ing_314 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_166
    )
    com_ing_315 = Component_ingredient.objects.create(
        component=com_30, ingredient=ing_61
    )
    com_ing_316 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_126
    )
    com_ing_317 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_129
    )
    com_ing_318 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_138
    )
    com_ing_319 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_139
    )
    com_ing_320 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_142
    )
    com_ing_321 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_149
    )
    com_ing_322 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_150
    )
    com_ing_323 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_152
    )
    com_ing_324 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_159
    )
    com_ing_325 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_28
    )
    com_ing_326 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_94
    )
    com_ing_327 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_29
    )
    com_ing_328 = Component_ingredient.objects.create(
        component=com_31, ingredient=ing_99
    )
    com_ing_329 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_129
    )
    com_ing_330 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_9
    )
    com_ing_331 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_138
    )
    com_ing_332 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_72
    )
    com_ing_333 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_150
    )
    com_ing_334 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_152
    )
    com_ing_335 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_48
    )
    com_ing_336 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_31
    )
    com_ing_337 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_166
    )
    com_ing_338 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_37
    )
    com_ing_339 = Component_ingredient.objects.create(
        component=com_32, ingredient=ing_169
    )
    com_ing_340 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_55
    )
    com_ing_341 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_1
    )
    com_ing_342 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_131
    )
    com_ing_343 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_138
    )
    com_ing_344 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_150
    )
    com_ing_345 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_152
    )
    com_ing_346 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_166
    )
    com_ing_347 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_81
    )
    com_ing_348 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_61
    )
    com_ing_349 = Component_ingredient.objects.create(
        component=com_33, ingredient=ing_97
    )
    com_ing_350 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_43
    )
    com_ing_351 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_128
    )
    com_ing_352 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_65
    )
    com_ing_353 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_44
    )
    com_ing_354 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_45
    )
    com_ing_355 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_46
    )
    com_ing_356 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_137
    )
    com_ing_357 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_138
    )
    com_ing_358 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_141
    )
    com_ing_359 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_142
    )
    com_ing_360 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_47
    )
    com_ing_361 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_152
    )
    com_ing_362 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_48
    )
    com_ing_363 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_49
    )
    com_ing_364 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_159
    )
    com_ing_365 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_50
    )
    com_ing_366 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_163
    )
    com_ing_367 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_51
    )
    com_ing_368 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_166
    )
    com_ing_369 = Component_ingredient.objects.create(
        component=com_34, ingredient=ing_169
    )
    com_ing_370 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_55
    )
    com_ing_371 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_129
    )
    com_ing_372 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_45
    )
    com_ing_373 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_137
    )
    com_ing_374 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_11
    )
    com_ing_375 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_138
    )
    com_ing_376 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_139
    )
    com_ing_377 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_152
    )
    com_ing_378 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_92
    )
    com_ing_379 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_95
    )
    com_ing_380 = Component_ingredient.objects.create(
        component=com_35, ingredient=ing_169
    )
    com_ing_381 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_4
    )
    com_ing_382 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_9
    )
    com_ing_383 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_137
    )
    com_ing_384 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_138
    )
    com_ing_385 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_150
    )
    com_ing_386 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_152
    )
    com_ing_387 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_48
    )
    com_ing_388 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_162
    )
    com_ing_389 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_166
    )
    com_ing_390 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_33
    )
    com_ing_391 = Component_ingredient.objects.create(
        component=com_36, ingredient=ing_169
    )
    com_ing_392 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_129
    )
    com_ing_393 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_65
    )
    com_ing_394 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_104
    )
    com_ing_395 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_134
    )
    com_ing_396 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_108
    )
    com_ing_397 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_138
    )
    com_ing_398 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_66
    )
    com_ing_399 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_152
    )
    com_ing_400 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_48
    )
    com_ing_401 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_164
    )
    com_ing_402 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_166
    )
    com_ing_403 = Component_ingredient.objects.create(
        component=com_37, ingredient=ing_169
    )
    com_ing_404 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_43
    )
    com_ing_405 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_4
    )
    com_ing_406 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_44
    )
    com_ing_407 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_45
    )
    com_ing_408 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_46
    )
    com_ing_409 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_11
    )
    com_ing_410 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_138
    )
    com_ing_411 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_47
    )
    com_ing_412 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_13
    )
    com_ing_413 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_152
    )
    com_ing_414 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_48
    )
    com_ing_415 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_49
    )
    com_ing_416 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_50
    )
    com_ing_417 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_162
    )
    com_ing_418 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_163
    )
    com_ing_419 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_51
    )
    com_ing_420 = Component_ingredient.objects.create(
        component=com_38, ingredient=ing_61
    )
    com_ing_421 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_82
    )
    com_ing_422 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_43
    )
    com_ing_423 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_55
    )
    com_ing_424 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_7
    )
    com_ing_425 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_135
    )
    com_ing_426 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_138
    )
    com_ing_427 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_147
    )
    com_ing_428 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_88
    )
    com_ing_429 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_152
    )
    com_ing_430 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_49
    )
    com_ing_431 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_32
    )
    com_ing_432 = Component_ingredient.objects.create(
        component=com_39, ingredient=ing_63
    )
    #
    print_rows(Component_ingredient.objects.filter(date=None))

    # -----------------------------------------------------------------------------
    ri_1 = Restricted_item.objects.create(
        name="fish", restricted_item_group="fish&seafood", description=""
    )
    ri_2 = Restricted_item.objects.create(
        name="seafood", restricted_item_group="fish&seafood", description=""
    )
    ri_3 = Restricted_item.objects.create(
        name="beef", restricted_item_group="meat", description=""
    )
    ri_4 = Restricted_item.objects.create(
        name="lamb", restricted_item_group="meat", description="gluten, salt"
    )
    ri_5 = Restricted_item.objects.create(
        name="pork", restricted_item_group="meat", description="text"
    )
    ri_6 = Restricted_item.objects.create(
        name="poultry", restricted_item_group="meat", description="text"
    )
    ri_7 = Restricted_item.objects.create(
        name="sausage", restricted_item_group="meat", description="text"
    )
    ri_8 = Restricted_item.objects.create(
        name="turkey ", restricted_item_group="meat", description="text"
    )
    ri_9 = Restricted_item.objects.create(
        name="nuts ", restricted_item_group="nuts&seeds", description=""
    )
    ri_10 = Restricted_item.objects.create(
        name="peanut butter", restricted_item_group="nuts&seeds", description=""
    )
    ri_11 = Restricted_item.objects.create(
        name="peanuts", restricted_item_group="nuts&seeds", description="gluten, salt"
    )
    ri_12 = Restricted_item.objects.create(
        name="seeds", restricted_item_group="nuts&seeds", description="text"
    )
    ri_13 = Restricted_item.objects.create(
        name="dairy", restricted_item_group="other", description="text"
    )
    ri_14 = Restricted_item.objects.create(
        name="gluten", restricted_item_group="other", description="text"
    )
    ri_15 = Restricted_item.objects.create(
        name="spicy", restricted_item_group="other", description="text"
    )
    ri_16 = Restricted_item.objects.create(
        name="green veggies", restricted_item_group="vegetables", description=""
    )
    ri_17 = Restricted_item.objects.create(
        name="leafy greens", restricted_item_group="vegetables", description=""
    )
    ri_18 = Restricted_item.objects.create(
        name="legumes", restricted_item_group="vegetables", description="gluten, salt"
    )
    #
    print_rows(Restricted_item.objects)

    # -----------------------------------------------------------------------------
    inc_1 = Incompatibility.objects.create(restricted_item=ri_3, ingredient=ing_69)
    inc_2 = Incompatibility.objects.create(restricted_item=ri_3, ingredient=ing_72)
    inc_3 = Incompatibility.objects.create(restricted_item=ri_3, ingredient=ing_78)
    inc_4 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_1)
    inc_5 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_2)
    inc_6 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_3)
    inc_7 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_4)
    inc_8 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_5)
    inc_9 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_6)
    inc_10 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_7)
    inc_11 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_8)
    inc_12 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_9)
    inc_13 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_10)
    inc_14 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_13)
    inc_15 = Incompatibility.objects.create(restricted_item=ri_13, ingredient=ing_15)
    inc_16 = Incompatibility.objects.create(restricted_item=ri_1, ingredient=ing_38)
    inc_17 = Incompatibility.objects.create(restricted_item=ri_1, ingredient=ing_39)
    inc_18 = Incompatibility.objects.create(restricted_item=ri_1, ingredient=ing_40)
    inc_19 = Incompatibility.objects.create(restricted_item=ri_1, ingredient=ing_41)
    inc_20 = Incompatibility.objects.create(restricted_item=ri_1, ingredient=ing_42)
    inc_21 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_52)
    inc_22 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_54)
    inc_23 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_57)
    inc_24 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_95)
    inc_25 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_61)
    inc_26 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_62)
    inc_27 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_33)
    inc_28 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_34)
    inc_29 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_35)
    inc_30 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_36)
    inc_31 = Incompatibility.objects.create(restricted_item=ri_14, ingredient=ing_37)
    inc_32 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_121)
    inc_33 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_125)
    inc_34 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_126)
    inc_35 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_127)
    inc_36 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_133)
    inc_37 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_136)
    inc_38 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_140)
    inc_39 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_141)
    inc_40 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_142)
    inc_41 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_143)
    inc_42 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_147)
    inc_43 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_160)
    inc_44 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_161)
    inc_45 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_162)
    inc_46 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_165)
    inc_47 = Incompatibility.objects.create(restricted_item=ri_16, ingredient=ing_169)
    inc_48 = Incompatibility.objects.create(restricted_item=ri_4, ingredient=ing_75)
    inc_49 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_121)
    inc_50 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_133)
    inc_51 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_143)
    inc_52 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_147)
    inc_53 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_162)
    inc_54 = Incompatibility.objects.create(restricted_item=ri_17, ingredient=ing_165)
    inc_55 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_64)
    inc_56 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_65)
    inc_57 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_66)
    inc_58 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_67)
    inc_59 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_14)
    inc_60 = Incompatibility.objects.create(restricted_item=ri_18, ingredient=ing_68)
    inc_61 = Incompatibility.objects.create(restricted_item=ri_9, ingredient=ing_16)
    inc_62 = Incompatibility.objects.create(restricted_item=ri_9, ingredient=ing_17)
    inc_63 = Incompatibility.objects.create(restricted_item=ri_9, ingredient=ing_24)
    inc_64 = Incompatibility.objects.create(restricted_item=ri_9, ingredient=ing_25)
    inc_65 = Incompatibility.objects.create(restricted_item=ri_9, ingredient=ing_32)
    inc_66 = Incompatibility.objects.create(restricted_item=ri_10, ingredient=ing_24)
    inc_67 = Incompatibility.objects.create(restricted_item=ri_11, ingredient=ing_24)
    inc_68 = Incompatibility.objects.create(restricted_item=ri_11, ingredient=ing_25)
    inc_69 = Incompatibility.objects.create(restricted_item=ri_5, ingredient=ing_73)
    inc_70 = Incompatibility.objects.create(restricted_item=ri_5, ingredient=ing_74)
    inc_71 = Incompatibility.objects.create(restricted_item=ri_5, ingredient=ing_77)
    inc_72 = Incompatibility.objects.create(restricted_item=ri_6, ingredient=ing_71)
    inc_73 = Incompatibility.objects.create(restricted_item=ri_6, ingredient=ing_81)
    inc_74 = Incompatibility.objects.create(restricted_item=ri_7, ingredient=ing_77)
    inc_75 = Incompatibility.objects.create(restricted_item=ri_2, ingredient=ing_98)
    inc_76 = Incompatibility.objects.create(restricted_item=ri_2, ingredient=ing_99)
    inc_77 = Incompatibility.objects.create(restricted_item=ri_12, ingredient=ing_30)
    inc_78 = Incompatibility.objects.create(restricted_item=ri_15, ingredient=ing_104)
    inc_79 = Incompatibility.objects.create(restricted_item=ri_15, ingredient=ing_109)
    inc_80 = Incompatibility.objects.create(restricted_item=ri_8, ingredient=ing_81)
    #
    print_rows(Incompatibility.objects)

    # =====================================================
    print("END dataload")
