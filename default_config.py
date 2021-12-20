SETTINGS = {
        'url_homepage': 'https://archlinux.org/',
        'url_archive': 'https://archlinux.org/news/',
        'headers': {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"
        },
        'source': 'homepage', # it can be either 'homepage' or 'archive'
        'parser': 'html.parser',
        'bottom_up': False,
}
