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


//function _0x1dfa(){const _0x579775=['352611ThxITn','5MsnNxO','innerText','140bhIxhg','getElementById','127784XkdsaQ','Сохраненная\x20закладка\x20актуальна\x20до\x20окончания\x20семестра.','12173650OHEaDl','14dsefbn','notifier','708228fFbabM','replace','7636908OfjGEY','4747836hprzMi','7945515CLPlDm'];_0x1dfa=function(){return _0x579775;};return _0x1dfa();}const _0x307bd3=_0x2ee5;(function(_0x204cfa,_0x1087f5){const _0x4ae95e=_0x2ee5,_0x48ec6c=_0x204cfa();while(!![]){try{const _0x24d43b=-parseInt(_0x4ae95e(0xa0))/0x1+-parseInt(_0x4ae95e(0x9e))/0x2*(parseInt(_0x4ae95e(0xa5))/0x3)+-parseInt(_0x4ae95e(0xa3))/0x4*(-parseInt(_0x4ae95e(0xa6))/0x5)+parseInt(_0x4ae95e(0xa2))/0x6+parseInt(_0x4ae95e(0x99))/0x7*(parseInt(_0x4ae95e(0x9b))/0x8)+parseInt(_0x4ae95e(0xa4))/0x9+-parseInt(_0x4ae95e(0x9d))/0xa;if(_0x24d43b===_0x1087f5)break;else _0x48ec6c['push'](_0x48ec6c['shift']());}catch(_0x47c58f){_0x48ec6c['push'](_0x48ec6c['shift']());}}}(_0x1dfa,0xdf138));function _0x2ee5(_0x45166a,_0x545435){const _0x1dfad0=_0x1dfa();return _0x2ee5=function(_0x2ee545,_0x457282){_0x2ee545=_0x2ee545-0x98;let _0x2d01ae=_0x1dfad0[_0x2ee545];return _0x2d01ae;},_0x2ee5(_0x45166a,_0x545435);}let notifier=document[_0x307bd3(0x9a)](_0x307bd3(0x9f));notifier['innerText']=notifier[_0x307bd3(0x98)][_0x307bd3(0xa1)](_0x307bd3(0x9c),'');


function remove_trash()
{
  function _0x3f57(){const _0x469a74=['2471913mZdDAA','1396955aMQpwc','2230010LDaJur','2164lGlqxw','querySelector','toLowerCase','967208yiOFMq','3IdtOna','10HUXyEr','300716XQLNlw','508538lhVdaf','6UYFfIp','children','remove','includes'];_0x3f57=function(){return _0x469a74;};return _0x3f57();}const _0x5222f3=_0x17fe;(function(_0x5939a7,_0x52370b){const _0x37fc3a=_0x17fe,_0x3f7977=_0x5939a7();while(!![]){try{const _0x12fb28=-parseInt(_0x37fc3a(0xf8))/0x1+-parseInt(_0x37fc3a(0xf9))/0x2*(parseInt(_0x37fc3a(0xf6))/0x3)+-parseInt(_0x37fc3a(0x101))/0x4+parseInt(_0x37fc3a(0x100))/0x5*(parseInt(_0x37fc3a(0xfa))/0x6)+parseInt(_0x37fc3a(0xff))/0x7+-parseInt(_0x37fc3a(0xf5))/0x8+parseInt(_0x37fc3a(0xfe))/0x9*(parseInt(_0x37fc3a(0xf7))/0xa);if(_0x12fb28===_0x52370b)break;else _0x3f7977['push'](_0x3f7977['shift']());}catch(_0x2f36f8){_0x3f7977['push'](_0x3f7977['shift']());}}}(_0x3f57,0x3b855));function _0x17fe(_0x490fa5,_0x564ef4){const _0x3f5742=_0x3f57();return _0x17fe=function(_0x17fe3e,_0x1ea59d){_0x17fe3e=_0x17fe3e-0xf4;let _0x5b8fef=_0x3f5742[_0x17fe3e];return _0x5b8fef;},_0x17fe(_0x490fa5,_0x564ef4);}let body_elements=document[_0x5222f3(0x102)]('body')[_0x5222f3(0xfb)];for(elem of body_elements){['br','hr'][_0x5222f3(0xfd)](elem['tagName'][_0x5222f3(0xf4)]())&&elem[_0x5222f3(0xfc)]();}
}


//Array.from(document.getElementsByClassName('comm3 zamena')).forEach(function (item) {item.addEventListener('click', function () {alert(item.title)})});


function _0x398d(_0x139fad,_0x526fe5){var _0x100651=_0x1006();return _0x398d=function(_0x398d9c,_0x3628cb){_0x398d9c=_0x398d9c-0x179;var _0x9107de=_0x100651[_0x398d9c];return _0x9107de;},_0x398d(_0x139fad,_0x526fe5);}function _0x1006(){var _0x103783=['1941207uhCllj','3845542QULSTt','1668RIMVWH','getElementsByTagName','29973050HBNqFS','12782601FOqYbK','title','remove','3998981pDCELI','8QpzQaB','from','div','2489700liZukV','21210zxaIvt','includes','1GbSbaR'];_0x1006=function(){return _0x103783;};return _0x1006();}var _0x4dd339=_0x398d;(function(_0x142292,_0x359d89){var _0x2849f9=_0x398d,_0x104a61=_0x142292();while(!![]){try{var _0x44fc16=parseInt(_0x2849f9(0x180))/0x1*(parseInt(_0x2849f9(0x182))/0x2)+parseInt(_0x2849f9(0x181))/0x3+-parseInt(_0x2849f9(0x17d))/0x4+parseInt(_0x2849f9(0x17e))/0x5*(parseInt(_0x2849f9(0x183))/0x6)+parseInt(_0x2849f9(0x179))/0x7*(-parseInt(_0x2849f9(0x17a))/0x8)+parseInt(_0x2849f9(0x186))/0x9+-parseInt(_0x2849f9(0x185))/0xa;if(_0x44fc16===_0x359d89)break;else _0x104a61['push'](_0x104a61['shift']());}catch(_0xcaf27c){_0x104a61['push'](_0x104a61['shift']());}}}(_0x1006,0xeedd8),Array[_0x4dd339(0x17b)](document['getElementsByTagName']('hr'))['forEach'](function(_0x57a2f3){var _0x501cb0=_0x4dd339;_0x57a2f3[_0x501cb0(0x188)]();}));if(document[_0x4dd339(0x187)][_0x4dd339(0x17f)]('-'))document[_0x4dd339(0x184)](_0x4dd339(0x17c))[0x1][_0x4dd339(0x188)]();else document[_0x4dd339(0x184)](_0x4dd339(0x17c))[0x2][_0x4dd339(0x188)]();


Array.from(document.getElementsByTagName('a')).forEach(function(item){item.removeAttribute("href")});
document.getElementById('notifier').remove();

[1, 2, 3, 4, 5, 6].forEach(clean_cabs);


function reload_window()
{
    window.location.reload();
}

remove_trash();
remove_trash();
setInterval(reload_window, 300000);