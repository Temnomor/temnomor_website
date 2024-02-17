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
  let body_elements = document.querySelector('body').children;
  for (elem of body_elements)
  {
    if (['br', 'hr'].includes(elem.tagName.toLowerCase()))
    {
      elem.remove();
    }
  }
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