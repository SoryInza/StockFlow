const API =
"http://127.0.0.1:8000/api"

document.getElementById(
    "navbar"
).innerHTML =
renderNavbar('statistiques')

async function chargerStatistiques(){

    const response = await fetch(

        `${API}/statistiques?boutique_id=1`
    )

    const data = await response.json()

    afficherCards(data)

    afficherCategorieChart(
        data.categories
    )

    afficherCommandeChart(
        data.commandes
    )
}

function afficherCards(data){

    document.getElementById(
        'totalStock'
    ).innerText =
    data.stock.total_stock

    document.getElementById(
        'valeurTotale'
    ).innerText =
    data.stock.valeur_totale +
    ' FCFA'

    document.getElementById(
        'produitsAlertes'
    ).innerText =
    data.stock.produits_alertes
}

function afficherCategorieChart(categories){

    const labels =
    Object.keys(categories)

    const values =
    Object.values(categories)

    new Chart(

        document.getElementById(
            'categorieChart'
        ),

        {
            type:'bar',

            data:{

                labels:labels,

                datasets:[{

                    label:'Produits',

                    data:values,

                    backgroundColor:[
                        '#2563eb',
                        '#16a34a',
                        '#dc2626',
                        '#f59e0b'
                    ]
                }]
            }
        }
    )
}

function afficherCommandeChart(commandes){

    new Chart(

        document.getElementById(
            'commandeChart'
        ),

        {
            type:'doughnut',

            data:{

                labels:[
                    'Livrées',
                    'En attente'
                ],

                datasets:[{

                    data:[
                        commandes.livrees,
                        commandes.en_attente
                    ],

                    backgroundColor:[
                        '#16a34a',
                        '#f59e0b'
                    ]
                }]
            }
        }
    )
}

chargerStatistiques()