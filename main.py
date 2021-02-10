# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Contact:
  def __init__(mysillyobject, name, email,phone):
    mysillyobject.name = name
    mysillyobject.email = email
    mysillyobject.phone = phone
  def __str__(self):
    return str(self.name)+"/ "+ str(self.email) +" / "+ str(self.phone)

class Lead:
  def __init__(mysillyobject, name, email,phone):
    mysillyobject.name = name
    mysillyobject.email = email
    mysillyobject.phone = phone
  def __str__(self):
    return str(self.name)+"/ "+ str(self.email) +" / "+ str(self.phone)
registrants = [{
  "registrant": 
     { 
        "name": "Lucy Liu", 
        "email": "lucy@liu.com",
        "phone": None,
     }},{
    "registrant": 
     { 
        "name": "Doug", 
        "email": "doug@emmy.com",
        "phone": "4564445556",
     }},{
     "registrant": 
     { 
        "name": "Uma Thurman", 
        "email": "uma@thurs.com",
        "phone": None,
     }
}]
ContactList = []
ContactList.append(Contact("Alice Brown",None,"1231112223"))
ContactList.append(Contact("Bob Crown","bob@crowns.com",None))
ContactList.append(Contact("Carlos Drew","carl@drewess.com","3453334445"))
ContactList.append(Contact("Doug Emerty",None,"4564445556"))
ContactList.append(Contact("Egan Fair","eg@fairness.com","5675556667"))
LeadsList =  []
LeadsList.append(Lead(None,"kevin@keith.com",None))
LeadsList.append(Lead("Lucy Liu","lucy@liu.com","3210001112"))
LeadsList.append(Lead("Mary Middle","mary@middle.com","3331112223"))
LeadsList.append(Lead(None,None,"4442223334"))
LeadsList.append(Lead(None,"ole@olson.com",None))

def matching(registrants,LeadsList,ContactList):
    j = 0
    print(len(registrants))
    for registrant in registrants:
        i =0
        rg = registrant["registrant"]
        isContact=isLead = False
        for contact in ContactList:
            if contact.email ==rg["email"] and contact.email is not None and rg["email"] is not None:
                isContact = True
                print("isLeac1")
            elif contact.phone  ==rg["phone"] and contact.phone is not None and rg["phone"] is not None:
                isContact = True
            if isContact:
                contact=updateObject(rg,contact)
                    
        if not isContact:
            for lead in LeadsList:
                if lead.email ==rg["email"]:
                    LeadsList.remove(lead)
                    lead=updateObject(rg,lead)
                    ContactList.append(lead)
                    isLead= True
            i=i+1
        j=j+1
        if (not isContact and not isLead ):
            new_c = Contact(rg["name"],rg["email"],rg["phone"])
            ContactList.append(new_c)
            
    print(len(LeadsList))
    print(len(ContactList))
def updateObject(o1,o2):
    if o1["name"] is not None and o2.name is None:  o2.name = o1["name"]
    if o1["phone"] is not None and o2.phone is None:  o2.phone = o1["phone"]
    if o1["email"] is not None and o2.email  is None:  o2.email = o1["email"]
    return o2
    
    
matching (registrants,LeadsList,ContactList)
