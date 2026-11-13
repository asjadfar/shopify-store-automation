---
name: shopify-store-automation
description: End-to-end Shopify store automation — Claude builds a complete ready-to-sell Shopify store from a product list (store setup, products from CSV, collections, theme, policies, payments, shipping, taxes, SEO, launch checklist with approval gate). Modeled on the live store Fragrance Empire (fragranceempire.my — 155 products, 18 brands, 28 collections, Malaysia market, Horizon theme). Use when the user asks to build, set up, launch, or rebuild a Shopify store, add products in bulk, set up collections, payments, shipping, or policies, or prepare a store for launch.
---

# Shopify Store Automation

## When to use

Use this skill when the user asks to build a Shopify store from scratch, set up or launch a store, import products in bulk, create collections, configure payments / shipping / taxes, write store policies, set up a theme, do store SEO, or run a pre-launch check. The end result is a complete, ready-to-sell store — not a demo.

Do not use it for a single-product tweak (use a direct edit instead), for marketplaces (Amazon, Etsy, eBay), or for a platform other than Shopify, unless the user explicitly asks to adapt it.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — brief, store setup plan, product CSV, collections, theme plan, policies, payments, shipping, taxes, SEO, launch checklist. The owner is involved only at these points:

1. **Store decisions only the owner can make** — store name, market / country, currency, domain, contact email and phone, business name for policies, payment and shipping choices, and the product list itself (names, brands, sizes, prices). Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — creating the Shopify account, connecting a domain, entering bank / card / gateway details, and paying for a plan or a paid app. These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password, bank details, or payment credentials.
3. **Approval gates** — the owner approves the product list, the prices, the theme look, the policies, and the final launch checklist before anything goes live (see Step 12). Nothing is published without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Shopify Admin access:** Claude works through the owner's Shopify Admin (browser, with the owner's sign-in) or through the Shopify Admin API with an access token the owner creates in a custom app. Claude never invents store credentials and never logs in as the owner.
- **Product photos:** Claude writes the image plan (which photo goes on which product, in which order, with what alt text). The photos themselves come from the owner / supplier. Claude never invents a product photo and never attaches a photo to the wrong product — if a photo cannot be identified with certainty, it stays unattached and is flagged for the owner.

Everything else — research, CSV building and validation, collection structure, theme configuration plan, policy drafts, payment / shipping / tax setup steps, SEO, checklists — is Claude's work. Do not hand any of it back to the owner as homework.

## Store facts — the live reference store (do not invent others)

Fragrance Empire (https://fragranceempire.my) is the live store this skill is modeled on. Use its real, verified facts as the reference example. Do not invent a different reference store.

- **Store:** Fragrance Empire, fragranceempire.my, Shopify Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia.
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections.
- **Collections:** For Him, For Her, Unisex, one collection per brand (18), and a Bundles collection. Products that fit two groups are in both (for example unisex products appear in For Him, For Her and Unisex).
- **Pricing model:** every product has a price and a compare-at price. Sale price is shown in red bold; compare-at is struck through in grey. A product's compare-at price is the price before the current offer — never a price the product was never sold at, and never invent a compare-at price.
- **Payments:** Cash on Delivery (COD) active; card payments live through a Stripe card-payments provider (Visa, Mastercard, Amex, JCB, Discover, Diners, plus Apple Pay and Google Pay). Shopify Payments is not available in Malaysia — do not promise it for a Malaysia store, and check availability for the owner's country before promising any gateway.
- **Shipping:** exactly one rate — Standard, FREE, 3–5 business days, across Malaysia.
- **Taxes:** Malaysia "Not collecting", SST 0% (owner-confirmed for this store; check the owner's own tax position before copying this).
- **Trust block on product pages:** Ordered = today, Packed = +1 day, Delivered = +2 days; subtext "Dispatched in 24 hours."
- **Inventory:** quantities recorded as 100 pieces per product at the store location, with inventory tracking OFF — sales do not decrement stock. Decide tracking ON or OFF with the owner for each new store; never claim tracking is ON when it is OFF, and never show a fake "Only X left" badge.
- **Reviews:** Judge.me review emails — request sent 1 day after an order is fulfilled, follow-up after 5 days.
- **Fulfilment:** Ninja Van (consignment created per order from Shopify, airway bill printed, parcel dropped off at a Ninja Van point).
- **Seller services (Fiverr gig https://www.fiverr.com/s/L34yBpA):** Basic $80 — 10 products, 5 pages, 3 days; Standard $180 — 30 products, 8 pages, 5 days; Premium $350 — 50 products, 10 pages, 7 days. Unlimited revisions on all three packages.

## Hard limits — state them honestly, do not work around them

- **No credentials in the skill.** Never put an API key, password, access token, bank detail or secret in a skill file, in chat, or in a repo. Logins, bank details and gateway setup happen on the owner's own device.
- **Approval gates are mandatory.** Nothing is published, priced or launched until the owner approves the exact version: product list and prices, theme look, policy text, and the launch checklist. A changed price, image or policy needs fresh approval.
- **Never invent products, prices, brands or claims.** Every product name, brand, size, price and compare-at price comes from the owner or the owner's verified supplier list. If a fact is missing, ask — do not fill it in.
- **Never write fake reviews.** Reviews come only from real customers, in their own words. Claude may draft wording only when a real customer asked for help with the wording and agrees with the text.
- **Never claim a product is original / authentic unless the owner states it and takes responsibility for it.** If the products are impressions / inspired-by, say so in the store's own terms or say nothing — do not write "100% original" into a store, ad or listing on Claude's own initiative.
- **Gateway availability varies by country.** Shopify Payments, Stripe, FPX and other gateways are not available everywhere. Check the owner's country before promising any payment method. Do not promise FPX through a Stripe card-payments provider — it is not offered that way.
- **Paid apps need the owner's approval.** Never install a paid app or accept a paid plan / trial that converts to a charge without the owner approving the exact price first. Free plans only unless approved.
- **Do not guess-attach product photos.** A photo is attached to a product only when it is identified with certainty (readable bottle / label text, supplier numbering, or elimination). Size-ambiguous photos stay unattached and are listed for the owner.

## Scope tiers — ask which one before starting

Mirror the seller's real packages. Ask the owner which tier the build is, and do not build a bigger scope than the tier covers without agreement.

| Tier | Products | Pages | Delivery | Revisions |
|---|---|---|---|---|
| Basic | 10 | 5 | 3 days | Unlimited |
| Standard | 30 | 8 | 5 days | Unlimited |
| Premium | 50 | 10 | 7 days | Unlimited |

"Pages" means store pages (Home, collections, product pages, About, Contact, policies). A product page per product is included in the product count, not the page count. If the owner's catalog is bigger than the tier, agree the split (for example: first 50 products now, the rest as a follow-up) before starting.

## Workflow

### Step 1 — Brief (decisions first, no building before this)

Collect and write down, in `templates/store-setup-checklist.md`:

1. Store name, market / country, currency, timezone, language.
2. What the store sells (niche, brands, product types), and who buys it.
3. The product list: name, brand, size / variant, price, compare-at price, supplier photo filename. Use `templates/product-catalog.csv`.
4. Domain: new Shopify domain, or an existing domain to connect (registrar, DNS access on the owner's device).
5. Contact: store email, phone / WhatsApp, shop address (only if the owner wants it public).
6. Payments the owner wants: COD, card gateway, bank transfer, other — and what is actually available in the owner's country.
7. Shipping: zones, rates, delivery time promise, fulfilment partner.
8. Tier (Basic / Standard / Premium) and the delivery date.
9. Anything the owner explicitly does NOT want (for example: no POS, no second gateway yet, no fake reviews, no "100% original" claims).

Do not start Step 2 until the brief is filled in and the owner has confirmed it. A missing price or a missing product name is a blocker, not something to guess.

### Step 2 — Store setup

1. Create the Shopify account on the owner's device (owner signs up, picks the plan, enters payment details).
2. Set store name, currency, timezone, language, and the store's market.
3. Set the store contact email, phone and address exactly as the owner gave them.
4. Connect the domain (owner's registrar) and set it as primary. Verify the store loads on the real domain before moving on.
5. Set the store's default location / warehouse for inventory.

### Step 3 — Products from CSV

1. Fill in `templates/product-catalog.csv` from the owner's product list — one row per variant (one row per product when there are no variants). Required columns: Handle, Title, Vendor, Type, Tags, Variant Price, Variant Compare At Price, Variant Inventory Qty, Image Src, Image Alt Text, Status. Optional but recommended: Body (HTML) description, Variant SKU, SEO Title, SEO Description.
2. Validate the CSV with `scripts/validate_products.py` before importing. Fix every error it reports — do not import a CSV that fails validation.
3. Product description template (same for every product, fill in the blanks):
   - Opening line: what the product is, in one sentence.
   - Notes paragraph: the product's notes / character (only facts the owner or supplier gave — never invent notes).
   - Size / variant line: exact size (for example "100 ML").
   - Trust line: delivery and returns promise, matching the shipping policy.
4. Images: first image is the main image. Alt text names the product, brand and size. Never use a photo that shows a different variant (for example a photo showing "200ml" on a 100 ML listing). If a product has no photo, leave the image blank and flag it — do not copy another product's photo without the owner's approval.
5. Pricing: Variant Price is the price the customer pays. Variant Compare At Price is the price before the current offer, and must be higher than the price. Never set a compare-at price the product never sold at.
6. Inventory: set Variant Inventory Qty per the owner's instruction (Fragrance Empire uses 100 per product). Decide with the owner whether inventory tracking is ON or OFF, and record the decision in the checklist — never claim one when the other is true.
7. Import via Shopify Admin > Products > Import, or add products through the Admin / API if the owner uses that route. After import, open 3–5 product pages live (desktop and mobile) and check: name, price, compare-at price, image, description, trust block.

### Step 4 — Collections and navigation

1. Create collections from the brief:
   - One collection per brand.
   - Audience collections (for example For Him / For Her / Unisex) — a product that fits two audiences goes in both.
   - A Bundles collection if the store sells bundles.
   - A Featured / Best Sellers collection for the homepage.
2. Set each collection's sort order (manual for a curated order, or best-selling / A–Z) and add a short collection description.
3. Build the main menu: Home, key audience collections, Bundles, brand collections, Contact, About Us. Check every menu link on desktop and mobile — a link to a collection that does not exist is a launch blocker.
4. Bundles (if the store sells them): each bundle is its own product with its own price and compare-at price. Set a maximum bundle price with the owner before pricing (Fragrance Empire caps bundles at RM 999 compare-at). Bundle descriptions must state the saving in the same currency as the prices, and the saving must match the actual prices.

### Step 5 — Theme setup

1. Pick the theme with the owner (Fragrance Empire uses Horizon). Do not publish a theme the owner has not seen.
2. Homepage sections, in order: announcement bar, slideshow / hero, trust strip, best sellers, brand / collection highlights, footer.
3. Announcement bar: the current offer first, then standing messages (for example free delivery, COD available). Keep it to one offer at a time — never show two different offers at once.
4. Trust block on product pages: Ordered today / Packed +1 day / Delivered +2 days, "Dispatched in 24 hours." — adjust the day counts to the owner's real dispatch and delivery times.
5. Product cards: product name first, price below it — sale price in red bold, compare-at struck through in grey. Quick-add button must work on mobile.
6. Footer: social links (Facebook, Instagram), contact email and phone, policy links, payment method icons for the methods the store actually accepts.
7. Mobile-first check: about 90% of customers order by mobile on a store like Fragrance Empire. Check the homepage, a collection page, a product page and checkout on a real phone width before launch. Fix anything that is cut off, overlapping or un-tappable.

### Step 6 — Policies and pages

Write the pages from `templates/policies.md`. Every policy must be filled in with the owner's real facts — no invented addresses, timeframes or promises.

1. **About Us** — who the store is, what it sells, where it ships from.
2. **Contact** — store email, phone / WhatsApp, address (only if public), and a contact form.
3. **Privacy Policy** — what customer data is collected and why.
4. **Refund / Return Policy** — return window, condition, who pays return shipping, refund method and timing.
5. **Shipping Policy** — zones, rates, delivery time, dispatch time, public-holiday note if the owner wants one.
6. **Terms of Service** — ordering, payment, delivery, liability.
7. Publish all six pages and link them from the footer. A store with missing policies is not ready to launch.

### Step 7 — Payments

1. Enable exactly the methods the owner approved, and no others.
2. Cash on Delivery (COD): enable it if the owner wants it. If an order-confirmation step is used (for example WhatsApp confirmation), record how unverified orders are handled and after how long.
3. Card payments: connect the gateway the owner chose (for example Stripe card payments where available). Verify test mode is OFF before launch, and that the methods the owner expects (Visa, Mastercard, Amex, Apple Pay, Google Pay) actually appear at checkout. Do a checkout test without completing a purchase, and record the result.
4. Do not enable a gateway the owner has not approved, and do not promise a gateway that is not available in the owner's country.

### Step 8 — Shipping

1. Set up the shipping zone(s) for the owner's market.
2. Add the rates the owner approved — one rate per zone unless the owner asks for more. (Fragrance Empire has exactly one rate: Standard, FREE, 3–5 business days.)
3. Match the rate and delivery time to the shipping policy and the product-page trust block — all three must say the same thing.
4. Set up the fulfilment partner's app / workflow if the owner uses one (for example a courier app), and test creating one consignment before launch.

### Step 9 — Taxes

1. Set the tax region(s) for the owner's market and whether the store collects tax.
2. Record the decision in the checklist (Fragrance Empire: Malaysia "Not collecting", SST 0%).
3. Do not invent a tax rate. If the owner is unsure, the owner checks with their accountant / the local rules before launch.

### Step 10 — Apps (only what the build needs)

Install only the apps the owner approved, free plans unless a paid plan was explicitly approved with its price:

- **Reviews** (for example Judge.me): review request after fulfilment + follow-up. Never write fake reviews.
- **Fulfilment / courier app** (for example Ninja Van in Malaysia): only if the owner uses that courier.
- **Discount app** (for example an automatic card-payment discount app): only if the owner approved the app and its monthly price, and only after recording when it ends.
- **Bundles app:** only if the store sells bundles that need it.

After installing each app, verify it does what the owner asked and record its plan and price in the checklist.

### Step 11 — SEO

1. Every product: SEO title and SEO description filled in (from the CSV or in Admin). No duplicate SEO titles across products.
2. Every product image: alt text naming the product, brand and size.
3. Every collection: description filled in.
4. Homepage: title and description set.
5. Verify the sitemap loads and submit the store to Google Search Console (owner's Google account, on their device).
6. Check the store on mobile and desktop for the exact search terms a customer would use — the store name and the main product names must appear.

### Step 12 — Launch checklist + approval gate

Complete `templates/store-setup-checklist.md` for the store. Then stop and get the owner's approval for: the product list and prices, the theme look (homepage + one product page, mobile), the policy text, and the payment / shipping setup.

Launch only after approval. The launch steps:

1. Remove any test products, test discounts and password protection.
2. Place one test order (COD if the store takes COD — never use a card the owner does not have) and cancel it after verifying checkout works. Record the test order number and that it was cancelled.
3. Verify the order confirmation and (if enabled) the review-request flow.
4. Check the live store on a phone: homepage, one collection, one product page, cart, checkout.
5. Return the live store URL to the owner, with the tier delivered, the product count, and anything still pending.

### Step 13 — After launch (first week)

1. Check for the first real order daily and confirm it flows to fulfilment correctly.
2. Fix any broken link, wrong price or missing image the owner reports, and re-verify live after each fix.
3. Do not change prices, offers or policies without the owner's approval.
4. Record what was delivered (product count, collections, pages, apps, tier) in the checklist so the next build starts from a known state.

## How to run one store build

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Fill in `templates/product-catalog.csv` and run `scripts/validate_products.py` until it passes.
3. Work Steps 2–11 in order. Do not skip a step because it looks small — policies, taxes and SEO are launch blockers, not extras.
4. Fill in `templates/store-setup-checklist.md` and get the owner's approval at the gate (Step 12).
5. Launch (Step 12), then do the first-week checks (Step 13).
