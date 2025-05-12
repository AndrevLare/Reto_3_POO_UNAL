``` mermaid
---
config:
  theme: neo-dark
---
classDiagram
    direction TB
    class MenuItem {
        +String Name
        +Float Price
        +init(self, Name, Price)
    }
    class MainCourse {
        +String flour
        +String Protein
        +String Salad
        +init(self, flour, Protein, Salad)
    }
    class Drink {
        +String Type
        +String Size
        +Bool hasSugar
        +init(self, Type, Size, hasSugar)
    }
    class Dessert {
        +String Type
        +init(self, Type)
    }
    class Order {
        +MenuItem[] Items
        +init(self, Name, Price)
        +getTotalPrice(self)
        +addItem(self, item: MenuItem)
        +calculateDiscounts(self)
    }

    
    MenuItem <|-- MainCourse
    MenuItem <|-- Drink
    MenuItem <|-- Dessert
    Order *-- MenuItem
