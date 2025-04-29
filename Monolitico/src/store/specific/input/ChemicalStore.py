from domain.Chemical import ChemicalComposition
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
            chemical_composition = ChemicalComposition(
                ind,
                df['FechaRegistroCQ'][ind],
                df['P'][ind],
                df['S'][ind],
                df['C'][ind],
                df['Si'][ind],
                df['Cu'][ind],
                df['Cr'][ind],
                df['Mg'][ind],
                df['Mn'][ind],
                df['Al'][ind],
                df['Ce'][ind],
                df['Sn'][ind],
                df['Zn'][ind],
                df['Mo'][ind],
                df['Sb'][ind],
                df['W'][ind],
                df['Ni'][ind],
                0,
                0,
                0,
                df['Ti'][ind],
                df['Pb'][ind],
                df['Bi'][ind],
                df['B'][ind],
                df['Fe'][ind],
                df['Zr'][ind]
            )

            chemical_composition_list.append(chemical_composition)        

        # We return de list of chemical compositions
        return chemical_composition_list