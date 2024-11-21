# Setting Up Alerts in Grafana for Calculator Errors

## 1. Create an Alert in the "Calculator Errors" Panel

1. In Grafana, navigate to the **Calculator Errors** panel on the **API Dashboard**.
2. Click on the **Alert** tab at the top of the panel.
3. Click **Create Alert** and set the condition to trigger when the error rate is greater than `5` for the `/calculator` route.
   - **Condition**: `avg() of query (A, 5m, now) is above 5`.

## 2. Set Up a Telegram Contact Point

1. Navigate to **Alerting** > **Contact points** in Grafana.
2. Click **Add contact point** and select **Telegram**.
3. Set up a Telegram bot:
   - Use [BotFather](https://core.telegram.org/bots#botfather) to create a bot and obtain your **Bot Token**.
   - Obtain your **Chat ID** using the [Telegram Bot API](https://api.telegram.org/bot<YourBotToken>/getUpdates).
4. Enter the **Bot Token** and **Chat ID** in the Grafana notification settings.

## 3. Configure the Alert Message

1. In the **Alert** tab of the "Calculator Errors" panel, go to **Notifications** and select the **Telegram** notification channel.
2. Set the message content to the following:
   ```text
   Alert: Calculator Errors increased on route /calculator.
   Error Rate: {{ $value }} requests per second.
