function hide_element_by_id(id){
    document.getElementById(id).style.display = 'none';
}

function change_element_display_prop(id, prop=''){
    document.getElementById(id).style.display = prop;
}

function check_submit_form(id) {

    if (document.getElementById(id).style.display != 'hidden')
    {
        return true
    }

}

function show_register_form() {
    document.getElementsByClassName('footer-heading-two')[0].style.top = '510vh';
    document.getElementsByClassName('footer-heading-two')[0].style.position = 'absolute';

    hide_element_by_id('loginFormDiv');
    change_element_display_prop('registerFormDiv')
}

function show_login_form() {
    document.getElementsByClassName('footer-heading-two')[0].style.top = '495vh';
    document.getElementsByClassName('footer-heading-two')[0].style.position = 'absolute';

    hide_element_by_id('registerFormDiv');
    change_element_display_prop('loginFormDiv')
}
show_register_form();

