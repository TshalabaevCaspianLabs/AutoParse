import requests
from loguru import logger



class ManheimDataCar:

    def __init__(self, id_user, car_name):
        self.id = id_user
        self.car = car_name

    def get_token_txt(self):
        data = []
        with open('MANHEIM/auth_data.txt', 'r') as file:
            for info in file:
                info = info.strip()
                auth_token, bearer_token = info.split(':')
                data.append([auth_token, bearer_token])

        return data


    def get_query_requests(self):
        try:
            auth_data = self.get_token_txt()
            headers = {
                'Content-Type': 'application/vnd.manheim.echov9+json',
                'Pragma': 'no-cache',
                'Accept': 'application/vnd.manheim.echov9+json',
                'Authorization': f'Bearer {auth_data[0][1]}',
                'Accept-Language': 'ru',
                'Cache-Control': 'no-cache',
                'Accept-Encoding': 'gzip, deflate, br',
                'Origin': 'https://members.manheim.com',
                'Content-Length': '186',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
                'Referer': 'https://members.manheim.com/members/results',
                'Connection': 'keep-alive',
                'Host': 'api.manheim.com',
                'x-source-env': 'production',
                'x-auth-tkt': f'{auth_data[0][0]}',
            }

            data = '{' \
                   '"statusIds":["00000000-0000-1000-0000-000000050083","00000000-0000-1000-0000-000000050084"],' \
                   '"keyword":"%s",' \
                   '"includeTestData":false,' \
                   '"contactGuid":"90fd7328-7ef0-e211-94b8-f04da208d950"}' % self.car

            response = requests.post('https://api.manheim.com/searches', headers=headers, data=data)
            url = response.text.split(',"href":"')[1].split('"}')[0]
            return url
        except:
            pass


    def manhaim(self):
        auth_data = self.get_token_txt()
        headers = {
            'Content-Type': 'application/vnd.manheim.echov9+json',
            'Pragma': 'no-cache',
            'Accept': 'application/vnd.manheim.echov9+json',
            'Authorization': f'Bearer {auth_data[0][1]}',
            'Accept-Language': 'ru',
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://members.manheim.com',
            'Content-Length': '2561',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Referer': 'https://members.manheim.com/members/results',
            'Connection': 'keep-alive',
            'Host': 'api.manheim.com',
            'x-source-env': 'production',
            'x-auth-tkt': f'{auth_data[0][0]}',
        }

        url = self.get_query_requests()
        searchId = url.split('id/')[1]
        data_request = '{"searchId":"%s","limit":250,"start":0,"sortOptions":"relevance:desc","includeAllListings":true,"includeAllFields":false,"includeNotes":true,"fields":["additionalAnnouncements","allowBids","allowBuyNow","allowPreviewBidding","allowTransportation","announcements","arbitrationRating","asIs","auctionEndTime","auctionId","auctionName","auctionStartTime","autocheck","autocheckCsHash","averageMMRValuation","bidCount","bidPrice","bidUrl","biddable","buyNowPrice","buyable","buyerGroupId","canTakeOffers","carfaxAccountNumber","carproofUrl","channelIds","channels","closedSale","comments","conditionGrade","conditionReportUrl","conditionType","conditionTypeIds","consignorId","currency","dealShieldAssurance","detailPageUrl","doorCount","doors","driveTrain","driveTrainIds","engineFuelType","engineFuelTypeIds","engineType","engineTypeIds","equipment","eventSaleId","eventSaleName","exteriorColor","exteriorColorIds","facilitationLocation","facilitationLocationIds","firstTimeListed","floorPriceMessage","foundInPowersearch","fyuse_uid","hasCarproof","hasFrameDamage","hasImages","hasPriorPaint","hasSellerDisclosure","id","interiorColor","interiorColorIds","interiorType","interiorTypeIds","inventorySource","inventorySourceIds","isAutoGradeOrManheimGrade","isCertified","isInfinite","laneNumber","listingQuality","mainImage","make","makeAnOffer","makeId","mmrPercentage","mmrPrice","mmrValuation","mid","modelIds","models","numVdpViews","numberOfAccidents","odometer","odometerCheckOK","odometerUnits","options","ownerCount","partnerWebsiteName","pickupLocation","pickupLocationState","pickupRegion","pickupRegionIds","portfolio","powersearchId","previouslyCanadianListing","priorPaint","promotions","remarks","runNumber","sale","saleChannelName","saleDate","saleIds","saleNumber","salesRating","salvageVehicle","sblu","sellerDisclosureGrade","sellerDisclosureUrl","sellerName","sellerNumber","sellerRating","sellerTypes","series","seriesId","sold","source","sourceMake","sourceModel","sourceSeries","sourceTrim","startNumberOfAccidents","startOwnerCount","statusIds","statuses","stopAutocheckScore","stopNumberOfAccidents","stopOwnerCount","titleAndProblemCheckOK","titleState","titleStatus","titleStatusIds","topTypeIds","totalSales","passengerCapacities","transmission","transmissionIds","trimIds","trims","unsoldRating","unifiedId","valuationsMmr","vehicleTypeIds","vehicleTypes","vehicleUseandEventCheckOK","vin","virtualLaneNumber","wsUrl","year","yearId"],"includeFilters":true,"includeFacets":true,"includeTestData":false}' % searchId
        response = requests.post(url, headers=headers, data=data_request)

        data = response.json()

        for i in range(250):
            try:

                vin_number = data['items'][i]['vin']
                vin_sourse = data['items'][i]['source']

                link = f'https://members.manheim.com/members/results#/details/{vin_number}/{vin_sourse}'
                image = data['items'][i]['mainImage']['largeUrl']
                mark_car = data['items'][i]['make']
                model = data['items'][i]['models'][0]
                sourse_model = data['items'][i]['sourceTrim']
                price = data['items'][i]['valuationsMmr']['adjustedValue']
                year = data['items'][i]['year']
                try:
                    with open(f'{self.id}.txt', 'a') as file:
                        file.write(f'{year} {mark_car} {model} {sourse_model}:{price}:{image}:{link}' + '\n')
                except:
                    with open(f'{self.id}.txt', 'w') as file:
                        file.write(f'{year} {mark_car} {model} {sourse_model}:{price}:{image}:{link}' + '\n')

                logger.debug('Car Accepted')
            except:
                pass


