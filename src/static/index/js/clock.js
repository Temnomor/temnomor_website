function clock()
{
    datetime_now = new Date();

    name_of_the_day = datetime_now.toLocaleString('ru-RU', {hour12: false, timeZone: 'Asia/Yekaterinburg', 'weekday': 'long'});

    time_tag = document.getElementById('time_now');

    datetime_formatted = datetime_now.toLocaleString('ru-RU', {hour12: false, timeZone: 'Asia/Yekaterinburg'});

    time_tag.innerHTML = `${name_of_the_day} ${datetime_formatted}`;
}


clock();
setInterval(clock, 1000);