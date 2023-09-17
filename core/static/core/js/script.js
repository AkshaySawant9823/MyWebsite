// --------------------------------------------------------------

var tablinks = document.getElementsByClassName('tab-links');
var tabcontents = document.getElementsByClassName('tab-contents');

function opentab(tabname) {
    for (tablink of tablinks) {
        tablink.classList.remove('active-link')
    }
    for (tabcontent of tabcontents) {
        tabcontent.classList.remove('active-tab')
    }
    event.currentTarget.classList.add("active-link")
    document.getElementById(tabname).classList.add("active-tab")
    if (['experience', 'education'].includes(tabname)){
        document.querySelector('#skills .left').hidden = true
        document.querySelector('#skills .right').hidden = true
    }
    else{
        document.querySelector('#skills .left').hidden = false
        document.querySelector('#skills .right').hidden = false
    }
}

// --------------------------------------------------------------

var sidemenu = document.getElementById('sidemenu');

function openmenu() {
    sidemenu.style.right = "0";
}

function closemenu() {
    sidemenu.style.right = "-200px";
}
