import pyqrcode

# Function to generate QR code
def generate_qr_code(data, filename):
    qr = pyqrcode.create(data)
    qr.png(filename, scale=8)

# Path to your provisioning XML file
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<config>
    <section name="sip">
        <entry name="proxy_url">pbx.zadarma.com</entry>
        <entry name="auth_userid">26502-100</entry>
        <entry name="auth_password">Ma1gicfonFa1tima1</entry>
        <entry name="register">1</entry>
    </section>
    <section name="sound">
        <entry name="codec_order">PCMU PCMA OPUS</entry>
    </section>
    <section name="misc">
        <entry name="ringtone">/path/to/ringtone/file.mp3</entry>
        <entry name="auto_answer">0</entry>
    </section>
</config>"""

# Generate QR code
generate_qr_code(xml_data, "linphone_provisioning_qr.png")
