# hellometer

## Instructions to run the program
pip install -r requirements.txt
Run run.py file

## About the plots
The plots were made using chartjs.


### Orders per day-part
This plot, plots the TTS for every day-part.
This plot is interactive (you can zoom & pan). You can choose to look into only a day-part at a time. Or even multiple ones. 

### Customer per hour starting Aug 3rd
This plot, plots the number of customer per hour starting Aug 3rd

There was a problem with sending the datetime to the javascript file & I could only display the hour & not the full
datetime. Everytime there's a 0 on the x-axis it's progressing to the next day.

### Mean TTS per hour starting Aug 3rd
This plot, plots the mean of TTS per hour starting Aug 3rd


### Distribution of TTS
This plot, plots the distribution of TTS across the readings
There were ~3000 readings in total


## Insights
I sorted the input according to the epoch time, & I noticed a couple of glitches, since a customer with a timestamp of 
much later on in the day was marked for day_part 1

Example can be seen here:

| customer_number | day_part | first_seen_datetime_local | first_seen_datetime_utc | first_seen_local |	first_seen_utc | id | location | model_id | tts |

| 1	| 1 | 1596465075 | 1596490275 | 289 | 1 | 83 | 309 |

| 2 | 1 | 1596465212 | 1596490412 | 290 | 1 | 97 | 257 |



#### What I could have done, if I had more time?
I would've worked on the front end as well. Making sure the plots are arranged into a flexible gird format.
The interactive plot zoom & pan are completely unlocked. Which means that you can scroll infinitely. I could limit the 
scrolling to the extremities of the data inside the plot.

I could also have dived deeper into the analytics part of the assignment other than the insights mentioned above.
