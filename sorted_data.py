from sys import argv

def main():

    # assign command line arguments
    script, filename = argv

    # open file
    file_handle = open(filename)

    # create empty dictionary
    ratings_dict = {}

    # reading file line by line, splitting on ':' and stripping newline, and putting restaurant
    # and rating pair in a dictionary. 
    for line in file_handle:
        pair = line.split(":")
        restaurant = pair[0]
        rating = int(pair[1].strip("\n"))
        ratings_dict[restaurant] = rating

    # printing by sorted restaurant name
    for restaurant in sorted(ratings_dict.keys()):
        print "Restaurant %r is rated at %d." % (restaurant, ratings_dict[restaurant])

    # close file
    file_handle.close()


main()