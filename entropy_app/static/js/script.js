var menublock = document.getElementById('menu-block')
var sidemenu = document.getElementById('desktop-mode')

var flag = 0

function openmenu(){
    if (flag==0){
        menublock.style = 'display:none;'
        sidemenu.style = 'display:block;'
        flag = 1
        console.log('yes')
    }
    else{
        menublock.style = 'display:block;'
        sidemenu.style = 'display:none;'
        flag = 0
    }
}