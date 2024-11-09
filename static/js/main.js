/* Confirmación en cada botón de eliminar contacto */
var del_links = document.getElementsByClassName("del_contact");

if (del_links.length > 0){
    var confirmar = function(e){
        if (!confirm("Delete now?")) e.preventDefault();
    };
    for (const del_link of del_links)
        del_link.addEventListener('click', confirmar, false);
}