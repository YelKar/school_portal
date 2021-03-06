function change_themes() {
    document.querySelector("html").classList.toggle("light-theme")
    let theme = document.querySelector("html").classList.toggle("dark-theme") ? "dark-theme" : "light-theme"
    document.cookie = `theme = ${theme}`
}

function open_navbar() {
    let is_open = document.querySelector('.navbar').classList.toggle('open') ? "open" : ""
    document.cookie = `navbar_is_open = ${is_open}`
}

function delete_post(post_id) {
    let ans = confirm('Удалить этот пост?');
    if (ans) {
        let req = new XMLHttpRequest();
        req.open("GET", `delete/${post_id}`, false);
        req.send(null)
        location.reload()
    }
}
