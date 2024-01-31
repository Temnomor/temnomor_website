let tgScript = document.createElement('script');
tgScript.src = 'https://telegram.org/js/telegram-web-app.js';
document.getElementsByTagName('body')[0].appendChild(tgScript);


cab = document.getElementsByClassName('cab');


const urlParams = new URLSearchParams(window.location.search);
const groupName = urlParams.get('group') || urlParams.get('lecturer') || urlParams.get('cabinet') || 'Календарный учебный график';
let title = document.createElement('title');
title.innerHTML = groupName;
document.getElementsByTagName('body')[0].insertAdjacentElement('beforeend', title);

function clean_cabs()
{
    for (i = 0; i < cab.length; i++)
    {
        if (cab[i].innerText == '' || cab[i].innerText == String.fromCharCode(160))
        {
            cab[i].parentElement.remove()
        }
    }
}


Array.from(document.getElementsByClassName('comm3 zamena')).forEach(function (item) {item.addEventListener('click', function () {alert(item.title)})});


//var _0x32541d=_0x1b57;function _0x1b57(_0x3f3e0e,_0x4fd88c){var _0x2a850f=_0x2a85();return _0x1b57=function(_0x1b5746,_0x54d9da){_0x1b5746=_0x1b5746-0x97;var _0x73c853=_0x2a850f[_0x1b5746];return _0x73c853;},_0x1b57(_0x3f3e0e,_0x4fd88c);}function _0x2a85(){var _0x3b8082=['5547066XpcWHG','body','458028OsCmKZ','prepend','forEach','getElementsByClassName','5970520VahiEz','87892cwhAuj','ОКЕЙ\x20ЧЕЛ,\x20БУДЕМ\x20ЖДАТЬ\x20ТВОЮ\x20ПОДАЧУ))\x20┌П┐(ಠ_ಠ)\x20\x09(*・‿・)ノ⌒*:･ﾟ✧','getElementsByTagName','1938725ZDHLrW','998108UqehHM','from','append','11328276SZyEng','27tScANX','createComment'];_0x2a85=function(){return _0x3b8082;};return _0x2a85();}(function(_0x1a525a,_0x2aa59b){var _0x4828eb=_0x1b57,_0x2b7c2c=_0x1a525a();while(!![]){try{var _0xe0c830=-parseInt(_0x4828eb(0xa6))/0x1+-parseInt(_0x4828eb(0xa2))/0x2+parseInt(_0x4828eb(0x99))/0x3*(-parseInt(_0x4828eb(0x9d))/0x4)+-parseInt(_0x4828eb(0xa5))/0x5+parseInt(_0x4828eb(0x98))/0x6+parseInt(_0x4828eb(0x9b))/0x7+parseInt(_0x4828eb(0xa1))/0x8;if(_0xe0c830===_0x2aa59b)break;else _0x2b7c2c['push'](_0x2b7c2c['shift']());}catch(_0x5a3053){_0x2b7c2c['push'](_0x2b7c2c['shift']());}}}(_0x2a85,0xebf25),document[_0x32541d(0xa4)](_0x32541d(0x9c))[0x0][_0x32541d(0x97)](document[_0x32541d(0x9a)](_0x32541d(0xa3))),document[_0x32541d(0xa4)](_0x32541d(0x9c))[0x0][_0x32541d(0x97)](document['createComment'](_0x32541d(0xa3))),document[_0x32541d(0xa4)]('body')[0x0][_0x32541d(0x97)](document['createComment'](_0x32541d(0xa3))),document[_0x32541d(0xa4)](_0x32541d(0x9c))[0x0]['prepend'](document[_0x32541d(0x9a)]('ОКЕЙ\x20ЧЕЛ,\x20БУДЕМ\x20ЖДАТЬ\x20ТВОЮ\x20ПОДАЧУ))\x20┌П┐(ಠ_ಠ)\x20\x09(*・‿・)ノ⌒*:･ﾟ✧')),document['getElementsByTagName'](_0x32541d(0x9c))[0x0][_0x32541d(0x9e)](document[_0x32541d(0x9a)](_0x32541d(0xa3))),document[_0x32541d(0xa4)](_0x32541d(0x9c))[0x0][_0x32541d(0x9e)](document[_0x32541d(0x9a)](_0x32541d(0xa3))),Array['from'](document[_0x32541d(0xa0)]('urok'))[_0x32541d(0x9f)](function(_0x4e99f3){var _0x2ac439=_0x32541d;_0x4e99f3['prepend'](document[_0x2ac439(0x9a)](_0x2ac439(0xa3)));}),Array[_0x32541d(0xa7)](document['getElementsByClassName']('para_num'))[_0x32541d(0x9f)](function(_0x527406){var _0x12f652=_0x32541d;_0x527406[_0x12f652(0x9e)](document[_0x12f652(0x9a)]('ОКЕЙ\x20ЧЕЛ,\x20БУДЕМ\x20ЖДАТЬ\x20ТВОЮ\x20ПОДАЧУ))\x20┌П┐(ಠ_ಠ)\x20\x09(*・‿・)ノ⌒*:･ﾟ✧'));}));


let newText = '- замены. Для того чтобы увидеть изменение, наведите курсор на замену или коснитесь экрана (на мобильном устройстве). Диспетчер расписания:';
/*for (const a of document.querySelectorAll("div")) {
    if (a.textContent.includes("Наведите курсор") && !a.textContent.includes('Расписание')) {
      a.textContent = newText;
    }
  }*/
[1, 2, 3, 4, 5, 6].forEach(clean_cabs);
try{document.querySelector("body > div.shedule_tek > div:nth-child(5)").style = 'display: none;';}catch{}
try{document.getElementsByClassName('counter')[0].remove();}catch{}

function reload_window()
{
  window.location.reload();
}

setInterval(reload_window, 300000);
