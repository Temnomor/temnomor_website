const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");

const wrapper2 = document.querySelector(".wrapper2"),
selectBtn2 = wrapper2.querySelector(".select-btn"),
searchInp2 = wrapper2.querySelector("input"),
options2 = wrapper2.querySelector(".options");

const wrapper3 = document.querySelector(".wrapper3"),
selectBtn3 = wrapper3.querySelector(".select-btn"),
searchInp3 = wrapper3.querySelector("input"),
options3 = wrapper3.querySelector(".options");

const wrapper4 = document.querySelector(".wrapper4"),
selectBtn4 = wrapper4.querySelector(".select-btn"),
searchInp4 = wrapper4.querySelector("input"),
options4 = wrapper4.querySelector(".options");

function NoWhitespace(event)
{
  if (event.which == 32)
    {
      event.preventDefault();
      return false;
    }
}

function updateName(group_tag)
{
    hide_all_links(wrapper);
    wrapper.classList.remove("active");
}


function updateName2(teacher_tag)
{
    hide_all_links(wrapper2);
    wrapper2.classList.remove("active");
}

function updateName3(cabinet_tag)
{
    hide_all_links(wrapper3);
    wrapper3.classList.remove("active");
}

function updateName4()
{
    hide_all_links(wrapper4);
    wrapper4.classList.remove('active');
}

function hide_all_links(wrapper_elem)
{
    let elem = document.getElementsByClassName('allLinks')[0];

    if (!wrapper_elem.classList.contains('active'))
        elem.style.display = 'none';
    else
        elem.style.display = '';
}

selectBtn.addEventListener("click", () => {
    hide_all_links(wrapper);
    document.getElementById('lecturers_list').scrollTop = 0;
    document.getElementById('cabinets_list').scrollTop = 0;
    document.getElementById('lecturers_fullname_list').scrollTop = 0;

    wrapper.classList.toggle("active");

    wrapper2.classList.remove('active');
    wrapper3.classList.remove('active');
    wrapper4.classList.remove('active');
});

selectBtn2.addEventListener("click", () => {
    hide_all_links(wrapper2);
    document.getElementById('groups_list').scrollTop = 0;
    document.getElementById('cabinets_list').scrollTop = 0;
    document.getElementById('lecturers_fullname_list').scrollTop = 0;

    wrapper2.classList.toggle("active");

    wrapper.classList.remove('active');
    wrapper3.classList.remove('active');
    wrapper4.classList.remove('active');
});

selectBtn3.addEventListener("click", () => {
    hide_all_links(wrapper3);
    document.getElementById('groups_list').scrollTop = 0;
    document.getElementById('lecturers_list').scrollTop = 0;
    document.getElementById('lecturers_fullname_list').scrollTop = 0;

    wrapper3.classList.toggle("active");

    wrapper.classList.remove('active');
    wrapper2.classList.remove('active');
    wrapper4.classList.remove('active');
});

selectBtn4.addEventListener("click", () => {
    hide_all_links(wrapper4);
    document.getElementById('groups_list').scrollTop = 0;
    document.getElementById('cabinets_list').scrollTop = 0;
    document.getElementById('lecturers_list').scrollTop = 0;

    wrapper4.classList.toggle("active");

    wrapper.classList.remove('active');
    wrapper2.classList.remove('active');
    wrapper3.classList.remove('active');
});

function filterFunction()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("groups_list");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}

function filterFunction2()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput2");
  filter = input.value.toUpperCase();
  div = document.getElementById("lecturers_list");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}

function filterFunction3()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput3");
  filter = input.value.toUpperCase();
  div = document.getElementById("cabinets_list");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}

function filterFunction4()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput4");
  filter = input.value.toUpperCase();
  div = document.getElementById("lecturers_fullname_list");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}

async function insertScheduleURLs(json_obj, url)
{
    for (key in json_obj)
    {
        switch (url)
        {
            case '/api/getGroupsData':
                let groups_list = document.querySelector('#groups_list');
                let group_href = `/api/groups?group=${key}`;
                groups_list.innerHTML += `<a id="${key}" href="${group_href}" target="_blank" onclick="updateName()">${key}</a>`;

                document.querySelector('.wrapper').style.display = '';
                break;
            case '/api/getLecturersData':
                let lecturers_list = document.querySelector('#lecturers_list');
                let lecturers_href = `/api/lecturers?lecturer=${key}`;
                lecturers_list.innerHTML += `<a href="${lecturers_href}" target="_blank" onclick="updateName2()">${key}</a>`;

                document.querySelector('.wrapper2').style.display = '';
                break;
            case '/api/getCabinetsData':
                let cabinets_list = document.querySelector('#cabinets_list');
                let cabinets_href = `/api/cabinets?cabinet=${key}`;
                cabinets_list.innerHTML += `<a href="${cabinets_href}" target="_blank" onclick="updateName3()">${key}</a>`;
                document.querySelector('.wrapper3').style.display = '';
                break;
        }
    }
}

function isObjEmpty(obj)
{
    for (const prop in obj)
    {
        if (Object.hasOwn(obj, prop))
        {
            return false;
        }
    }
    return true;
}

async function loadSchedule()
{
    let URLs = [
        '/api/getGroupsData',
        '/api/getLecturersData',
        '/api/getCabinetsData'
    ];

    document.querySelector('#groups_list').innerHTML = '';
    document.querySelector('#lecturers_list').innerHTML = '';
    document.querySelector('#cabinets_list').innerHTML = '';

    for (let url of URLs)
    {
        let response = await fetch(url, {method: 'POST'});
        let response_json = await response.json();

        if (!isObjEmpty(response_json))
        {
            await insertScheduleURLs(response_json, url);
        }
    }
}

function place_top_groups_on_top() // ;)))))
{
    let groups_list = document.querySelector('#groups_list');
    let pkst_20_9_2 = document.getElementById('ПКСт-20-(9)-2');
    let ispt_21_9_1 = document.getElementById('ИСПт-21-(9)-1');
    
    groups_list.insertAdjacentElement('afterbegin', ispt_21_9_1);
    groups_list.insertAdjacentElement('afterbegin', pkst_20_9_2);
}

function copyToClipboard(elem)
{
  let lecturer = elem.srcElement.innerText;
  searchInp4.value = lecturer;
  searchInp4.select();
  searchInp4.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(lecturer);
  searchInp4.value = '';
  alert(`ФИО преподавателя (${lecturer}) скопировано в буфер обмена`);
}

async function loadLecturersFullName()
{
    let lecturers_fullname_list = document.querySelector('#lecturers_fullname_list');
    lecturers_fullname_list.innerHTML = '';

    let response = await fetch('/api/getLecturersFullNameData', {method: 'POST'});
    let response_json = await response.json();

    for (let lecturer of response_json)
    {
        let elem = document.createElement('a');
        elem.onclick = copyToClipboard;
        elem.innerHTML = lecturer;
        lecturers_fullname_list.appendChild(elem);
    }
}

function replaceLatinToCyrillic(event)
{
  let replace_dict = {
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    '[': 'х',
    ']': 'ъ',
    'a': 'ф',
    's': 'ы',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    ';': 'ж',
    '\'': 'э',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    ',': 'б',
    '.': 'ю',
    '`': 'ё'
  };

  if (replace_dict.hasOwnProperty(String(event.key).toLowerCase()) &&! event.ctrlKey)
  {
    event.target.value += replace_dict[event.key];
    event.preventDefault();
  }
}

async function main()
{
    await loadSchedule();
    await loadLecturersFullName();
    Array.from(document.querySelectorAll('.search')).forEach((item) => item.onkeypress = "NoWhiteSpace(event)");
    Array.from(document.querySelectorAll('.search')).forEach((item) => addEventListener('keydown', replaceLatinToCyrillic));
    place_top_groups_on_top();
}

main();
