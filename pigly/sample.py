import json
import math

TRANS = '{ "transactions": [ { "transaction-id": "1425679320000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2015-03-05T18:58:00.000Z", "amount": -48000, "categorization": "Unknown" }, { "transaction-id": "1425452880000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK", "merchant": "Check", "is-pending": false, "transaction-time": "2015-03-03T00:56:00.000Z", "amount": -13642900, "categorization": "Unknown" }, { "transaction-id": "1425442800000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CC PAYMENT", "merchant": "CC Payment", "is-pending": false, "transaction-time": "2015-03-03T07:22:00.000Z", "amount": -5194500, "categorization": "Unknown" } , { "transaction-id": "1425274080000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ATM WITHDRAWAL", "merchant": "ATM Withdrawal", "is-pending": false, "transaction-time": "2015-02-28T11:29:00.000Z", "amount": -820000, "categorization": "Unknown" }, { "transaction-id": "1425254340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2015-03-01T17:19:00.000Z", "amount": -737757, "categorization": "Gas & Fuel" }, { "transaction-id": "1425218520000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1111", "merchant": "Check 1111", "is-pending": false, "transaction-time": "2015-03-01T14:02:00.000Z", "amount": -23379709, "categorization": "Check" }], "error": "no-error" }'#, { "transaction-id": "1425167940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2015-02-25T16:20:00.000Z", "amount": -101247, "categorization": "Uncategorized" }, { "transaction-id": "1425081540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-02-27T12:47:00.000Z", "amount": 8149204, "categorization": "Paycheck" }, { "transaction-id": "1424908740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2015-02-24T18:34:00.000Z", "amount": -2145218, "categorization": "Auto Insurance" }, { "transaction-id": "1424874540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2015-02-25T14:29:00.000Z", "amount": -43635, "categorization": "Bank Fee" }, { "transaction-id": "1424649540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2015-02-19T05:48:00.000Z", "amount": -3063884, "categorization": "Auto Payment" }, { "transaction-id": "1424494440000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2015-02-21T04:54:00.000Z", "amount": -97487, "categorization": "Auto Payment" }, { "transaction-id": "1424476740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-02-20T12:47:00.000Z", "amount": 8070722, "categorization": "Paycheck" }, { "transaction-id": "1424044740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2015-02-15T17:19:00.000Z", "amount": -739979, "categorization": "Gas & Fuel" }, { "transaction-id": "1423871940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-02-13T12:47:00.000Z", "amount": 8129494, "categorization": "Paycheck" }, { "transaction-id": "1423703520000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2015-02-12T01:12:00.000Z", "amount": -5285689, "categorization": "Shopping" }, { "transaction-id": "1423492380000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1110", "merchant": "Check 1110", "is-pending": false, "transaction-time": "2015-02-09T14:33:00.000Z", "amount": -3103402, "categorization": "Check" }, { "transaction-id": "1423267140001", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-02-06T12:47:00.000Z", "amount": 8144968, "categorization": "Paycheck" }, { "transaction-id": "1423267140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "KROGER LIMITED P 2009", "merchant": "Kroger Limited P 2009", "is-pending": false, "transaction-time": "2015-02-04T09:15:00.000Z", "amount": -409569, "categorization": "Groceries" }, { "transaction-id": "1423100100000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MAPCO EXP 501 NORTH", "merchant": "Mapco Exp 501 North", "is-pending": false, "transaction-time": "2015-02-05T01:35:00.000Z", "amount": -684830, "categorization": "Home Improvement" }, { "transaction-id": "1423094340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2015-02-03T22:04:00.000Z", "amount": -233460, "categorization": "Personal Care" }, { "transaction-id": "1423007940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "PAYPAL ECHECK J222", "merchant": "Paypal Echeck J222", "is-pending": false, "transaction-time": "2015-02-03T11:35:00.000Z", "amount": -417481, "categorization": "Shopping" }, { "transaction-id": "1422662340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-01-30T12:47:00.000Z", "amount": 8125981, "categorization": "Paycheck" }, { "transaction-id": "1422230340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2015-01-24T18:34:00.000Z", "amount": -1782798, "categorization": "Auto Insurance" }, { "transaction-id": "1422057540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-01-23T12:47:00.000Z", "amount": 8281028, "categorization": "Paycheck" }, { "transaction-id": "1421625540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2015-01-15T05:48:00.000Z", "amount": -3719919, "categorization": "Auto Payment" }, { "transaction-id": "1421556840000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2015-01-18T04:54:00.000Z", "amount": -100300, "categorization": "Auto Payment" }, { "transaction-id": "1421452740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-01-16T12:47:00.000Z", "amount": 8009587, "categorization": "Paycheck" }, { "transaction-id": "1421332140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2015-01-15T14:29:00.000Z", "amount": -37370, "categorization": "Bank Fee" }, { "transaction-id": "1420847940002", "account-id": "nonce:42069000-96459775", "raw-merchant": "LOWE'S #1186", "merchant": "Lowe's #1186", "is-pending": false, "transaction-time": "2015-01-09T23:13:00.000Z", "amount": -1758622, "categorization": "Home Improvement" }, { "transaction-id": "1420847940001", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-01-09T12:47:00.000Z", "amount": 8256029, "categorization": "Paycheck" }, { "transaction-id": "1420847940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2015-01-08T22:04:00.000Z", "amount": -263653, "categorization": "Personal Care" }, { "transaction-id": "1420761540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2015-01-05T16:20:00.000Z", "amount": -89964, "categorization": "Uncategorized" }, { "transaction-id": "1420502340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2015-01-05T17:19:00.000Z", "amount": -824572, "categorization": "Gas & Fuel" }, { "transaction-id": "1420333920000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2015-01-04T01:12:00.000Z", "amount": -5175680, "categorization": "Shopping" }, { "transaction-id": "1420243140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2015-01-02T12:47:00.000Z", "amount": 8185078, "categorization": "Paycheck" }, { "transaction-id": "1420070340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2014-12-28T05:48:00.000Z", "amount": -4197867, "categorization": "Auto Payment" }, { "transaction-id": "1420036140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2014-12-31T14:29:00.000Z", "amount": -31276, "categorization": "Bank Fee" }, { "transaction-id": "1419638340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-12-26T12:47:00.000Z", "amount": 8138694, "categorization": "Paycheck" }, { "transaction-id": "1419551940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2014-12-24T18:34:00.000Z", "amount": -1967964, "categorization": "Auto Insurance" }, { "transaction-id": "1419465540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2014-12-21T16:20:00.000Z", "amount": -123034, "categorization": "Uncategorized" }, { "transaction-id": "1419310440000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2014-12-23T04:54:00.000Z", "amount": -116934, "categorization": "Auto Payment" }, { "transaction-id": "1419256920000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1111", "merchant": "Check 1111", "is-pending": false, "transaction-time": "2014-12-22T14:02:00.000Z", "amount": -27190767, "categorization": "Check" }, { "transaction-id": "1419037920000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2014-12-20T01:12:00.000Z", "amount": -5952635, "categorization": "Shopping" }, { "transaction-id": "1419033540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-12-19T12:47:00.000Z", "amount": 8095455, "categorization": "Paycheck" }, { "transaction-id": "1418860740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "LOWE'S #1186", "merchant": "Lowe's #1186", "is-pending": false, "transaction-time": "2014-12-17T23:13:00.000Z", "amount": -1658795, "categorization": "Home Improvement" }, { "transaction-id": "1418515140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2014-12-12T22:04:00.000Z", "amount": -220981, "categorization": "Personal Care" }, { "transaction-id": "1418428740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-12-12T12:47:00.000Z", "amount": 8129480, "categorization": "Paycheck" }, { "transaction-id": "1418394780000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1110", "merchant": "Check 1110", "is-pending": false, "transaction-time": "2014-12-12T14:33:00.000Z", "amount": -2850207, "categorization": "Check" }, { "transaction-id": "1418169540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "KROGER LIMITED P 2009", "merchant": "Kroger Limited P 2009", "is-pending": false, "transaction-time": "2014-12-07T09:15:00.000Z", "amount": -391071, "categorization": "Groceries" }, { "transaction-id": "1417823940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-12-05T12:47:00.000Z", "amount": 8202658, "categorization": "Paycheck" }, { "transaction-id": "1417737540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "PAYPAL ECHECK J222", "merchant": "Paypal Echeck J222", "is-pending": false, "transaction-time": "2014-12-04T11:35:00.000Z", "amount": -500153, "categorization": "Shopping" }, { "transaction-id": "1417651140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2014-12-03T17:19:00.000Z", "amount": -874702, "categorization": "Gas & Fuel" }, { "transaction-id": "1417357740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2014-11-30T14:29:00.000Z", "amount": -40465, "categorization": "Bank Fee" }, { "transaction-id": "1417219140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-11-28T12:47:00.000Z", "amount": 8207624, "categorization": "Paycheck" }, { "transaction-id": "1416959940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2014-11-24T18:34:00.000Z", "amount": -1759150, "categorization": "Auto Insurance" }, { "transaction-id": "1416614340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-11-21T12:47:00.000Z", "amount": 8238531, "categorization": "Paycheck" }, { "transaction-id": "1416545640000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2014-11-21T04:54:00.000Z", "amount": -88407, "categorization": "Auto Payment" }, { "transaction-id": "1416268740001", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2014-11-14T16:20:00.000Z", "amount": -84319, "categorization": "Uncategorized" }, { "transaction-id": "1416268740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2014-11-14T05:48:00.000Z", "amount": -3125961, "categorization": "Auto Payment" }, { "transaction-id": "1416009540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-11-14T12:47:00.000Z", "amount": 8035103, "categorization": "Paycheck" }, { "transaction-id": "1415836740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "LOWE'S #1186", "merchant": "Lowe's #1186", "is-pending": false, "transaction-time": "2014-11-12T23:13:00.000Z", "amount": -1758517, "categorization": "Home Improvement" }, { "transaction-id": "1415663940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2014-11-09T22:04:00.000Z", "amount": -235306, "categorization": "Personal Care" }, { "transaction-id": "1415404740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-11-07T12:47:00.000Z", "amount": 8039840, "categorization": "Paycheck" }, { "transaction-id": "1415324100000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MAPCO EXP 501 NORTH", "merchant": "Mapco Exp 501 North", "is-pending": false, "transaction-time": "2014-11-07T01:35:00.000Z", "amount": -725450, "categorization": "Home Improvement" }, { "transaction-id": "1415282520000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1111", "merchant": "Check 1111", "is-pending": false, "transaction-time": "2014-11-06T14:02:00.000Z", "amount": -21163333, "categorization": "Check" }, { "transaction-id": "1414977120000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2014-11-03T01:12:00.000Z", "amount": -5573692, "categorization": "Shopping" }, { "transaction-id": "1414799940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-10-31T12:47:00.000Z", "amount": 8158853, "categorization": "Paycheck" }, { "transaction-id": "1414713540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2014-10-27T05:48:00.000Z", "amount": -3238024, "categorization": "Auto Payment" }, { "transaction-id": "1414281540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2014-10-24T18:34:00.000Z", "amount": -1685161, "categorization": "Auto Insurance" }, { "transaction-id": "1414195140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-10-24T12:47:00.000Z", "amount": 8298286, "categorization": "Paycheck" }, { "transaction-id": "1413763140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2014-10-16T16:20:00.000Z", "amount": -101997, "categorization": "Uncategorized" }, { "transaction-id": "1413728940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2014-10-19T14:29:00.000Z", "amount": -40257, "categorization": "Bank Fee" }, { "transaction-id": "1413590340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-10-17T12:47:00.000Z", "amount": 8172484, "categorization": "Paycheck" }, { "transaction-id": "1413503940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2014-10-16T17:19:00.000Z", "amount": -773520, "categorization": "Gas & Fuel" }, { "transaction-id": "1413262440000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2014-10-14T04:54:00.000Z", "amount": -91509, "categorization": "Auto Payment" }, { "transaction-id": "1412985540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-10-10T12:47:00.000Z", "amount": 8178503, "categorization": "Paycheck" }, { "transaction-id": "1412904900000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MAPCO EXP 501 NORTH", "merchant": "Mapco Exp 501 North", "is-pending": false, "transaction-time": "2014-10-10T01:35:00.000Z", "amount": -547228, "categorization": "Home Improvement" }, { "transaction-id": "1412899140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2014-10-08T22:04:00.000Z", "amount": -271047, "categorization": "Personal Care" }, { "transaction-id": "1412604120000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1111", "merchant": "Check 1111", "is-pending": false, "transaction-time": "2014-10-06T14:02:00.000Z", "amount": -26087245, "categorization": "Check" }, { "transaction-id": "1412471520000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2014-10-05T01:12:00.000Z", "amount": -4918210, "categorization": "Shopping" }, { "transaction-id": "1412433180000", "account-id": "nonce:42069000-96459775", "raw-merchant": "CHECK 1110", "merchant": "Check 1110", "is-pending": false, "transaction-time": "2014-10-04T14:33:00.000Z", "amount": -3573054, "categorization": "Check" }, { "transaction-id": "1412380740002", "account-id": "nonce:42069000-96459775", "raw-merchant": "LOWE'S #1186", "merchant": "Lowe's #1186", "is-pending": false, "transaction-time": "2014-10-03T23:13:00.000Z", "amount": -1717022, "categorization": "Home Improvement" }, { "transaction-id": "1412380740001", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-10-03T12:47:00.000Z", "amount": 8110737, "categorization": "Paycheck" }, { "transaction-id": "1412380740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "KROGER LIMITED P 2009", "merchant": "Kroger Limited P 2009", "is-pending": false, "transaction-time": "2014-10-01T09:15:00.000Z", "amount": -360782, "categorization": "Groceries" }, { "transaction-id": "1412294340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "PAYPAL ECHECK J222", "merchant": "Paypal Echeck J222", "is-pending": false, "transaction-time": "2014-10-02T11:35:00.000Z", "amount": -445339, "categorization": "Shopping" }, { "transaction-id": "1411775940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-09-26T12:47:00.000Z", "amount": 8246069, "categorization": "Paycheck" }, { "transaction-id": "1411689540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "GEICO 000-000-0000 DC", "merchant": "Geico 000-000-0000 DC", "is-pending": false, "transaction-time": "2014-09-24T18:34:00.000Z", "amount": -1678799, "categorization": "Auto Insurance" }, { "transaction-id": "1411343940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SWEENEYS CHEVROLET", "merchant": "Sweeneys Chevrolet", "is-pending": false, "transaction-time": "2014-09-18T05:48:00.000Z", "amount": -3856428, "categorization": "Auto Payment" }, { "transaction-id": "1411171140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-09-19T12:47:00.000Z", "amount": 8143145, "categorization": "Paycheck" }, { "transaction-id": "1410998340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SOAPS N SUDS NORFOLK VA", "merchant": "Soaps N Suds Norfolk VA", "is-pending": false, "transaction-time": "2014-09-16T22:04:00.000Z", "amount": -266417, "categorization": "Personal Care" }, { "transaction-id": "1410791340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SERVICE FEE", "merchant": "Service Fee", "is-pending": false, "transaction-time": "2014-09-15T14:29:00.000Z", "amount": -39520, "categorization": "Bank Fee" }, { "transaction-id": "1410657120000", "account-id": "nonce:42069000-96459775", "raw-merchant": "Payment to Chase card ending in", "merchant": "Chase Card Ending In", "is-pending": false, "transaction-time": "2014-09-14T01:12:00.000Z", "amount": -5107767, "categorization": "Shopping" }, { "transaction-id": "1410652740000", "account-id": "nonce:42069000-96459775", "raw-merchant": "LOWE'S #1186", "merchant": "Lowe's #1186", "is-pending": false, "transaction-time": "2014-09-13T23:13:00.000Z", "amount": -1841625, "categorization": "Home Improvement" }, { "transaction-id": "1410566340000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-09-12T12:47:00.000Z", "amount": 8144455, "categorization": "Paycheck" }, { "transaction-id": "1410479940000", "account-id": "nonce:42069000-96459775", "raw-merchant": "SHOPTRN*Thule", "merchant": "Shoptrn*Thule", "is-pending": false, "transaction-time": "2014-09-08T16:20:00.000Z", "amount": -98625, "categorization": "Uncategorized" }, { "transaction-id": "1410307140000", "account-id": "nonce:42069000-96459775", "raw-merchant": "FUEL CITY", "merchant": "Fuel City", "is-pending": false, "transaction-time": "2014-09-09T17:19:00.000Z", "amount": -942416, "categorization": "Gas & Fuel" }, { "transaction-id": "1410152040000", "account-id": "nonce:42069000-96459775", "raw-merchant": "MERCURY BLVD. CI", "merchant": "Mercury Blvd. CI", "is-pending": false, "transaction-time": "2014-09-08T04:54:00.000Z", "amount": -125469, "categorization": "Auto Payment" }, { "transaction-id": "1409961540000", "account-id": "nonce:42069000-96459775", "raw-merchant": "ZENPAYROLL", "merchant": "Zenpayroll", "is-pending": false, "transaction-time": "2014-09-05T12:47:00.000Z", "amount": 8027760, "categorization": "Paycheck" } ], "error": "no-error" }'
def _transactions():
	transactions = json.loads(TRANS)['transactions']
	# last week alone
	cat_len = int(math.floor(len(transactions)*0.25))
	print cat_len
	cat_list = [transactions[:cat_len], transactions[cat_len:cat_len*2], transactions[cat_len*2:cat_len*3], transactions[cat_len*3:]]
	amount_list = list()
	catname_list = ['Food and Drinks', 'Travel', 'Electronics', 'Clothes and Shoes']
	for transactions in cat_list:
		amount = 0
		for trans in transactions:
			if trans['transaction-time'][:7] == '2015-03' and trans['amount'] < 0:
				amount += trans['amount']
		amount_list.append(-amount)
	cat_spends = dict()
	for i in range(len(catname_list)):
		cat_spends[catname_list[i]] = cat_spends.get(catname_list[i],0) + amount_list[i]
	return cat_spends

# print _transactions()

ACTS = '{ "accounts": [ { "account-id": "nonce:42069000-96459775", "legacy-institution-id": 42069000, "institution-name": "NYBE (Not Your Bank Either)", "active": true, "account-name": "Really Swell Checking", "balance": 100000000, "account-type": "asset", "last-digits": "9645" } ], "error": "no-error" }'

def _accounts():
	accounts = json.loads(ACTS)['accounts']
	act_dict = dict()
	for ac in accounts:
		if ac['active'] == True:
			act_dict[ac['account-id']] = act_dict.get(ac['account-id'],dict())
			l_ac = dict()
			l_ac['name'] = ac['account-name']
			l_ac['balance'] = ac['balance']
			l_ac['type'] = ac['account-type']
			act_dict[ac['account-id']] = l_ac
	return act_dict

print _ac