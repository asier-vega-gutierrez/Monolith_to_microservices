from domain.chemical import ChemicalComposition
import pandas as pd

class ChemicalStore():
    """ Specific store to manage the Alarm Store """
    
    def __init__(self, path) -> None:
        """ Constructor of the class wth the path to the file to manage """
        self._csv_path = path

    def get_chemical_compistions(self):
        """ Method to get all alarms """
        
        # We create the list with all domain information
        chemical_composition_list = []

        # We read CSV with pandas
        df = pd.read_csv(self._csv_path, index_col=0)

        for ind in df.index:
            chemical_composition = ChemicalComposition()

            chemical_composition.id = ind
            chemical_composition.date = df['FechaRegistroCQ'][ind] 
            chemical_composition.p = df['P'][ind] 
            chemical_composition.s = df['S'][ind] 
            chemical_composition.c = df['C'][ind] 
            chemical_composition.si = df['Si'][ind] 
            chemical_composition.cu = df['Cu'][ind] 
            chemical_composition.cr = df['Cr'][ind] 
            chemical_composition.mg = df['Mg'][ind] 
            chemical_composition.mn = df['Mn'][ind] 
            chemical_composition.al = df['Al'][ind] 
            chemical_composition.ce = df['Ce'][ind] 
            chemical_composition.sn = df['Sn'][ind] 
            chemical_composition.zn = df['Zn'][ind] 
            chemical_composition.mo = df['Mo'][ind] 
            chemical_composition.sb = df['Sb'][ind] 
            chemical_composition.w = df['W'][ind] 
            chemical_composition.ni = df['Ni'][ind] 
            chemical_composition.ti = df['Ti'][ind] 
            chemical_composition.pb = df['Pb'][ind] 
            chemical_composition.bi = df['Bi'][ind] 
            chemical_composition.b = df['B'][ind] 
            chemical_composition.fe = df['Fe'][ind] 
            chemical_composition.zr = df['Zr'][ind] 

            chemical_composition_list.append(chemical_composition)        

        # We return de list of chemical compositions
        return chemical_composition_list