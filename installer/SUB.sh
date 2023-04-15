#!/bin/bash

## Colors (FG & BG)
RED="$(printf '\033[31m')"
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"
CYAN="$(printf '\033[36m')"
WHITE="$(printf '\033[37m')"
BLACK="$(printf '\033[30m')"
RED_BG="$(printf '\033[41m')"
GREEN_BG="$(printf '\033[42m')"
ORANGE_BG="$(printf '\033[43m')"
BLUE_BG="$(printf '\033[44m')"
MAGENTA_BG="$(printf '\033[45m')"
CYAN_BG="$(printf '\033[46m')"
WHITE_BG="$(printf '\033[47m')"
BLACK_BG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"
DEFAULT_BG="$(printf '\033[49m')"



function help {
    clear
    echo "
    [-h] - help (Это окно)
    [-i] - install (Окно установки)
    [-u] - update (Окно обновления)
    [-d] - delete (Окно удаления)"
    { echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
}

function install {
    clear
    sleep 1
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install."
    sleep 0.1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install.."
    sleep 0.1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install..."
    sleep 0.1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install."
    sleep 0.1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install.."
    sleep 0.1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Install..."
    sleep 0.1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Upgrating ${MAGENTA}apt${CYAN} and ${MAGENTA}pkg.."; echo; echo; }
        apt upgrade -y
        pkg upgrade -y
    sleep 1
    clear    
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Updating ${MAGENTA}apt${CYAN} and ${MAGENTA}pkg.."; echo; echo; }
        pkg update -y
        apt update -y
    sleep 1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Installing ${BLUE}pyt${ORANGE}hon.."; echo; echo; }
        pkg install python -y
    sleep 1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Installing ${MAGENTA}git..${CYAN}"; echo; echo; }
        pkg install git -y
    sleep 1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Downloading ${MAGENTA}resource for ${BLUE}Swee${CYAN}User${MAGENTA}Bot${CYAN}.."; echo; echo; }    
        git clone https://github.com/AT0M1CX/SweeUserBot/
    sleep 1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Installing ${MAGENTA}requirements${CYAN}.."; echo; echo; }
        pip install -r SweeUserBot/requirements.txt
        pkg install libjpeg-turbo -y
        LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators
        pip install simpledemotivators
    sleep 1
    clear
    { echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Installing ${GREEN}Successfully ✅${CYAN}"; echo; echo; }
    echo "1" > SweeUserBot/installed.txt
    { echo; echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; } 
}



delete_yes () {
    clear
    rm -rf SweeUserBot/
    echo "0" > SweeUserBot/installed.txt
    echo delete.
    sleep 0.1
    clear
    echo delete..
    sleep 0.1
    clear
    echo delete...
    sleep 0.1
    clear
    echo delete.
    sleep 0.1
    clear
    echo delete..
    sleep 0.1
    clear
    echo delete...
    sleep 0.1
    clear
    echo delete.
    sleep 0.1
    clear
    echo delete..
    sleep 0.1
    clear
    echo delete...
    sleep 0.1
    clear
    echo delete.
    sleep 0.1
    clear
    echo delete..
    sleep 0.1
    clear
    echo delete...
    sleep 0.1
    clear
    echo delete.
    sleep 0.1
    clear
    echo delete..
    sleep 0.1
    clear
    echo delete...
    sleep 0.1
    clear
    exit 
}

function delete {
    until [[ "$REPLY" =~ ^[2/N/n]$ ]]; do
    clear
    { read -p "${CYAN}Are you sure you want to delete? ${MAGENTA}[${GREEN}Y${MAGENTA}/${RED}n${MAGENTA}]${ORANGE}: ${WHITE}"; echo; }
    if [[ "$REPLY" =~ ^[1/Y/y/2/N/n]$ ]]; then      #validate input
        if [[ "$REPLY" =~ ^[1/Y/y]$ ]]; then
            delete_yes
        fi
    else
        echo -n "${ORANGE}[${RED}!${ORANGE}]${RED} Invalid option, ${MAGENTA}please try again."
        sleep 1.3
    fi
done 
    exit; }

function upgrade {
    clear
    path=`pwd`
    mv SweeUserBot/session.txt $path
    rm -rf SweeUserBot/
    git clone https://github.com/AT0M1CX/SweeUserBot
    rm -rf SweeUserBot/session.txt
    mv session.txt SweeUserBot/
    echo "upgrade."
    sleep 0.1
    clear
    echo "upgrade.."
    sleep 0.1
    clear
    echo "upgrade..."
    sleep 0.1
    clear
    echo "upgrade."
    sleep 0.1
    clear
    echo "upgrade.."
    sleep 0.1
    clear
    echo "upgrade..."
    sleep 0.1
    clear
    echo "upgrade."
    sleep 0.1
    clear
    echo "upgrade.."
    sleep 0.1
    clear
    echo "upgrade..."
    sleep 0.1
    clear
    echo "upgrade."
    sleep 0.1
    clear
    echo "upgrade.."
    sleep 0.1
    clear
    echo "upgrade..."
    sleep 0.1
    clear
    echo "upgrade."
    sleep 0.1
    clear
    echo "upgrade.."
    sleep 0.1
    clear
    echo "upgrade..."
    sleep 0.1
    clear
    whats_new=`cat SweeUserBot/whats_new.txt`
    echo $whats_new

    { echo; echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
}

textsesion () {
    echo "$ORANGE   ░██████╗███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
   ██╔════╝██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║
   ╚█████╗░█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║
   ░╚═══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║
   ██████╔╝███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║
   ╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝"
}


textswitch () {
    echo "$BLUE        ░██████╗░██╗░░░░░░░██╗██╗░█████╗░██╗░░██╗
        ██╔════╝░██║░░██╗░░██║██║██╔══██╗██║░░██║
        ╚█████╗░░╚██╗████╗██╔╝██║██║░░╚═╝███████║
        ░╚═══██╗░░████╔═████║░██║██║░░██╗██╔══██║
        ██████╔╝░░╚██╔╝░╚██╔╝░██║╚█████╔╝██║░░██║
        ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"
}

banner () {
    clear
    echo "
              $BLUE░██████╗░██╗░░░░░░░██╗███████╗███████╗
              ██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝
              ╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░
              ░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░
              ██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗
              ╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝$ORANGE
    ██╗░░░██╗░██████╗███████╗██████╗░██████╗░░█████╗░████████╗
    ██║░░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
    ██║░░░██║╚█████╗░█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
    ██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
    ╚██████╔╝██████╔╝███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
    ░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░$WHITE"
}


start () {
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN} Loading data.."
    sleep 0.5
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN} Loading user data..."
    sleep 1
    clear
    session=`cat SweeUserBot/session.txt`
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN} Login to the session: ${MAGENTA}$session${CYAN}..."
    sleep 1
    clear
    echo "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN} Successfully!$WHITE"
    sleep 0.5
    python SweeUserBot/SUB.py
    exit
    
}

import () {
    clear
    until [[ "$REPLY" =~ ^[6/six]$ ]]; do
    sleep 0.01
    clear
    textswitch
    textsesion
    sleep 0.3
    session=`cat SweeUserBot/session.txt`
    echo " "
    echo "    ${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Selected session${ORANGE}: ${MAGENTA}$session${GREEN}"
    sleep 0.1
    echo " "
    echo "    ${BLUE}[${MAGENTA}1${BLUE}] ${GREEN}${CYAN}SUB ${ORANGE}- ${MAGENTA}Main session"
    sleep 0.1
    echo "    ${BLUE}[${MAGENTA}2${BLUE}] ${GREEN}${CYAN}Session_2 ${ORANGE}- ${MAGENTA}2 Session"
    sleep 0.1
    echo "    ${BLUE}[${MAGENTA}3${BLUE}] ${GREEN}${CYAN}Session_3 ${ORANGE}- ${MAGENTA}3 Session"
    sleep 0.1
    echo "    ${BLUE}[${MAGENTA}4${BLUE}] ${GREEN}${CYAN}Session_4 ${ORANGE}- ${MAGENTA}4 Session"
    sleep 0.1
    echo "    ${BLUE}[${MAGENTA}5${BLUE}] ${GREEN}${CYAN}Session_5 ${ORANGE}- ${MAGENTA}5 Session"
    sleep 0.1
    echo " "
    echo "    ${BLUE}[${MAGENTA}6${BLUE}] ${RED}Back to main menu"
    echo " "
    sleep 0.1
    { read -p ${BLUE}"    [${CYAN}Choose an option${BLUE}]${ORANGE}: ${GREEN}"; echo; }

    if [[ "$REPLY" =~ ^[1/one/2/two/3/three/4/four/5/five/6/six]$ ]]; then      #validate input
        if [[ "$REPLY" =~ ^[1/one]$ ]]; then
            echo "1" > SweeUserBot/session.txt
            clear
            echo "Selected SUB session"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
        elif [[ "$REPLY" =~ ^[2/two]$ ]]; then
            echo "2" > SweeUserBot/session.txt
            clear
            echo "Selected 2 session"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
        elif [[ "$REPLY" =~ ^[3/three]$ ]]; then
            echo "3" > SweeUserBot/session.txt
            clear
            echo "Selected 3 session"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
        elif [[ "$REPLY" =~ ^[4/four]$ ]]; then
            echo "4" > SweeUserBot/session.txt
            clear
            echo "Selected 4 session"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
        elif [[ "$REPLY" =~ ^[5/five]$ ]]; then
            echo "5" > SweeUserBot/session.txt
            clear
            echo "    ${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Selected ${MAGENTA}5${CYAN} session"
            echo " "
            echo " "
            { echo; read -p "    ${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
        
        fi
    else
        echo -n "    ${ORANGE}[${RED}!${ORANGE}]${RED}Invalid option, ${MAGENTA}please try again."
        sleep 2
        fi
done
   mainmenu; }


about_program () {
    clear
    echo "${BLUE}    ░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝
    ███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░
    ██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░
    ██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░
    ╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░
 "
    sleep 0.1
    echo "${MAGENTA}>>  ${BLUE}S${CYAN}U${MAGENTA}B ${CYAN}full name ${BLUE}Swee${CYAN}User${MAGENTA}Bot${CYAN} is such"
    sleep 0.1
    echo "    app for ${GREEN_BG}${BLACK}Telegram ${DEFAULT_BG}${CYAN} that works"
    sleep 0.1
    echo "    using ${GREEN_BG}${BLACK}Telegram API${DEFAULT_BG}${CYAN} namely ${BLACK_BG}${BLUE}pyt${ORANGE}hon${DEFAULT_BG}${CYAN}"
    sleep 0.1
    echo "    libs ${GREEN_BG}${BLACK}Pyrogram${DEFAULT_BG}${CYAN} and has more than ${CYAN}"
    sleep 0.1
    echo "    50 ${CYAN} both fun and useful
    animations or functions."
    sleep 0.15
    echo " "
    sleep 0.15
    echo "${MAGENTA}>>  ${ORANGE}Author${BLUE}: ${MAGENTA}ATOMICX"
    sleep 0.1
    echo "${ORANGE}    Twitter${BLUE}: ${MAGENTA}Coming soon..."
    sleep 0.1
    echo "${ORANGE}    Github${BLUE}: ${MAGENTA}https://github.com/AT0M1CX/SweeUserBot"
    sleep 0.1
    echo "${ORANGE}    Reddit${BLUE}: ${MAGENTA}Coming soon..."
    sleep 0.1
    echo "${ORANGE}    Telegram${BLUE}: ${MAGENTA}https://t.me/ROmAanChiG"
    sleep 0.1
    echo "${ORANGE}    Telegram channel${BLUE}: ${MAGENTA}https://t.me/SweeSoft"
    sleep 0.1
    { echo; echo; read -p "    ${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
}

commands () {
    clear
    commands=`cat SweeUserBot/commands.txt` 
    echo "$commands"
    { echo; echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
}

comingsoon () {
    clear
    echo "${GREEN}    Comming Soon..."
    echo " "
    
    { echo; read -p "    ${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
}

mainmenu () {
    until [[ "$REPLY" =~ ^[none/None]$ ]]; do
    clear
    sleep 0.05
    banner
    sleep 0.1
    echo " "
    echo "    ${BLUE}[${MAGENTA}1${BLUE}] ${CYAN}Start"
    sleep 0.05
    echo "    ${BLUE}[${MAGENTA}2${BLUE}] ${CYAN}Commands"
    sleep 0.05
    echo "    ${BLUE}[${MAGENTA}3${BLUE}] ${CYAN}Coming soon..."
    sleep 0.05
    echo "    ${BLUE}[${MAGENTA}4${BLUE}] ${CYAN}Select session"
    sleep 0.05
    echo "    ${BLUE}[${MAGENTA}5${BLUE}] ${CYAN}About"
    sleep 0.05
    echo " "
    echo "    ${BLUE}[${MAGENTA}6${BLUE}] ${RED}Quit"
    echo " "
    sleep 0.1
    echo " "
    { read -p ${BLUE}"    [${MAGENTA}Select option${BLUE}]${ORANGE}: ${GREEN}"; echo; }

    if [[ "$REPLY" =~ ^[1/one/2/two/3/three/4/four/5/five/6/six]$ ]]; then      #validate input
        if [[ "$REPLY" =~ ^[1/one]$ ]]; then
            start
        elif [[ "$REPLY" =~ ^[2/two]$ ]]; then
            commands
        elif [[ "$REPLY" =~ ^[3/three]$ ]]; then
            comingsoon
        elif [[ "$REPLY" =~ ^[4/four]$ ]]; then
            import
        elif [[ "$REPLY" =~ ^[5/five]$ ]]; then
            about_program
        elif [[ "$REPLY" =~ ^[6/six]$ ]]; then
            clear
            exit
            
        fi
    else
        echo -n "    ${MAGENTA}[${RED}!${MAGENTA}] ${GREEN}Invalid option, please try again."
        sleep 2
    fi
done
}


if [ -n "$1" ] ; then
    case "$1" in
        -h) help
            ;;
        -i) install
            ;;
        -u) upgrade
            ;;
        -d) delete
            ;;
        *) echo "Invalid option: [$1] or no such parameter.
Existing options: -h, -i, -u, -d"
            ;;
    esac
else
    what_install=`cat SweeUserBot/installed.txt`
    echo $what_install
    sleep 1
   if [[ "$what_install" =~ ^[0]$ ]]; then
        clear
        echo "SUB is not installed
to install it, run the script with the [-i] argument"
    { echo; echo; read -p "${BLUE}[${MAGENTA}*${BLUE}] ${CYAN}Press ${GREEN_BG}${BLACK} Enter ${DEFAULT_BG}${CYAN} To return to the main menu."; }
    exit 
    else
        mainmenu
    fi
fi
