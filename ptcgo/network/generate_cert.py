"""Self-signed certificate for the game socket.

The client validates the name it dialled against the certificate, so the CN has
to be whatever host players use: an IP for local play, a domain for hosting.
It comes from PTCGO_PUBLIC_HOST, falling back to the config default.

    python ptcgo/network/generate_cert.py
    PTCGO_PUBLIC_HOST=tcgo.example.com python ptcgo/network/generate_cert.py

Do not install this into an OS trust store: the README notes the client's own
validator rejects a cert it trusts.
"""

import datetime
import ipaddress
import os

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

from ptcgo import config


def _host():
    return (os.environ.get("PTCGO_PUBLIC_HOST") or config.PUBLIC_HOST or "127.0.0.1").strip()


def generate_self_signed_cert(host=None):
    host = (host or _host()).strip()
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    san = [x509.DNSName(host)]
    try:  # a dialled IP must be in the SAN list as an IP, not a DNS name
        san.append(x509.IPAddress(ipaddress.ip_address(host.rstrip("[]"))))
    except ValueError:
        pass
    # keep loopback working so local testing never breaks when hosting
    for extra in ("localhost",):
        if extra != host:
            san.append(x509.DNSName(extra))
    san.append(x509.IPAddress(ipaddress.ip_address("127.0.0.1")))

    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, host)])
    now = datetime.datetime.now(datetime.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=3650))
        .add_extension(x509.SubjectAlternativeName(san), critical=False)
        .sign(private_key, hashes.SHA256())
    )

    with open("server.key", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    with open("server.crt", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    print(f"Generated server.key and server.crt for {host}")


if __name__ == "__main__":
    generate_self_signed_cert()
