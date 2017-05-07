# swy: as seen here <https://github.com/travis-ci/travis-ci/issues/2285> but made prettier with custom wrappers
_fold_start_() { echo -en "travis_fold:start:script.$(( ++fold_count ))\\r" && echo -ne '\033[1;33m' && echo $1 && echo -ne '\e[0m'; }
_fold_final_() { echo -en "travis_fold:end:script.$fold_count\\r"; }

echo HI THERE!

# grab the revision count of the latest merge commit,
# parse the changelog page to find the previous one
SVNREV=$(curl -s https://api.bitbucket.org/2.0/repositories/Swyter/tld-downloads/downloads | \
         sed -s 's/ /\n/g' | sed -n 's/.*_r\([0-9]*\)\.7z.*/\1/p' | head -1)

PREREV=$(curl -s http://steamcommunity.com/sharedfiles/filedetails/changelog/299974223 | \
         sed -n 's/^.*Equivalent to nightly r\([0-9]*\).*$/\1/p' | head -1)


# prefix the new changelog with the standard introduction and
# make the bullet points and em-dashes pretty
echo -e "Submitted a new build. Equivalent to nightly r$SVNREV.\r\n\r\n\
Main changes since the previous r$PREREV build are:\r\n\
`git log -1 --pretty=%B`" > /tmp/desc.txt

WORKSHOP_DESC="`cat '/tmp/desc.txt'`"

echo "$WORKSHOP_DESC"
echo "----"

cd ModuleSystem

_fold_start_ "[Compiling retail revision $SVNREV]"
    # disable cheat mode for the generated nightly builds...
    sed -i 's/cheat_switch = 1/cheat_switch = 0/' module_constants.py

    ./build_module.sh     2> /dev/null
    ./build_module_wb.sh  2> /dev/null

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
   #rm -rf ./Data
    rm -f  ./Data/*.py
    rm -f  ./Data/*.log
    rm -f  ./Data/*.exe
    rm -f  ./Data/*.bik
    rm -f  ./Data/*.fxo
    rm -f  ./Data/*.bat
    rm -f  ./Data/*_old.xml
    rm -f  ./Data/*.xml.weapons_lay_down

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
    rm -rf ./_*.txt
   #rm -rf ./_*

    rm -rf .git
    
    # add a watermark to make it clear that this is not the official build
    convert main.bmp -gravity center -pointsize 30 -fill red -stroke darkred -annotate -10 '(TEST THINGIE)' -type truecolor main.bmp

_fold_final_


_fold_start_ '[Final tree view]'
    ls -lash
    #tree .

_fold_final_


_fold_start_ '[Deploying Steam Workshop build]'

    CONT_FLDR='The Last Days of the Third Age (TEST THINGIE)'

    cd .. && mv tldmod "$CONT_FLDR"

    echo ' "workshopitem"                   '   > workshop_entry.vdf
    echo ' {                                '  >> workshop_entry.vdf
    echo '    "appid"               "48700" '  >> workshop_entry.vdf
    echo '    "publishedfileid" "742606214" '  >> workshop_entry.vdf
    echo "    'contentfolder'  '$CONT_FLDR' "  >> workshop_entry.vdf
    echo "    'changenote' '--------------' "  >> workshop_entry.vdf
    echo ' }                                '  >> workshop_entry.vdf

    curl -LOJs 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' && tar xvf steamcmd_linux.tar.gz

    # do the actual submission using this (totally stable) work of art
    ./steamcmd.sh +login "$steam_ac" "$steam_tk" +workshop_build_item workshop_entry.vdf +quit | tee workshop.log

    # fail the build if things didn't go as expected
    grep --no-messages 'Success.' workshop.log || exit 1;

_fold_final_
