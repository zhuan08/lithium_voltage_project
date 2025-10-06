from mp_api.client import MPRester
from pymatgen.io.ase import AseAtomsAdaptor
from ase.visualize import view
from ase.calculators.emt import EMT

with MPRester(api_key="WZO3e0HvLSFA4IEfbpLgopWVlDoXDhRB") as mpr:
    data = mpr.materials.search(material_ids=["mp-81"])
structure = data[0].structure
atoms = AseAtomsAdaptor.get_atoms(structure)
view(atoms)

fast_calc = EMT()
atoms.calc = fast_calc
energy = atoms.get_potential_energy()
print(f'Fast calculation energy: {energy} eV')