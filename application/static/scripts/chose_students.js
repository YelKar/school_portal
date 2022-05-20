/**
 * Script for checkboxes in details
 */

const details_all = document.querySelectorAll(" details") //

function all_checked(list) {
    for (let el of list) {
        if (el.id != "check" && !el.checked) return false
    }
    return true
}

for (let det of details_all) {
    let summary_input = det.querySelector("summary input");
    summary_input.addEventListener("change", (e) => {
        for (let input of det.querySelectorAll("input")) {
            input.checked = det.querySelector("summary input").checked;
        }
    })

    det.addEventListener("click", (e) => {
        setTimeout(() => {
            if (e.target != summary_input
                && all_checked(det.querySelectorAll("input")) != summary_input.checked) {
                summary_input.checked = all_checked(det.querySelectorAll("input"));
            }
        }, 10)
    })
}

function submit(action_type) {
    let form = document.querySelector("form");
    let type_input = document.getElementById("action_type");
    console.log(type_input);
    type_input.value = action_type;
    form.submit();
}
