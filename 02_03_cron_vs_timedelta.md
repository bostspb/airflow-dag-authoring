# Cron vs Timedelta

```
start_date = `2023-07-20 10:00`
 
# Cron: schedule_interval is stateless
schedule_interval = "@daily" 
- execution_date will be `2023-07-20 00:00`
- dagrun triggered at `2023-07-21 00:00`

# Timedelta: schedule_interval is stateful
schedule_interval = timedelta(days=1)
- execution_date will be `2023-07-20 10:00`
- dagrun triggered at `2023-07-21 10:00`

```
