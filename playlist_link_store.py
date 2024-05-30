from colorama import Fore

file_links = open('playlist_links.txt', 'r')


def Meni() -> None:
    print("Here you can enter/delete your Spotify playlist links")
    print("Enter:")
    print("1-if you want to add link")
    print("2-if you want to remove link")
    print("3-if you want to see the list")
    print("Leave blank for program to shutdown")


def RefreshList() -> list:
    file_links_refresh = open('playlist_links.txt', 'r')
    track_list = file_links_refresh.read().split('\n')
    # print(track_list)
    for item in track_list:
        if(item == ''):
            track_list.remove(item)
    file_links_refresh.close()
    return track_list


def Colorlink(choice:int) -> int:
    for id_item, item in enumerate(final_track_list):
        index_to_remove = 1
        id_set = id_item + 1
        if(choice != id_set):
            print(f"{id_set},{item}")
        else:
            print(Fore.RED + f"{id_set}-{item}")
            print(Fore.RESET)
            index_to_remove = id_item
    return index_to_remove


def Removelink(track_list, index) -> None:
    del track_list[index]
    print("Link deleted")    

    with open('playlist_links.txt', 'w') as f:
        for idi, item in enumerate(final_track_list):
            # print(f"{idi + 1}-{item.split(',')}")
            f.write(item + "\n")

    


# valid_answers = [*range(1,4)]  # Unpacking operator '*' was used otherwise we would get an output like range(1,4)
# https://open.spotify.com/playlist/2myW2EQLU9T5h6s6hKvOid?si=e72ff2584e6045cb


final_track_list = RefreshList();
for item in final_track_list:
    if(item == ''):
        final_track_list.remove(item)
# print(final_track_list)
while True:
    Meni()
    user_ans = input() or "/"

    if user_ans == "1":
        print("Please enter name of the album:")
        album_name = input()
        print("Please enter a valid link:")
        valid_link = input()
        with open('playlist_links.txt', 'a') as file_add:
            file_add.write(f"{album_name},{valid_link}\n")
        print("Link added")
        print("-"*40)
        final_track_list = RefreshList();
        
    elif user_ans == "2":
        if len(final_track_list) != 0:
            for id_item, item in enumerate(final_track_list):
                print(f"{id_item + 1},{item}")
            print("Select which one to remove (default 1) please put in number")
            remove_choice = int(input())
            index = Colorlink(remove_choice)
            final_track_list = RefreshList()
            Removelink(final_track_list, index)
            final_track_list = RefreshList()
        else:
            print("Nothing added yet")
            print("-"*40)
    elif user_ans == "3":
        if len(final_track_list) == 0:
            print("Nothing added yet")
            print("-"*40)
        else:
            for id_item, item in enumerate(final_track_list):
                print(f"{id_item + 1}-{item}")
            print("-"*40)
                
    else:
         break

file_links.close()