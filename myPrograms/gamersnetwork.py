#/usr/bin/python

class GamersNetwork(object):
    
    def __init__(self,data_input):
        self.data_input = data_input

    def create_data_structure(self):
       
        '''{'john':
                {'connections' : ['bob', 'mary', 'smith'],
                 '      likes' : ['games of throne', 'angry bird']
                }
           } '''
        if not self.data_input:
            return {}
        individual_list = self.data_input.split('.')
        network = {}
        for individual in individual_list:
            
            personal_dict = {}
            if 'is connected to' in individual:
                name, _, connection = individual.split('is connected to')
                personal_dict['connections'] = connection.strip(',').strip()
                if name.strip() in network.keys():
                    network[name.strip()].update(personal_dict)
                else:
                    network[name.strip()] = personal_dict
            if 'likes to play' in  individual:
                name, _, like = individual.split('likes to play')
                personal_dict['likes'] = like.strip(',').strip()
                if name.strip() in network.keys():
                    network[name.strip()].update(personal_dict)
                else:
                    network[name.strip()] = personal_dict
        return network
                
    def get_connections(self, network, user):
        if user in network:
            try:
                return network[user]['connections']
            except KeyError:
                return []
        else:
            return None

    def get_games_liked(self, network,user):
        if user in network:
            try:
                return network[user]['likes']
            except KeyError:
                return []
        else:
            return None

    def add_connection(self, network, user_A, user_B):
        A_connection = get_connections(network,user_A)
        if A_connection:
            if not user_B in A_connection:
                network[user_A]['connections'].append[user_B]
            else:
                pass
        elif A_connection == []:
            network[user_A].update({'connections':user_B})
        else:
            network[user_A] = {'connections': user_B}
        return network

    def add_new_user(self, network,user,games):
        if user in network:
            return network
        else:
            network[user] = {'likes':games}
            return network

  
    def get_secondary_connections(self, network, user):
        if not user in network:
            return None
        elif not 'connections' in network[user]:
            return []
        else:
            secondary_list = []
            for each_person in network[user]['connections']:
                if get_connections(network,each_person):
                    secondary_list.extend(get_connections(network,each_person))
            return list(set(secondary_list))  #remove duplicate entries

    def count_common_connections(self, network, user_A, user_B):
        count = 0
        if user_A in network and user_B in network:
            userB_connections = get_connections(network, user_B)
            for each_person in get_connections(network,user_A):
                if each_person in userB_connections:
                    count += 1
        return count

    def find_path_to_friend(self, network, user_A, user_B):
        path_list = []
        if user_A in network and user_B in network:
            userA_connections = get_connections(network, user_A)
            if user_B in userA_connections:
                path_list.extend([user_A,user_B])
                return path_list
            else:
               path_list.append(user_A)
               for each_person in userA_connections:
                   find_path_to_friend(network, each_person, user_B)
        
        return path_list
           
