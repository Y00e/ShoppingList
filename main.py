class ShoppingList:
  #I konstruktorn skapa en lista för varorna
  def __init__(self):
    self.items = []

  #En metod för att lägga till.
  # Kolla så att värdet är en text (string)
  def add_item(self, item):
    if not isinstance(item, str):
      print("Item is not a string")
      return False

    self.items.append(item)

  #En metod för att se listans innehåll
  # Om listan är tom, skriv ut "list is empty"
  def view_content(self):
    pass

  #Ta bort det första item:et som stämmer överens med parametern "item"
  # Om listan inte innehåller "item", skriv ut "item coult not be found"
  def delete_item(self, item):
    pass


## ÖVNING: Skapa ett program där ni implementerar ett konsol gränssnitt för att lägga till varor, se innehåll, och ta bort en vara
if __name__ == '__main__':
  pass