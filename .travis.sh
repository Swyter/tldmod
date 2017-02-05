# swy: as seen here <https://github.com/travis-ci/travis-ci/issues/2285> but made prettier with custom wrappers
_fold_start_() { echo -en "travis_fold:start:script.$(( ++fold_count ))\\r" && echo -ne '\033[1;33m' && echo $1 && echo -ne '\e[0m'; }
_fold_final_() { echo -en "travis_fold:end:script.$fold_count\\r"; }

echo HI THERE! && SVNREV=$(git rev-list --count HEAD)

WORKSHOP_DESC="$(git log -1 --pretty=%B)"
echo "$WORKSHOP_DESC"
echo "----"

cd ModuleSystem

_fold_start_ "[Compiling retail revision $SVNREV]"
    curl https://ccrma.stanford.edu/~craig/utility/flip/flip.cpp -O -J && sudo g++ flip.cpp -o /usr/bin/flip

    # disable cheat mode for the generated nightly builds...
    sed -i 's/cheat_switch = 1/cheat_switch = 0/' module_constants.py

    # add a placeholder 'title' program to avoid log spam...
    sudo sh -c 'echo "#/usr/bin/bash" > /usr/bin/title && chmod +x /usr/bin/title'

    ./build_module.sh
    ./build_module_wb.sh

_fold_final_

cd ..

_fold_start_ "[Packaging and stripping revision $SVNREV into a Steam Workshop build]"
    # override the M&B 1.011 files with the Warband counterparts
    cp -rf ./_wb/* ./
    rm -rf _wb

    # fixed Linux case-sensitive language files detection
    mv Languages languages

    # paste the original optimized warband glsl shaders in GLShadersOptimized
    curl https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/vanilla_glsl_opt.zip -L -O
    unzip vanilla_glsl_opt.zip -d ./ && rm vanilla_glsl_opt.zip

    # move our custom tld shaders into their rightful place
    mv GLShaders/*.glsl GLShadersOptimized/

    # strip it accordingly
    rm -rf ./Data

    rm -f  ./languages/*
    rm -rf ./languages/.tx
    rm -rf ./languages/_base
    rm -rf ./languages/_base_new_language
    rm -rf ./languages/_*

    rm -rf ./ModuleSystem

    rm -f  ./Music/Readme.txt
    rm -rf ./Music/LowQualityTLDSoundtrack

    rm -rf ./Resource/_*

    rm -f  ./SceneObj/*.exe
    rm -rf ./SceneObj/_*

    rm -rf ./Sounds/_*
    rm -f  ./Sounds/Readme.txt

    rm -rf ./Textures/_*
    rm -rf ./Textures/Merl\'s\ old\ original\ textures
    rm -f  ./Textures/*.xcf
    rm -f  ./Textures/*.psd
    rm -f  ./Textures/*.jpg
    rm -f  ./Textures/*.png
    rm -f  ./Textures/Readme.txt


    rm -f  ./*.bat
    rm -f  ./*.cmd
    rm -f  ./*.exe
    rm -f  ./*.dll
    rm -f  ./*.h
    rm -f  ./*src*
    rm -f  ./*.odt
    rm -f  ./*.psd
    rm -f  ./*.zip
    rm -f  ./*.rar
    rm -f  ./.*
    rm -f  ./*.yml
    rm -f  ./*.cdd
    rm -f  ./*.lua
    rm -f  ./*.htm
    rm -f  ./*.nsi
    rm -f  ./module-wb.ini
    rm -f  ./game_variables-wb.txt
    rm -f  ./*orc*

    rm -rf ./_*

    rm -rf .git

_fold_final_


_fold_start_ '[Final tree view]'
    ls -lash
    #tree .

_fold_final_


_fold_start_ '[Initializing Steamworks service]'
    Xvfb :1 -screen 0 800x600x16 &
    export DISPLAY=:1

    cd .. && mkdir steam && chmod 777 steam && cd steam
    curl -LOJ https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/Steam.exe
    curl -LOJ "$STEAM_SS"

    ls -lash
    
    echo "$PATH"

    killall -I Xvfb
    exit 0

    # initialize the Wine environment and disable the sound driver output (travis-ci doesn't have any dummy ALSA devices)
    WINEDLLOVERRIDES="mscoree,mshtml=" wineboot -u && winetricks sound=disabled
    WINEDEBUG=-all wine steam -silent -forceservice -no-browser -no-cef-sandbox -opengl -login "$STEAM_AC" "`openssl base64 -d <<< "$STEAM_TK"`" &

    ((t = 290)); while ((t > 0)); do
        grep 'RecvMsgClientLogOnResponse()' logs/connection_log.txt | grep 'OK'                   && echo '>> OK'                   && break;
        grep 'RecvMsgClientLogOnResponse()' logs/connection_log.txt | grep 'Invalid Password'     && echo '>> Invalid Password'     && exit 1;
        grep 'RecvMsgClientLogOnResponse()' logs/connection_log.txt | grep 'Account Logon Denied' && echo '>> Account Logon Denied' && exit 1;

        if ((t == 1)); then
            curl -LOJ https://raw.githubusercontent.com/tremby/imgur.sh/master/imgur.sh && chmod +x ./imgur.sh
            
            ls -lash && scrot screenshot.png && ls -lash;
            ./imgur.sh screenshot.png;
            
            ls -lash
            
            exit 1;
        fi;

        sleep 1;
        echo $t;
        ((t--));
    done

_fold_final_


_fold_start_ '[Uploading Steam Workshop build]'
    cd .. && mv tldmod 'The Last Days of the Third Age'

    curl -L -O https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/mbw_workshop_uploader_glsl.exe
    curl -L -O https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/steam_api.dll
    curl -L -O https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/tldmod.ini
    curl -L -O https://github.com/tldmod/tldmod/releases/download/TLD3.3REL/tldmod.png

    echo 48700 > steam_appid.txt
    yes NO | env WINEDEBUG=-all wine mbw_workshop_uploader_glsl.exe update -mod tldmod.ini -id 742666341 -icon tldmod.png -changes "$WORKSHOP_DESC"
    sleep 10 && killall -I steam.exe

_fold_final_
