# Shopify Store Automation Skill

A Claude skill for end-to-end Shopify store automation, built from Asjad's real store-building work. Claude handles all the work end to end — brief, store setup, products from CSV, collections, theme, policies, payments, shipping, taxes, SEO and launch checklist — with the owner involved only for the decisions, accounts, sign-ins and approval gates. It is modeled on the live store Fragrance Empire, a complete Shopify store with 155 products, 18 brands and 28 collections.

## What it does

Takes a store from brief to launch in one repeatable workflow:

1. **Brief** — store name, market, currency, product list, prices, payments, shipping, tier. No building before the brief is confirmed.
2. **Store setup** — account, currency, timezone, domain, contact details, location.
3. **Products from CSV** — a product catalog template, a validator script, import, images with alt text, descriptions, pricing with compare-at prices, inventory.
4. **Collections and navigation** — brand collections, audience collections (For Him / For Her / Unisex), bundles, main menu.
5. **Theme** — homepage sections, announcement bar, trust block, product cards, footer, mobile-first check.
6. **Policies and pages** — About, Contact, Privacy, Refund/Return, Shipping, Terms of Service.
7. **Payments** — COD, card gateway (where available), checkout test.
8. **Shipping** — zones, rates, delivery time promise, fulfilment partner.
9. **Taxes** — tax regions, collecting or not, recorded decision.
10. **Apps** — reviews, fulfilment, discounts, bundles — only what the owner approved.
11. **SEO** — product and collection SEO, image alt text, sitemap, Search Console.
12. **Launch checklist + approval gate** — nothing goes live until the owner approves the exact products, prices, theme look and policies.
13. **First week** — first-order check, fixes, delivery record.

## Who does what — Claude handles all the work end to end

Claude runs every step — brief, CSV, collections, theme plan, policies, payment / shipping / tax setup steps, SEO, checklists. The owner is involved only at three points: (1) store decisions only the owner can make (name, market, currency, domain, contact details, product list and prices, payment and shipping choices); (2) accounts, sign-ins and money (Shopify account, domain, bank / card / gateway details, plan and paid-app payments — all on the owner's own device); and (3) approval gates (product list and prices, theme look, policies, final launch checklist). The two device-bound exceptions are Shopify Admin access (browser with the owner's sign-in, or Admin API with an access token the owner creates) and product photos (Claude plans them; the photos come from the owner / supplier). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example store

- **Store:** Fragrance Empire — https://fragranceempire.my
- **Platform:** Shopify, Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections
- **Payments:** Cash on Delivery (COD) + card payments via Stripe (Visa, Mastercard, Amex, JCB, Discover, Diners, Apple Pay, Google Pay)
- **Shipping:** Standard, FREE, 3–5 business days across Malaysia
- **Reviews:** Judge.me — request 1 day after fulfilment, follow-up after 5 days
- **Fulfilment:** Ninja Van
- **Built by:** Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA

## Service tiers (the seller's real packages)

| Tier | Products | Pages | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 10 | 5 | 3 days | Unlimited |
| Standard | 30 | 8 | 5 days | Unlimited |
| Premium | 50 | 10 | 7 days | Unlimited |

Prices: Basic $80, Standard $180, Premium $350. Ask the owner which tier the build is before starting, and do not build a bigger scope than the tier covers without agreement.

## Files

```
shopify-store-automation/
├── README.md                                  # this file
└── shopify-store-automation/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── validate_products.py               # validates the product CSV before import
    └── templates/
        ├── product-catalog.csv                # Shopify product import template
        ├── store-setup-checklist.md           # brief + pre-launch checklist + approval gate
        └── policies.md                        # policy and page template outlines
```

## Setup

### 1. Get the brief first

Fill in `templates/store-setup-checklist.md` (Step 1 of `SKILL.md`) with the owner: store name, market, currency, product list, prices, payments, shipping, tier. Do not start building until the owner confirms the brief.

### 2. Choose the store-build route (one of these)

**Route A — Shopify Admin in the browser (recommended to start).** The owner signs in to Shopify Admin on their own device and approves each step, or approves a browser session. Claude prepares everything (CSV, collections plan, theme plan, policies) and the owner applies it in Admin. No API key needed.

**Route B — Shopify Admin API with a custom app.** The owner creates a custom app in Shopify Admin, sets the needed access scopes, and creates an access token on their own device. The skill then follows the API steps. This is more setup, and it is the only route that lets an agent change the store without the browser.

Do not use any other route. Do not paste API keys, passwords or credentials into the skill files, into chat, or into a repo — credentials live only in the owner's secure storage.

### 3. Product photos

Photos come from the owner / supplier. Claude writes the image plan (which photo goes on which product, in which order, with what alt text) and never attaches a photo to the wrong product. If a photo cannot be identified with certainty, it stays unattached and is flagged for the owner.

### 4. Use in Claude

Copy the `shopify-store-automation/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `shopify-store-automation/SKILL.md`. Then ask Claude to run the workflow, for example: "Build a Shopify store for my perfume business using the shopify-store-automation skill. Tier: Standard."

## Honest limits — read before using

- **No direct Shopify connection.** Claude does not have a built-in Shopify connection. Store changes go through the browser (owner's sign-in + approval) or the Shopify Admin API with an access token the owner sets up. Never claim direct auto-setup without one of those.
- **No credentials in the skill.** No API keys, passwords, access tokens, bank details or secrets are stored in these files. If a step needs a login or a payment detail, the owner does it on their own device.
- **Approval gate is mandatory.** No product, price, theme change or policy is published until the owner approves the exact final version. A changed price, image or policy needs fresh approval.
- **Never invent products, prices, brands or claims.** Every product name, brand, size, price and compare-at price comes from the owner or the owner's verified supplier list. Missing facts are asked, not guessed.
- **No fake reviews.** Reviews come only from real customers, in their own words.
- **Gateway availability varies by country.** Shopify Payments, Stripe, FPX and other gateways are not available everywhere. Check the owner's country before promising any payment method.
- **Paid apps need approval.** Never install a paid app or accept a paid plan / trial that converts to a charge without the owner approving the exact price first.
- **Do not guess-attach product photos.** A photo is attached only when identified with certainty. Size-ambiguous photos stay unattached.

## How to run one store build

1. Fill in the brief in `templates/store-setup-checklist.md` and get the owner to confirm it.
2. Fill in `templates/product-catalog.csv` and run `scripts/validate_products.py` until it passes.
3. Work Steps 2–11 of `SKILL.md` in order.
4. Fill in the launch checklist and get the owner's approval at the gate (Step 12).
5. Launch, then do the first-week checks (Step 13).
