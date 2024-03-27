class Cola:

   def __init__(self, title, taste, date):

       self.title = title

       self.taste = taste

       self.date = date

       self.status = "available"


class Supermarket:

   def __init__(self):

       self.Colas = []


   def add_cola(self, cola):

       self.Colas.append(cola)


   def remove_cola(self, cola):

       self.Colas.remove(cola)


   def lend_cola(self, cola):

       if cola.status == "available":

           cola.status = "lent"

           print(f"{cola.title} {cola.taste} було закінчено.")

       else:

           print("Вибачте, але цей тип коли не існує.")


   def return_cola(self, cola):

       if cola.status == "lent":

           cola.status = "available"

           print(f"{cola.title} {cola.taste} була завезена до магазину.")

       else:

           print("Цей тип коли існує.")

supermarket = Supermarket()

cola1 = Cola("Cola", "with Mango", 2023)

cola2 = Cola("Cola", "with Apple", 2025)

cola3 = Cola("Cola", "with Cherry", 2024)

supermarket.add_cola(cola1)

supermarket.add_cola(cola2)

supermarket.add_cola(cola3)

supermarket.lend_cola(cola1)


supermarket.return_cola(cola1)
