import datetime
import os
import webbrowser

def create_paypal_receipt_html(name, email, amount, recipient, date=None, transaction_type="Payment", currency="EUR", lang="pt"):
    if not date:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate transaction ID
    transaction_id = f"PAY-{datetime.datetime.now().strftime('%Y%m%d')}-{os.urandom(4).hex().upper()}"
    
    # Currency symbols and formatting
    currency_data = {
        "EUR": {"symbol": "€", "name": "EUR", "format": "{symbol}{amount} {name}"},
        "USD": {"symbol": "$", "name": "USD", "format": "{symbol}{amount} {name}"},
        "GBP": {"symbol": "£", "name": "GBP", "format": "{symbol}{amount} {name}"},
        "BRL": {"symbol": "R$", "name": "BRL", "format": "{symbol}{amount} {name}"},
        "EGP": {"symbol": "ج.م", "name": "EGP", "format": "{amount} {symbol}"},
        # Add more as needed
    }
    curr = currency_data.get(currency, currency_data["EUR"])
    # Format amount for display
    def format_amount(amount):
        if lang == "ar-eg":
            # Arabic numerals and RTL
            return f"{amount:,.2f}".replace(",", "٬").replace(".", "٫")
        else:
            return f"{amount:,.2f}"
    amount_str = curr["format"].format(symbol=curr["symbol"], amount=format_amount(amount), name=curr["name"])
    
    # Language dictionary
    translations = {
        "pt": {
            "home": "Início",
            "send_request": "Enviar e solicitar",
            "wallet": "Carteira",
            "activity": "Atividade",
            "help": "Ajuda",
            "notifications": "Notificações",
            "settings": "Configurações",
            "logout": "TERMINAR SESSÃO",
            "sent_to": "Enviou {amount} para {recipient}",
            "subtext": "Informaremos {recipient} de que enviou dinheiro.",
            "feedback": "Feedback sobre esta transação",
            "send_more": "Enviar mais dinheiro",
            "summary": "Aceder ao Resumo",
            "footer_help": "Ajuda",
            "footer_contact": "Contacte-nos",
            "footer_security": "Segurança",
            "copyright": f"©1999-{datetime.datetime.now().year} PayPal. Todos os direitos reservados.",
            "privacy": "Privacidade",
            "cookies": "Cookies",
            "legal": "Legal",
            "complaints": "Reclamações",
            "fake1": "This is a simulated PayPal receipt for educational purposes only.",
            "fake2": "Not a real transaction. This is a demonstration only.",
            "fake3": "FAKE RECEIPT - FOR EDUCATIONAL PURPOSES ONLY"
        },
        "en": {
            "home": "Home",
            "send_request": "Send & Request",
            "wallet": "Wallet",
            "activity": "Activity",
            "help": "Help",
            "notifications": "Notifications",
            "settings": "Settings",
            "logout": "LOG OUT",
            "sent_to": "You sent {amount} to {recipient}",
            "subtext": "We'll let {recipient} know you sent money.",
            "feedback": "Feedback about this transaction",
            "send_more": "Send more money",
            "summary": "Go to Summary",
            "footer_help": "Help",
            "footer_contact": "Contact us",
            "footer_security": "Security",
            "copyright": f"©1999-{datetime.datetime.now().year} PayPal. All rights reserved.",
            "privacy": "Privacy",
            "cookies": "Cookies",
            "legal": "Legal",
            "complaints": "Complaints",
            "fake1": "This is a simulated PayPal receipt for educational purposes only.",
            "fake2": "Not a real transaction. This is a demonstration only.",
            "fake3": "FAKE RECEIPT - FOR EDUCATIONAL PURPOSES ONLY"
        },
        "ar-eg": {
            "home": "الرئيسية",
            "send_request": "إرسال وطلب",
            "wallet": "المحفظة",
            "activity": "النشاط",
            "help": "مساعدة",
            "notifications": "الإشعارات",
            "settings": "الإعدادات",
            "logout": "تسجيل الخروج",
            "sent_to": "لقد أرسلت {amount} إلى {recipient}",
            "subtext": "سنعلم {recipient} أنك أرسلت المال.",
            "feedback": "ملاحظات حول هذه المعاملة",
            "send_more": "إرسال المزيد من المال",
            "summary": "الانتقال إلى الملخص",
            "footer_help": "مساعدة",
            "footer_contact": "اتصل بنا",
            "footer_security": "الأمان",
            "copyright": f"©1999-{datetime.datetime.now().year} باي بال. جميع الحقوق محفوظة.",
            "privacy": "الخصوصية",
            "cookies": "الكوكيز",
            "legal": "قانوني",
            "complaints": "الشكاوى",
            "fake1": "هذه إيصال باي بال وهمي لأغراض تعليمية فقط.",
            "fake2": "هذه ليست معاملة حقيقية. هذا للعرض فقط.",
            "fake3": "إيصال وهمي - لأغراض تعليمية فقط"
        }
        # Add more languages as needed
    }
    t = translations.get(lang, translations["en"])
    rtl = ' dir="rtl"' if lang == "ar-eg" else ''
    
    # HTML template with white icons, multi-language, RTL for Arabic, and secret code for hiding fake alerts
    html_content = f"""
    <!DOCTYPE html>
    <html lang=\"{lang}\"{rtl}>
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>PayPal Receipt</title>
        <style>
            @font-face {{
                font-family: 'pp-sans-big-regular';
                src: url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Regular.eot');
                src: url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Regular.eot?#iefix') format('embedded-opentype'),
                     url('https://www.paypalobjects.com/paypal-ui/fonts/PayPalSansBig-Regular.woff2') format('woff2'),
                     url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Regular.svg') format('svg');
            }}
            @font-face {{
                font-family: 'pp-sans-big-bold';
                src: url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Bold.eot');
                src: url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Bold.eot?#iefix') format('embedded-opentype'),
                     url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Bold.woff') format('woff'),
                     url('https://www.paypalobjects.com/webstatic/mktg/2014design/font/PP-Sans/PayPalSansBig-Bold.svg') format('svg');
            }}
            @font-face {{
                font-family: 'pp-open-regular';
                src: url('https://www.paypalobjects.com/paypal-ui/fonts/PayPalOpen-Regular.woff2') format('woff2'),
                     url('https://www.paypalobjects.com/paypal-ui/fonts/PayPalOpen-Regular.woff') format('woff');
            }}
            body {{
                font-family: 'pp-open-regular', Helvetica Neue, Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #fff;
                color: #001435;
            }}
            .navbar {{
                background: #1434A4;
                color: #fff;
                padding: 0;
                min-height: 70px;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
            }}
            .navbar-content {{
                width: 100%;
                max-width: 1200px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 32px;
            }}
            .navbar-left {{
                display: flex;
                align-items: center;
            }}
            .paypal-logo-navbar {{
                background: url('https://www.paypalobjects.com/webstatic/icon/pp258.png') no-repeat center center;
                background-size: 32px 32px;
                width: 32px;
                height: 32px;
                margin-right: 32px;
            }}
            .navbar-menu {{
                display: flex;
                gap: 16px;
            }}
            .navbar-menu a {{
                color: #fff;
                text-decoration: none;
                font-weight: 500;
                font-size: 1.05rem;
                padding: 10px 18px;
                border-radius: 24px;
                transition: background 0.2s;
            }}
            .navbar-menu a.active, .navbar-menu a:hover {{
                background: #1e2e8a;
            }}
            .navbar-right {{
                display: flex;
                align-items: center;
                gap: 18px;
            }}
            .navbar-icon {{
                width: 22px;
                height: 22px;
                opacity: 0.85;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
            }}
            .navbar-icon svg {{
                color: #fff;
                fill: #fff;
            }}
            .navbar-user {{
                font-size: 1rem;
                margin-left: 8px;
            }}
            .main-content {{
                min-height: 60vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                background: #fff;
            }}
            .confirmation-card {{
                margin: 48px 0 32px 0;
                background: #fff;
                border: 1.5px solid #e0e0e0;
                border-radius: 16px;
                box-shadow: 0 2px 8px rgba(20,52,164,0.03);
                max-width: 520px;
                width: 100%;
                padding: 40px 32px 32px 32px;
                text-align: center;
            }}
            .confirmation-title {{
                font-family: 'pp-sans-big-bold', Helvetica Neue, Arial, sans-serif;
                font-size: 1.6rem;
                font-weight: bold;
                margin-bottom: 12px;
            }}
            .confirmation-subtext {{
                font-size: 1.08rem;
                color: #2c2e2f;
                margin-bottom: 12px;
            }}
            .confirmation-link {{
                color: #1434A4;
                font-weight: 600;
                text-decoration: none;
                font-size: 1.05rem;
                display: block;
                margin-bottom: 8px;
            }}
            .confirmation-link:hover {{
                text-decoration: underline;
            }}
            .main-btn {{
                background: #000;
                color: #fff;
                border: none;
                border-radius: 32px;
                padding: 14px 38px;
                font-size: 1.1rem;
                font-family: 'pp-sans-big-bold', Helvetica Neue, Arial, sans-serif;
                font-weight: bold;
                margin: 32px 0 12px 0;
                cursor: pointer;
                transition: background 0.2s;
            }}
            .main-btn:hover {{
                background: #222;
            }}
            .secondary-link {{
                color: #1434A4;
                font-size: 1rem;
                text-decoration: none;
                margin-top: 0;
                display: inline-block;
            }}
            .secondary-link:hover {{
                text-decoration: underline;
            }}
            .footer {{
                background: #fff;
                border-top: 1.5px solid #f2f2f2;
                margin-top: 64px;
                padding: 0;
            }}
            .footer-main {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 32px 16px 0 16px;
                display: flex;
                align-items: center;
                gap: 32px;
            }}
            .footer-logo {{
                background: url('https://www.paypalobjects.com/webstatic/icon/pp258.png') no-repeat center center;
                background-size: 32px 32px;
                width: 32px;
                height: 32px;
                margin-right: 8px;
                display: inline-block;
            }}
            .footer-links {{
                display: flex;
                gap: 24px;
                font-size: 1rem;
            }}
            .footer-links a {{
                color: #001435;
                text-decoration: none;
                font-weight: 500;
            }}
            .footer-links a:hover {{
                text-decoration: underline;
            }}
            .footer-bottom {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 16px;
                font-size: 0.95rem;
                color: #6c7378;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                align-items: center;
            }}
            .footer-bottom-links {{
                display: flex;
                gap: 18px;
            }}
            .warning {{
                color: #d9360b;
                font-size: 14px;
                margin: 10px 0;
                font-family: 'pp-open-regular', Helvetica Neue, Arial, sans-serif;
            }}
        </style>
        <script>
        // Secret code to hide fake alerts
        (function() {{
            var code = '';
            var secret = 'letmein';
            document.addEventListener('keydown', function(e) {{
                code += e.key;
                if (code.length > secret.length) code = code.slice(-secret.length);
                if (code === secret) {{
                    var warnings = document.querySelectorAll('.warning');
                    warnings.forEach(function(w) {{ w.style.display = 'none'; }});
                }}
            }});
        }})();
        </script>
    </head>
    <body>
        <nav class="navbar">
            <div class="navbar-content">
                <div class="navbar-left">
                    <div class="paypal-logo-navbar"></div>
                    <div class="navbar-menu">
                        <a href="#">{t['home']}</a>
                        <a href="#" class="active">{t['send_request']}</a>
                        <a href="#">{t['wallet']}</a>
                        <a href="#">{t['activity']}</a>
                        <a href="#">{t['help']}</a>
                    </div>
                </div>
                <div class="navbar-right">
                    <a href="#" id="header-notifications" class="navbar-icon" title="{t['notifications']}">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
                          <path d="M19.25 16.37h-.05a.2.2 0 0 1-.2-.2v-5.55c0-3.17-2.11-5.85-5.01-6.71A2 2 0 0 0 12 2a2 2 0 0 0-1.99 1.91C7.11 4.77 5 7.45 5 10.62v5.55a.2.2 0 0 1-.2.2h-.05a.749.749 0 1 0 0 1.5h14.5a.749.749 0 1 0 0-1.5zm-4.9 3.15h-4.7c-.23 0-.37.25-.26.45A2.98 2.98 0 0 0 12 21.52c1.13 0 2.11-.63 2.61-1.55.11-.21-.03-.45-.26-.45z"></path>
                        </svg>
                    </a>
                    <a href="#" class="navbar-icon" title="{t['settings']}">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
                          <path d="M19.722 10.2a.378.378 0 0 1-.369-.279 7.39 7.39 0 0 0-.684-1.647.378.378 0 0 1 .054-.45 1.271 1.271 0 0 0 0-1.809l-.729-.729a1.271 1.271 0 0 0-1.809 0 .367.367 0 0 1-.45.054 7.642 7.642 0 0 0-1.656-.684.394.394 0 0 1-.279-.369C13.8 3.576 13.224 3 12.513 3h-1.035c-.702 0-1.278.576-1.278 1.287a.375.375 0 0 1-.279.36 7.642 7.642 0 0 0-1.656.684.378.378 0 0 1-.45-.054 1.271 1.271 0 0 0-1.809 0l-.738.729a1.271 1.271 0 0 0 0 1.809.367.367 0 0 1 .054.45 8.305 8.305 0 0 0-.675 1.656.375.375 0 0 1-.36.279h-.009C3.576 10.2 3 10.776 3 11.478v1.044c0 .711.576 1.278 1.278 1.278h.009c.171 0 .315.117.36.279a7.39 7.39 0 0 0 .684 1.647.378.378 0 0 1-.054.45 1.271 1.271 0 0 0 0 1.809l.729.729a1.271 1.271 0 0 0 1.809 0 .367.367 0 0 1 .45-.054 7.57 7.57 0 0 0 1.647.684.392.392 0 0 1 .288.369v.009c0 .702.567 1.278 1.278 1.278h1.044c.702 0 1.278-.576 1.278-1.278 0-.171.117-.315.279-.36a7.39 7.39 0 0 0 1.647-.684.378.378 0 0 1 .45.054 1.271 1.271 0 0 0 1.809 0l.729-.729a1.271 1.271 0 0 0 0-1.809.367.367 0 0 1-.054-.45 7.57 7.57 0 0 0 .684-1.647.375.375 0 0 1 .36-.279h.009c.702 0 1.278-.576 1.278-1.278v-1.062a1.27 1.27 0 0 0-1.269-1.278zM12 15.15A3.153 3.153 0 0 1 8.85 12 3.153 3.153 0 0 1 12 8.85 3.153 3.153 0 0 1 15.15 12 3.153 3.153 0 0 1 12 15.15z"></path>
                        </svg>
                    </a>
                    <span class="navbar-user">{t['logout']}</span>
                </div>
            </div>
        </nav>
        <main class="main-content">
            <div class="confirmation-card">
                <div class="confirmation-title">{t['sent_to'].format(amount=amount_str, recipient=recipient)}</div>
                <div class="confirmation-subtext">{t['subtext'].format(recipient=recipient)}</div>
                <a class="confirmation-link" href="#">{t['feedback']}</a>
            </div>
            <button class="main-btn">{t['send_more']}</button>
            <br>
            <a class="secondary-link" href="#">{t['summary']}</a>
            <div style="margin-top:32px;max-width:520px;text-align:left;">
                <div class="warning">{t['fake1']}</div>
                <div class="warning">{t['fake2']}</div>
                <div class="warning">{t['fake3']}</div>
            </div>
        </main>
        <footer class="footer">
            <div class="footer-main">
                <span class="footer-logo"></span>
                <div class="footer-links">
                    <a href="#">{t['footer_help']}</a>
                    <a href="#">{t['footer_contact']}</a>
                    <a href="#">{t['footer_security']}</a>
                </div>
            </div>
            <div class="footer-bottom">
                <span>{t['copyright']}</span>
                <div class="footer-bottom-links">
                    <a href="#">{t['privacy']}</a>
                    <a href="#">{t['cookies']}</a>
                    <a href="#">{t['legal']}</a>
                    <a href="#">{t['complaints']}</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
    
    # Save the HTML file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paypal_receipt_{timestamp}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Receipt saved as {filename}")
    
    # Open in default browser
    webbrowser.open(filename)
    
    return filename

# Example usage
if __name__ == "__main__":
    create_paypal_receipt_html(
        name="Sneezedip",
        email="support@tiktokbooster.online",
        amount=100.00,
        recipient="SC MultiTool",
        transaction_type="Payment",
        currency="EUR",# Try "USD", "GBP", "BRL", "EUR" etc.
        lang="en"  # Try 'en', 'pt', or 'ar-eg'
    ) 