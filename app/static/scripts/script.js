function click_hello() {
    const hello = document.querySelector(".hello");
    hello.classList.add("click_hello");
    setTimeout(
        function () {
            hello.classList.remove("click_hello");
        }, 800
    )
}
function click_h1() {
    const h1 = document.querySelector("h1")
    h1.classList.add("click_h1")
    setTimeout(
        function () {
            h1.classList.remove("click_h1")
        }, 400
    )
}