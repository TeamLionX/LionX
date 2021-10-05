# corona virus stats for LionX
from covid import Covid

from . import covidindia, edit_delete, edit_or_reply, lionub

plugin_category = "extra"


@lionub.lion_cmd(
    pattern="covid(?:\s|$)([\s\S]*)",
    command=("covid", plugin_category),
    info={
        "header": "To get latest information about covid-19.",
        "description": "Get information about covid-19 data in the given country/state(only Indian States).",
        "usage": "{tr}covid <state_name/country_name>",
        "examples": ["{tr}covid andhra pradesh", "{tr}covid india", "{tr}covid world"],
    },
)
async def corona(event):
    "To get latest information about covid-19."
    input_str = event.pattern_match.group(1)
    country = (input_str).title() if input_str else "World"
    lionevent = await edit_or_reply(event, "`Collecting data...`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️ Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔 Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️ Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕 Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊 Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉 Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺 New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟 New Deaths : <code>{country_data['new_deaths']}</code>"
        await lionevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️ Confirmed   : <code>{data['new_positive']}</code>\
                \n😔 Active           : <code>{data['new_active']}</code>\
                \n⚰️ Deaths         : <code>{data['new_death']}</code>\
                \n😊 Recovered   : <code>{data['new_cured']}</code>\
                \n🥺 New Cases   : <code>{cat1}</code>\
                \n😟 New Deaths : <code>{cat2}</code>\
                \n😃 New cured  : <code>{cat3}</code> </b>"
            await lionevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                lionevent,
                "`Corona Virus Info of {} is not avaiable or unable to fetch`".format(
                    country
                ),
                5,
            )
