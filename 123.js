function checkForm(el) {
    let name = el.name.value
    let pass = el.pass.value
    let repass = el.repass.value
    let state = el.state.value
    var fail = ""

    if(name == "" || pass == "" || repass == "" || state == "")
        fail = "Поле не должно быть пустым";
    else if(name.length <= 3 || name.length >= 20)
        fail = "Введите корректное имя";
    else if(pass != repass)
        fail = "Введеные пароли не совпадают";
    else if('@' in pass || ' ' in pass)
        fail = "Для пароля запрещено использование следующих символов: @, #, $, %, &, (, ),";


    if(fail != "") {
        document.getElementById('error').innerHTML = fail;

        return false;
    } else {
        alert("sdaiojsaoiddad");

        return true;
    }
}
