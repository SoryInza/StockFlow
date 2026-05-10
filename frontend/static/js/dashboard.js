const API = "http://127.0.0.1:8000/api"

const boutiqueSelect =
document.getElementById(
    "boutiqueSelect"
)

const refreshBtn =
document.getElementById(
    "refreshBtn"
)

async function chargerDashboard(){

    const boutiqueId =
    boutiqueSelect.value

    const response = await fetch(

        `${API}/dashboard?boutique_id=${boutiqueId}`
    )

    const data = await response.json()

    afficherResume(data.resume)

    afficherAlertes(
        data.alertes_critiques
    )

    afficherCommandes(
        data.commandes_en_attente
    )

    afficherRecentes(
        data.commandes_recentes
    )
}

function afficherResume(resume){

    document.getElementById(
        "totalProduits"
    ).innerText =
    resume.total_produits

    document.getElementById(
        "produitsAlerte"
    ).innerText =
    resume.produits_en_alerte

    document.getElementById(
        "produitsRupture"
    ).innerText =
    resume.produits_en_rupture

    document.getElementById(
        "valeurStock"
    ).innerText =
    resume.valeur_totale_stock +
    " FCFA"
}

function afficherAlertes(alertes){

    const container =
    document.getElementById(
        "alertesContainer"
    )

    container.innerHTML = ""

    if(alertes.length === 0){

        container.innerHTML =
        "<p>Aucune alerte</p>"

        return
    }

    alertes.forEach(alerte => {

        container.innerHTML += `

            <div class="alert-item">

                <div>

                    <strong>
                        ${alerte.nom}
                    </strong>

                    <p>
                        Stock:
                        ${alerte.stock}
                    </p>

                </div>

                <div>

                    Déficit:
                    ${alerte.deficit}

                </div>

            </div>
        `
    })
}

function afficherCommandes(data){

    document.getElementById(
        "cmdAttente"
    ).innerText =
    data.total

    document.getElementById(
        "cmdRetard"
    ).innerText =
    data.en_retard
}

function afficherRecentes(commandes){

    const table =
    document.getElementById(
        "commandesTable"
    )

    table.innerHTML = ""

    commandes.forEach(cmd => {

        table.innerHTML += `

            <tr>

                <td>
                    ${cmd.id}
                </td>

                <td>
                    ${cmd.fournisseur}
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
                    ${cmd.date}
                </td>

            </tr>
        `
    })
}

refreshBtn.addEventListener(
    'click',
    chargerDashboard
)

boutiqueSelect.addEventListener(
    'change',
    chargerDashboard
)

chargerDashboard()