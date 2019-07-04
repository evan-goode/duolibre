#!/usr/bin/env python3

import click
from Crypto.PublicKey import RSA
import base64
import pyotp
import qrcode
import qrcode.image.svg
import requests
from urllib.parse import urlparse


def get_secret(activation_uri):
    parsed = urlparse(activation_uri)
    subdomain = parsed.netloc.split(".")[0]
    host_id = subdomain.split("-")[-1]
    slug = parsed.path.split("/")[-1]

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": f"api-{host_id}.duosecurity.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.0.0",
    }
    params = {"customer_protocol": "1"}
    data = {
        "touchid_status": "not_supported",
        "jailbroken": False,
        "architecture": "arch64",
        "region": "US",
        "app_id": "com.duosecurity.duomobile",
        "full_disk_encryption": True,
        "passcode_status": True,
        "platform": "Android",
        "pkpush": "rsa-sha512",
        "pubkey": RSA.generate(2048).publickey().export_key().decode(),
        "app_version": "3.28.1",
        "app_build_number": 328104,
        "version": "9.0.0",
        "manufacturer": "Samsung",
        "language": "en",
        "model": "Samsung Smart Fridge",
        "security_patch_level": "2019-07-05",
    }

    address = f"https://{parsed.netloc}/push/v2/activation/{slug}"

    request = requests.post(address, headers=headers, params=params, data=data)
    request.raise_for_status()
    return base64.b32encode(request.json()["response"]["hotp_secret"].encode())


@click.command()
@click.argument("activation-uri")
@click.argument("output-file")
def duolibre(activation_uri, output_file):
    secret = get_secret(activation_uri)
    print("secret is", secret)
    hotp = pyotp.hotp.HOTP(secret)
    uri = hotp.provisioning_uri("Duolibre", initial_count=1)

    factory = qrcode.image.svg.SvgPathImage
    image = qrcode.make(uri, image_factory=factory)

    image.save(output_file)
    print(f"Wrote {output_file}")


if __name__ == "__main__":
    duolibre()
