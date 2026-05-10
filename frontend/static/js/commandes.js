const API =
"http://127.0.0.1:8000/api"

const table =
document.getElementById(
    "commandesTable"
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

const addLigneBtn =
document.getElementById(
    "addLigneBtn"
)

const lignesContainer =
document.getElementById(
    "lignesContainer"
)

const commandeForm =
document.getElementById(
    "commandeForm"
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

async function chargerCommandes(){

    let url =
    `${API}/commandes`

    const statut =
    statutFilter.value

    if(statut){

        url += `?statut=${statut}`
    }

    const response =
    await fetch(url)

    const commandes =
    await response.json()

    afficherCommandes(commandes)
}

function afficherCommandes(commandes){

    table.innerHTML = ""

    const aujourdHui =
    new Date()

    commandes.forEach(cmd => {

        const datePrevue =
        new Date(
            cmd.date_livraison_prevue
        )

        const enRetard =
        (
            datePrevue < aujourdHui &&
            cmd.statut !== 'livree' &&
            cmd.statut !== 'annulee'
        )

        table.innerHTML += `

            <tr class="
                ${enRetard ? 'retard' : ''}
            ">

                <td>
                    ${cmd.id}
                </td>

                <td>
                    ${cmd.fournisseur_nom}
                </td>

                <td>
                    ${cmd.date_livraison_prevue}
                </td>

                <td>

                    <span class="
                        badge
                        ${cmd.statut}
                    ">

                        ${cmd.statut}

                    </span>

                </td>

                <td>
                    ${cmd.lignes.length}
                </td>

                <td>

                    <div class="actions">

                        ${boutonsTransition(cmd)}

                    </div>

                </td>

            </tr>
        `
    })
}

function boutonsTransition(cmd){

    let html = ""

    if(cmd.statut === 'en_attente'){

        html += `
            <button
                onclick="
                changerStatut(
                    ${cmd.id},
                    'confirmee'
                )">

                Confirmer

            </button>
        `

        html += `
            <button
                onclick="
                changerStatut(
                    ${cmd.id},
                    'annulee'
                )">

                Annuler

            </button>
        `
    }

    if(cmd.statut === 'confirmee'){

        html += `
            <button
                onclick="
                livrerCommande(
                    ${cmd.id}
                )">

                Livrer

            </button>
        `
    }

    return html
}

async function changerStatut(
    id,
    statut
){

    await fetch(

        `${API}/commandes/${id}/statut`,

        {

            method:'PATCH',

            headers:{
                'Content-Type':
                'application/json'
            },

            body:JSON.stringify({
                statut:statut
            })
        }
    )

    chargerCommandes()
}

async function livrerCommande(id){

    const confirmation =
    confirm(
        "Passer en livrée ? Le stock sera mis à jour."
    )

    if(!confirmation){

        return
    }

    await changerStatut(
        id,
        'livree'
    )

    alert(
        "Commande livrée avec succès"
    )
}

function ajouterLigne(){

    lignesContainer.innerHTML += `

        <div class="ligne">

            <input
                type="number"
                placeholder="Produit ID"
                class="produit"
                required
            >

            <input
                type="number"
                placeholder="Quantité"
                class="quantite"
                required
            >

            <input
                type="number"
                placeholder="Prix achat"
                class="prix"
                required
            >

        </div>
    `
}

addLigneBtn.addEventListener(
    'click',
    ajouterLigne
)

commandeForm.addEventListener(
    'submit',

    async (e) => {

        e.preventDefault()

        const lignes = []

        const produits =
        document.querySelectorAll(
            '.produit'
        )

        const quantites =
        document.querySelectorAll(
            '.quantite'
        )

        const prixs =
        document.querySelectorAll(
            '.prix'
        )

        for(let i = 0; i < produits.length; i++){

            lignes.push({

                produit:
                produits[i].value,

                quantite_commandee:
                quantites[i].value,

                prix_achat_unitaire:
                prixs[i].value
            })
        }

        const data = {

            fournisseur_nom:
            document.getElementById(
                'fournisseurNom'
            ).value,

            fournisseur_contact:
            document.getElementById(
                'fournisseurContact'
            ).value,

            date_livraison_prevue:
            document.getElementById(
                'dateLivraison'
            ).value,

            boutique_id:1,

            lignes:lignes
        }

        const response =
        await fetch(

            `${API}/commandes`,

            {

                method:'POST',

                headers:{
                    'Content-Type':
                    'application/json'
                },

                body:JSON.stringify(data)
            }
        )

        if(response.status === 400){

            alert(
                "Erreur formulaire"
            )

            return
        }

        modal.style.display = "none"

        commandeForm.reset()

        lignesContainer.innerHTML = ""

        chargerCommandes()
    }
)

statutFilter.addEventListener(
    'change',
    chargerCommandes
)

ajouterLigne()

chargerCommandes()