class Contact(object):
    all_contacts: list("Contact")=[]

    def __init__(self,name: str, email: str) -> None:
        self.name=name
        self.email=email
        self.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )
class Supplier(Contact):
    def order (self, order: "order") ->None :
        print("if it was a real system" 
        f" we would order {order} from {self.name}")


print ("called from: ",__name__)