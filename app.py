import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

st.title("AI Drug Property Predictor")
st.write("By Darshan - B.Pharm + AI")

drugs = {
    'Paracetamol (Dolo)': 'CC(=O)NC1=CC=C(C=C1)O',
    'Aspirin': 'CC(=O)OC1=CC=C1C(=O)O',
    'Ibuprofen (Brufen)': 'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',
    'Cetirizine (Zyrtec)': 'C1=CC(=CC=C1CCN2CCN(CC2)CC(=O)O)C3=CC=C(C=C3)Cl',
    'Omeprazole (Omez)': 'COC1=C(N=C(C=C1)CS(=O)C2=NC3=CC=C3N2)OC',
    'Metformin (Glycomet)': 'CN(C)C(=N)NC(=N)N',
    'Amoxicillin': 'CC1(C(N2C(S1)C(C2=O)NC(=O)C(C3=CC=C(C=C3)O)N)C(=O)O)C',
    'Ciprofloxacin': 'C1CC1N2C=C(C(=O)C3=CC(=C(C=C32)N4CCNCC4)F)C(=O)O',
}
choice = st.radio("Select a Drug", list(drugs.keys()))

if st.button("Predict"):
    mol = Chem.MolFromSmiles(drugs[choice])
    wt = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    st.write(f"**Molecular Weight:** {wt:.2f}")
    st.write(f"**LogP:** {logp:.2f}")
    if 1 <= logp <= 3:
        st.success("Prediction: Good - Easy to absorb")
    elif logp < 1:
        st.warning("Prediction: Poor - Too water soluble")
    else:
        st.warning("Prediction: Poor - Too oily")
