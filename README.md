# zappy

### Zappy integrates with a Slack bot and listens on specific messages. For simplicity, we the tool will listen on all messages containing the word “go”. places a messages on a bot containing the message “go”, the tool fetches twitter feeds from the specific account and saves in a mongo collection. the view that fetches tweets from mongoDB and shows in a table.

# Diagram below visualizes the process.

![Image description](zappy.png)

# how to run in development mode:
 ```
 bash start.sh Your_SLACK_BOT_TOKEN
 ```

# How to run using docker 
## To run the full system just use docker-compose:

``` 
docker-compose up 
```

### check the tweets at 
``` http://IP:4200/```
