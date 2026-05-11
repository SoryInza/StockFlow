const API =
"http://127.0.0.1:8000/api"

const table =
document.getElementById(
    "produitsTable"
)

const categorieFilter =
document.getElementById(
    "categorieFilter"
)

const statutFilter =
document.getElementById(
    "statutFilter"
)

const modal =
document.getElementById(
    "modal"
)

const openModalBtn =
document.getElementById(
    "openModalBtn"
)

const produitForm =
document.getElementById(
    "produitForm"
)

openModalBtn.addEventListener(
    'click',
    () => {

        modal.style.display = "flex"
    }
)

window.addEventListener(
    'click',
    (e) => {

        if(e.target === modal){

            modal.style.display = "none"
        }
    }
)

async function chargerProduits(){

    let url =
    `${API}/produits`

    const categorie =
    categorieFilter.value

    const statut =
    statutFilter.value

    const params = []

    if(categorie){

        params.push(
            `categorie=${categorie}`
        )
    }

    if(statut){

        params.push(
            `statut=${statut}`
        )
    }

    if(params.length > 0){

        url += '?' + params.join('&')
    }

    const response =
    await fetch(url)

    const produits =
    await response.json()

    afficherProduits(produits)
}

function afficherProduits(produits){

    table.innerHTML = ""

    produits.forEach(produit => {

        let statut = "ok"

        if(produit.quantite_stock === 0){

            statut = "rupture"
        }

        else if(produit.en_alerte){

            statut = "alerte"
        }

        table.innerHTML += `

            <tr 
    class="produit-row">

                <td>
                    ${produit.nom}
                </td>

                <td>
                    ${produit.sku}
                </td>

                <td>
                    ${produit.categorie}
                </td>

                <td>
                    ${produit.quantite_stock}
                </td>

                <td>
                    ${produit.seuil_alerte}
                </td>

                <td>
                    ${produit.prix_unitaire}
                </td>

                <td>

                    <span class="
                        status
                        ${statut}
                    ">

                        ${statut}

                    </span>

                </td>

                <td>

                    <div class="actions">

                        <button
                            class="stock-btn"
                            onclick="
                            modifierStock(
                                ${produit.id},
                                1
                            )">

                            +

                        </button>

                        <button
                            class="stock-btn"
                            onclick="
                            modifierStock(
                                ${produit.id},
                                -1
                            )">

                            -

                        </button>

                        <button
                            class="delete-btn"
                            onclick="
                            supprimerProduit(
                                ${produit.id}
                            )">

                            Supprimer

                        </button>

                        <button
                            class="consult-btn"
                            onclick="voirProduit(${produit.id})">

                            Voir

                        </button>

                    </div>

                </td>

            </tr>
        `
    })
}

async function modifierStock(
    id,
    delta
){

    await fetch(

        `${API}/produits/${id}/stock`,

        {

            method:'PATCH',

            headers:{
                'Content-Type':
                'application/json'
            },

            body:JSON.stringify({

                delta:delta
            })
        }
    )

    chargerProduits()
}

async function supprimerProduit(id){

    const confirmation =
    confirm(
        "Supprimer ce produit ?"
    )

    if(!confirmation){

        return
    }

    const response =
    await fetch(

        `${API}/produits/${id}`,

        {
            method:'DELETE'
        }
    )

    if(response.status === 409){

        alert(
            "Suppression refusée : commande active"
        )

        return
    }

    chargerProduits()
}

async function voirProduit(id){

    const response = await fetch(

        `http://127.0.0.1:8000/api/produits/${id}`
    )

    const produit = await response.json()

    document.getElementById(
        'detailsContent'
    ).innerHTML = `

        <div class="detail-item">

            <span class="detail-label">

                Nom :

            </span>

            ${produit.nom}

        </div>

        <div class="detail-item">

            <span class="detail-label">

                SKU :

            </span>

            ${produit.sku}

        </div>

        <div class="detail-item">

            <span class="detail-label">

                Catégorie :

            </span>

            ${produit.categorie}

        </div>

        <div class="detail-item">

            <span class="detail-label">

                Prix :

            </span>

            ${produit.prix_unitaire} FCFA

        </div>

        <div class="detail-item">

            <span class="detail-label">

                Stock :

            </span>

            ${produit.quantite_stock}

        </div>

        <div class="detail-item">

            <span class="detail-label">

                Seuil :

            </span>

            ${produit.seuil_alerte}

        </div>

        <div class="detail-item">

            <span class="detail-label">

                Statut :

            </span>

            ${

                produit.en_alerte

                ?

                '⚠️ En alerte'

                :

                '✅ OK'
            }

        </div>
    `

    document.getElementById(
        'detailsModal'
    ).style.display = 'flex'
}

produitForm.addEventListener(
    'submit',

    async (e) => {

        e.preventDefault()

        const data = {

            nom:
            document.getElementById(
                'nom'
            ).value,

            sku:
            document.getElementById(
                'sku'
            ).value,

            categorie:
            document.getElementById(
                'categorie'
            ).value,

            prix_unitaire:
            document.getElementById(
                'prix'
            ).value,

            quantite_stock:
            document.getElementById(
                'stock'
            ).value,

            seuil_alerte:
            document.getElementById(
                'seuil'
            ).value,

            boutique_id:1
        }

        const response =
        await fetch(

            `${API}/produits`,

            {

                method:'POST',

                headers:{
                    'Content-Type':
                    'application/json'
                },

                body:JSON.stringify(data)
            }
        )

        const result =
        await response.json()

        if(response.status === 400){

            alert(

                JSON.stringify(result.sku[0])
            )

            return
        }


        modal.style.display = "none"

        produitForm.reset()

        chargerProduits()
    }
)

categorieFilter.addEventListener(
    'change',
    chargerProduits
)

statutFilter.addEventListener(
    'change',
    chargerProduits
)

chargerProduits()

document.getElementById(
    'closeDetailsModal'
).addEventListener(

    'click',

    () => {

        document.getElementById(
            'detailsModal'
        ).style.display = 'none'
    }
)