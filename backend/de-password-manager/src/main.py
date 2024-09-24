from password_manager import make_secret, list_secrets, get_secret, delete_secret


def main():
    exited = False
    while not exited:
        command = input(
            "Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: "
        )
        match command:
            case "e":
                name = input("Secret identifier: ")
                user_id = input("UserId: ")
                password = input("Password: ")
                print(make_secret(name, user_id, password))
            case "r":
                name = input("")
                print(get_secret(name))
            case "d":
                name = input("Specify secret to delete:")
                print(delete_secret(name))
            case "l":
                secrets = list_secrets()
                print(f"{len(secrets)} secret(s) available")
                for secret in secrets:
                    print(secret)
            case "x":
                exited = True
                print("Thank you. Goodbye")
            case _:
                print('Invalid command')



if __name__ == "__main__":
    main()
