from bs4 import BeautifulSoup

def oulunlippo_194(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    upcoming_events = soup.find('div', class_='upcoming-events')
    events = upcoming_events.find('div', class_='events')
    
    data = {}
    data['upcoming_events'] = []
    
    for event in events.find_all('div', class_='event'):
        event_data = {}
        event_data['date'] = event.find('div', class_='date').text.strip()
        event_data['time'] = event.find('div', class_='time').text.strip()
        event_data['location'] = event.find('div', class_='location').text.strip()
        data['upcoming_events'].append(event_data)
    
    return data

