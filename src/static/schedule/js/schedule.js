let tgScript = document.createElement('script');
tgScript.src = 'https://telegram.org/js/telegram-web-app.js';
document.getElementsByTagName('body')[0].appendChild(tgScript);


const urlParams = new URLSearchParams(window.location.search);
const groupName = urlParams.get('group') || urlParams.get('lecturer') || urlParams.get('cabinet') || 'Календарный учебный график';
let title = document.createElement('title');
title.innerHTML = groupName;
document.getElementsByTagName('body')[0].insertAdjacentElement('beforeend', title);


function clean_cabs()
{
    cab = document.getElementsByClassName('cab');

    for (i = 0; i < cab.length; i++)
    {
        if (cab[i].innerText == '' || cab[i].innerText == String.fromCharCode(160))
        {
            cab[i].parentElement.remove();
        }
    }
}


document.querySelector('html').style.overflowX = 'auto';


function remove_trash()
{
  function _0x3f57(){const _0x469a74=['2471913mZdDAA','1396955aMQpwc','2230010LDaJur','2164lGlqxw','querySelector','toLowerCase','967208yiOFMq','3IdtOna','10HUXyEr','300716XQLNlw','508538lhVdaf','6UYFfIp','children','remove','includes'];_0x3f57=function(){return _0x469a74;};return _0x3f57();}const _0x5222f3=_0x17fe;(function(_0x5939a7,_0x52370b){const _0x37fc3a=_0x17fe,_0x3f7977=_0x5939a7();while(!![]){try{const _0x12fb28=-parseInt(_0x37fc3a(0xf8))/0x1+-parseInt(_0x37fc3a(0xf9))/0x2*(parseInt(_0x37fc3a(0xf6))/0x3)+-parseInt(_0x37fc3a(0x101))/0x4+parseInt(_0x37fc3a(0x100))/0x5*(parseInt(_0x37fc3a(0xfa))/0x6)+parseInt(_0x37fc3a(0xff))/0x7+-parseInt(_0x37fc3a(0xf5))/0x8+parseInt(_0x37fc3a(0xfe))/0x9*(parseInt(_0x37fc3a(0xf7))/0xa);if(_0x12fb28===_0x52370b)break;else _0x3f7977['push'](_0x3f7977['shift']());}catch(_0x2f36f8){_0x3f7977['push'](_0x3f7977['shift']());}}}(_0x3f57,0x3b855));function _0x17fe(_0x490fa5,_0x564ef4){const _0x3f5742=_0x3f57();return _0x17fe=function(_0x17fe3e,_0x1ea59d){_0x17fe3e=_0x17fe3e-0xf4;let _0x5b8fef=_0x3f5742[_0x17fe3e];return _0x5b8fef;},_0x17fe(_0x490fa5,_0x564ef4);}let body_elements=document[_0x5222f3(0x102)]('body')[_0x5222f3(0xfb)];for(elem of body_elements){['br','hr'][_0x5222f3(0xfd)](elem['tagName'][_0x5222f3(0xf4)]())&&elem[_0x5222f3(0xfc)]();}
}


//Array.from(document.getElementsByClassName('comm3 zamena')).forEach(function (item) {item.addEventListener('click', function () {alert(item.title)})});


[1, 2, 3, 4, 5, 6].forEach(clean_cabs);


function reload_window()
{
    window.location.reload();
}

remove_trash();
remove_trash();
setInterval(reload_window, 300000);