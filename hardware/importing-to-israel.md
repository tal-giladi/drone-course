# Importing drone parts to Israel

Most of Hermon's avionics come in by post. Four rules decide how much that costs, how long it
takes, and whether it arrives at all.

> [!WARNING]
> This page is engineering guidance written on **2026-09-22**, not legal or customs advice.
> The personal-import threshold moved **three times in twelve months**. Check the current
> figure before a large order.

## 1. The VAT threshold — check it every time

| Value of the shipment | What you owe |
|---|---|
| Up to **$75** | Nothing |
| $75 – $500 | **18 % VAT** on the goods |
| Above $500 | 18 % VAT, plus customs duty and purchase tax where they apply |

The recent history, because it explains why nobody agrees on the number:

- The exemption was **$75** for years.
- Raised to **$150** — Finance Ministry announcement 26 Nov 2025, amendment published 23 Dec 2025.
- The Knesset revoked it.
- A **$130** order signed by the minister, effective 25 Feb 2026.
- The Knesset revoked that on 1 June 2026 (59–23).
- **Back to $75 from 2 June 2026.**

**What this means for the Stage 1 order.** The import basket is ≈ $390–530, so you will pay
18 % VAT on it. Splitting it into sub-$75 parcels is usually *not* cheaper once you count
shipping, and it delays the build. Order it as one basket, budget the VAT, and be done.

## 2. Lithium batteries do not come by post

Lithium-polymer packs are effectively not air-freighted to private addresses in Israel. This
is not a rule you can work around with a friendly seller — it is how the carriers handle
UN3480/UN3481 goods.

**Buy the packs in Israel.** [Sollan](suppliers-israel.md#batteries-chargers-safety),
Dominator and RCBattery all stock 6S. This is why items 10–12 on the
[Stage 1 list](stage-1-first-flight.md) are the only mandatory local lines.

The same applies in reverse: do not put a LiPo in checked baggage, and do not post one to
anyone. [03.10](../03-power-system/03.10-lipo-in-israel.md) covers transport properly.

## 3. Radio transmitters need to be legal here, not just where you bought them

Three of Hermon's parts transmit: the ExpressLRS transmitter, the ExpressLRS receivers, and
the telemetry radio.

| Part | Band | Israeli status |
|---|---|---|
| ExpressLRS TX/RX | 2400–2483.5 MHz | Licence-exempt band. Keep the output power at the ~100 mW class the exemption contemplates rather than running a 1 W module at full power |
| Telemetry radio | **917–920 MHz only** | The licence-exempt sub-GHz window. **You must reconfigure the radio** — see below |
| FPV video (optional, not required) | 5725–5875 MHz | Permit-based. Check before you transmit |

**The telemetry radio is the trap.** Buy the **900 MHz-class** hardware (sold as "915 MHz").
Do **not** buy the "868 MHz" SKU — its front end is filtered for the European 863–870 MHz
band, which is not an Israeli allocation. Do **not** buy 433 MHz at all — 430–440 MHz is the
amateur service here.

Then, before the first transmission:

```text
ATS8=917000      # MIN_FREQ in kHz
ATS9=920000      # MAX_FREQ in kHz
ATS10=10         # NUM_CHANNELS
RTS8=917000      # and the SAME on the REMOTE radio
RTS9=920000
RTS10=10
AT&W             # write
ATZ              # reboot
```

[09.04](../09-telemetry-datalink/09.04-telemetry-917.md) walks through it on both radios;
[09.05](../09-telemetry-datalink/09.05-spectrum-and-regulation.md) covers the regulatory
framework, including Israel's three-track system of licensing, conformity approval
(אישור התאמה) and exemption, and where CE-marked equipment sits in it.

**Practical advice:** prefer CE-marked equipment when the price is close. It is the cleaner
paperwork story and the EU Radio Equipment Directive is named in the Israeli regulations'
framing of the exemption path.

## 4. Shipping realities

| Route | Time | Notes |
|---|---|---|
| **DigiKey Israel, billed in ₪** | 7–10 business days | DigiKey clears customs. The premium buys away the whole customs step — worth it for connectors and anything catalogued |
| DigiKey/Mouser billed in USD | ~3 days to Israeli customs | You release it yourself |
| Holybro / T-Motor direct | 1–3 weeks | Confirm they ship to Israel before you build the basket; some vendors route through a regional distributor |
| AliExpress | 2–4 weeks | The realistic source for the frame, props, ELRS and clones. Choose a seller with a track record, not the cheapest listing |
| EU hobby shops | 1–2 weeks | Sometimes cheaper all-in than AliExpress once VAT is counted, and the CE paperwork is better |

## The checklist before you place the Stage 1 order

- [ ] Today's import-VAT threshold confirmed.
- [ ] Batteries, charger and LiPo bag ordered **separately, from an Israeli shop**.
- [ ] Telemetry radio is the **900 MHz** SKU, not 868 and not 433.
- [ ] ExpressLRS is 2.4 GHz.
- [ ] One spare motor and one spare set of props in the same basket.
- [ ] Every part on the list has a substitute spec written down, so a stock-out does not stop you.
- [ ] Vendor confirmed to ship to Israel.
- [ ] Total basket value written down, and the VAT you expect to owe budgeted.
