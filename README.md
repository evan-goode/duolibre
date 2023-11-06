# Duolibre

Duolibre lets you authenticate to Duo 2FA systems without the proprietary Duo Mobile app. It forges an activation request from Duo Mobile to Duo's servers and hands the resulting HOTP secret over to you. You can use this secret to generate HOTP codes programmatically, or import it into the two-factor authenticator of your choice; for Android users, I recommend [Aegis](https://f-droid.org/app/com.beemdevelopment.aegis) or [FreeOTP+](https://f-droid.org/app/org.liberty.android.freeotpplus) from F-Droid. Note that Duolibre doesn't provide a reverse-engineered alternative to Duo Push, so you'll have to use one-time passwords.

## Getting started

Install via pip:

```
pip install --user git+https://github.com/evan-goode/duolibre.git
```

Or, using Nix, start a shell with Duolibre

```
nix shell github:evan-goode/duolibre
```

Run Duolibre against the activation URL that was sent to your phone via SMS, or the URL of the QR code displayed on the web interface:

```
duolibre https://m-XXXXXXXX.duosecurity.com/android/XXXXXXXXXXXXXXXXXXXX
```

If you'd rather save the generated provisioning QR code to an SVG file instead of printing it to the terminal, pass `--output-file`:

```
duolibre https://m-XXXXXXXX.duosecurity.com/android/XXXXXXXXXXXXXXXXXXXX --output-file ./qr-code.svg
```

## Background

The Duo Mobile app [collects](https://help.duo.com/s/article/2939?language=en_US) a considerable amount of analytics data from its users. Privacy-conscious folks and those who simply do not wish to run proprietary software on their phones should have a way to opt-out without special intervention from their organization. Duolibre makes it easy to use an alternative authenticator that's more respectful of one's privacy and freedoms.

I developed Duolibre by man-in-the-middling communication between the Duo Mobile client and Duo's servers. Duo Mobile for Android implements certificate pinning to defend against this reverse-engineering technique, but I was able to circumvent that using the Xposed module [JustTrustMe](https://github.com/Fuzion24/JustTrustMe).

## Usage

```
Usage: duolibre [OPTIONS] ACTIVATION_URI

Options:
  --output-file TEXT
  --help              Show this message and exit.
```

## License

[The Unlicense](https://unlicense.org)
