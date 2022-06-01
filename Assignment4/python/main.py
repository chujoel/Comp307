import utility as utility
import loader as loader
import numpy as np



def main():

    # Paths to the data and solution files.
    vrp_file = "n32-k5.vrp"  # "data/n80-k10.vrp"
    sol_file = "n32-k5.sol"  # "data/n80-k10.sol"

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)

    # Displaying to console the distance and visualizing the optimal VRP solution.
    vrp_best_sol = loader.load_solution(sol_file)
    best_distance = utility.calculate_total_distance(vrp_best_sol, px, py, depot)
    print("Best VRP Distance:", best_distance)
    utility.visualise_solution(vrp_best_sol, px, py, depot, "Optimal Solution")

    # Executing and visualizing the nearest neighbour VRP heuristic.
    # Uncomment it to do your assignment!

    nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!
    
    # sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    # sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    # print("Saving VRP Heuristic Distance:", sh_distance)
    # utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")

def get_distance_dict(nodes, px,py,currNode):
    distanceList = []
    for node in nodes:
        distanceList.append([node, utility.calculate_euclidean_distance(px,py,node,currNode)])

        

    return sorted(distanceList, key = lambda x: x[1])
     

def nearest_neighbour_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for the nearest neighbour heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Nearest Neighbour Heuristic to generate VRP solutions.
    tours = []
    
    remainingNodes = list(range(0,len(px)))
    remainingNodes.remove(depot)
    distanceList = []
    newRoute = True
    currNode = None
    
    currRoute = []
    currCapacity = 0
    while(len(remainingNodes)>0):
        foundNode = False
        if newRoute:
            currNode=depot
        distanceList = get_distance_dict(remainingNodes,px,py, currNode)
        print(distanceList)
        for distance in distanceList:
            if demand[distance[0]] + (currCapacity) <= (capacity):
                print(distance[0])
                newRoute=False
                currCapacity+=demand[distance[0]]
                currRoute.append(distance[0])
                remainingNodes.remove(distance[0])
                currNode = distance[0]
                foundNode = True
                break
        if len(remainingNodes)==0 or not foundNode:
            # Current route will end
            newRoute=True
            tours.append(currRoute)
            currRoute = []
            currCapacity=0
    return tours


def savings_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for Implementing the savings heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Saving Heuristic to generate VRP solutions.

    return None


if __name__ == '__main__':
    main()
