function renderNavbar(activePage) {
    return `

        <nav class="navbar">

            <div class="navbar-container">

                <!-- LOGO -->

                <div class="logo">

                    STOCKFLOW

                </div>

                <!-- MENU MOBILE -->

                <div
                    class="menu-toggle"
                    id="menuToggle"
                >

                    ☰

                </div>

                <!-- LIENS -->

                <div
                    class="nav-links"
                    id="navLinks"
                >

                    <a
                        href="./dashboard.html"

                        class="
                            nav-link

                            ${activePage === "dashboard" ? "nav-active" : ""}
                        "
                    >

                        Dashboard

                    </a>

                    <a
                        href="./inventaire.html"

                        class="
                            nav-link

                            ${activePage === "inventaire" ? "nav-active" : ""}
                        "
                    >

                        Inventaire

                    </a>

                    <a
                        href="./commandes.html"

                        class="
                            nav-link

                            ${activePage === "commandes" ? "nav-active" : ""}
                        "
                    >

                        Commandes

                    </a>

                    <a
    href="./statistiques.html"

    class="
        nav-link

        ${activePage === "statistiques" ? "nav-active" : ""}
    "
>

    Statistiques

</a>

                </div>

            </div>

        </nav>
    `;
}

/* MENU MOBILE */

document.addEventListener(
    "click",

    (e) => {
        const menuToggle = document.getElementById("menuToggle");

        const navLinks = document.getElementById("navLinks");

        if (menuToggle && e.target === menuToggle) {
            navLinks.classList.toggle("active");
        }
    },
);
