def minimumPlatform(n,arr,dep):
        
        trains = []
        
        # Initially at least one platform is required
        trains.append(dep[0])
        platform = 1


        for i in range(1, n):

            isPlatformPresent = False

            # checking that if any platform is empty 
            for j in range(len(trains)):
                # if empty platform is found
                if trains[j] < arr[i]:
                    # Changing the train in that platform
                    trains[j] = dep[i]
                    isPlatformPresent = True
                    break
                    
            # If There is not empty Platform then adding one more platform
            if not isPlatformPresent:
                platform += 1
                trains.append(dep[i])

        return platform

if __name__ == '__main__':

    arrival = [900, 1100, 1235]
    departure = [1000, 1200, 1240]

    n = len(arrival)

    platforms = minimumPlatform(n, arrival, departure)

    print("Minimum Platform Needed Are ", platforms)

