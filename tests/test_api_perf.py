import pytest
import json
import requests
import os

BASE_URL = os.getenv('BASE_URL', default='http://localhost:5000')
print("")
print("testing against", BASE_URL)

# Class to test performance of api.py
# We use pytest-benchmark to perform run many iterations of the request
# and benchmark the performance of the server.
class TestApiPerformance:

    # Benchmark api with simple hidden malicious request.
    def test_request_forbid_perf_benchmark(self, benchmark):
        url = f'{BASE_URL}/api/handle-request'
        headers = {'Content-Type': 'application/json'}

        payload = json.dumps({
            "hidden": {"is_malicious": True}
        })
        result = benchmark(requests.post, url, headers=headers, data=payload)

        assert result.status_code == 403

    # Benchmark api with large complex non-malicious request
    def test_massive_request_ok_perf_benchmark(self, benchmark):
        url = f'{BASE_URL}/api/handle-request'
        headers = {'Content-Type': 'application/json'}

        payload = json.dumps([
            {
                "_id": "5fcc06200a8ac0b3c0b6ac9d",
                "index": 0,
                "guid": "84f0aa98-b57a-4fe6-a98d-34c3fd7ccd10",
                "isActive": False,
                "balance": "$1,067.14",
                "picture": "http://placehold.it/32x32",
                "age": 30,
                "eyeColor": "blue",
                "name": "Annmarie Harding",
                "gender": "female",
                "company": "CUBIX",
                "email": "annmarieharding@cubix.com",
                "phone": "+1 (834) 518-3577",
                "address": "752 Ridgewood Avenue, Jugtown, Ohio, 3858",
                "about": "Exercitation reprehenderit laboris do ullamco qui eu dolor duis incididunt est anim qui. Et Lorem ut in dolor proident elit officia est tempor non ad proident aliqua. Ad sit anim commodo minim quis officia occaecat esse consequat veniam officia. Dolore ullamco aliquip laboris in consectetur mollit laboris eu dolor anim Lorem tempor ipsum.\r\n",
                "registered": "2015-06-26T04:49:40 +04:00",
                "latitude": -40.106472,
                "longitude": -105.380377,
                "tags": [
                    "tempor",
                    "incididunt",
                    "elit",
                    "tempor",
                    "excepteur",
                    "reprehenderit",
                    "sit"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Black Mcfarland"
                    },
                    {
                        "id": 1,
                        "name": "Robbins Dillard"
                    },
                    {
                        "id": 2,
                        "name": "Sheri Shannon"
                    }
                ],
                "greeting": "Hello, Annmarie Harding! You have 8 unread messages.",
                "favoriteFruit": "strawberry"
            },
            {
                "_id": "5fcc06200498f1cc4e8285ce",
                "index": 1,
                "guid": "ef8013cd-41ce-48cf-a595-21c2516b6ccd",
                "isActive": False,
                "balance": "$2,986.98",
                "picture": "http://placehold.it/32x32",
                "age": 22,
                "eyeColor": "green",
                "name": "Marisol Buckley",
                "gender": "female",
                "company": "SATIANCE",
                "email": "marisolbuckley@satiance.com",
                "phone": "+1 (882) 593-2669",
                "address": "194 Allen Avenue, Caron, Washington, 7958",
                "about": "Nostrud ipsum occaecat Lorem ad et Lorem minim eu laboris officia est dolore occaecat nisi. Eu deserunt do sit esse do proident fugiat officia ipsum magna. Eiusmod sit sint magna nostrud eu laboris laboris dolor irure nisi non magna.\r\n",
                "registered": "2019-04-09T10:49:16 +04:00",
                "latitude": -53.086747,
                "longitude": 116.750299,
                "tags": [
                    "quis",
                    "ipsum",
                    "exercitation",
                    "tempor",
                    "aliqua",
                    "sint",
                    "ex"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Laurel Lewis"
                    },
                    {
                        "id": 1,
                        "name": "Josefa Gilmore"
                    },
                    {
                        "id": 2,
                        "name": "Tessa Jarvis"
                    }
                ],
                "greeting": "Hello, Marisol Buckley! You have 7 unread messages.",
                "favoriteFruit": "apple"
            },
            {
                "_id": "5fcc06201e656e344eeb15a3",
                "index": 2,
                "guid": "5cc48193-8ac2-4a6c-8b82-3b7796aa3b0c",
                "isActive": True,
                "balance": "$3,385.76",
                "picture": "http://placehold.it/32x32",
                "age": 30,
                "eyeColor": "green",
                "name": "Britney Beard",
                "gender": "female",
                "company": "MAGNEATO",
                "email": "britneybeard@magneato.com",
                "phone": "+1 (832) 485-3617",
                "address": "435 Krier Place, Allensworth, North Carolina, 280",
                "about": "Nostrud amet enim nostrud magna anim est elit occaecat. Aute consectetur aliquip deserunt eiusmod occaecat eiusmod quis laborum culpa mollit nostrud. Elit esse et quis deserunt ex ea velit est dolore eu. Do voluptate dolore minim culpa sit. Cupidatat ipsum ullamco amet nisi dolore dolor aliquip ad irure Lorem velit. Dolore aliqua ipsum ea do fugiat cillum excepteur velit laborum in aliqua.\r\n",
                "registered": "2017-02-23T07:04:12 +05:00",
                "latitude": 54.280287,
                "longitude": 43.246228,
                "tags": [
                    "sunt",
                    "cupidatat",
                    "sint",
                    "nostrud",
                    "nostrud",
                    "ex",
                    "esse"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Ball Mills"
                    },
                    {
                        "id": 1,
                        "name": "Wilcox Johnston"
                    },
                    {
                        "id": 2,
                        "name": "Annette Delgado"
                    }
                ],
                "greeting": "Hello, Britney Beard! You have 3 unread messages.",
                "favoriteFruit": "banana"
            },
            {
                "_id": "5fcc0620a97891ddac2b04ea",
                "index": 3,
                "guid": "278eefae-4bb7-45af-bf9c-7a4e0ed96b22",
                "isActive": True,
                "balance": "$2,268.45",
                "picture": "http://placehold.it/32x32",
                "age": 26,
                "eyeColor": "blue",
                "name": "Bethany Lamb",
                "gender": "female",
                "company": "PREMIANT",
                "email": "bethanylamb@premiant.com",
                "phone": "+1 (829) 486-3982",
                "address": "252 Clarendon Road, Brenton, Texas, 7201",
                "about": "Anim irure adipisicing incididunt ad nostrud reprehenderit commodo cupidatat et. Incididunt est ad est laborum magna exercitation consequat magna. Cillum do irure dolor tempor ullamco. Ex eiusmod id eu esse cillum adipisicing mollit in non consectetur consectetur est do. Eu duis nulla ut proident velit magna aute reprehenderit laboris aliqua.\r\n",
                "registered": "2018-07-23T01:31:59 +04:00",
                "latitude": 36.928806,
                "longitude": -39.566768,
                "tags": [
                    "fugiat",
                    "sint",
                    "quis",
                    "minim",
                    "adipisicing",
                    "duis",
                    "pariatur"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Oliver White"
                    },
                    {
                        "id": 1,
                        "name": "Josephine Perry"
                    },
                    {
                        "id": 2,
                        "name": "Michele Lynch"
                    }
                ],
                "greeting": "Hello, Bethany Lamb! You have 4 unread messages.",
                "favoriteFruit": "strawberry"
            },
            {
                "_id": "5fcc062059331c2c0d89f2d0",
                "index": 4,
                "guid": "f9c4ad46-70be-42de-b95d-9c2de4b18ae0",
                "isActive": False,
                "balance": "$2,384.86",
                "picture": "http://placehold.it/32x32",
                "age": 22,
                "eyeColor": "green",
                "name": "Zimmerman Vaughan",
                "gender": "male",
                "company": "CORPULSE",
                "email": "zimmermanvaughan@corpulse.com",
                "phone": "+1 (800) 424-3750",
                "address": "511 Jackson Place, Coinjock, Nevada, 6982",
                "about": "Mollit dolore ex adipisicing exercitation pariatur proident ut culpa commodo velit laboris sunt aute laborum. Occaecat ea ullamco Lorem reprehenderit. Nostrud ea fugiat cillum incididunt eiusmod Lorem labore incididunt elit. Pariatur aliqua nisi Lorem veniam duis sit.\r\n",
                "registered": "2016-08-26T10:58:42 +04:00",
                "latitude": -5.540977,
                "longitude": 114.950457,
                "tags": [
                    "sit",
                    "incididunt",
                    "cillum",
                    "irure",
                    "qui",
                    "adipisicing",
                    "labore"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Bell Chen"
                    },
                    {
                        "id": 1,
                        "name": "Carole Merrill"
                    },
                    {
                        "id": 2,
                        "name": "Becky Gay"
                    }
                ],
                "greeting": "Hello, Zimmerman Vaughan! You have 6 unread messages.",
                "favoriteFruit": "strawberry"
            },
            {
                "_id": "5fcc06208641ccda454f2d13",
                "index": 5,
                "guid": "d4d02354-66e9-4b5b-8b03-de4b073889d1",
                "isActive": True,
                "balance": "$3,800.48",
                "picture": "http://placehold.it/32x32",
                "age": 35,
                "eyeColor": "brown",
                "name": "Wooten Terry",
                "gender": "male",
                "company": "NIQUENT",
                "email": "wootenterry@niquent.com",
                "phone": "+1 (886) 533-3831",
                "address": "573 Clara Street, Veyo, Maine, 9768",
                "about": "Ex id esse elit veniam. Lorem exercitation dolor aliqua cillum tempor. Consequat ullamco est anim non labore. Deserunt in enim occaecat ipsum amet.\r\n",
                "registered": "2019-10-31T03:50:02 +04:00",
                "latitude": 57.392065,
                "longitude": 87.644665,
                "tags": [
                    "esse",
                    "sunt",
                    "tempor",
                    "eu",
                    "ea",
                    "ut",
                    "esse"
                ],
                "friends": [
                    {
                        "id": 0,
                        "name": "Erica Ashley"
                    },
                    {
                        "id": 1,
                        "name": "Elinor Washington"
                    },
                    {
                        "id": 2,
                        "name": "Potts Osborn"
                    }
                ],
                "greeting": "Hello, Wooten Terry! You have 9 unread messages.",
                "favoriteFruit": "apple"
            }
        ])

        result = benchmark(requests.post, url, headers=headers, data=payload)

        assert result.status_code == 200


# Result of running ./bin/test:
# ------------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------------
# Name (time in ms)                             Min                 Max              Mean             StdDev            Median               IQR            Outliers       OPS            Rounds  Iterations
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_request_forbid_perf_benchmark         4.1670 (1.0)       13.7188 (1.0)      4.8911 (1.0)       0.8765 (1.0)      4.7168 (1.0)      0.5644 (1.0)           8;6  204.4529 (1.0)         178           1
# test_massive_request_ok_perf_benchmark     4.4013 (1.06)     722.1281 (52.64)    9.6356 (1.97)     54.4919 (62.17)    5.3320 (1.13)     0.8068 (1.43)         1;11  103.7816 (0.51)        173           1
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
