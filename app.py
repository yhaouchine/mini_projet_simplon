import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')



# Calcule CA et ventes par produit
données['ca_par_ligne'] = données['qte'] * données['prix']

tableau = données.groupby('produit', as_index=False).agg(
    quantité_par_produit = ('qte', 'sum'),
    chiffre_affaire_par_produit = ('ca_par_ligne', 'sum') 
    )

# Figure ventes par produit
figure1 = px.pie(tableau, values='quantité_par_produit', names='produit', title='Quantité vendue par produit')
figure1.write_html('ventes_par_produit.html')
print('ventes_par_produit.html généré avec succès.')

# Figure chiffre d'affaire par produit
figure2 = px.pie(tableau, values='chiffre_affaire_par_produit', names='produit', title='CA par produit')
figure2.write_html('CA_par_produit.html')
print('CA_par_produit.html généré avec succès.')

# Figure ventes par régions
figure3 = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure3.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')
