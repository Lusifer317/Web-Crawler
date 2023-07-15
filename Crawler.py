import requests
from bs4 import BeautifulSoup
import tkinter as tk


def crawl_website():
    # Retrieve the URL entered by the user
    url = entry.get()

    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the web page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data from the web page
        titles = [title.text for title in soup.find_all('title')]
        urls = [link['href'] for link in soup.find_all('a', href=True)]

        # Clear the text widget
        text_widget.delete(1.0, tk.END)

        # Display the extracted data in the text widget
        for title in titles:
            text_widget.insert(tk.END, f'Title: {title}\n')

        for url in urls:
            text_widget.insert(tk.END, f'URL: {url}\n')


# Create a Tkinter window
window = tk.Tk()
window.title('Web Crawler')

# Create a label and an entry widget for entering the URL
label = tk.Label(window, text='Enter URL:')
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the web crawling process
button = tk.Button(window, text='Crawl', command=crawl_website)
button.pack()

# Create a text widget to display the extracted data
text_widget = tk.Text(window, height=10, width=50)
text_widget.pack()

# Start the Tkinter event loop
window.mainloop()