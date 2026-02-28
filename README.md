
# Job Alert Automation System

Automatically scans job portals for new listings and sends real-time notifications based on your preferences.

---

## Features
- Real-time monitoring of job portals.
- Customizable filters for location, role, and keywords.
- Notifications via email, Slack, or messaging apps.
- Handles multiple portals simultaneously.

---

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** Requests, BeautifulSoup / Selenium, smtplib, schedule
- **Other Tools:** Cron (for scheduling), GitHub Actions (optional for cloud automation)

---

## Installation
```bash
# Clone the repository
git clone https://github.com/reddemanilkumarreddy/job-alert-automation.git
cd job-alert-automation

# Install dependencies
pip install -r requirements.txt

# Run the script
python job_alert.py
````

---

## Usage

1. Update `config.json` with your preferred job keywords and notification settings.
2. Run the script.
3. Receive alerts automatically whenever a matching job is posted.

---

## Demo

Include a screenshot or GIF of the notifications in action to showcase functionality.

---

## Future Enhancements

* Add more portals and API integrations.
* Dashboard to visualize job stats.
* Mobile push notifications for instant updates.

---

## License

MIT License 

