from django.db import models
from django.utils.translation import ugettext_lazy as _

COMPONENT_GROUP_CHOICES = (
    ('main_dish', _('Main Dish')),
    ('dessert', _('Dessert')),
    ('diabetic', _('Diabetic Dessert')),
    ('fruit_salad', _('Fruit Salad')),
    ('green_salad', _('Green Salad')),
    ('pudding', _('Pudding')),
    ('compote', _('Compote')),
)

COMPONENT_GROUP_CHOICES_MAIN_DISH = COMPONENT_GROUP_CHOICES[0][0]

INGREDIENT_GROUP_CHOICES = (
    ('meat', _('Meat')),
    ('dairy', _('Dairy')),
    ('fish', _('Fish')),
    ('seafood', _('Seafood')),
    ('veggies_and_fruits', _('Veggies and fruits')),
    ('legumineuse', _('Legumineuse')),
    ('grains', _('Grains')),
    ('fresh_herbs', _('Fresh herbs')),
    ('spices', _('Spices')),
    ('dry_and_canned_goods', _('Dry and canned goods')),
    ('oils_and_sauces', _('Oils and sauces')),
)

RESTRICTED_ITEM_GROUP_CHOICES = (
    ('meat', _('Meat')),
    ('vegetables', _('Vegetables')),
    ('seafood', _('Seafood')),
    ('seeds and nuts', _('Seeds and nuts')),
    ('other', _('Other')),
)


class Ingredient(models.Model):
    class Meta:
        verbose_name_plural = _('ingredients')

    # Information about the ingredient (in the recipe of a component)
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )

    ingredient_group = models.CharField(
        max_length=100,
        choices=INGREDIENT_GROUP_CHOICES,
        verbose_name=_('ingredient group')
    )

    def __str__(self):
        return self.name


class Component(models.Model):

    class Meta:
        verbose_name_plural = _('components')

    # Meal component (ex. main dish, vegetable, seasonal) information
    name = models.CharField(
        max_length=50,
        verbose_name=_('name'),
        unique=True,
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )

    component_group = models.CharField(
        max_length=100,
        choices=COMPONENT_GROUP_CHOICES,
        verbose_name=_('component group')
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_day_ingredients(component_id, delivery_date):
        """Returns a list of the actual ingredients
        of a component for the delivery date."""
        q = Component_ingredient.objects.\
            filter(component__id=component_id, date=delivery_date)
        # print("query=", q.query)  # DEBUG
        return [ci.ingredient for ci in q]


class Component_ingredient(models.Model):
    component = models.ForeignKey(
        'meal.Component',
        verbose_name=_('component'),
        related_name='+')

    ingredient = models.ForeignKey(
        'meal.Ingredient',
        verbose_name=_('ingredient'),
        related_name='+')

    date = models.DateField(
        verbose_name=_('date'),
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.date:
            return "<{}> includes <{}> on <{}>". \
                format(self.component.name,
                       self.ingredient.name,
                       self.date)
        else:
            return "<{}> contains <{}>". \
                format(self.component.name,
                       self.ingredient.name)


class Restricted_item(models.Model):

    class Meta:
        verbose_name_plural = _('restricted items')

    # Information about restricted item categories that some clients never eat
    #   for allergy or other reasons (ex. Gluten, Nuts, Pork)
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )

    restricted_item_group = models.CharField(
        max_length=100,
        choices=RESTRICTED_ITEM_GROUP_CHOICES,
        verbose_name=_('restricted item group')
    )

    def __str__(self):
        return self.name


class Incompatibility(models.Model):
    restricted_item = models.ForeignKey(
        'meal.Restricted_item',
        verbose_name=_('restricted item'),
        related_name='+')

    ingredient = models.ForeignKey(
        'meal.Ingredient',
        verbose_name=_('ingredient'),
        related_name='+')

    def __str__(self):
        return "{} <clash> {}".format(self.restricted_item.name,
                                      self.ingredient.name)


class Menu(models.Model):

    class Meta:
        verbose_name_plural = _('menus')

    # Menu information for a specific date
    date = models.DateField(verbose_name=_('date'))

    def __str__(self):
        return "Menu for {}".format(str(self.date))

    @staticmethod
    def create_menu_and_components(menu_date, dish_names):
        """Create the menu and its components for the date.

        Parameters:
          menu_date : date on which menu will apply
          dish_names : a list of names of dishes included in the menu

        Behavior:
          - if Menu already exists for the date, all its menu components
            are replaced by the new ones

        Raises :
          - Exception if dish does not exist
          - Exception if more that one dish per component_group
          - Exception if no dish for COMPONENT_GROUP_CHOICES_MAIN_DISH

        Returns:
          Number of menu components created.
        """

        num_menu_comp_created = 0
        component_groups = {}
        try:
            menu = Menu.objects.get(date=menu_date)
        except Menu.DoesNotExist:
            menu = Menu(date=menu_date)
            menu.save()
        else:
            # menu existed, must flush its menu_components
            Menu_component.objects.filter(menu=menu).delete()
        for dish_name in dish_names:
            components = Component.objects.filter(name=dish_name)
            if not components:
                raise Exception(
                    "Component ", dish_name, " does not exist")
            component = components[0]
            if component_groups.get(component.component_group):
                raise Exception(
                    "Menu can only have one dish for component group " +
                    component.component_group)
            component_groups[component.component_group] = dish_name
            menu_component = Menu_component(menu=menu, component=component)
            menu_component.save()
            num_menu_comp_created += 1
        # END FOR
        if not component_groups.get(COMPONENT_GROUP_CHOICES_MAIN_DISH):
            raise Exception(
                "Menu must include one dish for component group " +
                COMPONENT_GROUP_CHOICES_MAIN_DISH)
        return num_menu_comp_created


class Menu_component(models.Model):
    menu = models.ForeignKey(
        'meal.Menu',
        verbose_name=_('menu'),
        related_name='+')

    component = models.ForeignKey(
        'meal.Component',
        verbose_name=_('component'),
        related_name='+')

    def __str__(self):
        return "On {} <menu includes> {}".format(str(self.menu.date),
                                                 self.component.name)
