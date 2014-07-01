#Command To Run Script in Cron

Ensure path is correct and file has sufficient permissions (755)

The first two numbers are minutes and hours, then we get into days of week etc.

This example runs every minute. Note that &ast; and */1 are equivalent.

We would ideally want this to repeat at the same pace as the drop data age limit

		*/1 * * * * /home/ubuntu/Documents/djDuino/take_reading.py
