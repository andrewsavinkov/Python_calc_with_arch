import view
import model


def start():
    choice=''
    
    while choice !=2:
        choice = view.welcome_menu()
        print(choice)
        match choice:
            case 1:
                exmpl=view.user_input()
                answer=model.operating_func(exmpl)
                view.show_result(answer)
            case 2:
                pass
            
            case _:
                pass