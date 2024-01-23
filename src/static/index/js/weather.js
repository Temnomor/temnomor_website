function get_weather()
{
    var URL = atob('aHR0cHM6Ly9hcGkub3BlbndlYXRoZXJtYXAub3JnL2RhdGEvMi41L3dlYXRoZXI/bGF0PTU3LjE1MjImbG9uPTY1LjUyNzImdW5pdHM9bWV0cmljJmxhbmc9cnUmYXBwaWQ9MDQ4ZWQwNTVkZWI0NGRkNjViNjZhN2QxMmUzMzc5Yzk=')

    $.ajax(URL,
    {
        success: function(response)
        {
          var current_temperature = Math.round(response?.main?.temp);
          var current_description = response?.weather[0]?.description

          if (typeof(current_temperature) == 'number' && typeof(current_description) == 'string')
          {
            $('#weather_text')?.html(`Погода: ${current_temperature}°C, ${current_description}`);
          }
        }
    })
}


get_weather();
setInterval(get_weather, 60000);