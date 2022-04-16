let textarea;

function add(open_tag= "", close_tag="") {
    let ss = textarea.selectionStart
    let se = textarea.selectionEnd
    textarea.value = textarea.value.slice(0, ss)
        + open_tag
        + textarea.value.slice(ss, se)
        + close_tag
        + textarea.value.slice(se)
    textarea.focus()
    textarea.selectionStart = ss + open_tag.length
    textarea.selectionEnd = textarea.selectionStart + (se - ss)
}
onload = () => {
     textarea = document.querySelector("textarea");
}