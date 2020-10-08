############
# Part 1   #
############

print("this is the correct file")

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name,pairings):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

   
    print("initialized")
          

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code=new_code
        print(f'Code updated to {new_code}')


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    melon_1=MelonType("musk", 1998, "green", True,False,"Muskmelon",[] )
    melon_1.add_pairing('mint')
    all_melon_types.append(melon_1)

    melon_2 = MelonType( 'cas' , 2003, 'orange', False, False, 'Casaba',[])
    melon_2.add_pairing ('strawberries')
    melon_2.add_pairing ('mint')
    all_melon_types.append(melon_2)

    melon_3=MelonType("cren", 1996, "green", True,False,"Crenshaw",[] )
    melon_3.add_pairing('proscuitto')
    all_melon_types.append(melon_3)

    melon_4 = MelonType("yw", 2013, "yellow", True,True,"Yellow Watermelon",[])
    melon_4.add_pairing('ice cream')
    all_melon_types.append(melon_4)
    print(all_melon_types)
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    make_melon_types()
    all_melon_type= make_melon_types()
    print(all_melon_type[melon_types])
 
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    lst =make_melon_types()
    for item in lst:
        # melon_dict[item.name]=lst[item.code]
         melon_dict[item.name] = item.code
    return melon_dict

############
# Part 2   #
############

class Melon:
    """A melon in a melon harvest."""

    def __init__(self, mel_type, shape, color, field, harvester ):
        self.mel_type = mel_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    
    
    def is_sellable(self,color,shape,field):
        
        if (self.shape > 5 and self.color > 5) and self.field !=3:
            return True 
        else:
            return False

        
    def make_melons(self,melon_types):
        """Returns a list of Melon objects."""
        melon_list = []
        melon1 = Melon("yw",8,7,2,"Sheila")
        melon2 = Melon("yw",3, 4, 2,"Sheila")
        melon3 = Melon("yw",9,8,3,"Sheila")
        melon4 = Melon("cas",10,6,35,"Sheila")
        melon6 = Melon("cren",8,2,35,"Michael")
        melon5 = Melon("cren", 8, 9, 35,"Michael")
        melon7= Melon("cren",2, 3, 4, "Michael")
        melon8 = Melon("musk", 6, 7, 4,"Michael")
        melon9 = Melon("yw" ,7,10,3,"Sheila")
        melon_list=melon_list.append(melon9,melon8,
        melon7,melon6,melon5,melon4,melon3,melon2,melon1)

        return melon_list

    def melon_make_melons(self, melon_types):
        melon_lst=[]
        melon_types = make_melon_types()

        melons_by_id = make_melon_type_lookup(melon_types)
        melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
        melon2 = Melon(melons_by_id['yw'],3, 4, 2,"Sheila")
        melon3 = Melon(melons_by_id['yw'],9,8,3,"Sheila")
        melon4 = Melon(melons_by_id["cas"],10,6,35,"Sheila")
        melon6 = Melon(melons_by_id["cren"],8,2,35,"Michael")
        melon5 = Melon(melons_by_id["cren"], 8, 9, 35,"Michael")
        melon7= Melon(melons_by_id["cren"],2, 3, 4, "Michael")
        melon8 = Melon(melons_by_id["musk"], 6, 7, 4,"Michael")
        melon9 = Melon(melons_by_id['yw'],7,10,3,"Sheila")
        melon_lst.extend(melon9,melon8,
        melon7,melon6,melon5,melon4,melon3,melon2,melon1)
        
        return melon_lst
    
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        harvested_by = f'Harvested by {melon.harvester}'
        field_num = f'Field #{melon.field}'
        status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'
        print(f'{harvested_by} from {field_num} {status}')

    



