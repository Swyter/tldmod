#OUTPUT module_items copy column to python
from module_constants import *
from header_items import  *
from header_operations import *
from header_triggers import *
from header_factions import *
from module_info import wb_compile_switch as is_a_wb_item
#
#
####################################################################################################################
### Each item record contains the following fields:
### 1) Item id: used for referencing items in other files.
###    The prefix itm_ is automatically added before each item id.
### 2) Item name. Name of item as it'll appear in inventory window
### 3) List of meshes.  Each mesh record is a tuple containing the following fields:
###   3.1) Mesh name.
###   3.2) Modifier bits that this mesh matches.
###    Note that the first mesh record is the default.
### 4) Item flags. See header_items.py for a list of available flags.
### 5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
### 6) Item value.
### 7) Item stats: Bitwise-or of various stats about the item such as:
###     weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
### 8) Modifier bits: Modifiers that can be applied to this item.
### 9)[Optional] Triggers: List of simple triggers to be associated with the item.
####################################################################################################################
#
###Some constants for ease of use.
### Kham - Unused imods for mesh hack
### Poor, Old, Cheap, Well_Made, Sharp, Deadly, Exquisite, Powerful, Rough, Robust, Tough, Trophy, Fresh, Day Old, Two-Day Old, Rotten

imodbits_none = 0
imodbits_polearm =        0#imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_sword   =         0#imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = 0#imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   =            0#imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_heavy
imodbits_mace   =         0#imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_heavy
imodbits_pick   =           0#imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_thrown   =       0#imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
#
imodbits_horse_basic = imodbit_swaybacked | imodbit_lame | imodbit_heavy | imodbit_stubborn | imodbit_timid | imodbit_thick
imodbits_horse_good = imodbit_spirited | imodbit_heavy | imodbit_thick | imodbit_reinforced | imodbit_champion | imodbit_lordly
imodbits_warg = imodbit_swaybacked | imodbit_lame | imodbit_heavy | imodbit_stubborn | imodbit_thick | imodbit_reinforced
#
imodbits_good   = 0#imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = 0#imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
#
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_orc_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_smelling
imodbits_elf_cloth  = imodbit_thick | imodbit_hardened | imodbit_reinforced
#
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced | imodbit_lordly
imodbits_orc_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced | imodbit_smelling | imod_meek 
imodbits_elf_armor  = imodbit_thick | imodbit_reinforced | imodbit_lordly
#
imodbits_missile  = imodbit_crude | imodbit_bent | imodbit_large_bag | imodbit_fine | imodbit_balanced
imodbits_good_missile  = imodbit_large_bag | imodbit_fine | imodbit_balanced
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_crude | imodbit_fine | imodbit_strong | imodbit_masterwork
imodbits_good_bow = imodbit_fine | imodbit_strong | imodbit_masterwork
#
imodbits_shield  = imodbit_cracked | imodbit_battered | imodbit_crude | imodbit_sturdy | imodbit_hardened | imodbit_thick | imodbit_reinforced
imodbits_shield_good = imodbit_thick | imodbit_hardened | imodbit_reinforced | imodbit_lordly
imodbits_weapon   = imodbit_rusty | imodbit_chipped | imodbit_crude | imodbit_fine | imodbit_heavy | imodbit_balanced |imodbit_tempered
imodbits_weapon_bad  = imodbit_cracked | imodbit_rusty | imodbit_chipped | imodbit_crude | imodbit_heavy | imodbit_balanced | imodbit_tempered
imodbits_weapon_good  = imodbit_fine | imodbit_balanced | imodbit_tempered | imodbit_masterwork
imodbits_weapon_wood   = imodbit_bent | imodbit_crude | imodbit_fine | imodbit_heavy | imodbit_balanced
#
items =[
###item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID_ITEM",[("invalid_item",0)],itp_type_goods,0,3,weight(1.5)|abundance(90)|0,imodbits_none],
["horse_meat","Horse_Meat",[("raw_meat",0)],itp_type_goods|itp_consumable|itp_food,0,12,weight(40)|abundance(0)|food_quality(30)|max_ammo(40),imodbits_none],
###Items before this point are hardwired and their order should not be changed!
["practice_sword","Practice_Sword",[("practice_sword",0)],itp_primary|itp_wooden_parry|itp_type_one_handed_wpn|itp_secondary|itp_wooden_attack,itc_longsword,1,weight(1.5)|difficulty(0)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(12,blunt),0],
#["arena_axe","Axe",[("arena_axe",0)],itp_primary|itp_wooden_parry|itp_type_one_handed_wpn|itp_secondary|itp_bonus_against_shield,itc_scimitar|itcf_carry_axe_left_hip,1,weight(1.5)|difficulty(0)|spd_rtng(100)|weapon_length(69)|swing_damage(23,blunt)|thrust_damage(0,blunt),0],
#["arena_sword","Sword",[("arena_sword_one_handed",0)],itp_primary|itp_wooden_parry|itp_type_one_handed_wpn,itc_longsword|itcf_carry_sword_left_hip,1,weight(1.5)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(21,blunt)|thrust_damage(17,blunt),0],
#["arena_sword_two_handed","Two_Handed_Sword",[("arena_sword_two_handed",0)],itp_primary|itp_wooden_parry|itp_type_two_handed_wpn|itp_two_handed,itc_greatsword|itcf_carry_sword_back,1,weight(2.75)|difficulty(0)|spd_rtng(93)|weapon_length(110)|swing_damage(29,blunt)|thrust_damage(21,blunt),0],
["arena_lance","Lance",[("arena_lance",0)],itp_primary|itp_wooden_parry|itp_type_polearm|itp_spear|itp_penalty_with_shield|itp_couchable,itc_staff|itcf_carry_spear, 1,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(25,blunt),0],
["practice_staff","Wooden_Staff",[("wooden_staff",0)],itp_primary|itp_wooden_parry|itp_type_polearm|itp_spear|itp_penalty_with_shield|itp_wooden_attack, itc_staff|itcf_carry_sword_back,1,weight(2.5)|difficulty(0)|spd_rtng(103)|weapon_length(118)|swing_damage(16,blunt)|thrust_damage(12,blunt),0],
["practice_bow","Practice_Bow",[("small_bow",0),("small_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_type_bow|itp_primary|itp_two_handed, itcf_shoot_bow|itcf_carry_bow_back,1,weight(1.5)|difficulty(0)|shoot_speed(40)|spd_rtng(90)|thrust_damage(19,blunt),0],
["wooden_javelin","Wooden_javelin",[("wooden_javelin",0)],itp_type_thrown|itp_primary|itp_bonus_against_shield, itcf_throw_javelin,100,weight(3)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(65)|thrust_damage(25,blunt)|max_ammo(5),imodbits_thrown],
#["practice_throwing_axe","Practice_Throwing_Axes",[("rohan_throwing_axe",0)],itp_type_thrown|itp_primary|itp_bonus_against_shield,itcf_throw_axe,100,weight(1.5)|difficulty(0)|shoot_speed(20)|spd_rtng(99)|weapon_length(30)|thrust_damage(25,blunt)|max_ammo(14),imodbits_thrown],
#
#foods (first one is smoked_fish)
["human_meat","Human_Flesh",[("human_flesh",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,103,weight(20)|abundance(50)|food_quality(80)|max_ammo(30),imodbits_none],
["maggoty_bread","Maggoty_Bread",[("maggoty_bread",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,32,weight(10)|abundance(100)|food_quality(50)|max_ammo(50),imodbits_none],
["cram","Cram_Ration",[("cram",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,44,weight(10)|abundance(100)|food_quality(50)|max_ammo(50),imodbits_none],
["lembas","Lembas",[("lembas",0)],itp_type_goods|itp_unique|itp_consumable,0,200,weight(1.3)|abundance(10)|food_quality(80)|max_ammo(100),imodbits_none],
["smoked_fish","Smoked_Fish",[("smoked_fish",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,59,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
["dried_meat","Dried_Meat",[("smoked_meat",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,72,weight(15)|abundance(100)|food_quality(60)|max_ammo(50),imodbits_none],
["cattle_meat","Beef",[("raw_meat",0)],itp_shop|itp_type_goods|itp_consumable|itp_food,0,103,weight(20)|abundance(100)|food_quality(70)|max_ammo(70),imodbits_none],
#other trade goods (first one is wine)
["grain","Wheat",[("wheat_sack",0)],itp_shop|itp_type_goods|itp_consumable,0,77,weight(50)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
["tools","Tools",[("iron_hammer",0)],itp_shop|itp_type_goods,0,410,weight(50)|abundance(90)|0,imodbits_none],
#************************************************************************************************
###ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************
###Quest Items
["siege_supply","Supplies",[("ale_barrel",0)],itp_type_goods,0,96,weight(40)|abundance(70)|0,imodbits_none],
["quest_wine","Wine",[("amphora_slim",0)],itp_type_goods,0,46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale",[("ale_barrel",0)],itp_type_goods,0,31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

["metal_scraps_bad","Low_grade_metal_scraps",[("weapon_scraps_a",0)],itp_type_goods,0,scrap_bad_value,weight(40)|abundance(0)|0,imodbits_none],
["metal_scraps_medium","Usable_metal_scraps",[("weapon_scraps_b",0)],itp_type_goods,0,scrap_medium_value,weight(40)|abundance(0)|0,imodbits_none],
["metal_scraps_good","Good_quality_metal_scraps",[("weapon_scraps_c",0)],itp_type_goods,0,scrap_good_value,weight(40)|abundance(0)|0,imodbits_none],
# 
###Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
###Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
# scraps_end in constants points here
["oliphant","Oliphaunt",[("oliphant",0)],itp_type_horse,0,1,hit_points(255)|body_armor(255)|difficulty(255)|horse_speed(1)|horse_maneuver(1)|horse_charge(500),imodbits_horse_basic|0],

["sumpter_horse","Sumpter_Horse",[("sumpter_horse",0)],itp_type_horse|itp_shop,0,50,hit_points(40)|body_armor(1)|difficulty(1)|horse_speed(28)|horse_maneuver(33)|horse_charge(5),imodbits_horse_basic|imodbits_horse_basic,[]],
["saddle_horse","Saddle_Horse",[("saddle_horse",0)],itp_type_horse|itp_shop,0,120,hit_points(60)|body_armor(7)|difficulty(1)|horse_speed(39)|horse_maneuver(34)|horse_charge(8),imodbits_horse_basic|imodbits_horse_basic,[]],
["steppe_horse","Steppe_Horse",[("steppe_horse",0)],itp_type_horse|itp_shop,0,120,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(35)|horse_maneuver(41)|horse_charge(7),imodbits_horse_basic|imodbits_horse_basic,[]],
["courser","Courser",[("courser",0)],itp_type_horse|itp_shop,0,400,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(43)|horse_maneuver(37)|horse_charge(11),imodbits_horse_basic|imodbits_horse_basic,[]],
["hunter","Hunter",[("hunting_horse",0)],itp_type_horse|itp_shop,0,500,hit_points(90)|body_armor(20)|difficulty(3)|horse_speed(36)|horse_maneuver(34)|horse_charge(18),imodbits_horse_basic|imodbits_horse_basic,[]],
["pony","Pony",[("pony",0)],itp_type_horse|itp_shop,0,300,hit_points(30)|body_armor(0)|difficulty(0)|horse_speed(20)|horse_maneuver(40)|horse_charge(1),imodbits_horse_basic|imodbits_horse_good,[]],
#ARNOR MOUNTS########
["arnor_warhorse","Arnorian_Warhorse",[("arnor_mail",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(52)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(30),imodbits_horse_basic|imodbits_horse_good,[]],
["dunedain_warhorse","Dunedain_Warhorse",[("arnor_leather",0)],itp_type_horse|itp_shop,0,3000,hit_points(140)|body_armor(65)|difficulty(4)|horse_speed(35)|horse_maneuver(32)|horse_charge(35),imodbits_horse_basic|imodbits_horse_good,[]],
##ROHAN MOUNTS#############
["rohirrim_courser","Rohirrim_Courser",[("rohan_horse01",0)],itp_type_horse|itp_shop,0,900,hit_points(90)|body_armor(10)|difficulty(2)|horse_speed(46)|horse_maneuver(40)|horse_charge(18),imodbits_horse_basic|imodbits_horse_basic,[]],
["rohirrim_hunter","Rohirrim_Hunter",[("rohan_horse02",0)],itp_type_horse|itp_shop,0,724,hit_points(110)|body_armor(18)|difficulty(3)|horse_speed(41)|horse_maneuver(38)|horse_charge(18),imodbits_horse_basic|imodbits_horse_basic,[]],
["rohirrim_courser2","Rohirrim_Courser",[("rohan_horse03",0)],itp_type_horse|itp_shop,0,900,hit_points(100)|body_armor(10)|difficulty(2)|horse_speed(46)|horse_maneuver(40)|horse_charge(18),imodbits_horse_basic|imodbits_horse_basic,[]],
["rohan_warhorse","Rohirrim_Warhorse",[("rohan_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(25),imodbits_horse_basic|imodbits_horse_good,[]],
["thengel_warhorse","Thengel_Guard_Warhorse",[("rohan_warhorse02",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(42)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(30),imodbits_horse_basic|imodbits_horse_good,[]],
["rhun_horse_a","Rhun_Horse",[("rhunhorselight1",0)],itp_type_horse|itp_shop,0,500,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(35)|horse_maneuver(39)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_b","Rhun_Horse",[("rhunhorselight2",0)],itp_type_horse|itp_shop,0,500,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(35)|horse_maneuver(39)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_d","Rhun_Horse",[("rhunhorselight4",0)],itp_type_horse|itp_shop,0,500,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(35)|horse_maneuver(39)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_e","Rhun_Heavy_Horse",[("rhunhorseheav1",0)],itp_type_horse|itp_shop,0,1500,hit_points(130)|body_armor(30)|difficulty(3)|horse_speed(35)|horse_maneuver(34)|horse_charge(25),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_f","Rhun_Heavy_Horse",[("rhunhorseheav2",0)],itp_type_horse|itp_shop,0,1500,hit_points(130)|body_armor(30)|difficulty(3)|horse_speed(35)|horse_maneuver(34)|horse_charge(25),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_g","Rhun_Heavy_Horse",[("rhunhorseheav3",0)],itp_type_horse|itp_shop,0,1500,hit_points(160)|body_armor(35)|difficulty(4)|horse_speed(34)|horse_maneuver(32)|horse_charge(25),imodbits_horse_basic|imodbits_horse_basic,[]],
["rhun_horse_h","Rhun_Heavy_Horse",[("rhunhorseheav4",0)],itp_type_horse|itp_shop,0,1500,hit_points(160)|body_armor(35)|difficulty(4)|horse_speed(34)|horse_maneuver(32)|horse_charge(25),imodbits_horse_basic|imodbits_horse_basic,[]],
["dale_horse","Dale_Horse",[("sumpter_horse",0)],itp_type_horse|itp_shop,0,724,hit_points(65)|body_armor(11)|difficulty(2)|horse_speed(37)|horse_maneuver(35)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["dale_warhorse","Dale_Warhorse",[("warhorse",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(35)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(23),imodbits_horse_basic|imodbits_horse_basic,[]],
["riv_warhorse","Rivendell Warhorse",[("rivendell_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(36)|horse_charge(30),imodbits_horse_basic|imodbits_horse_good,[]],
["riv_warhorse2","Imladris Steed",[("rivendell_warhorse02",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(36)|horse_charge(30),imodbits_horse_basic|imodbits_horse_good,[]],
["mordor_warhorse","Mordor_Warhorse",[("mordor_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(52)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(33),imodbits_horse_basic|imodbits_horse_basic,[]],
["mordor_warhorse2","Mordor_Sinister_Warhorse",[("mordor_warhorse02",0)],itp_type_horse|itp_unique,0,2000,hit_points(150)|body_armor(60)|difficulty(4)|horse_speed(35)|horse_maneuver(34)|horse_charge(40),imodbits_horse_basic|imodbits_horse_good,[]],
["gondor_courser","Gondor_Courser",[("gondor_horse02",0)],itp_type_horse|itp_shop,0,900,hit_points(80)|body_armor(16)|difficulty(2)|horse_speed(43)|horse_maneuver(37)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["gondor_hunter","Gondor_Hunter",[("gondor_horse01",0)],itp_type_horse|itp_shop,0,724,hit_points(100)|body_armor(21)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(18),imodbits_horse_basic|imodbits_horse_basic,[]],
["dol_amroth_warhorse","Dol_Amroth_Warhorse",[("da_warhorse02",0)],itp_type_horse|itp_shop,0,1500,hit_points(140)|body_armor(35)|difficulty(4)|horse_speed(35)|horse_maneuver(33)|horse_charge(30),imodbits_horse_basic|imodbits_horse_good,[]],
["dol_amroth_warhorse2","Dol_Amroth_Heavy_Warhorse",[("da_warhorse01",0)],itp_type_horse|itp_shop,0,2000,hit_points(140)|body_armor(35)|difficulty(4)|horse_speed(35)|horse_maneuver(33)|horse_charge(35),imodbits_horse_basic|imodbits_horse_good,[]],
["gondor_warhorse","Gondor_Warhorse",[("gondor_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(26),imodbits_horse_basic|imodbits_horse_basic,[]],
["gondor_lam_horse","Lamedon_Armored_Horse",[("lam_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(35)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(26),imodbits_horse_basic|imodbits_horse_basic,[]],
["lorien_warhorse","Lothlorien_Warhorse",[("loth_warhorse01",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(32),imodbits_horse_basic|imodbits_horse_good,[]],
["harad_horse","Harad_Horse",[("harad_horse01",0)],itp_type_horse|itp_shop,0,900,hit_points(80)|body_armor(10)|difficulty(2)|horse_speed(36)|horse_maneuver(34)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["harad_warhorse","Harad_Warhorse",[("harad_horse02",0)],itp_type_horse|itp_shop,0,1500,hit_points(135)|body_armor(40)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(23),imodbits_horse_basic|imodbits_horse_basic,[]],
#["camel","Far Harad Camel",[("camel",0)], itp_shop|itp_type_horse, 0, 92,abundance(80)|body_armor(15)|difficulty(2)|horse_speed(22)|horse_maneuver(32)|horse_charge(27),imodbits_horse_basic],
["variag_pony","Variag_Pony",[("horse_c",0)],itp_type_horse|itp_shop,0,900,hit_points(70)|body_armor(10)|difficulty(2)|horse_speed(36)|horse_maneuver(34)|horse_charge(10),imodbits_horse_basic|imodbits_horse_basic,[]],
["variag_kataphrakt","Easterling_Warhorse",[("easterling_warhorse01",0)],itp_type_horse|itp_shop,0,2000,hit_points(135)|body_armor(46)|difficulty(4)|horse_speed(36)|horse_maneuver(34)|horse_charge(35),imodbits_horse_basic|imodbits_horse_basic,[]],
#########WARGS#########

#first warg in list: warg_1b (see in module_constants)
["warg_1b","Warg",[("warg_1B",0)],itp_type_horse|itp_shop,0,600,hit_points(80)|body_armor(10)|difficulty(2)|horse_speed(33)|horse_maneuver(64)|horse_charge(45),imodbits_horse_basic|imodbits_warg,[]],
["warg_1c","Warg",[("warg_1C",0)],itp_type_horse|itp_shop,0,600,hit_points(80)|body_armor(10)|difficulty(2)|horse_speed(33)|horse_maneuver(64)|horse_charge(45),imodbits_horse_basic|imodbits_warg,[]],
["warg_1d","Warg",[("warg_1D",0)],itp_type_horse|itp_shop,0,600,hit_points(80)|body_armor(10)|difficulty(2)|horse_speed(33)|horse_maneuver(64)|horse_charge(45),imodbits_horse_basic|imodbits_warg,[]],
["wargarmored_1b","Armored_Warg",[("wargArmored_1B",0)],itp_type_horse|itp_shop,0,1200,hit_points(100)|body_armor(30)|difficulty(4)|horse_speed(30)|horse_maneuver(61)|horse_charge(50),imodbits_horse_basic|imodbits_warg,[]],
["wargarmored_1c","Armored_Warg",[("wargArmored_1C",0)],itp_type_horse|itp_shop,0,1200,hit_points(100)|body_armor(30)|difficulty(4)|horse_speed(30)|horse_maneuver(61)|horse_charge(50),imodbits_horse_basic|imodbits_warg,[]],
["wargarmored_2b","Armored_Warg",[("wargArmored_2B",0)],itp_type_horse|itp_shop,0,1200,hit_points(110)|body_armor(30)|difficulty(4)|horse_speed(30)|horse_maneuver(61)|horse_charge(50),imodbits_horse_basic|imodbits_warg,[]],
["wargarmored_2c","Armored_Warg",[("wargArmored_2C",0)],itp_type_horse|itp_shop,0,1200,hit_points(120)|body_armor(30)|difficulty(4)|horse_speed(30)|horse_maneuver(61)|horse_charge(50),imodbits_horse_basic|imodbits_warg,[]],
["wargarmored_3a","Armored_Warg",[("wargArmored_3A",0)],itp_type_horse|itp_shop,0,2500,hit_points(130)|body_armor(40)|difficulty(5)|horse_speed(29)|horse_maneuver(60)|horse_charge(55),imodbits_horse_basic|imodbits_warg,[]],
["warg_reward","Huge_Warg",[("wargArmored_huge",0)],itp_type_horse|itp_unique,0,3000,hit_points(180)|body_armor(45)|difficulty(5)|horse_speed(35)|horse_maneuver(62)|horse_charge(62),imodbits_horse_basic,[]],
#first non WARG item: troll_feet_boots (see in module_constants)

#TROLL "ITEMS"#########
["troll_feet_boots","Troll_Feet",[("troll_feet",0)],itp_no_pick_up_from_ground|itp_type_foot_armor|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(55)|leg_armor(55)|difficulty(70),0],
["troll_head_helm","Troll_Head",[("troll_head",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(40)|difficulty(70),0],
["troll_head_helm_b","Troll_Head",[("troll_head_b",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(40)|difficulty(70),0],
["troll_head_helm_c","Troll_Head",[("troll_head_c",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(40)|difficulty(70),0],
#
["tree_trunk_club_a","Tree_Trunk",[("troll_club",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(87)|weapon_length(186)|swing_damage(48,blunt)|thrust_damage(48,blunt),0],
["tree_trunk_club_b","Tree_Trunk",[("tree_trunk_club",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(92)|weapon_length(175)|swing_damage(48,blunt)|thrust_damage(48,blunt),0],
["tree_trunk_invis","Tree_Trunk",[("0",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(92)|weapon_length(175)|swing_damage(48,blunt)|thrust_damage(48,blunt),0],
["giant_hammer","Giant_Hammer",[("giant_hammer",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|0,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(96)|weapon_length(150)|swing_damage(80,blunt)|thrust_damage(65,blunt),0],
["giant_mace","Giant_Mace",[("giant_mace",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|0,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(96)|weapon_length(150)|swing_damage(90,blunt)|thrust_damage(65,blunt),0],
["giant_mace_b","Giant_Spiked_Mace",[("giant_mace_b",0)],itp_no_pick_up_from_ground|itp_type_one_handed_wpn|itp_primary|0,itc_big_weapon|0,1,weight(250)|difficulty(0)|spd_rtng(96)|weapon_length(150)|swing_damage(90,blunt)|thrust_damage(65,blunt),0],
#
["olog_feet_boots","Olog_Hai_Feet",[("olog_feet",0)],itp_no_pick_up_from_ground|itp_type_foot_armor|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(0)|leg_armor(62)|difficulty(70),0],
["olog_head_helm","Olog_Hai_Head",[("olog_head",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(62)|difficulty(70),0],
["olog_head_helm_b","Olog_Hai_Head",[("olog_head_b",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(62)|difficulty(70),0],
["olog_head_helm_c","Olog_Hai_Head",[("olog_head_c",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(62)|difficulty(70),0],
["olog_body","Olog_Hai_Armor",[("olog_body",0)],itp_no_pick_up_from_ground|itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(62)|leg_armor(0)|difficulty(70),0,],
["olog_body_b","Olog_Hai_Armor",[("olog_body_b",0)],itp_no_pick_up_from_ground|itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(62)|leg_armor(0)|difficulty(70),0,],
["olog_hands","Olog_Hai_Hands",[("olog_hand_L",0)],itp_no_pick_up_from_ground|itp_type_hand_armor|itp_unique,0,1,weight(250)|body_armor(1)|difficulty(70),0],
#
# warg ghost items...  (mtarini)
#  invisible items which are used for ghost riders (riding unmounted wargs)
["warg_ghost_armour","HIDEME_armour" ,[("0",0)],itp_unique|itp_no_pick_up_from_ground|itp_type_body_armor|itp_covers_head|itp_covers_legs,0,0,weight(0)|head_armor(200)|body_armor(200)|leg_armor(200)|difficulty(0),0],
["warg_ghost_lance" ,"HIDEME_lance"  ,[("0",0)],itp_unique|itp_no_pick_up_from_ground|itp_type_polearm|itp_primary|itp_no_parry,0,0,weight(1)|difficulty(0)|spd_rtng(100)|weapon_length(1)|thrust_damage(0,pierce),imodbits_none],
# CC: ghost lance had itcf_thrust_onehanded_lance_horseback before, changed to prevent animals from couching
# other HIDEME items already ingame

#BOW MISSILES
["arrows","Arrows",[("plain_arrow",0),("plain_arrow_flying",ixmesh_flying_ammo),("common_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,72,weight(3)|thrust_damage(1,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["gondor_arrows","Gondor_Arrows",[("gondor_arrow",0),("gondor_arrow_flying",ixmesh_flying_ammo),("gondor_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,100,weight(3)|thrust_damage(2,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["gondor_auxila_arrows","Gondorian_Arrows",[("gondor_arrow",0),("gondor_arrow_flying",ixmesh_flying_ammo),("gondor_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,100,weight(3)|thrust_damage(1,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["khergit_arrows","Barbed_Arrows",[("rohan_arrow2",0),("rohan_arrow2_flying",ixmesh_flying_ammo),("rohan_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,300,weight(3.5)|thrust_damage(2,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["rohan_arrows_2","Rohirrim_Arrows",[("rohan_arrow1",0),("rohan_arrow1_flying",ixmesh_flying_ammo),("rohan_quiver2",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,300,weight(3.5)|thrust_damage(2,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["harad_arrows","Haradrim_Arrows",[("harad_arrow",0),("harad_arrow_flying",ixmesh_flying_ammo),("harad_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,300,weight(3)|thrust_damage(1,cut)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["corsair_arrows","Corsair_Arrows",[("corsair_arrow",0),("corsair_arrow_flying",ixmesh_flying_ammo),("corsair_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_front_right,300,weight(3)|thrust_damage(1,cut)|max_ammo(29)|weapon_length(91),imodbits_missile,[]],
["ithilien_arrows","Ithilien_Arrows",[("ilithien_arrow",0),("ilithien_arrow_flying",ixmesh_flying_ammo),("ithilien_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_back_right,500,weight(3)|thrust_damage(3,cut)|max_ammo(29)|weapon_length(91),imodbits_good_missile,[]],
["woodelf_arrows","Woodelf_Arrows",[("mirkwood_arrow",0),("mirkwood_arrow_flying",ixmesh_flying_ammo),("mirkwood_quiver_new",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_back,500,weight(3)|thrust_damage(4,pierce)|max_ammo(29)|weapon_length(91),imodbits_good_missile,[]],
["elven_arrows","Elven_Arrows",[("white_elf_arrow",0),("white_elf_arrow_flying",ixmesh_flying_ammo),("lothlorien_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_back,500,weight(3)|thrust_damage(4,pierce)|max_ammo(29)|weapon_length(91),imodbits_good_missile,[]],
#["loth_arrows"    ,"Ghaladrim_Arrows",[("white_elf_arrow",0),("flying_missile",ixmesh_flying_ammo),("lothlorien_quiver", ixmesh_carry)],itp_type_arrows|itp_shop, itcf_carry_quiver_back_right ,350,weight(3.0)|abundance(50) |weapon_length(91)|thrust_damage(3,    pierce)|max_ammo(29),imodbits_missile],
["orc_hook_arrow","Orc_Hook_Arrows",[("orc_hook_arrow",0),("orc_hook_arrow_flying",ixmesh_flying_ammo),("orc_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_back_right,100,weight(3)|thrust_damage(0,pierce)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["isengard_arrow","Isengard_Arrows",[("isengard_arrow",0),("isengard_arrow_flying",ixmesh_flying_ammo),("isengard_quiver",ixmesh_carry)],itp_type_arrows|itp_shop,itcf_carry_quiver_back_right,200,weight(3)|thrust_damage(1,pierce)|max_ammo(30)|weapon_length(95),imodbits_missile,[]],
["pilgrim_disguise","Pilgrim_Disguise",[("tld_robe_generic_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,25,weight(2)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0),imodbits_cloth,[]],
#["pilgrim_hood", "Pilgrim Hood",[("pilgrim_hood",0)], 0|itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
###ARMOR
#handwear
["leather_gloves","Leather_Gloves",[("lthr_glove_L",0), ("undeadtest_handL",imodbit_poor)],itp_type_hand_armor|itp_shop,0,200,weight(0.2)|body_armor(2)|difficulty(0),imodbits_cloth,[]],
["mail_mittens","Mail_Mittens",[("mail_mitten_L",0)],itp_type_hand_armor|itp_shop,0,600,weight(0.5)|body_armor(4)|difficulty(0),imodbits_elf_armor,[]],
["leather_boots","Leather_Boots",[("boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature|itp_civilian,0,200,weight(1)|leg_armor(12)|difficulty(0),imodbits_cloth],
# TLD civilian wear
["black_dress","Black_Dress",[("gondor_dress_a",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,500,weight(3)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[]],
["blackwhite_dress","Lady_Dress",[("gondor_dress_b",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,500,weight(3)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[]],
["white_tunic_a","White_Tunic",[("generic_tunic_a",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["white_tunic_b","Simple_Tunic",[("gondor_tunic_b",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["white_tunic_c","Tunic_Jacket",[("generic_tunic_c",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["blue_tunic","Blue_Tunic",[("dale_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["black_tunic","Black_Tunic",[("gondor_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["green_tunic","Green_Tunic",[("rohan_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["red_tunic","Red_Tunic",[("haradrim_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[]],
["leather_apron","Leather_Apron",[("smith_leather_apron",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,50,weight(3)|head_armor(0)|body_armor(8)|leg_armor(7)|difficulty(0),imodbits_cloth,[]],
["leather_jerkin","Leather_Jerkin",[("generic_leather_jerkin",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,300,weight(6)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0),imodbits_cloth,[]],
["fur_coat","Dale_Coat",[("dale_coat",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,400,weight(6)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0),imodbits_cloth,[]],
["green_dress","Green_Dress",[("rohan_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,500,weight(6)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0),imodbits_cloth,[]],
#["rich_outfit"   , "Rich Outfit" ,[("merchant_outf"  ,0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["tld_tunic","Tunic",[("tld_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,100,weight(2)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0),imodbits_cloth,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_initialize_civilian_clothes", "tableau_tld_tunic", ":agent_no", ":troop_no")])]],
#combos
["gondor_fine_outfit_dress","Fine_Outfit",[("gondor_fine_outfit_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,500,weight(3)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[]],
["rohan_fine_outfit_dale_dress","Fine_Outfit",[("rohan_fine_outfit_dale_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,500,weight(3)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[]],
["robe_generic_dress","Robe",[("tld_robe_generic_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,500,weight(3)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[]],
#civ headgear
["wimple_a","Wimple",[("gondor_wimple_a",0)],itp_type_head_armor|itp_civilian|itp_shop|itp_fit_to_head,0,10,weight(0.5)|head_armor(4)|difficulty(0),imodbits_cloth,[]],
["wimple_with_veil","Wimple",[("gondor_wimple_b",0)],itp_type_head_armor|itp_civilian|itp_shop|itp_fit_to_head,0,10,weight(0.5)|head_armor(4)|difficulty(0),imodbits_cloth,[]],
["fine_hat","Fine_Hat",[("gondor_fine_fem_hat",0)],itp_type_head_armor|itp_civilian|itp_shop,0,10,weight(0.5)|head_armor(4)|difficulty(0),imodbits_cloth,[]],
#
#["sword_two_handed_a",         "Great Sword",[("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_shop|itp_always_loot|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1123 , weight(2.75)|difficulty(10)|spd_rtng(89) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
#["bastard_sword_a", "Bastard Sword",[("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_shop|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 294 , weight(2.25)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(37 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
#["one_handed_war_axe_a","One_Handed_War_Axe",[("one_handed_war_axe_a",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,87,weight(1.5)|difficulty(0)|spd_rtng(100)|weapon_length(60)|swing_damage(32,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
#["two_handed_axe",         "Two_Handed_Axe",[("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_shop|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 110 , weight(4.5)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["sword_medieval_b_small", "Short Sword",[("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 152 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
#["sword_medieval_c","Arming_Sword",[("sword_medieval_c",0),("sword_medieval_c_scabbard",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,410,weight(1.5)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(29,cut)|thrust_damage(24,pierce),imodbits_sword_high],
["shortened_spear","Shortened_Spear",[("spear_g_1-9m",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_staff,100,weight(2)|difficulty(0)|spd_rtng(102)|weapon_length(120)|swing_damage(19,blunt)|thrust_damage(25,pierce),imodbits_weapon_wood,[]],
["spear","Spear",[("spear_h_2-15m",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_staff,200,weight(2.25)|difficulty(0)|spd_rtng(98)|weapon_length(135)|swing_damage(20,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood,[]],
["light_lance","Light_Lance",[("spear_b_2-75m",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_cutting_spear,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(175)|swing_damage(16,blunt)|thrust_damage(27,pierce),imodbits_weapon_wood,[]],
["lance","Lance",[("spear_d_2-8m",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_pike,200,weight(2.5)|difficulty(0)|spd_rtng(88)|weapon_length(180)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood,[]],
###SHIELDS
#["tab_shield_round_a", "Old Round Shield",[("tableau_shield_round_5",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  26 , weight(2.5)|hit_points(350)|body_armor(0)|spd_rtng(93)|weapon_length(50),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
#["tab_shield_round_b", "Plain Round Shield",[("tableau_shield_round_3",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  65 , weight(3)|hit_points(460)|body_armor(2)|spd_rtng(90)|weapon_length(50),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
#["tab_shield_round_c", "Round_Shield",[("tableau_shield_round_2",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  105 , weight(3.5)|hit_points(540)|body_armor(4)|spd_rtng(87)|weapon_length(50),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
#["tab_shield_round_d", "Heavy Round_Shield",[("tableau_shield_round_1",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  210 , weight(4)|hit_points(600)|body_armor(6)|spd_rtng(84)|weapon_length(50),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
#["tab_shield_round_e", "Huscarl's Round_Shield",[("tableau_shield_round_4",0)], itp_shop|itp_type_shield, itcf_carry_round_shield,  430 , weight(4.5)|hit_points(690)|body_armor(8)|spd_rtng(81)|weapon_length(50),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],
#["tab_shield_small_round_a", "Plain Cavalry Shield",[("tableau_shield_small_round_3",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  96 , weight(2)|hit_points(310)|body_armor(3)|spd_rtng(105)|weapon_length(40),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b","Round_Cavalry_Shield",[("tableau_shield_small_round_1",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(370)|body_armor(5)|spd_rtng(103)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
#["tab_shield_small_round_c", "Elite Cavalry Shield",[("tableau_shield_small_round_2",0)], itp_shop|itp_type_shield, itcf_carry_round_shield,  370 , weight(3)|hit_points(420)|body_armor(14)|spd_rtng(100)|weapon_length(40),imodbits_shield,
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],
#
#RANGED
#["stones","Troll Stones",[("throwing_stone",0)], itp_type_thrown |itp_primary ,itcf_throw_stone, 1, weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
["short_bow","Short_Bow",[("small_bow",0),("small_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bow_back,50,weight(1)|difficulty(0)|shoot_speed(48)|spd_rtng(99)|thrust_damage(25,cut),imodbits_bow,[]],
["regular_bow","Bow",[("regular_bow",0),("regular_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bow_back,100,weight(1)|difficulty(0)|shoot_speed(52)|spd_rtng(98)|thrust_damage(28,cut),imodbits_bow,[]],
["nomad_bow","Nomad_Bow",[("nomad_bow",0),("nomad_bow_case",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,200,weight(1.3)|difficulty(0)|shoot_speed(53)|spd_rtng(96)|thrust_damage(30,cut),imodbits_bow,[]],
["gondor_bow","Gondor_Bow",[("gondor_bow",0),("gondor_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bow_back,400,weight(1.8)|difficulty(0)|shoot_speed(54)|spd_rtng(82)|thrust_damage(42,cut),imodbits_bow,[]],
["strong_bow","Strong_Bow",[("strong_bow",0),("strong_bow_case",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,400,weight(1.3)|difficulty(0)|shoot_speed(57)|spd_rtng(94)|thrust_damage(43,cut),imodbits_bow,[]],
["elven_bow","Elven_Bow",[("elven_bow",0),("elven_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.5)|difficulty(3)|shoot_speed(65)|spd_rtng(93)|thrust_damage(25,pierce),imodbits_good_bow,[]],
["corsair_bow","Corsair_Bow",[("corsair_bow",0),("corsair_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,500,weight(1.5)|difficulty(0)|shoot_speed(58)|spd_rtng(93)|thrust_damage(35,cut),imodbits_bow,[]],
["dwarf_horn_bow","Dwarf_Horn_Bow",[("dwarf_horn_bow",0),("dwarf_horn_bow",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bowcase_left,500,weight(1.3)|difficulty(0)|shoot_speed(56)|spd_rtng(95)|thrust_damage(31,cut),imodbits_good_bow,[]],
["dwarf_short_bow","Dwarf_Short_Bow",[("dwarf_short_bow",0),("dwarf_short_bow",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bowcase_left,300,weight(1.3)|difficulty(0)|shoot_speed(53)|spd_rtng(96)|thrust_damage(30,cut),imodbits_bow,[]],
["harad_bow","Harad_Curved_Bow",[("harad_bow",0),("harad_bow",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_back,300,weight(1.3)|difficulty(0)|shoot_speed(56)|spd_rtng(95)|thrust_damage(31,cut),imodbits_bow,[]],
["lg_bow","Eagle_Guard_Bow",[("lg_bow",0),("lg_bow",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_back,500,weight(1.3)|difficulty(0)|shoot_speed(56)|spd_rtng(95)|thrust_damage(31,cut),imodbits_bow,[]],
["riv_bow","Rivendell_Bow",[("rivendellbow",0),("rivendellbow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.8)|difficulty(3)|shoot_speed(65)|spd_rtng(93)|thrust_damage(25,pierce),imodbits_good_bow,[]],
["glorfi_bow","Glorfindeil_Bow",[("rivendellbow",0),("rivendellbow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_unique,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.8)|difficulty(3)|shoot_speed(65)|spd_rtng(93)|thrust_damage(25,pierce),imodbits_good_bow,[]],
["lorien_bow","Galadhrim_Bow",[("Elfbow",0),("Elfbow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.5)|difficulty(3)|shoot_speed(65)|spd_rtng(93)|thrust_damage(25,pierce),imodbits_good_bow,[]],
["isengard_large_bow","Isengard_Large_Bow",[("isengard_large_bow",0),("isengard_large_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,600,weight(1.5)|difficulty(0)|shoot_speed(58)|spd_rtng(87)|thrust_damage(23,pierce),imodbits_bow,[]],
["dale_bow","Dale_Bow",[("dale_bow",0),("dale_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,500,weight(1.5)|difficulty(0)|shoot_speed(58)|spd_rtng(93)|thrust_damage(35,cut),imodbits_bow,[]],
["uruk_bow","Orc_Bow",[("orc_bow",0),("orc_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_bow|itcf_carry_bowcase_left,500,weight(1.3)|difficulty(0)|shoot_speed(57)|spd_rtng(94)|thrust_damage(25,cut),imodbits_bow,[]],
["mirkwood_bow","Mirkwood_Bow",[("mirkwood_bow",0),("mirkwood_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.5)|difficulty(3)|shoot_speed(65)|spd_rtng(93)|thrust_damage(25,pierce),imodbits_good_bow,[]],
#
["dunland_javelin","Dunland_Javelins",[("dunland_javelin",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(85)|thrust_damage(55,pierce)|max_ammo(2),imodbits_thrown,[]],
["orc_throwing_arrow","Orc_Darts",[("orc_throwing_arrow",0),("orc_throwing_arrow_bag",ixmesh_carry)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back_right|itcf_show_holster_when_drawn,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(65)|thrust_damage(33,pierce)|max_ammo(7),imodbits_thrown,[]],
["heavy_throwing_spear","Heavy_Throwing_Spear",[("rohan_throwing_spear",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(93)|thrust_damage(63,pierce)|max_ammo(2),imodbits_thrown,[]],
["javelin","Javelin",[("javelin",0),("javelins_quiver",ixmesh_carry)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,200,weight(5)|difficulty(0)|shoot_speed(28)|spd_rtng(91)|weapon_length(75)|thrust_damage(45,pierce)|max_ammo(3),imodbits_thrown,[]],
["harad_javelin","Harad_Javelin",[("harad_javelin",0),("harad_javelins_quiver",ixmesh_carry)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(67)|thrust_damage(45,pierce)|max_ammo(3),imodbits_thrown,[]],
["gondor_javelin","Gondor_Javelin",[("gondor_javelin",0),("jarid_quiver",ixmesh_carry)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(80)|thrust_damage(50,pierce)|max_ammo(3),imodbits_thrown,[]],
["rohirrim_throwing_axe","Rohirrim_Throwing_Axes",[("rohan_throwing_axe",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_axe,300,weight(5)|difficulty(0)|shoot_speed(20)|spd_rtng(99)|weapon_length(35)|thrust_damage(60,cut)|max_ammo(3),imodbits_thrown,[]],
["loss_throwing_axes","Lossarnach_Throwing_Axes",[("loss_throwing_axe",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_axe,300,weight(5)|difficulty(0)|shoot_speed(20)|spd_rtng(99)|weapon_length(33)|thrust_damage(60,cut)|max_ammo(3),imodbits_thrown,[]],
##########TLD ITEMS START##########
#####TLD RIVENDELL/DUNEDAIN ITEMS##########
###ARNOR HELMS########
["arnor_helm_a","Arnor_Helm",[("dunedain_helm_a",0)],itp_type_head_armor|itp_shop,0,1000,weight(1.5)|head_armor(32)|difficulty(0),imodbits_elf_armor,[]],
["arnor_helm_b","Arnor_Helm",[("dunedain_helm_b",0)],itp_type_head_armor|itp_shop,0,1000,weight(1.5)|head_armor(32)|difficulty(0),imodbits_elf_armor,[]],
["arnor_helm_c","Arnor_Helm",[("dunedain_helm_c",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(35)|difficulty(0),imodbits_elf_armor,[]],
["dunedain_helm_a","Dunedain_Hood",[("arnor_hood",0)],itp_type_head_armor|itp_shop|itp_fit_to_head,0,300,weight(1)|head_armor(14)|difficulty(0),imodbits_elf_cloth,[]],
["dunedain_helm_b","Arnor_Decorated_Helm",[("arnor_helm_a",0)],itp_type_head_armor|itp_shop,0,1500,weight(2)|head_armor(38)|difficulty(0),imodbits_elf_armor,[]],
#ARNOR ARMORS########
["arnor_armor_a","Arnorian_Armor",[("arnor_blue",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2300,weight(20)|head_armor(0)|body_armor(40)|leg_armor(13)|difficulty(0),imodbits_elf_armor,[]],
["arnor_armor_b","Arnorian_Armor",[("arnor_brown",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2300,weight(20)|head_armor(0)|body_armor(40)|leg_armor(13)|difficulty(0),imodbits_elf_armor,[]],
["arnor_armor_c","Dunedain_Ranger_Leather",[("arnor_ranger",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0),imodbits_elf_armor,[]],
["arnor_armor_d","Dunedain_Ranger_Leather",[("arnor_ranger_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0),imodbits_elf_armor,[]],
["arnor_armor_e","Arnorian_Reinforced_Jerkin",[("arnor_reinf_jerkin",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(15)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,[]],
["arnor_armor_f","Arnorian_High_Armor",[("arnor_knight",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3100,weight(24)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(0),imodbits_elf_armor,[]],
["arnor_greaves","Arnorian_Greaves",[("arnor_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,800,weight(3)|leg_armor(24)|difficulty(0),imodbits_elf_armor,[]],
["arnor_splinted","Arnorian_Splinted_Greaves",[("arnor_splinted",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1200,weight(3.5)|leg_armor(28)|difficulty(0),imodbits_elf_armor,[]],
#ARNOR SHIELDS########
["arnor_shield_a","Arnor_Shield",[("arnor_shield_inf",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2)|hit_points(380)|body_armor(14)|spd_rtng(100)|weapon_length(50),imodbits_shield_good,[]],
#["arnor_shield_b", "Arnor Buckler",[("arnor_buckler",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  118 , weight(1.3)|hit_points(380)|body_armor(1)|spd_rtng(100)|weapon_length(39),imodbits_shield ],
["arnor_shield_c","Arnor_Cavalry_Shield",[("arnor_cav_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2)|hit_points(380)|body_armor(14)|spd_rtng(100)|weapon_length(50),imodbits_shield_good,[]],
["arnor_shield_b","Arnor_Shield",[("arnor_shield_inf_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2)|hit_points(380)|body_armor(14)|spd_rtng(100)|weapon_length(50),imodbits_shield_good,[]],
["arnor_shield_d","Arnor_Cavalry_Shield",[("arnor_cav_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2)|hit_points(380)|body_armor(14)|spd_rtng(100)|weapon_length(50),imodbits_shield_good,[]],
####RNOR WEAPONS########
["arnor_sword_a","Arnor_Bastard_Sword",[("dunedain_bastard_a",0),("scab_dunedain_bastard_a",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294,weight(2.05)|difficulty(0)|spd_rtng(99)|weapon_length(100)|swing_damage(33,cut)|thrust_damage(26,pierce),imodbits_weapon_good,[]],
#["arnor_sword_b", "Arnor Bastard Sword",[("dunedain_bastard_c",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_shop|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,324 , weight(2.25)|difficulty(9)|spd_rtng(97) | weapon_length(110)|swing_damage(38 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["arnor_sword_c","Arnor_Bastard_Sword",[("dunedain_bastard_d",0),("scab_dunedain_bastard_d",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294,weight(2.25)|difficulty(0)|spd_rtng(93)|weapon_length(109)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon_good,[]],
#["arnor_sword_d", "Arnor Bastard Sword",[("dunedain_bastard_d",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_shop|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 294 , weight(2.25)|difficulty(9)|spd_rtng(99) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
#["arnor_sword_e", "Arnor Shortsword",[("dunedain_1h",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,152 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["arnor_sword_f","Arnor_Shortsword",[("dunedain_1h",0),("scab_dunedain_1h",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(1.25)|difficulty(0)|spd_rtng(107)|weapon_length(83)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon_good,[]],
#
#RIVENDELL HELMS##########
["riv_helm_a","Rivendell_Coif",[("rivendell_coif_new",0)],itp_type_head_armor|itp_shop,0,800,weight(1)|head_armor(24)|difficulty(0),imodbits_elf_armor,[]],
["riv_helm_b","Rivendell_Archer_Helm",[("rivendellarcherhelmet",0)],itp_type_head_armor|itp_shop,0,1300,weight(1)|head_armor(35)|difficulty(0),imodbits_elf_armor,[]],
["riv_helm_c","Rivendell_Infantry_Helm",[("rivendellswordfighterhelmet",0)],itp_type_head_armor|itp_shop,0,1800,weight(1.2)|head_armor(40)|difficulty(0),imodbits_elf_armor,[]],
["riv_helm_glorfi","Glorfi_Hair",[("glorfindelhair",0)],itp_no_pick_up_from_ground|itp_type_head_armor|itp_unique,0,3000,weight(1.2)|head_armor(70)|difficulty(0),0,[]],
["riv_tiara","Elf_Lord_Tiara",[("tiara",0)],itp_type_head_armor|itp_unique|itp_doesnt_cover_hair,0,3000,weight(2.5)|head_armor(60)|difficulty(0),0,[]],
##########RIVENDELL SHIELDS##########
["riv_shield_a","Rivendell_Shield",[("riv_inf_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,700,weight(2.5)|hit_points(1000)|body_armor(20)|spd_rtng(85)|weapon_length(82),imodbits_shield_good,[]],
["riv_shield_b","Rivendell_Shield",[("riv_cav_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,600,weight(2)|hit_points(800)|body_armor(13)|spd_rtng(92)|weapon_length(60),imodbits_shield_good,[]],
#["riv_shield_c", "Rivendell Shield",[("riv_inf_shield_long_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  218 , weight(2.0)|hit_points(380)|body_armor(1)|spd_rtng(99)|weapon_length(50),imodbits_shield ],
#["riv_shield_d", "Rivendell Shield",[("riv_inf_shield_long_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  318 , weight(2.5)|hit_points(440)|body_armor(1)|spd_rtng(85)|weapon_length(82),imodbits_shield ],
#["riv_shield_e", "Rivendell Shield",[("riv_inf_shield_short_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  418, weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["riv_shield_f", "Rivendell Shield",[("riv_inf_shield_short_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  218 , weight(2.0)|hit_points(380)|body_armor(1)|spd_rtng(99)|weapon_length(50),imodbits_shield  ],
#####RIVENDELL WEAPONS########
["riv_bas_sword","Rivendell_Bastard_Sword",[("rivendell_handandahalf1",0),("scab_rivendell_handandahalf1",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294,weight(2.25)|difficulty(0)|spd_rtng(98)|weapon_length(105)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon_good,[]],
["riv_1h_sword","Rivendell_Sword",[("rivendellsword1",0),("scab_rivendell_sword1",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(95)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon_good,[]],
["riv_riding_sword","Rivendell_Cavalry_Sword",[("rivendelllongsword1",0),("scab_rivendelllongsword1",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(2)|difficulty(0)|spd_rtng(98)|weapon_length(103)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon_good,[]],
["riv_archer_sword","Rivendell_Archer's_Sword",[("rivendellshortsword1",0),("scab_rivendell_shortsword1",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(1.25)|difficulty(0)|spd_rtng(110)|weapon_length(80)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon_good,[]],
["riv_spear","Rivendell_Spear",[("elf_spear_2",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_wooden_parry|itp_couchable,itc_staff|itcf_carry_spear,700,weight(2.25)|difficulty(0)|spd_rtng(102)|weapon_length(171)|swing_damage(20,blunt)|thrust_damage(30,pierce),imodbits_weapon_good,[]],
########RIVENDELL ARMORS########
["riv_armor_light","Rivendell_Armor",[("rivendellrecruitarcher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(6)|head_armor(0)|body_armor(10)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,[]],
["riv_armor_light_inf","Rivendell_Armor",[("rivendellrecruitswordfighter",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(6)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_archer","Rivendell_Armor",[("rivendellnormalarcher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(8)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_m_archer","Rivendell_Armor",[("rivendellelitearcher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1400,weight(8)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_med","Rivendell_Armor",[("rivendellnormalswordfighter",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(12)|head_armor(0)|body_armor(28)|leg_armor(15)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_heavy","Rivendell_Armor",[("rivendelleliteswordfighter",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2500,weight(15)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_h_archer","Rivendell_Armor",[("rivendellmountedarcher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2500,weight(12)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(0),imodbits_elf_armor,[]],
["riv_armor_leader","Rivendell_Leader_Armor",[("rivendellleader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,5000,weight(12)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0),imodbits_elf_armor,[]],
["riv_boots","Rivendell_Boots",[("rivendell_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature|itp_civilian,0,1200,weight(1)|leg_armor(23)|difficulty(0),imodbits_elf_cloth],
#####TLD GONDOR ITEMS##########
####ARMORS
["gon_footman","Gondor_Mail_Shirt",[("gondor_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(15)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0),imodbits_elf_armor,[]],
["gon_jerkin","Gondor_Jerkin",[("gondor_jerkin",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(6)|head_armor(0)|body_armor(12)|leg_armor(4)|difficulty(0),imodbits_elf_cloth,[]],
["gon_regular","Gondor_Heavy_Mail",[("gondor_regular",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1400,weight(19)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(0),imodbits_elf_armor,[]],
["gon_bowman","Gondor_Gambeson",[("gondor_bowman",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_cloth,[]],
["gon_archer","Gondor_Gambeson_with_Cloak",[("gondor_archer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,900,weight(13)|head_armor(0)|body_armor(24)|leg_armor(9)|difficulty(0),imodbits_cloth,[]],
["gon_noble_cloak","Gondor_Noble's_Jerkin",[("gondor_noble_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(8)|head_armor(0)|body_armor(18)|leg_armor(5)|difficulty(0),imodbits_elf_cloth,[]],
["gon_squire","Gondor_Mail_with_Cloak",[("gondor_squire",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(16)|head_armor(0)|body_armor(26)|leg_armor(9)|difficulty(0),imodbits_elf_armor,[]],
["gon_knight","Gondor_Heavy_Mail_and_Cloak",[("gondor_knight",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(20)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(0),imodbits_elf_armor,[]],
["gon_ranger_cloak","Gondor_Ranger_Cloak",[("gondor_ranger_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(8)|head_armor(0)|body_armor(18)|leg_armor(7)|difficulty(0),imodbits_elf_cloth,[]],
["gon_ranger_skirt","Gondor_Ranger_Skirt",[("gondor_ranger_skirt",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(10)|head_armor(0)|body_armor(18)|leg_armor(12)|difficulty(0),imodbits_elf_armor,[]],
["gon_steward_guard","Gondor_Steward_Guard_Armor",[("gondor_steward_guard",0)],itp_type_body_armor|itp_covers_legs|0,0,4000,weight(22)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0),imodbits_elf_armor,[]],
["gon_tower_guard","Gondor_Tower_Guard_Armor",[("gondor_tower_guard",0)],itp_type_body_armor|itp_covers_legs|0,0,4000,weight(22)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0),imodbits_elf_armor,[]],
["gon_tower_knight","Gondor_Tower_Knight_Armor",[("gon_tower_knight",0)],itp_type_body_armor|itp_covers_legs|0,0,5000,weight(25)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(0),imodbits_elf_armor,[]],
["gon_leader_surcoat_cloak","Gondor_Leader's_Surcoat",[("gon_leader_surcoat_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(22)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(0),imodbits_elf_armor,[]],
["gondor_ranger_hood","Green_Hood",[("gondor_ranger_hood",0)],itp_type_head_armor|itp_shop|itp_fit_to_head,0,100,weight(0.5)|head_armor(13)|difficulty(0),imodbits_cloth,[]],
["gondor_ranger_hood_mask","Gondor_Ranger_Hood",[("gondor_ranger_hood_mask",0)],itp_type_head_armor|itp_shop|itp_fit_to_head,0,400,weight(0.6)|head_armor(15)|difficulty(0),imodbits_elf_cloth,[]],
["gondor_light_greaves","Gondorian_Leather_Greaves",[("gondor_light_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,600,weight(3)|leg_armor(16)|difficulty(0),imodbits_cloth,[]],
["gondor_med_greaves","Gondorian_Medium_Greaves",[("gondor_medium_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1000,weight(3.5)|leg_armor(22)|difficulty(0),imodbits_armor,[]],
["gondor_heavy_greaves","Gondorian_Mailed_Greaves",[("gondor_heavy_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1300,weight(3)|leg_armor(25)|difficulty(0),imodbits_armor,[]],
####Helms
["gondorian_light_helm","Gondorian_Footman_Helm",[("gondor_footman_helm",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(29)|difficulty(0),imodbits_armor | imodbit_cracked,[]],
["gondor_infantry_helm","Gondor_Infantry_Helm",[("gondor_regular_helm",0)],itp_type_head_armor|itp_shop,0,1300,weight(2.4)|head_armor(34)|difficulty(0),imodbits_elf_armor,[]],
["gondor_auxila_helm","Gondorian_Auxilia_Helm",[("gondor_auxila_helm",0)],itp_type_head_armor|itp_shop,0,300,weight(1.5)|head_armor(20)|difficulty(0),imodbits_elf_armor,[]],
["gondorian_light_helm_b","Gondorian_Bowman_Helm",[("gondor_bowman_helm",0)],itp_type_head_armor|itp_shop,0,500,weight(1.5)|head_armor(25)|difficulty(0),imodbits_elf_armor,[]],
["gondorian_archer_helm","Gondorian_Archer_Helm",[("gondor_archer_helm",0)],itp_type_head_armor|itp_shop,0,800,weight(1.75)|head_armor(27)|difficulty(0),imodbits_elf_armor,[]],
["tower_archer_helm","Tower_Archer_Helm",[("gondor_tower_archer_helm",0)],itp_type_head_armor|itp_shop,0,1200,weight(1.5)|head_armor(31)|difficulty(0),imodbits_elf_armor,[]],
["gondor_leader_helm","Gondor_High_Helmet",[("gondor_leader_helm",0)],itp_type_head_armor|itp_shop,0,3000,weight(2.5)|head_armor(40)|difficulty(0),imodbits_elf_armor,[]],
["tower_guard_helm","Tower_Guard_Helm",[("gondor_tower_guard_helm",0)],itp_type_head_armor|itp_shop,0,3000,weight(2.5)|head_armor(40)|difficulty(0),imodbits_elf_armor,[]],
["gondor_citadel_knight_helm","Citadel_Knight_Helm",[("gondor_citadel_knight_helm",0)],itp_type_head_armor|itp_shop,0,3000,weight(2.5)|head_armor(40)|difficulty(0),imodbits_elf_armor,[]],
["gondor_squire_helm","Gondor_Squire_Helm",[("gondor_squire_helm",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(29)|difficulty(0),imodbits_elf_armor],
["gondor_knight_helm","Gondor_Knight_Helm",[("gondor_knight_helm",0)],itp_type_head_armor|itp_shop,0,1300,weight(2)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["gondor_dolamroth_helm","Dol_Amroth_Helm",[("gondor_dolamroth_helm",0)],itp_type_head_armor|itp_shop,0,1300,weight(2.5)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["swan_knight_helm","Swan_Knight_Helm",[("gondor_dolamroth_knight_helm",0)],itp_type_head_armor|itp_shop,0,1500,weight(3)|head_armor(39)|difficulty(0),imodbits_elf_armor],
["gondor_lamedon_helm","Lamedon_Helm",[("gondor_lamedon_helm",0)],itp_type_head_armor|itp_shop,0,1100,weight(2)|head_armor(32)|difficulty(0),imodbits_elf_armor],
["gondor_lamedon_leader_helm","Lamedon_High_Helmet",[("gondor_lamedon_leader_helm",0)],itp_type_head_armor|itp_shop,0,1400,weight(2.5)|head_armor(36)|difficulty(0),imodbits_elf_armor],
###BRV
["blackroot_archer","Blackroot_Vale_Archer_Armor",[("blackroot_archer",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["blackroot_bowman","Blackroot_Vale_Bowman_Armor",[("blackroot_bowman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(10)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,],
["blackroot_footman","Blackroot_Vale_Footman_Armor",[("blackroot_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(15)|head_armor(0)|body_armor(20)|leg_armor(7)|difficulty(0),imodbits_elf_armor,],
["blackroot_warrior","Blackroot_Vale_Warrior_Armor",[("blackroot_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(14)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["blackroot_leader","Blackroot_Vale_Leader_Armor",[("blackroot_leader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(20)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["blackroot_hood","Blackroot_Hood",[("blackroot_hood",0)],itp_type_head_armor|itp_shop|itp_fit_to_head|itp_civilian,0,100,weight(0.5)|head_armor(12)|difficulty(0),imodbits_cloth],
#["blackroot_helm", "Blackroot Helm",[("blackroot_helm",0)], itp_shop|itp_type_head_armor,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
###DOL AMROTH
["dol_hauberk","Dol_Amroth_Hauberk",[("dol_hauberk",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(19)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["dol_heavy_mail","Dol_Amroth_Heavy_Mail",[("dol_heavy_mail",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(0)|body_armor(33)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["dol_padded_coat","Dol_Amroth_Padded_Coat",[("dol_padded_coat",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,900,weight(14)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_cloth,],
["dol_shirt","Dol_Amroth_Shirt",[("dol_shirt",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_shop,0,300,weight(5)|head_armor(0)|body_armor(10)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["dol_very_heavy_mail","Dol_Amroth_Very_Heavy_Mail",[("dol_very_heavy_mail",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3500,weight(25)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["dol_greaves","Dol_Amroth_Greaves",[("dol_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1800,weight(3)|leg_armor(27)|difficulty(0),imodbits_elf_armor],
["dol_shoes","Dol_Amroth_Light_Boots",[("dol_shoes",0)],itp_type_foot_armor|itp_shop|itp_attach_armature|itp_civilian,0,100,weight(1)|leg_armor(10)|difficulty(0),imodbits_cloth],
######LAMEDON
["lamedon_clansman","Lamedon_Clansman_Armor",[("lamedon_clansman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(8)|head_armor(0)|body_armor(8)|leg_armor(5)|difficulty(0),imodbits_elf_cloth,],
["lamedon_footman","Lamedon_Footman_Armor",[("lamedon_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(13)|head_armor(0)|body_armor(18)|leg_armor(5)|difficulty(0),imodbits_elf_armor,],
["lamedon_knight","Lamedon_Knight_Armor",[("lamedon_knight",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2100,weight(22)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["lamedon_leader_surcoat_cloak","Lamedon_Leader_Armor",[("lamedon_leader_surcoat_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1800,weight(18)|head_armor(0)|body_armor(31)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["lamedon_warrior","Lamedon_Warrior_Armor",[("lamedon_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(22)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["lamedon_veteran","Lamedon_Veteran_Armor",[("lamedon_veteran",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(20)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["lamedon_vet_warrior","Lamedon_Veteran_Warrior_Armor",[("lamedon_vet_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1700,weight(22)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["lamedon_hood","Lamedon_Hood",[("lamedon_hood",0)],itp_type_head_armor|itp_civilian|itp_shop,0,100,weight(1)|head_armor(10)|difficulty(0),imodbits_cloth],
#["lamedon_helmet", "Lamedon Helm",[("lamedon_helmet",0)], itp_shop|itp_type_head_armor,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#####PINNATH GELIN
["pinnath_archer","Pinnath_Gelin_Archer_Armor",[("pinnath_archer",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(14)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,],
["pinnath_footman","Pinnath_Gelin_Footman_Armor",[("pinnath_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(12)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0),imodbits_elf_armor,],
["pinnath_leader","Pinnath_Gelin_Leader_Armor",[("pinnath_leader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1100,weight(18)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["pinnath_vet_footman","Pinnath_Gelin_Veteran_Footman_Armor",[("pinnath_vet_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(14)|head_armor(0)|body_armor(20)|leg_armor(4)|difficulty(0),imodbits_elf_armor,],
["pinnath_warrior","Pinnath_Gelin_Warrior_Armor",[("pinnath_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(20)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
#["pinnath_hood", "Pinnath Gelin Hood",[("pinnath_hood",0)], 0|itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
######PEL
["pel_footman","Pelargir_Footman_Armor",[("pelargir_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(20)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["pel_jerkin","Pelargir_Jerkin",[("pelargir_jerkin",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(12)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0),imodbits_elf_cloth,],
["pel_leader","Pelargir_Leader_Armor",[("pelargir_leader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1300,weight(22)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["pel_marine","Pelargir_Marine",[("pelargir_marine",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(20)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0),imodbits_elf_armor,],
["pelargir_marine_leader","Pelargir_Marine_Leader",[("pelargir_marine_leader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1300,weight(21)|head_armor(0)|body_armor(33)|leg_armor(6)|difficulty(0),imodbits_elf_armor,],
["pelargir_regular","Pelargir_Regular",[("pelargir_regular",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(22)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["pelargir_hood","Pelargir_Hood",[("pelargir_hood",0)],itp_type_head_armor|itp_civilian|itp_shop,0,100,weight(1)|head_armor(10)|difficulty(0),imodbits_cloth],
["pelargir_helmet_light","Pelargir_Helm",[("pelargir_helmet_light",0)],itp_type_head_armor|itp_shop,0,1100,weight(2)|head_armor(32)|difficulty(0),imodbits_elf_armor],
["pelargir_helmet_heavy","Pelargir_Heavy_Helm",[("pelargir_helmet_heavy",0)],itp_type_head_armor|itp_shop,0,1400,weight(3)|head_armor(38)|difficulty(0),imodbits_elf_armor],
["pelargir_greaves","Pelargir_Greaves",[("pelargir_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,800,weight(3)|leg_armor(23)|difficulty(0),imodbits_elf_armor],
######LOS
["lossarnach_shirt","Lossarnach_Shirt",[("lossarnach_shirt",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(6)|head_armor(0)|body_armor(8)|leg_armor(4)|difficulty(0),imodbits_elf_cloth,],
["lossarnach_axeman","Lossarnach_Axeman_Armor",[("lossarnach_axeman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(10)|head_armor(0)|body_armor(16)|leg_armor(5)|difficulty(0),imodbits_elf_cloth,],
["lossarnach_leader","Lossarnach_Leader_Armor",[("lossarnach_leader",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(17)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["lossarnach_vet_axeman","Lossarnach_Veteran_Axeman_Armor",[("lossarnach_vet_axeman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(12)|head_armor(0)|body_armor(20)|leg_armor(7)|difficulty(0),imodbits_elf_armor,],
["lossarnach_vet_warrior","Lossarnach_Veteran_Warrior_Armor",[("lossarnach_vet_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1100,weight(18)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["lossarnach_warrior","Lossarnach_Warrior_Armor",[("lossarnach_warrior",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(16)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["lossarnach_cloth_cap","Lossarnach_Cloth_Cap",[("lossarnach_cloth_cap",0)],itp_type_head_armor|itp_shop,0,100,weight(1)|head_armor(12)|difficulty(0),imodbits_cloth],
["lossarnach_leather_cap","Lossarnach_Leather_Cap",[("lossarnach_leather_cap",0)],itp_type_head_armor|itp_shop,0,500,weight(1.6)|head_armor(22)|difficulty(0),imodbits_cloth],
["lossarnach_scale_cap","Lossarnach_Scale_Cap",[("lossarnach_scale_cap",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(28)|difficulty(0),imodbits_elf_armor],
["lossarnach_greaves","Lossarnach_Greaves",[("lossarnach_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,800,weight(3)|leg_armor(23)|difficulty(0),imodbits_elf_armor],
####SHIELDS#####
["gondor_shield_a","Gondor_Square_Shield",[("gondor_square_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,600,weight(3)|hit_points(480)|body_armor(12)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["gondor_shield_b","Gondor_Kite_Shield",[("gondor_point_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(2.5)|hit_points(480)|body_armor(12)|spd_rtng(82)|weapon_length(70),imodbits_shield,],
["gondor_shield_c","Gondor_Tower_Shield",[("gondor_tower_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,500,weight(3)|hit_points(480)|body_armor(12)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["gondor_shield_d","Gondor_Kite_Shield",[("gondorian_kite_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(2.5)|hit_points(480)|body_armor(12)|spd_rtng(82)|weapon_length(70),imodbits_shield,],
["gondor_shield_e","Gondor_Royal_Shield",[("denethor_shield",0)],itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback,itcf_carry_kite_shield,1000,weight(2.5)|hit_points(480)|body_armor(12)|spd_rtng(82)|weapon_length(90),imodbits_shield_good,],
#
["gon_tab_shield_a","Heraldic_Gondor_Round_Shield",[("tableau_shield_round",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(310)|body_armor(3)|spd_rtng(105)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_round_shield_banner", "tableau_gon_shield_round", ":agent_no", ":troop_no")])]],
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_round_shield_banner", "tableau_gon_shield_round", ":agent_no", ":troop_no")])]],
["gon_tab_shield_b","Heraldic_Gondor_Square_Shield",[("tableau_shield_square",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,200,weight(4.5)|hit_points(760)|body_armor(2)|spd_rtng(81)|weapon_length(84),imodbits_shield,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_square_shield_banner", "tableau_gon_shield_square", ":agent_no", ":troop_no")])]],
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_square_shield_banner", "tableau_gon_shield_square", ":agent_no", ":troop_no")])]],
["gon_tab_shield_c","Heraldic_Gondor_Kite_Shield",[("tableau_shield_kite",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(2.5)|hit_points(370)|body_armor(16)|spd_rtng(100)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_kite_shield_banner", "tableau_gon_shield_kite", ":agent_no", ":troop_no")])]],
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_kite_shield_banner", "tableau_gon_shield_kite", ":agent_no", ":troop_no")])]],
["gon_tab_shield_d","Heraldic_Gondor_Tower_Shield",[("tableau_shield_tower",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,300,weight(3.5)|hit_points(510)|body_armor(9)|spd_rtng(87)|weapon_length(90),imodbits_shield,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_tower_shield_banner", "tableau_gon_shield_tower", ":agent_no", ":troop_no")])]],
# [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_TLD_gondor_tower_shield_banner", "tableau_gon_shield_tower", ":agent_no", ":troop_no")])]],
#######WEAPONS##########
["amroth_sword_a","Dol_Amroth_Sword",[("DA_sword_a",0),("scab_DA_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.25)|difficulty(0)|spd_rtng(105)|weapon_length(88)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon],
["amroth_sword_b","Dol_Amroth_Knight_Sword",[("DA_sword_b",0),("scab_DA_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(2)|difficulty(0)|spd_rtng(99)|weapon_length(100)|swing_damage(33,cut)|thrust_damage(26,pierce),imodbits_weapon_good],
["gondor_sword","Gondor_Infantry_Sword",[("gondor_inf_new",0),("scab_gondor_inf_new",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.25)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon],
["amroth_bastard","Dol_Amroth_Heavy_Sword",[("DA_bastard",0),("scab_DA_bastard",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294,weight(2.25)|difficulty(0)|spd_rtng(96)|weapon_length(105)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon_good],
#
["gondor_short_sword","Linhir_Eket",[("linhir_eket",0),("scab_linhir_eket",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.25)|difficulty(0)|spd_rtng(113)|weapon_length(55)|swing_damage(28,cut)|thrust_damage(25,pierce),imodbits_weapon],
["pelargir_eket","Pelargir_Eket",[("pelargir_eket",0),("scab_pelargir_eket",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.25)|difficulty(0)|spd_rtng(115)|weapon_length(49)|swing_damage(28,cut)|thrust_damage(25,pierce),imodbits_weapon],
["pelargir_sword","Pelargir_Sword",[("pelargir_sword",0),("scab_pelargir_sword",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(72)|swing_damage(30,cut)|thrust_damage(21,pierce),imodbits_weapon],
#
["gondor_ranger_sword","Gondor_Ranger_Sword",[("gondor_bastard",0),("scab_gondor_ranger",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,800,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(103)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon],
#["lamedon_bastard",         "Gondor War Sword",[("gondor_bastard",0),("scab_gondor_bastard", ixmesh_carry)], itp_type_two_handed_wpn|itp_shop|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294 , weight(2.25)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(37 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["gondor_bastard","Gondor_Bastard_Sword",[("gondor_bastard",0),("scab_gondor_bastard",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,800,weight(2.25)|difficulty(0)|spd_rtng(98)|weapon_length(103)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon],
#["gondor_bastard_b",         "Dagmor",[("Dagmor",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_shop|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,294 , weight(2.25)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(37 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["gondor_citadel_sword","Gondor_Citadel_Sword",[("gondor_citadel",0),("scab_gondor_citadel",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1000,weight(1.25)|difficulty(0)|spd_rtng(100)|weapon_length(94)|swing_damage(39,cut)|thrust_damage(30,pierce),imodbits_weapon_good],
["gondor_cav_sword","Gondor_Cavalry_Sword",[("gondor_riding_sword",0),("scab_gondor_riding_sword",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(2)|difficulty(0)|spd_rtng(103)|weapon_length(100)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon],
#
["gondor_spear","Gondorian_Spear",[("gondor_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_wooden_parry, itc_staff|itcf_carry_spear,200,weight(2.25)|difficulty(0)|spd_rtng(102)|weapon_length(153)|swing_damage(20,blunt)|thrust_damage(30,pierce),imodbits_weapon_good],
["gondor_tower_spear","Gondorian_Tower_Spear",[("gondor_tower_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_staff,600,weight(2.35)|difficulty(0)|spd_rtng(99)|weapon_length(173)|swing_damage(23,cut)|thrust_damage(37,pierce),imodbits_weapon_good],
["gondor_lance","Gondor_Lance",[("amroth_lance",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_staff,400,weight(2.35)|difficulty(0)|spd_rtng(89)|weapon_length(204)|swing_damage(20,blunt)|thrust_damage(34,pierce),imodbits_weapon_good],
["loss_axe","Lossarnach_Fighting_Axe",[("loss_axe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(103)|weapon_length(47)|swing_damage(28,cut)|thrust_damage(0,pierce),imodbits_weapon],
["loss_war_axe","Lossarnach_War_Axe",[("loss_axe_2h",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back,300,weight(4.5)|difficulty(0)|spd_rtng(87)|weapon_length(75)|swing_damage(44,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
#
###########TLD LORIEN ITEMS##########
#######LORIEN WEAPONS########
["lorien_sword_a","Lorien_Longsword",[("lorien_sword_long",0),("scab_lorien_sword_long",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(100)|swing_damage(30,cut)|thrust_damage(20,pierce),imodbits_weapon_good],
["lorien_sword_b","Lorien_Shortsword",[("lorien_sword_short",0),("scab_lorien_sword_short",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.5)|difficulty(0)|spd_rtng(110)|weapon_length(65)|swing_damage(28,cut)|thrust_damage(25,pierce),imodbits_weapon_good],
["lorien_sword_c","Lorien_War_Sword",[("lorien_sword_hand_and_half",0),("scab_lorien_sword_hand_and_half",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,900,weight(2.5)|difficulty(0)|spd_rtng(98)|weapon_length(103)|swing_damage(33,cut)|thrust_damage(23,pierce),imodbits_weapon_good],
###########LORIEN ARMORS########
["lorien_archer","Lorien_Archer_Armor",[("lorien_archer",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(8)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,],
["lorien_armor_a","Lorien_Infantry_Armor",[("lorien_infantry_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
["lorien_armor_b","Lorien_Heavy_Infantry_Armor",[("lorien_vetinfantry_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(12)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
#["lorien_armor_d", "Lorien Armor",[("loth_full_leather"       ,0)], itp_shop|itp_type_body_armor|itp_covers_legs|itp_civilian,0,454, weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["lorien_armor_e", "Lorien Armor",[("loth_half_scale"         ,0)], itp_shop|itp_type_body_armor|itp_covers_legs|itp_civilian,0,454, weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["lorien_armor_f", "Lorien Armor",[("loth_full_scale"         ,0)], itp_shop|itp_type_body_armor|itp_covers_legs|itp_civilian,0,454, weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["lorien_armor_c","Lorien_Royal_Archer_Armor",[("lorien_royalarcher_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(12)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
["lorien_armor_d","Lorien_Royal_Swordsman_Armor",[("lorien_royalswordsman_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2400,weight(12)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
["lorien_armor_e","Lorien_Warden_Cloak",[("lorien_warden_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(12)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
["lorien_armor_f","Lorien_Elite_Armor",[("lorien_eliteinfantry_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(12)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0),imodbits_elf_cloth,],
#
["lorien_boots","Lothlorien_Boots",[("lorien_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1500,weight(1)|leg_armor(28)|difficulty(0),imodbits_elf_cloth],
########LORIEN SHIELDS#####
#["lorien_shield_a", "Lorien Shield",[("loth_long_shield_a" ,0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
["lorien_shield_b","Lorien_Tower_Shield",[("lorien_kite",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,700,weight(2)|hit_points(1000)|body_armor(20)|spd_rtng(82)|weapon_length(90),imodbits_shield_good,],
["lorien_shield_c","Lorien_Kite_Shield",[("lorien_kite_small",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,500,weight(2)|hit_points(800)|body_armor(18)|spd_rtng(92)|weapon_length(70),imodbits_shield_good,],
["lorien_round_shield","Lorien_Round_Shield",[("lorien_round_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(1)|hit_points(700)|body_armor(15)|spd_rtng(96)|weapon_length(50),imodbits_shield_good,],
# 
########LORIEN HELMS#######
["lorien_helm_a","Lorien_Archer_Helm",[("lorienhelmetarcherlow",0)],itp_type_head_armor|itp_shop,0,1300,weight(1)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["lorien_helm_b","Lorien_Archer_Helm",[("lorienhelmetarcherhigh",0)],itp_type_head_armor|itp_shop,0,1800,weight(1)|head_armor(40)|difficulty(0),imodbits_elf_armor],
#["lorien_helm_c", "Lorien Helm"         ,[("lorien_helm"           ,0)], itp_shop|itp_type_head_armor,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["lorien_helm_c","Lorien_Infantry_Helm",[("lorienhelmetinf",0)],itp_type_head_armor|itp_shop,0,1900,weight(1.2)|head_armor(42)|difficulty(0),imodbits_elf_armor],
#["lorien_helm_e", "Lorien Hood"         ,[("elven_cloth_hood_blue" ,0)], itp_shop|itp_type_head_armor,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
########GENERIC ORC ITEMS#####
["orc_chain_greaves","Orc_Greaves",[("orc_chain_greaves_lr",0)],itp_type_foot_armor|itp_shop,0,701,weight(3)|leg_armor(15)|difficulty(0),imodbits_orc_armor],
["orc_coif","Orc_Coif",[("orc_coif",0)],itp_type_head_armor|itp_shop|itp_fit_to_head,0,200,weight(2.3)|head_armor(12)|difficulty(0),imodbits_orc_armor],
["orc_greaves","Orc_Chain_Boots",[("old_orc_chain_greave_lr",0)],itp_type_foot_armor|itp_shop,0,401,weight(3)|leg_armor(12)|difficulty(0),imodbits_orc_armor],
["orc_ragwrap","Orc_Ragwrap",[("orc_ragwrap_lr",0)],itp_type_foot_armor|itp_shop,0,11,weight(1)|leg_armor(3)|difficulty(0),imodbits_orc_cloth],
["orc_furboots","Orc_Fur_Boots",[("orc_furboot_lr",0)],itp_type_foot_armor|itp_shop,0,201,weight(3)|leg_armor(10)|difficulty(0),imodbits_orc_cloth],
["orc_furboot_tall","Orc_Fur_Boots",[("orc_furboot_tall",0)],itp_type_foot_armor|itp_shop,0,201,weight(3)|leg_armor(10)|difficulty(0),imodbits_orc_cloth],
#
["orc_tribal_a","Untreated_Skin",[("orc_tribal_a",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(3)|head_armor(0)|body_armor(3)|leg_armor(0)|difficulty(0),imodbits_orc_cloth,],
["orc_tribal_b","Untreated_Skin",[("orc_tribal_b",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(3)|head_armor(0)|body_armor(2)|leg_armor(1)|difficulty(0),imodbits_orc_cloth,],
["orc_tribal_c","Untreated_Skin",[("orc_tribal_c",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(3)|head_armor(0)|body_armor(1)|leg_armor(2)|difficulty(0),imodbits_orc_cloth,],
["evil_gauntlets_a","Gauntlets",[("gauntlet_a_L",0)],itp_type_hand_armor|itp_shop,0,500,weight(1)|body_armor(4)|difficulty(0),imodbits_armor],
["evil_gauntlets_b","Gauntlets",[("gauntlet_b_L",0)],itp_type_hand_armor|itp_shop,0,500,weight(1)|body_armor(4)|difficulty(0),imodbits_armor],
#
####TLD ISENGARD ITEMS##########
##########ARMORS##########
["isen_orc_armor_a","Isengard_Orc_Armor",[("orc_isen_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,201,weight(5)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),imodbits_orc_cloth,],
["isen_orc_armor_b","Isengard_Orc_Armor",[("orc_isen_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,401,weight(10)|head_armor(0)|body_armor(10)|leg_armor(3)|difficulty(0),imodbits_orc_cloth,],
["isen_orc_armor_c","Isengard_Orc_Armor",[("orc_isen_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,901,weight(15)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0),imodbits_orc_cloth,],
["isen_orc_armor_d","Isengard_Orc_Armor",[("orc_isen_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1401,weight(19)|head_armor(0)|body_armor(18)|leg_armor(5)|difficulty(0),imodbits_orc_armor,],
["isen_orc_armor_e","Isengard_Orc_Armor",[("orc_isen_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1301,weight(21)|head_armor(0)|body_armor(16)|leg_armor(9)|difficulty(0),imodbits_orc_armor,],
["isen_orc_armor_f","Isengard_Orc_Armor",[("orc_isen_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1401,weight(25)|head_armor(0)|body_armor(18)|leg_armor(9)|difficulty(0),imodbits_orc_armor,],
["isen_orc_armor_g","Isengard_Orc_Armor",[("orc_isen_g",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1501,weight(25)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_light_a","Uruk-hai_Light_Harness",[("urukhai_isen_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,204,weight(4)|head_armor(0)|body_armor(8)|leg_armor(3)|difficulty(0),imodbits_orc_cloth,],
["isen_uruk_light_b","Uruk-hai_Leather_Armor",[("urukhai_isen_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,504,weight(10)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0),imodbits_orc_cloth,],
["isen_uruk_light_c","Uruk-hai_Leather_Armor",[("urukhai_isen_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,704,weight(12)|head_armor(0)|body_armor(13)|leg_armor(9)|difficulty(0),imodbits_orc_cloth,],
["isen_uruk_light_d","Uruk-hai_Mail_and_Leather",[("urukhai_isen_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(0)|body_armor(19)|leg_armor(13)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_light_e","Uruk-hai_Mail_Harness",[("urukhai_isen_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(20)|head_armor(0)|body_armor(17)|leg_armor(12)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_heavy_a","Uruk-hai_Mail_and_Leather",[("urukhai_isen_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_heavy_b","Uruk-hai_Heavy_Armor",[("urukhai_isen_g",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2800,weight(25)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_heavy_c","Uruk-hai_Heavy_Armor",[("urukhai_isen_h",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(26)|head_armor(0)|body_armor(25)|leg_armor(14)|difficulty(0),imodbits_orc_armor,],
["isen_uruk_heavy_d","Uruk-hai_Tracker_Leather",[("urukhai_isen_tracker_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,694,weight(14)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0),imodbits_orc_cloth,],
["isen_uruk_heavy_e","Uruk-hai_Tracker_Leather",[("urukhai_isen_tracker_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,794,weight(15)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0),imodbits_orc_cloth,],
["uruk_tracker_boots","Uruk_Tracker_Boots",[("uruk_furboot_lr",0)],itp_type_foot_armor|itp_shop,0,300,weight(2.2)|leg_armor(12)|difficulty(0),imodbits_orc_cloth],
["uruk_greaves","Uruk_Greaves",[("uruk_greave_lr",0)],itp_type_foot_armor|itp_shop,0,500,weight(4)|leg_armor(15)|difficulty(0),imodbits_orc_armor],
["uruk_chain_greaves","Uruk_Chain_Greaves",[("uruk_chain_greave_lr",0)],itp_type_foot_armor|itp_shop,0,500,weight(3)|leg_armor(15)|difficulty(0),imodbits_orc_armor],
["uruk_ragwrap","Uruk_Ragwrap",[("uruk_ragwrap_lr",0)],itp_type_foot_armor|itp_shop,0,10,weight(1)|leg_armor(3)|difficulty(0),imodbits_orc_armor],
#["isengard_surcoat"  , "Isengard Surcoat"  ,[("uruk_body",0)], itp_shop|itp_type_body_armor  |itp_covers_legs ,0, 500 , weight(25)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(13)|difficulty(8) ,imodbits_armor ],
#########HELMS##########
["isen_orc_helm_a","Isen_Orc_Helm",[("orc_isen_helm_a",0)],itp_type_head_armor|itp_shop,0,300,weight(2)|head_armor(20)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_orc_helm_b","Isen_Orc_Helm",[("orc_isen_helm_b",0)],itp_type_head_armor|itp_shop|itp_fit_to_head,0,350,weight(2)|head_armor(21)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_orc_helm_c","Isen_Orc_Helm",[("orc_isen_helm_c",0)],itp_type_head_armor|itp_shop,0,600,weight(3)|head_armor(25)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_uruk_helm_a","Uruk-Hai_Helm",[("urukhai_helm_a",0)],itp_type_head_armor|itp_shop,0,600,weight(3)|head_armor(25)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_uruk_helm_b","Uruk-Hai_Helm",[("urukhai_helm_b",0)],itp_type_head_armor|itp_shop,0,700,weight(3)|head_armor(27)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_uruk_helm_c","Uruk-Hai_Helm",[("urukhai_helm_c",0)],itp_type_head_armor|itp_shop,0,1000,weight(3.5)|head_armor(30)|difficulty(0),imodbits_elf_armor],
["isen_uruk_helm_d","Uruk-Hai_Captain_Helm",[("urukhai_captainhelm",0)],itp_type_head_armor|itp_shop,0,1200,weight(3.5)|head_armor(31)|difficulty(0),imodbits_elf_armor],
["isen_uruk_helm_e","Uruk-Hai_Tracker_Helm",[("urukhai_trackerhelm_a",0)],itp_type_head_armor|itp_shop,0,500,weight(2)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["isen_uruk_helm_f","Uruk-Hai_Tracker_Helm",[("urukhai_trackerhelm_b",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(25)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
##############WEAPONS##########
########Uruk Weapons
["uruk_pike_a","Uruk_Pike",[("isengard_pike",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_spear|itp_two_handed|itp_wooden_parry,itc_cutting_spear,400,weight(3)|difficulty(0)|spd_rtng(81)|weapon_length(227)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
["uruk_pike_b","Uruk_Pike",[("uruk_skull_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_spear|itp_two_handed|itp_wooden_parry,itc_cutting_spear,400,weight(3)|difficulty(0)|spd_rtng(81)|weapon_length(176)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
["uruk_falchion_a","Uruk_Falchion",[("uruk_falchion_a",0)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardfalchion|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(85)|weapon_length(72)|swing_damage(25,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["uruk_falchion_b","Uruk_Falchion",[("uruk_falchion_b",0)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardfalchion|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(67)|swing_damage(25,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["uruk_spear","Uruk_Spear",[("uruk_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry, itc_staff,300,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(168)|swing_damage(20,blunt)|thrust_damage(27,pierce),imodbits_weapon_wood],
["uruk_skull_spear","Uruk_Skull_Spear",[("uruk_skull_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_couchable, itc_staff,300,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(176)|swing_damage(20,blunt)|thrust_damage(27,pierce),imodbits_weapon_bad],
["uruk_voulge","Uruk_Voulge",[("uruk_voulge",0)],itp_type_polearm|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,400,weight(4.5)|difficulty(0)|spd_rtng(87)|weapon_length(108)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["uruk_heavy_axe","Uruk_Heavy_Axe",[("uruk_heavy_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,300,weight(4.5)|difficulty(0)|spd_rtng(90)|weapon_length(99)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
############Isengard Weapons
["isengard_sword","Isengard_Sword",[("isengard_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_bastardfalchion|itcf_carry_sword_left_hip,105,weight(2.5)|difficulty(0)|spd_rtng(93)|weapon_length(75)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["isengard_axe","Isengard_Axe",[("isengard_axe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,300,weight(2)|difficulty(0)|spd_rtng(85)|weapon_length(73)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["isengard_hammer","Isengard_Hammer",[("isengard_hammer",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,200,weight(3)|difficulty(0)|spd_rtng(85)|weapon_length(61)|swing_damage(24,blunt)|thrust_damage(15,blunt),imodbits_weapon_bad],
["isengard_halberd","Isengard_Halberd",[("isengard_halberd",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_staff,352,weight(4.5)|difficulty(0)|spd_rtng(83)|weapon_length(156)|swing_damage(38,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
["isengard_mallet","Isengard_Mallet",[("isengard_mallet",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack,itc_nodachi,300,weight(7)|difficulty(0)|spd_rtng(82)|weapon_length(83)|swing_damage(35,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["isengard_heavy_axe","Isengard_Heavy_Axe",[("isengard_heavy_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(4.5)|difficulty(0)|spd_rtng(87)|weapon_length(116)|swing_damage(38,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["isengard_heavy_sword","Isengard_Heavy_Sword",[("isengard_heavy_sword",0)],itp_type_two_handed_wpn|itp_primary|itp_cant_use_on_horseback|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_shop,itc_nodachi|itcf_carry_sword_left_hip,500,weight(4.5)|difficulty(0)|spd_rtng(90)|weapon_length(102)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["isengard_spear","Isengard_Spear",[("isengard_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_staff,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(27,pierce),imodbits_weapon_wood],
["isengard_pike","Isengard_Pike",[("isengard_pike",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_cant_use_on_horseback|itp_two_handed|itp_wooden_parry,itc_cutting_spear,500,weight(3.5)|difficulty(0)|spd_rtng(92)|weapon_length(226)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
########shields
["isen_orc_shield_a","Isen_Orc_Shield",[("isen_orc_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["isen_orc_shield_b","Isen_Orc_Shield",[("isen_orc_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["isen_uruk_shield_b","Isen_Uruk_Shield",[("isen_uruk_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,200,weight(4)|hit_points(600)|body_armor(1)|spd_rtng(76)|weapon_length(81),imodbits_shield,],
########Orc Weapons
#
#N/A
["wood_club","Wooden_Club",[("wood_club",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(60)|swing_damage(15,blunt)|thrust_damage(0,blunt),imodbits_weapon_wood],
["twohand_wood_club","Large_Wooden_Club",[("twohand_wood_club",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_shop|itp_wooden_attack,itc_nodachi|itcf_carry_axe_back,10,weight(3.5)|difficulty(0)|spd_rtng(85)|weapon_length(79)|swing_damage(25,blunt)|thrust_damage(0,blunt),imodbits_weapon_wood],
#
["bone_cudgel","Bone_Cudgel",[("bone_cudgel",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(53)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["skull_club","Skull_Club",[("skull_club",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(55)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_club_a","Orc_Club",[("orc_club_a",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(62)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_club_b","Orc_Club",[("orc_club_b",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(65)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_club_c","Orc_Club",[("orc_club_c",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(75)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_club_d","Orc_Club",[("orc_club_d",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_no_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,5,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(67)|swing_damage(15,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_sledgehammer","Orc_Sledgehammer",[("orc_sledgehammer",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_no_parry|itp_wooden_attack|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_back,100,weight(7)|difficulty(0)|spd_rtng(80)|weapon_length(75)|swing_damage(30,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["orc_simple_spear","Orc_Spear",[("orc_simple_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_no_parry|itp_covers_head,itc_spear,100,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(152)|swing_damage(15,blunt)|thrust_damage(22,pierce),imodbits_weapon_wood],
["orc_skull_spear","Orc_Skull_Spear",[("orc_skull_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_no_parry|itp_covers_head,itc_spear,200,weight(3)|difficulty(0)|spd_rtng(92)|weapon_length(162)|swing_damage(15,blunt)|thrust_damage(27,pierce),imodbits_weapon_wood],
["orc_bill","Orc_Bill",[("orc_bill",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_no_parry|itp_cant_use_on_horseback,itc_staff|itcf_carry_spear,400,weight(4.5)|difficulty(0)|spd_rtng(83)|weapon_length(122)|swing_damage(30,cut)|thrust_damage(12,pierce),imodbits_weapon_bad],
["orc_slasher","Orc_Slasher",[("orc_slasher",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(54)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_falchion","Orc_Falchion",[("orc_falchion",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(65)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_scimitar","Orc_Scimitar",[("orc_scimitar",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(56)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_sabre","Orc_Sabre",[("orc_sabre",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(1.5)|difficulty(0)|spd_rtng(85)|weapon_length(71)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_machete","Orc_Machete",[("orc_machete",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_no_parry,itc_scimitar|itcf_carry_sword_left_hip,200,weight(1.5)|difficulty(0)|spd_rtng(90)|weapon_length(55)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_axe","Orc_Axe",[("orc_axe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_no_parry,itc_scimitar|itcf_carry_axe_left_hip,300,weight(2)|difficulty(0)|spd_rtng(85)|weapon_length(61)|swing_damage(25,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_two_handed_axe","Orc_Double_Handed_Axe",[("orc_twohanded_axe",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_no_parry|itp_shop|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,500,weight(4.5)|difficulty(0)|spd_rtng(90)|weapon_length(84)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["orc_throwing_axes","Orc_Throwing_Axes",[("orc_throwing_axe",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_axe,150,weight(5)|difficulty(0)|shoot_speed(20)|spd_rtng(99)|weapon_length(33)|thrust_damage(45,cut)|max_ammo(3),imodbits_thrown],
["orc_bow","Orc_Bow",[("orc_bow",0),("orc_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_shop,itcf_shoot_ganstabow|itcf_carry_bowcase_left,200,weight(1.25)|difficulty(0)|shoot_speed(53)|spd_rtng(86)|thrust_damage(20,cut),imodbits_bow],
# uruk_bow is a orc_bow intended for uruks/humans (vertical shooting position)
####Orc Shields
["orc_shield_a","Orc_Shield",[("orc_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(100)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["orc_shield_b","Orc_Shield",[("orc_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(100)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["orc_shield_c","Orc_Shield",[("orc_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,100,weight(3)|hit_points(100)|body_armor(1)|spd_rtng(76)|weapon_length(81),imodbits_shield,],
["mordor_orc_shield_a","Mordor_Orc_Shield",[("mordor_orc_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(200)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_orc_shield_b","Mordor_Orc_Shield",[("mordor_orc_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(200)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_orc_shield_c","Mordor_Orc_Shield",[("mordor_orc_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(200)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_orc_shield_d","Mordor_Orc_Shield",[("mordor_orc_shield_d",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(200)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_orc_shield_e","Mordor_Orc_Shield",[("mordor_orc_shield_e",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(200)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_uruk_shield_a","Mordor_Uruk_Shield",[("mordor_uruk_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_round_shield,100,weight(4)|hit_points(310)|body_armor(3)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_uruk_shield_b","Mordor_Uruk_Shield",[("mordor_uruk_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_round_shield,100,weight(4)|hit_points(310)|body_armor(4)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_uruk_shield_c","Mordor_Uruk_Shield",[("mordor_uruk_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_round_shield,100,weight(4)|hit_points(310)|body_armor(3)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_man_shield_a","Mordor_Man_Shield",[("mordor_man_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(3)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["mordor_man_shield_b","Mordor_Man_Shield",[("mordor_man_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(3)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["angmar_shield","Angmar_Shield",[("angmar_shield",0)],itp_type_shield|itp_wooden_parry|itp_unique,itcf_carry_round_shield,3000,weight(4)|hit_points(1600)|body_armor(20)|spd_rtng(96)|weapon_length(40),0,],
#### Generic orc helmets
["orc_helm_a","Orc_Longnosehelm",[("orc_helm_a",0)],itp_type_head_armor|itp_shop,0,300,weight(2)|head_armor(14)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_b","Orc_Gratehelm",[("orc_helm_b",0)],itp_type_head_armor|itp_shop,0,350,weight(2.5)|head_armor(22)|difficulty(0),imodbits_orc_cloth],
["orc_helm_c","Orc_Buckethelm",[("orc_helm_c",0)],itp_type_head_armor|itp_shop,0,400,weight(3)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_d","Orc_Grillhelm",[("orc_helm_d",0)],itp_type_head_armor|itp_shop,0,350,weight(2.5)|head_armor(22)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_e","Orc_Beakhelm",[("orc_helm_e",0)],itp_type_head_armor|itp_shop,0,400,weight(3)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_f","Orc_Bughelm",[("orc_helm_f",0)],itp_type_head_armor|itp_shop,0,500,weight(3)|head_armor(24)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_g","Orc_Crowhelm",[("orc_helm_g",0)],itp_type_head_armor|itp_shop,0,400,weight(3)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_h","Orc_Jawhelm",[("orc_helm_h",0)],itp_type_head_armor|itp_shop,0,500,weight(3)|head_armor(24)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_i","Orc_Snouthelm",[("orc_helm_i",0)],itp_type_head_armor|itp_shop,0,600,weight(3)|head_armor(25)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_j","Orc_Lizardhelm",[("orc_helm_j",0)],itp_type_head_armor|itp_shop,0,400,weight(3)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["orc_helm_k","Orc_Vulturehelm",[("orc_helm_k",0)],itp_type_head_armor|itp_shop,0,500,weight(3)|head_armor(24)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
#TLD MORDOR ITEMS##########
###ORC ARMORS##########
["m_orc_light_a","Mordor_Orc_Light_Armor",[("orc_mordor_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,101,weight(1.5)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),imodbits_orc_cloth,],
["m_orc_light_b","Mordor_Orc_Light_Armor",[("orc_mordor_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,101,weight(3)|head_armor(0)|body_armor(7)|leg_armor(5)|difficulty(0),imodbits_orc_cloth,],
["m_orc_light_c","Mordor_Orc_Light_Armor",[("orc_mordor_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,201,weight(3)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0),imodbits_orc_cloth,],
["m_orc_light_d","Mordor_Orc_Light_Armor",[("orc_mordor_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,501,weight(5)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0),imodbits_orc_cloth,],
["m_orc_light_e","Mordor_Orc_Light_Armor",[("orc_mordor_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,501,weight(6)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0),imodbits_orc_cloth,],
["m_orc_heavy_a","Mordor_Orc_Heavy_Armor",[("orc_mordor_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,801,weight(15)|head_armor(0)|body_armor(17)|leg_armor(8)|difficulty(0),imodbits_orc_cloth,],
["m_orc_heavy_b","Mordor_Orc_Heavy_Armor",[("orc_mordor_g",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1001,weight(17)|head_armor(0)|body_armor(18)|leg_armor(7)|difficulty(0),imodbits_orc_armor,],
["m_orc_heavy_c","Mordor_Orc_Heavy_Armor",[("orc_mordor_h",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1001,weight(18)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0),imodbits_orc_armor,],
["m_orc_heavy_d","Mordor_Orc_Heavy_Armor",[("orc_mordor_i",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1501,weight(22)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_orc_armor,],
["m_orc_heavy_e","Mordor_Orc_Heavy_Armor",[("orc_mordor_j",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2001,weight(22)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0),imodbits_orc_armor,],
["m_uruk_light_a","Uruk_Harness",[("uruk_mordor_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,402,weight(10)|head_armor(0)|body_armor(9)|leg_armor(3)|difficulty(0),imodbits_orc_cloth,],
["m_uruk_light_b","Uruk_Thick_Harness",[("uruk_mordor_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,502,weight(12)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),imodbits_orc_cloth,],
["m_uruk_heavy_c","Uruk_Leather_Armor",[("uruk_mordor_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,802,weight(15)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0),imodbits_orc_cloth,],
["m_uruk_heavy_d","Uruk_Segmented_Armor",[("uruk_mordor_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,602,weight(15)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0),imodbits_orc_cloth,],
["m_uruk_heavy_e","Uruk_Mail",[("uruk_mordor_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1502,weight(22)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0),imodbits_orc_armor,],
["m_uruk_heavy_f","Uruk_Mail",[("uruk_mordor_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(22)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0),imodbits_orc_armor,],
["m_uruk_heavy_g","Uruk_Mail",[("uruk_mordor_g",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(22)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0),imodbits_orc_armor,],
["m_uruk_heavy_h","Uruk_Scale",[("uruk_mordor_h",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(21)|head_armor(0)|body_armor(22)|leg_armor(10)|difficulty(0),imodbits_orc_armor,],
["m_uruk_heavy_i","Uruk_Thick_Scale",[("uruk_mordor_i",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(24)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["m_uruk_heavy_j","Uruk_Heavy_Armor",[("uruk_mordor_j",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(26)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["m_uruk_heavy_k","Uruk_Guard_Armor",[("uruk_mordor_k",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2500,weight(28)|head_armor(0)|body_armor(26)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["m_cap_armor","Mordor_Captain_Armor",[("mordor_captain_armor",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(30)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(0),imodbits_elf_armor,],
["black_num_armor","Black_Numenorean_Armor",[("black_numenor_armor",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,4000,weight(30)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0),imodbits_elf_armor,],
["m_armor_a","Mordor_Armor",[("mordor_armor_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(15)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["m_armor_b","Mordor_Armor",[("mordor_armor_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(15)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["evil_light_armor","Sinister_Garb",[("evil_light_armor",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(10)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0),imodbits_orc_cloth,],
######HELMS##########
["uruk_helm_a","Uruk_Helm",[("uruk_helm_a",0)],itp_type_head_armor|itp_shop,0,700,weight(3)|head_armor(27)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["uruk_helm_b","Uruk_Helm",[("uruk_helm_b",0)],itp_type_head_armor|itp_shop,0,800,weight(3)|head_armor(29)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["uruk_helm_c","Uruk_Beak_Helm",[("uruk_helm_c",0)],itp_type_head_armor|itp_shop,0,700,weight(3)|head_armor(27)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["uruk_helm_d","Uruk_Grill_Helm",[("uruk_helm_d",0)],itp_type_head_armor|itp_shop,0,750,weight(3)|head_armor(28)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["uruk_helm_e","Uruk_Mask_Helm",[("uruk_helm_e",0)],itp_type_head_armor|itp_shop,0,900,weight(4)|head_armor(32)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["uruk_helm_f","Uruk_Helm",[("uruk_helm_f",0)],itp_type_head_armor|itp_shop,0,800,weight(3.5)|head_armor(30)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
#####HELMS##########
["mordor_cap_helm","Mordor_Captain_Helm",[("mordor_captain_helmet",0)],itp_type_head_armor|itp_shop,0,2000,weight(3)|head_armor(37)|difficulty(0),imodbits_elf_armor],
["mordor_helm","Mordor_Helm",[("mordor_helmet_a",0)],itp_type_head_armor|itp_shop,0,1400,weight(3)|head_armor(33)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["black_num_helm","Black_Numenorean_Helm",[("black_numenor_helmet",0)],itp_type_head_armor|itp_shop,0,3000,weight(3)|head_armor(38)|difficulty(0),imodbits_elf_armor],
#######WEAPONS##########
["mordor_sword","Bastard_Sword_of_Mordor",[("mordor_sword",0)],itp_type_two_handed_wpn|itp_primary|itp_shop,itc_bastardsword|itcf_carry_sword_back,294,weight(2.25)|difficulty(0)|spd_rtng(98)|weapon_length(109)|swing_damage(37,cut)|thrust_damage(26,pierce),imodbits_weapon_bad],
["mordor_longsword","Sword_of_Mordor",[("sword_of_mordor",0),("scab_sword_of_mordor",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(2.75)|difficulty(0)|spd_rtng(95)|weapon_length(125)|swing_damage(39,cut)|thrust_damage(31,pierce),imodbits_weapon_bad],
##TLD MORIA ITEMS##########
#["goblin_king_sword",         "Goblin King's Sword",[("orc_slasher",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
#["moria_sword", "Goblin Slasher",[("orc_slasher",0)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#########ARMORS##########
["moria_armor_a","Moria_Breast_Harness",[("orc_moria_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,201,weight(10)|head_armor(0)|body_armor(6)|leg_armor(4)|difficulty(0),imodbits_orc_armor | imodbit_cracked,],
["moria_armor_b","Moria_Breast_and_Shoulders",[("orc_moria_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,501,weight(12)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0),imodbits_orc_armor | imodbit_cracked,],
["moria_armor_c","Moria_Orc_Mail",[("orc_moria_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,901,weight(19)|head_armor(0)|body_armor(16)|leg_armor(7)|difficulty(0),imodbits_orc_armor,],
["moria_armor_d","Moria_Bolted_Leather",[("orc_moria_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1101,weight(22)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0),imodbits_orc_armor,],
["moria_armor_e","Moria_Orc_Heavy_Mail",[("orc_moria_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1401,weight(24)|head_armor(0)|body_armor(23)|leg_armor(11)|difficulty(0),imodbits_elf_armor,],
#######SHIELDS##########
["moria_orc_shield_a","Moria_Orc_Shield",[("moria_orc_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["moria_orc_shield_b","Moria_Orc_Shield",[("moria_orc_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
["moria_orc_shield_c","Moria_Orc_Shield",[("moria_orc_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(3)|hit_points(310)|body_armor(1)|spd_rtng(96)|weapon_length(40),imodbits_shield,],
###TLD GUNDABAD ITEMS##########
#ARMORS##########
["gundabad_armor_a","Gundabad_Orc_Rags",[("orc_gunda_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,201,weight(15)|head_armor(0)|body_armor(5)|leg_armor(4)|difficulty(0),imodbits_orc_cloth,],
["gundabad_armor_b","Gundabad_Orc_Fur",[("orc_gunda_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,501,weight(18)|head_armor(0)|body_armor(9)|leg_armor(6)|difficulty(0),imodbits_orc_cloth,],
["gundabad_armor_c","Gundabad_Orc_Armor",[("orc_gunda_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,901,weight(20)|head_armor(0)|body_armor(14)|leg_armor(7)|difficulty(0),imodbits_orc_armor,],
["gundabad_armor_d","Gundabad_Orc_Armor",[("orc_gunda_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1101,weight(24)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0),imodbits_orc_armor,],
["gundabad_armor_e","Gundabad_Orc_Heavy_Armor",[("orc_gunda_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1401,weight(25)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
#HELMS##########
["gundabad_helm_a","Gundabad_Cap",[("orc_gunda_cap",0)],itp_type_head_armor|itp_shop,0,200,weight(1)|head_armor(12)|difficulty(0),imodbits_orc_cloth],
["gundabad_helm_b","Gundabad_Helm",[("orc_gunda_helm_a",0)],itp_type_head_armor|itp_shop,0,300,weight(2)|head_armor(18)|difficulty(0),imodbits_orc_cloth],
["gundabad_helm_c","Gundabad_Helm",[("orc_gunda_helm_b",0)],itp_type_head_armor|itp_shop,0,350,weight(2)|head_armor(22)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["gundabad_helm_d","Gundabad_Helm",[("orc_gunda_helm_c",0)],itp_type_head_armor|itp_shop,0,400,weight(2)|head_armor(23)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
["gundabad_helm_e","Wargrider_Helm",[("orc_wargrider_helm",0)],itp_type_head_armor|itp_fit_to_head,0,350,weight(1.5)|head_armor(25)|difficulty(0),imodbits_orc_armor | imodbit_cracked],
#WEAPONS##########
#["gundabad_sabre", "Gundabad Sabre",[("orc_sabre",0),("scab_orc_sabre", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
####DUNLAND ITEMS##########
["dunland_wolfboots","Dunland_Wolfboots",[("dunland_wolfboots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,300,weight(3)|leg_armor(10)|difficulty(0),imodbits_cloth],
##ARMORS########
["dunland_armor_a","Dunnish_Fur_Armor",[("dunland_fur_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,300,weight(14)|head_armor(1)|body_armor(10)|leg_armor(4)|difficulty(0),imodbits_cloth,],
["dunland_armor_b","Dunnish_Fur_Armor",[("dunland_fur_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(15)|head_armor(1)|body_armor(12)|leg_armor(8)|difficulty(0),imodbits_cloth,],
["dunland_armor_c","Dunnish_Fur_Armor",[("dunland_fur_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(15)|head_armor(1)|body_armor(12)|leg_armor(8)|difficulty(0),imodbits_cloth,],
["dunland_armor_d","Dunnish_Fur_Armor",[("dunland_fur_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,350,weight(14)|head_armor(1)|body_armor(12)|leg_armor(4)|difficulty(0),imodbits_cloth,],
["dunland_armor_e","Dunnish_Fur_Armor",[("dunland_fur_e",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(15)|head_armor(1)|body_armor(14)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["dunland_armor_g","Dunnish_Fur_Armor",[("dunland_fur_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(16)|head_armor(1)|body_armor(14)|leg_armor(8)|difficulty(0),imodbits_cloth,],
["dunland_armor_h","Dun_Long_Fur_Armor",[("dunland_long_fur",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(16)|head_armor(2)|body_armor(16)|leg_armor(9)|difficulty(0),imodbits_cloth,],
["dunland_armor_i","Dunnish_Hauberk",[("dunland_hauberk_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(23)|head_armor(2)|body_armor(22)|leg_armor(7)|difficulty(0),imodbits_armor,],
["dunland_armor_j","Dunland_Hauberk",[("dunland_hauberk_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(23)|head_armor(2)|body_armor(22)|leg_armor(10)|difficulty(0),imodbits_armor,],
["dunland_armor_k","Dun_Chief_Armor",[("dunland_chieftain",0), ("dunland_chieftain_spirit",imodbit_old),("barf_skeleton_greaves", imodbit_poor)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(26)|head_armor(2)|body_armor(25)|leg_armor(13)|difficulty(0),imodbits_elf_armor,],
#######HELMS##########
["dun_helm_a","Dunnish_Wolf_Cap",[("dunland_wolfcap",0)],itp_type_head_armor|itp_shop,0,300,weight(2)|head_armor(25)|difficulty(0),imodbits_cloth],
["dun_helm_b","Dunnish_Antler_Cap",[("dunland_antlercap",0)],itp_type_head_armor|itp_shop,0,200,weight(2)|head_armor(21)|difficulty(0),imodbits_cloth],
["dun_helm_c","Dunnish_Tall_Helm",[("dunland_helm_a",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["dun_helm_d","Dunnish_Tall_Helm",[("dunland_helm_c",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["dun_helm_e","Dun_Tall_War_Helm",[("dunland_helm_b",0)],itp_type_head_armor|itp_shop,0,1200,weight(3)|head_armor(35)|difficulty(0),imodbits_elf_armor],
#["dun_helm_f", "Dunnish Helm",[("dunland_helm_c",0)], itp_shop|itp_type_head_armor,0, 980 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#######SHIELDS##########
["dun_shield_a","Dunnish_Shield",[("dun_roundshield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,120,weight(2)|hit_points(500)|body_armor(3)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["dun_shield_b","Dunnish_Shield",[("dun_roundshield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,100,weight(2)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
#["dun_shield_c", "Dunnish Shield",[("dunland_shield_c",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dun_shield_z", "Dunnish Shield",[("dunland_shield_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dun_shield_e", "Dunnish Shield",[("dunland_shield_e",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dun_shield_f", "Dunnish Shield",[("dunland_shield_f_spike",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dun_shield_g", "Dunnish Shield",[("dunland_shield_g",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#WEAPONS##########
["dun_berserker","Dunland_Chieftain_Sword",[("dunland_sword",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,400,weight(1.25)|difficulty(0)|spd_rtng(140)|weapon_length(98)|swing_damage(33,cut)|thrust_damage(24,pierce),imodbits_weapon_bad],
["dunnish_antler_axe","Dunnish_Antler_Axe",[("dunland_antleraxe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(85)|weapon_length(73)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["dunnish_war_axe","Dunnish_War_Axe",[("dunland_axe_a",0)],itp_type_one_handed_wpn|itp_shop|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(97)|weapon_length(50)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["dunnish_axe","Dunnish_Axe",[("dunland_axe_b",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(50)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["dunland_spear","Dunnish_Spear",[("dunland_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_spear,125,weight(2)|difficulty(0)|spd_rtng(95)|weapon_length(150)|swing_damage(12,blunt)|thrust_damage(20,pierce),imodbits_weapon_wood],
["dunnish_pike","Dunnish_Pike",[("dunland_pike",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_cant_use_on_horseback|itp_penalty_with_shield|itp_wooden_parry,itc_pike,400,weight(3)|difficulty(0)|spd_rtng(85)|weapon_length(205)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
####TLD ROHAN ITEMS##########
########ARMORS##########
["rohan_armor_a","Rohan_Shirt",[("L_roh_shirt_M1",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,200,weight(2)|head_armor(0)|body_armor(3)|leg_armor(2)|difficulty(0),imodbits_cloth,],
["rohan_armor_b","Rohan_Shirt_Cape",[("L_roh_shirt_cape_M2",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(3)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["rohan_armor_c","Rohan_Long_Shirt",[("L_roh_long_shirt_cape_M4",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(5)|head_armor(0)|body_armor(8)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["rohan_armor_d","Rohan_Hauberk",[("LH_roh_hauberk_cape_a_M6",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0),imodbits_armor,],
["rohan_armor_e","Rohan_Hauberk",[("LH_roh_hauberk_cape_b_M7",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0),imodbits_armor,],
["rohan_armor_f","Rohan_Hauberk",[("LH_roh_hauberk_cape_c_M5",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(12)|head_armor(0)|body_armor(22)|leg_armor(9)|difficulty(0),imodbits_armor,],
["rohan_armor_g","Rohan_Mail_Shirt",[("M_roh_shirt_cape_b_M2",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(15)|head_armor(0)|body_armor(18)|leg_armor(7)|difficulty(0),imodbits_armor,],
["rohan_armor_h","Rohan_Long_Mail",[("M_roh_long_shirt_cape_b_M4",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,750,weight(15)|head_armor(0)|body_armor(18)|leg_armor(9)|difficulty(0),imodbits_armor,],
["rohan_armor_i","Rohan_Long_Mail",[("M_roh_long_shirt_cape_c_M3",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(15)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0),imodbits_armor,],
["rohan_armor_j","Rohan_Hauberk",[("MH_roh_hauberk_leather_cape_a_M6",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(17)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(0),imodbits_armor,],
["rohan_armor_k","Rohan_Hauberk",[("MH_roh_hauberk_leather_cape_b_M7",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(17)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(0),imodbits_armor,],
["rohan_armor_l","Rohan_Hauberk",[("MH_roh_hauberk_leather_cape_c_M8",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1600,weight(18)|head_armor(0)|body_armor(33)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["rohan_armor_m","Rohan_Scale_Armor",[("H_roh_scale_cape_a_M10",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(15)|head_armor(0)|body_armor(31)|leg_armor(10)|difficulty(0),imodbits_armor,],
["rohan_armor_n","Rohan_Scale_Armor",[("H_roh_scale_cape_b_M11",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(15)|head_armor(0)|body_armor(31)|leg_armor(10)|difficulty(0),imodbits_armor,],
["rohan_armor_o","Rohan_Scale_Armor",[("H_roh_scale_cape_c_M12",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1600,weight(15)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0),imodbits_armor,],
["rohan_armor_p","Rohan_Armor",[("E_roh_hauberk_a_cape_M13",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(20)|head_armor(0)|body_armor(33)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["rohan_armor_q","Rohan_Armor",[("E_roh_hauberk_b_cape_M14",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(20)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["rohan_armor_r","Rohan_Armor",[("E_roh_hauberk_c_cape_M15",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(20)|head_armor(0)|body_armor(33)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["rohan_armor_s","Rohan_Heraldric_Mail",[("VH_heraldic_rohan_armor_M16",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(22)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(0),imodbits_elf_armor,[(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
##HELMS##########
["rohan_light_helmet_a","Rohan_Light_Helm",[("rohan_light_helmet_a",0)],itp_type_head_armor|itp_shop,0,500,weight(1)|head_armor(23)|difficulty(0),imodbits_cloth],
["rohan_light_helmet_b","Rohan_Light_Helmet",[("rohan_light_helmet_b",0)],itp_type_head_armor|itp_shop,0,600,weight(1)|head_armor(25)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_inf_helmet_a","Rohan_Infantry_Helm",[("rohan_inf_helmet_a",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_inf_helmet_b","Rohan_Infantry_Helm",[("rohan_inf_helmet_b",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_archer_helmet_a","Rohan_Archer_Helmet",[("rohan_archer_helmet_a",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_archer_helmet_b","Rohan_Archer_Helmet",[("rohan_archer_helmet_b",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_archer_helmet_c","Rohan_Horse_Archer_Helmet",[("rohan_archer_helmet_c",0)],itp_type_head_armor|itp_shop,0,1100,weight(2)|head_armor(32)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_cav_helmet_a","Rohan_Cavalry_Helmet",[("rohan_cav_helmet_a",0)],itp_type_head_armor|itp_shop,0,1300,weight(2)|head_armor(34)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_cav_helmet_b","Rohan_Cavalry_Helmet",[("rohan_cav_helmet_b",0)],itp_type_head_armor|itp_shop,0,1300,weight(2)|head_armor(34)|difficulty(0),imodbits_armor | imodbit_cracked],
["rohan_cav_helmet_c","Rohan_Cavalry_Helmet",[("rohan_cav_helmet_c",0)],itp_type_head_armor|itp_shop,0,1500,weight(2)|head_armor(36)|difficulty(0),imodbits_elf_armor],
["rohan_captain_helmet","Rohan_Captain_Helmet",[("rohan_captain_helmet",0)],itp_type_head_armor|itp_shop,0,3000,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
##SHIELDS##########
["rohan_shield_a","Rohan_Shield",[("rohan_shield_green",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(310)|body_armor(4)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",0,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_plain_shield",":p")])]],
["rohan_shield_b","Rohan_Shield",[("rohan_shield_red",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(310)|body_armor(4)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",0,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_plain_shield",":p")])]],
["rohan_shield_c","Rohan_Shield",[("rohan_shield_plain",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(310)|body_armor(4)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",0,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_plain_shield",":p")])]],
["rohan_shield_d","Rohan_Shield",[("rohan_shield_green_boss",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2.5)|hit_points(400)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",4,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_boss_shield" ,":p")])]],
["rohan_shield_e","Rohan_Shield",[("rohan_shield_red_boss",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2.5)|hit_points(400)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",4,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_boss_shield" ,":p")])]],
["rohan_shield_f","Rohan_Shield",[("rohan_shield_plain_boss",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,400,weight(2.5)|hit_points(400)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(store_random_in_range,":p",4,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_boss_shield" ,":p")])]],
["rohan_shield_g","Rohan_Royal_Shield",[("rohan_shield_royal",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,600,weight(3)|hit_points(600)|body_armor(12)|spd_rtng(96)|weapon_length(40),imodbits_shield_good,[(ti_on_init_item,[(store_random_in_range,":p",4,7), (val_add,":p","mesh_rohan_paint_1"),(cur_item_set_tableau_material, "tableau_rohan_boss_shield" ,":p")])]],
#["rohan_shield_h", "Rohan Shield",[("rohanshield_iron"   ,0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield ],
#["rohan_shield_i","Rohan Shield",[("rohanshield_noble_gilt",0)],itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield ],
#["rohan_shield_j","Rohan Shield",[("rohanshield_oval_gilt",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield ],
#["rohan_shield_k", "Rohan Noble Shield",[("rohanshield_noble_a",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield ],
#["rohan_shield_l", "Rohan Noble Shield",[("rohanshield_noble_b",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield ],
##FOOTGEAR##########
["rohan_light_greaves","Rohan_Light_Greaves",[("M_rohan_light_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1200,weight(2)|leg_armor(15)|difficulty(0),imodbits_cloth],
["rohirrim_war_greaves","Rohirrim_War_Greaves",[("H_rohan_scale_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1200,weight(3.5)|leg_armor(26)|difficulty(0),imodbits_elf_armor],
["rohan_shoes","Leather_Shoes",[("L_rohan_shoes",0)],itp_type_foot_armor|itp_shop|itp_attach_armature|itp_civilian,0,50,weight(1)|leg_armor(8)|difficulty(0),imodbits_cloth],
##WEAPONS##########
["rohan_cav_sword","Rohan_Riding_Sword",[("rohan_sword_a",0),("scab_rohan_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.5)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(31,cut)|thrust_damage(21,pierce),imodbits_weapon],
["rohan_inf_sword","Rohan_Sword",[("rohan_sword_b",0),("scab_rohan_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(100)|weapon_length(95)|swing_damage(29,cut)|thrust_damage(22,pierce),imodbits_weapon],
["rohan_spear","Rohan_Spear",[("rohan_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_rohan_spear,189,weight(2.5)|difficulty(0)|spd_rtng(92)|weapon_length(170)|swing_damage(16,blunt)|thrust_damage(37,pierce),imodbits_weapon_wood],
["rohan_lance","Rohan_Lance",[("rohan_lance",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_pike,300,weight(2.5)|difficulty(0)|spd_rtng(88)|weapon_length(208)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
# rohan_lance_standard
["rohan_sword_c","Rohan_Sword",[("rohan_sword_c",0),("scab_rohan_sword_c",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(96)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon],
["rohirrim_short_axe","Rohirrim_Short_Axe",[("rohan_1haxe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(110)|weapon_length(50)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon],
["rohirrim_long_hafted_axe","Rohirrim_Long_Hafted_Axe",[("rohan_2haxe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(92)|weapon_length(70)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon],
["rohan_2h_sword","Rohan_War_Sword",[("rohan_sword_a_2h",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_shop|itp_cant_use_on_horseback,itc_greatsword|itcf_carry_sword_back,524,weight(3)|difficulty(0)|spd_rtng(94)|weapon_length(101)|swing_damage(40,cut)|thrust_damage(31,pierce),imodbits_weapon],
###TLD WOODELF ITEMS##########
#ARMORS##########
["mirkwood_light_scale","Light_Woodelf_Scale",[("mirkwood_light_scale",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(12)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["mirkwood_armor_a","Light_Leather",[("mirkwood_leather",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(10)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,],
["mirkwood_armor_b","Light_Quilted_and_Scale_Armor",[("mirkwood_scalequilted_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1100,weight(12)|head_armor(0)|body_armor(32)|leg_armor(16)|difficulty(0),imodbits_elf_armor,],
["mirkwood_armor_c","Light_Scale_over_Mail",[("mirkwood_scaleovermaille_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(12)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0),imodbits_elf_armor,],
["mirkwood_armor_d","Light_Quilted_Surcoat",[("mirkwood_quiltedsurcoat_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(13)|head_armor(0)|body_armor(28)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["mirkwood_armor_e","Light_Mail_and_Surcoat",[("mirkwood_maillewithsurcoat_01",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2500,weight(15)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(0),imodbits_elf_armor,],
["mirkwood_armor_f","Royal_Woodelf_Armor",[("mirkwood_royal",0)], itp_type_body_armor  |itp_covers_legs ,0, 4000, weight(20)|abundance(100)|head_armor(3)|body_armor(50)|leg_armor(16)|difficulty(0) ,imodbits_elf_armor ],
#WEAPONS##########
["mirkwood_great_spear","Mirkwood_Great_Spear",[("mirkwood_great_spear_large",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_pike,900,weight(2.5)|difficulty(0)|spd_rtng(101)|weapon_length(148)|swing_damage(0,blunt)|thrust_damage(35,pierce),imodbits_weapon_good],
["mirkwood_war_spear","Mirkwood_War_Spear",[("mirkwood_war_spear",0)],            itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_cutting_spear,500,weight(2.5)|difficulty(0)|spd_rtng(99)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(31,pierce),imodbits_weapon_good],
["mirkwood_short_spear","Mirkwood_Spear",[("mirkwood_short_spear",0)],            itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_cutting_spear,500,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(117)|swing_damage(20,blunt)|thrust_damage(27,pierce),imodbits_weapon_good],
["mirkwood_knife","Mirkwood_White_Knife",[("mirkwood_white_knife",0),("scab_mirkwood_white_knife",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_primary|itp_secondary|itp_no_parry,itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(0.75)|difficulty(0)|spd_rtng(120)|weapon_length(51)|swing_damage(24,cut)|thrust_damage(17,pierce),imodbits_weapon_bad],
#["mirkwood_arrows","Mirkwood Arrows",[("green_elf_arrow",0),("flying_missile",ixmesh_flying_ammo),("mirkwood_quiver", ixmesh_carry)], itp_type_arrows|itp_shop, itcf_carry_quiver_back_right , 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,bow_damage)|max_ammo(29),imodbits_missile],
#["elf_war_spear", "Elf War Spear",[("elf_spear_1",0)], itp_type_polearm|itp_shop|itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,390 , weight(2.5)|difficulty(0)|spd_rtng(97) | weapon_length(185)|swing_damage(20 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["mirkwood_sword","Mirkwood_Sword",[("mirkwood_longsword",0),("scab_mirkwood_longsword",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700,weight(1.25)|difficulty(0)|spd_rtng(96)|weapon_length(92)|swing_damage(30,cut)|thrust_damage(25,pierce),imodbits_weapon_good],
#SHIELDS##########
["mirkwood_spear_shield_a","Mirkwood_Spearman_Shield",[("mirkwood_spear_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_kite_shield,1000,weight(3)|hit_points(1000)|body_armor(20)|spd_rtng(82)|weapon_length(90),imodbits_shield_good,],
["mirkwood_spear_shield_b","Mirkwood_War_Shield",[("mirkwood_med_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,1000,weight(2)|hit_points(800)|body_armor(15)|spd_rtng(90)|weapon_length(60),imodbits_shield_good,],
["mirkwood_spear_shield_c","Mirkwood_Swordsman_Shield",[("mirkwood_royal_round",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,1000,weight(2)|hit_points(1000)|body_armor(20)|spd_rtng(82)|weapon_length(90),imodbits_shield_good,],
#["mirkwood_spear_shield_d", "Mirkwood Spearman Shield",[("elven_oval_a"         ,0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#HELMETS##########
["mirkwood_helm_a","Mirkwood_Archer_Helm",[("mirkwood_helm",0)],itp_type_head_armor|itp_shop,0,1300,weight(1)|head_armor(37)|difficulty(0),imodbits_elf_armor],
["mirkwood_helm_b","Mirkwood_Helm",[("mirkwoodnormalspearman",0)],itp_type_head_armor|itp_shop,0,1800,weight(1)|head_armor(42)|difficulty(0),imodbits_elf_armor],
["mirkwood_helm_c","Mirkwood_Royal_Spearman_Helm",[("mirkwoodroyalspearman",0)],itp_type_head_armor|itp_shop,0,2000,weight(1.2)|head_armor(45)|difficulty(0),imodbits_elf_armor],
["mirkwood_helm_d","Mirkwood_Royal_Archer_Helm",[("mirkwoodroyalarcher",0)],itp_type_head_armor|itp_shop,0,2100,weight(1.2)|head_armor(45)|difficulty(0),imodbits_elf_armor],
####BOOTS
["mirkwood_boots","Mirkwood_boots",[("mirkwood_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1200,weight(1)|leg_armor(23)|difficulty(0),imodbits_elf_cloth],
["mirkwood_leather_greaves","Mirkwood_Leather_Greaves",[("mirkwood_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1500,weight(1)|leg_armor(28)|difficulty(0),imodbits_elf_cloth],
#####TLD HARAD ITEMS##########
###########ARMOR##########
#########HARONDOR##
["harad_tunic","Harad_Tunic",[("harad_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,300,weight(7)|head_armor(0)|body_armor(8)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["harad_padded","Harondor_Padded_Armor",[("harad_padded",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(13)|head_armor(0)|body_armor(14)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["harad_hauberk","Harondor_Hauberk",[("harad_hauberk",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(20)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_armor,],
["harad_lamellar","Harasjala_Armor",[("harad_lamellar",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1300,weight(22)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_armor,],
["harad_heavy","Harad_Swordsman_Armor",[("harad_heavy",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,4000,weight(22)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0),imodbits_elf_armor,],
["harad_skirmisher","Light_Harad_Garb",[("harad_skirmisher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(7)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["harad_archer","Harad_Archer_Armor",[("harad_archer",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(14)|head_armor(0)|body_armor(16)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["black_snake_armor","Maranka_Armor",[("black_snake_armor",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(20)|head_armor(2)|body_armor(30)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["harad_champion","Far_Harad_Garb",[("harad_champion",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(10)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0),imodbits_cloth,],
["panther_guard","Panther_Hide",[("panther_guard",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(10)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0),imodbits_cloth,],
["harad_scale","Harad_Scale_Armor",[("harad_scale",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2500,weight(19)|head_armor(0)|body_armor(27)|leg_armor(8)|difficulty(0),imodbits_armor,],
["harad_tiger_scale","Tiger_Guard_Armor",[("harad_tiger_scale",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(20)|head_armor(2)|body_armor(30)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["harad_lion_scale","Lion_Guard_Armor",[("harad_lion_scale",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(20)|head_armor(2)|body_armor(30)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
#["harad_armor_l", "Parsanah Armor",[("harad_padded",0)],itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
###########HELMS##########
#HARONDOR
["harad_dragon_helm","Kiloka_Helm",[("harad_dragon_helm",0)],itp_type_head_armor|itp_shop,0,1500,weight(2.5)|head_armor(39)|difficulty(0),imodbits_armor],
#need meshes for these 2
#["harad_cap_b","Harondor Embroidered Cap",[("harad_heavy_inf_helm",0)],itp_shop|itp_type_head_armor,0,479, weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["harad_cav_helm_a","Harondor_Cavalry_Helm",[("harad_cav_helm_a",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["harad_cav_helm_b","Harondor_Cavalry_Helm",[("harad_cav_helm_b",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["black_snake_helm","Maranka_Helm",[("black_snake_helm",0)],itp_type_head_armor|itp_shop,0,1400,weight(2)|head_armor(38)|difficulty(0),imodbits_elf_armor],
#GREAT HARAD
["harad_finhelm","Great_Harad_Helmet",[("harad_finhelm",0)],itp_type_head_armor|itp_shop,0,1000,weight(3)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["harad_heavy_inf_helm","Great_Harad_Helmet",[("harad_heavy_inf_helm",0)],itp_type_head_armor|itp_shop,0,1000,weight(2.5)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["harad_wavy_helm","Great_Harad_Helmet",[("harad_wavy_helm",0)],itp_type_head_armor|itp_shop,0,1100,weight(3)|head_armor(33)|difficulty(0),imodbits_armor | imodbit_cracked],
#waiting for mesh from giles...
#["harad_helm_g"    , "Leopard Guard Helm" ,[("harad_wavy_helm"   ,0)],itp_shop|itp_type_head_armor,0,479, weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#need meshes for these 3
["harad_eaglehelm","Eagle_Guard_Helm",[("eagle_guard_helmet",0)],itp_type_head_armor|itp_shop,0,1400,weight(3)|head_armor(38)|difficulty(0),imodbits_elf_armor],
#["harad_cap_a"     , "Harad Cloth Cap"  ,[("harad_heavy_inf_helm",0)],itp_shop|itp_type_head_armor,0,479, weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["harad_cloth_helm", "Harad Cloth Covered Helmet",[("black_snake_helm",0)],itp_shop|itp_type_head_armor,0,479, weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["lion_helm","Lion_Guard_Helm",[("lion_helm",0)],itp_type_head_armor|itp_shop,0,1400,weight(3)|head_armor(38)|difficulty(0),imodbits_elf_armor],
#FAR HARAD
["harad_pantherhelm","Panther_Guard_Cap",[("harad_pantherhelm",0)],itp_type_head_armor|itp_shop,0,600,weight(1)|head_armor(25)|difficulty(0),imodbits_cloth],
##########WEAPONS##########
["harad_khopesh","Harad_Khopesh",[("harad_khopesh",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(80)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["black_snake_sword","Harad_Heavy_Falchion",[("black_snake_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(100)|weapon_length(71)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["harad_heavy_sword","Harad_Heavy_Sword",[("harad_heavy_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(92)|weapon_length(80)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["horandor_a","Harad_Scimitar",[("horandor_a",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(90)|swing_damage(22,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["skirmisher_sword","Harad_Skirmisher_Sword",[("skirmisher_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(60)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["harad_sabre","Harad_Sabre",[("harad_sabre",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(70)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["harad_mace","Far_Harad_Mace",[("harad_mace",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(50)|swing_damage(30,blunt)|thrust_damage(0,blunt),imodbits_weapon_bad],
["far_harad_2h_mace","Far_Harad_Two_Handed_Mace",[("far_harad_2h_mace",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_back,700,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(74)|swing_damage(28,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["harad_dagger","Harad_Knife",[("harad_dagger",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_primary|itp_secondary|itp_no_parry,itc_dagger|itcf_carry_dagger_front_left,100,weight(0.75)|difficulty(0)|spd_rtng(112)|weapon_length(47)|swing_damage(22,cut)|thrust_damage(19,pierce),imodbits_weapon_bad],
["harad_short_spear","Harad_Short_Spear",[("harad_short_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear|itp_couchable,200,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(132)|swing_damage(10,blunt)|thrust_damage(20,pierce),imodbits_weapon_wood],
["harad_long_spear","Harad_Spear",[("harad_long_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear|itp_couchable,300,weight(3)|difficulty(0)|spd_rtng(81)|weapon_length(190)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
["eagle_guard_spear","Harasjala_Polearm",[("eagle_guard_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear,1000,weight(3)|difficulty(0)|spd_rtng(86)|weapon_length(149)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_good],
###########SHIELDS##########
["harad_long_shield_a","Harad_Leopard_Shield",[("harad_long_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,500,weight(3)|hit_points(600)|body_armor(5)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["harad_long_shield_b","Harad_Bronze_Shield",[("harad_long_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,800,weight(4)|hit_points(900)|body_armor(10)|spd_rtng(80)|weapon_length(90),imodbits_shield,],
["harad_long_shield_c","Harad_Sun_Shield",[("harad_long_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_board_shield,200,weight(2.5)|hit_points(600)|body_armor(5)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["harad_long_shield_d","Harad_Snake_Shield",[("harad_long_shield_d",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,200,weight(2.5)|hit_points(600)|body_armor(5)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["harad_long_shield_e","Harad_Snake_Shield",[("harad_long_shield_e",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,200,weight(2.5)|hit_points(600)|body_armor(5)|spd_rtng(82)|weapon_length(90),imodbits_shield,],
["harad_shield_a","Harondor_Shield",[("harad_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(50),imodbits_shield,],
["harad_shield_b","Harondor_Buckler",[("harad_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(40),imodbits_shield,],
["harad_shield_c","Harondor_Buckler",[("harad_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(40),imodbits_shield,],
["harad_tribal_a","Far_Harad_Shield",[("far_harad_c_giles",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,200,weight(2.5)|hit_points(480)|body_armor(0)|spd_rtng(82)|weapon_length(80),imodbits_shield,],
["harad_tribal_b","Far_Harad_Shield",[("far_harad_c_giles",0)],itp_type_shield|itp_wooden_parry|itp_shop|itp_cant_use_on_horseback,itcf_carry_board_shield,200,weight(2.5)|hit_points(480)|body_armor(0)|spd_rtng(82)|weapon_length(80),imodbits_shield,],
["harad_yellow_shield","Harad_Shield",[("harad_yellow_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,500,weight(2.5)|hit_points(600)|body_armor(8)|spd_rtng(82)|weapon_length(50),imodbits_shield,],
############BOOTS##########
["desert_boots","Desert_Boots",[("desert_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,200,weight(1)|leg_armor(10)|difficulty(0),imodbits_cloth],
["harad_leather_greaves","Harad_Greaves",[("harad_leather_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,400,weight(2)|leg_armor(14)|difficulty(0),imodbits_cloth],
["harad_scale_greaves","Harad_Boots",[("harad_scale_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,500,weight(3)|leg_armor(22)|difficulty(0),imodbits_armor],
["harad_lamellar_greaves","Harad_Boots",[("harad_lamellar_greaves",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1000,weight(3)|leg_armor(24)|difficulty(0),imodbits_elf_armor],
#####TLD KHAND ITEMS##########
###HELMS###########
["khand_helmet_a1","Khand_Helm_With_Camail",[("Khand_Helmet_A1",0)],itp_type_head_armor|itp_shop,0,1000,weight(3)|head_armor(35)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_a2","Khand_Helm",[("Khand_Helmet_A2",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_a3","Khand_Veiled_Helm",[("Khand_Helmet_A3",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_b1","Khand_Decorated_Helm",[("Khand_Helmet_B1",0)],itp_type_head_armor|itp_shop,0,900,weight(3)|head_armor(33)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_b2","Khand_Masked_Helm",[("Khand_Helmet_B2",0)],itp_type_head_armor|itp_shop,0,1200,weight(3.5)|head_armor(38)|difficulty(0),imodbits_elf_armor],
["khand_helmet_b3","Khand_Veiled_Helm",[("Khand_Helmet_B3",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_b4","Khand_Helm_With_Camail",[("Khand_Helmet_B4",0)],itp_type_head_armor|itp_shop,0,1000,weight(3)|head_armor(35)|difficulty(0),imodbits_armor | imodbit_cracked],
#["khand_helmet_c1", "Khand Helm",[("Khand_Helmet_C1",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["khand_helmet_c2", "Khand Helm",[("Khand_Helmet_C2",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["khand_helmet_c3","Khand_Infantry_Helm",[("Khand_Helmet_C3",0)],itp_type_head_armor|itp_shop,0,800,weight(3)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_c4","Khand_Infantry_Helm",[("Khand_Helmet_C4",0)],itp_type_head_armor|itp_shop,0,800,weight(3)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
#["khand_helmet_c5", "Khand Helm",[("Khand_Helmet_C5",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["khand_helmet_d1","Khand_Masked_Helm",[("Khand_Helmet_D1",0)],itp_type_head_armor|itp_shop,0,1200,weight(3.5)|head_armor(38)|difficulty(0),imodbits_elf_armor],
["khand_helmet_d2","Khand_Helm_With_Camail",[("Khand_Helmet_D2",0)],itp_type_head_armor|itp_shop,0,1000,weight(3)|head_armor(35)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_d3","Khand_Masked_Helm",[("Khand_Helmet_D3",0)],itp_type_head_armor|itp_shop,0,1200,weight(3.5)|head_armor(38)|difficulty(0),imodbits_elf_armor],
["khand_helmet_e1","Khand_Veiled_Helm",[("Khand_Helmet_E1",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_e2","Khand_Helm_With_Camail",[("Khand_Helmet_E2",0)],itp_type_head_armor|itp_shop,0,1000,weight(3)|head_armor(35)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_e3","Khand_Helm",[("Khand_Helmet_E3",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_e4","Khand_Veiled_Helm",[("Khand_Helmet_E4",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_f1","Khand_Veiled_Helm",[("Khand_Helmet_F1",0)],itp_type_head_armor|itp_shop,0,500,weight(2)|head_armor(26)|difficulty(0),imodbits_armor | imodbit_cracked],
#["khand_helmet_f2", "Khand Helm",[("Khand_Helmet_F2",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["khand_helmet_f3", "Khand Helm",[("Khand_Helmet_F3",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["khand_helmet_f4", "Khand Helm",[("Khand_Helmet_F4",0)], itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["khand_helmet_mask1","Khand_Mask",[("Khand_Helmet_Mask1",0)],itp_type_head_armor|itp_shop|itp_doesnt_cover_hair,0,300,weight(2)|head_armor(20)|difficulty(0),imodbits_armor | imodbit_cracked],
["khand_helmet_mask2","Khand_Mask",[("Khand_Helmet_Mask2",0)],itp_type_head_armor|itp_shop|itp_doesnt_cover_hair,0,300,weight(2)|head_armor(20)|difficulty(0),imodbits_armor | imodbit_cracked],
#########ARMOR##########
["khand_light","Khand_Kilt",[("khand_light",0)],itp_type_body_armor|itp_covers_legs|0,0,300,weight(7)|head_armor(0)|body_armor(2)|leg_armor(8)|difficulty(0),imodbits_cloth,],
["khand_foot_lam_a","Khand_Armor",[("khand_foot_lam_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(18)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0),imodbits_armor,],
["khand_foot_lam_b","Khand_Armor",[("khand_foot_lam_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1100,weight(18)|head_armor(0)|body_armor(21)|leg_armor(8)|difficulty(0),imodbits_armor,],
["khand_foot_lam_c","Khand_Armor",[("khand_foot_lam_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(17)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_armor,],
["khand_heavy_lam","Khand_Heavy_Lamellar",[("khand_heavy_lam",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(25)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["khand_light_lam","Khand_Light_Lamellar",[("khand_light_lam",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(19)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_armor,],
#["khand_med_lam_a", "Khand Armor",[("khand_med_lam_a" ,0)],itp_shop|itp_type_body_armor|itp_covers_legs,0,65,weight(7)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["khand_med_lam_b","Khand_Medium_Lamellar",[("khand_med_lam_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(22)|head_armor(0)|body_armor(26)|leg_armor(10)|difficulty(0),imodbits_armor,],
["khand_med_lam_c","Khand_Medium_Lamellar",[("khand_med_lam_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1300,weight(23)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0),imodbits_armor,],
["khand_med_lam_d","Khand_Medium_Lamellar",[("khand_med_lam_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1400,weight(23)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0),imodbits_armor,],
["khand_noble_lam","Khand_Noble_Armor",[("khand_noble_lam",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(26)|head_armor(2)|body_armor(32)|leg_armor(13)|difficulty(0),imodbits_elf_armor,],
["variag_greaves","Variag_Greaves",[("variag_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1000,weight(2)|leg_armor(24)|difficulty(0),imodbits_armor],
#########WEAPONS##########
["khand_axe_great","Khand_Great_Axe",[("Khand_Weapon_Axe_Great",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(4.5)|difficulty(0)|spd_rtng(87)|weapon_length(109)|swing_damage(41,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["khand_axe_winged","Khand_Winged_Axe",[("Khand_Weapon_Axe_Winged",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(3)|difficulty(0)|spd_rtng(93)|weapon_length(96)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
#["khand_glaive"    ,"Khand Glaive"     ,[("Khand_Weapon_Glaive"     ,0)],itp_type_polearm       |itp_shop|itp_spear|itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 352 , weight(4.5)|difficulty(0)|spd_rtng(88) | weapon_length(183)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["khand_halberd","Khand_Halberd",[("Khand_Weapon_Halberd",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_cutting_spear|itcf_carry_axe_back,800,weight(4.5)|difficulty(0)|spd_rtng(88)|weapon_length(164)|swing_damage(38,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
["khand_trident","Khand_Trident",[("Khand_Weapon_Trident",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_cutting_spear|itcf_carry_axe_back,400,weight(4.5)|difficulty(0)|spd_rtng(88)|weapon_length(164)|swing_damage(28,cut)|thrust_damage(35,pierce),imodbits_weapon_bad],
["khand_voulge","Khand_Voulge",[("Khand_Weapon_Voulge",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback,itc_cutting_spear|itcf_carry_axe_back,400,weight(4.5)|difficulty(0)|spd_rtng(88)|weapon_length(126)|swing_damage(38,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
["khand_mace1","Khand_Mace",[("Khand_Weapon_Mace1",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,200,weight(3.5)|difficulty(0)|spd_rtng(99)|weapon_length(77)|swing_damage(21,blunt)|thrust_damage(0,pierce),imodbits_weapon_bad],
["khand_mace2","Khand_Mace",[("Khand_Weapon_Mace2",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,200,weight(3.5)|difficulty(0)|spd_rtng(99)|weapon_length(77)|swing_damage(21,blunt)|thrust_damage(0,pierce),imodbits_weapon_bad],
#["khand_mace3"     ,"Khand Mace"       ,[("Khand_Weapon_Mace3"      ,0)],itp_type_one_handed_wpn|itp_shop|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 122 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(77)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["khand_mace_spiked","Khand_Spiked_Mace",[("Khand_Weapon_Mace_Spiked",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,300,weight(3.5)|difficulty(0)|spd_rtng(99)|weapon_length(82)|swing_damage(21,blunt)|thrust_damage(0,pierce),imodbits_weapon_bad],
["khand_rammace","Khand_Ram_Mace",[("Khand_Weapon_Mace_Ram",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack,itc_nodachi|itcf_carry_back,500,weight(6)|difficulty(0)|spd_rtng(84)|weapon_length(102)|swing_damage(33,blunt)|thrust_damage(0,pierce),imodbits_weapon_wood],
["khand_pitsword","Pit_Fighter_Sword",[("Khand_Weapon_Sword_Pit",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip,300,weight(1.25)|difficulty(0)|spd_rtng(96)|weapon_length(66)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
["khand_tulwar","Khand_Tulwar",[("Khand_Weapon_Tulwar",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip,500,weight(1.25)|difficulty(0)|spd_rtng(91)|weapon_length(94)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
["khand_2h_tulwar","Khand_Tulwar",[("Khand_Weapon_Tulwar_Long",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_shop,itc_greatsword|itcf_carry_sword_back,1123,weight(2.75)|difficulty(0)|spd_rtng(89)|weapon_length(116)|swing_damage(42,cut)|thrust_damage(28,pierce),imodbits_weapon_bad],
["khand_lance","Khand_Lance",[("khand_lance",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_spear,210,weight(2.5)|difficulty(0)|spd_rtng(88)|weapon_length(218)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_bad],
####KHAND SHIELDS
["easterling_round_horseman","Easterling_Round_Shield",[("eastershield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(50),imodbits_shield,],
["variag_gladiator_shield","Variag_Gladiator_Shield",[("eastershield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(50),imodbits_shield,],
["easterling_hawk_shield","Easterling_Hawk_Shield",[("eastershield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(80),imodbits_shield,],
["rhun_bull1_shield","Rhun_Shield",[("eastershield_d",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(6)|spd_rtng(90)|weapon_length(50),imodbits_shield,],
["rhun_bull2_shield","Rhun_Shield",[("eastershield_e",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(6)|spd_rtng(90)|weapon_length(50),imodbits_shield,],
["rhun_bull3_shield","Rhun_Shield",[("eastershield_f",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2.5)|hit_points(480)|body_armor(6)|spd_rtng(90)|weapon_length(50),imodbits_shield,],
###TLD RHUN ITEMS##########
["furry_boots","Furry_Boots",[("furry_boots",0)],itp_type_foot_armor|itp_shop,0,200,weight(3)|leg_armor(10)|difficulty(0),imodbits_orc_cloth],
###ARMOR##########
["rhun_armor_a","Rhun_Light_Battlewear",[("RhunArmorLight1",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,300,weight(5)|head_armor(0)|body_armor(2)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["rhun_armor_b","Rhun_Light_Battlewear",[("RhunArmorLight2",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,350,weight(5)|head_armor(0)|body_armor(3)|leg_armor(6)|difficulty(0),imodbits_cloth,],
#["rhun_armor_c", "Rhun Armor",[("RhunArmorLight3",0)], itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rhun_armor_d","Rhun_Light_Battlewear",[("RhunArmorLight4",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(6)|head_armor(0)|body_armor(4)|leg_armor(6)|difficulty(0),imodbits_cloth,],
#["rhun_armor_e", "Rhun Armor",[("RhunArmorLight5",0)], itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["rhun_armor_f", "Rhun Armor",[("RhunArmorHeavy1",0)], itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rhun_armor_g","Rhun_Heavy_Battlewear",[("RhunArmorHeavy2",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(10)|head_armor(0)|body_armor(18)|leg_armor(16)|difficulty(0),imodbits_armor,],
["rhun_armor_h","Rhun_Heavy_Battlewear",[("RhunArmorHeavy3",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(9)|head_armor(0)|body_armor(17)|leg_armor(16)|difficulty(0),imodbits_armor,],
#["rhun_armor_i", "Rhun Armor",[("RhunArmorHeavy4",0)], itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rhun_armor_j","Rhun_Medium_Battlewear",[("RhunArmorMedium1",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(7)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0),imodbits_cloth,],
#["rhun_armor_l", "Rhun Armor",[("RhunArmorMedium2",0)], itp_shop|itp_type_body_armor|itp_covers_legs,0,65, weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rhun_armor_m","Rhun_Medium_Battlewear",[("RhunArmorMedium3",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,850,weight(7)|head_armor(0)|body_armor(11)|leg_armor(12)|difficulty(0),imodbits_cloth,],
["rhun_armor_n","Rhun_Medium_Battlewear",[("RhunArmorMedium4",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,900,weight(8)|head_armor(0)|body_armor(12)|leg_armor(14)|difficulty(0),imodbits_cloth,],
["rhun_armor_o","Rhun_Medium_Battlewear",[("RhunArmorMedium5",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(8)|head_armor(0)|body_armor(14)|leg_armor(14)|difficulty(0),imodbits_cloth,],
["rhun_armor_p","Rhun_Noble_Armor",[("RhunArmorNoble1A",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(24)|head_armor(0)|body_armor(30)|leg_armor(17)|difficulty(0),imodbits_elf_armor,],
["rhun_armor_k","Rhun_Noble_Armor",[("RhunArmorNoble1B",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,3000,weight(24)|head_armor(0)|body_armor(30)|leg_armor(17)|difficulty(0),imodbits_elf_armor,],
#########Helms##########
["rhun_helm_a","Rhun_Barbed_Helm",[("RhunHelmConical1",0)],itp_type_head_armor|itp_shop,0,500,weight(2)|head_armor(25)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_b","Rhun_Barbed_Helm_Camail",[("RhunHelmConical2",0)],itp_type_head_armor|itp_shop,0,700,weight(3)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_c","Rhun_Horde_Helm",[("RhunHelmHorde1",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
#["rhun_helm_d", "Rhun Helm",[("RhunHelmHorde2"   ,0)],itp_shop|itp_type_head_armor,0,479,weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["rhun_helm_e","Rhun_Horde_Horned_Helm",[("RhunHelmHorde3",0)],itp_type_head_armor|itp_shop,0,600,weight(2.5)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
#["rhun_helm_f", "Rhun Helm",[("RhunHelmPot1"     ,0)],itp_shop|itp_type_head_armor,0,479,weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["rhun_helm_g","Rhun_Horned_Pot",[("RhunHelmPot2",0)],itp_type_head_armor|itp_shop,0,800,weight(3)|head_armor(34)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_h","Rhun_Horned_Pot",[("RhunHelmPot3",0)],itp_type_head_armor|itp_shop,0,750,weight(2.5)|head_armor(32)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_i","Rhun_Round_Helm",[("RhunHelmRound1",0)],itp_type_head_armor|itp_shop,0,600,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_j","Rhun_Round_Masked_Helm",[("RhunHelmRound2",0)],itp_type_head_armor|itp_shop,0,700,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["rhun_helm_k","Rhun_Leather_Helm",[("RhunHelmLeather1",0)],itp_type_head_armor|itp_shop,0,500,weight(1.5)|head_armor(25)|difficulty(0),imodbits_cloth],
["rhun_helm_l","Rhun_Leather_Helm",[("RhunHelmLeather2",0)],itp_type_head_armor|itp_shop,0,500,weight(1.5)|head_armor(25)|difficulty(0),imodbits_cloth],
["rhun_helm_m","Rhun_Leather_Helm",[("RhunHelmLeather3",0)],itp_type_head_armor|itp_shop,0,500,weight(1.5)|head_armor(25)|difficulty(0),imodbits_cloth],
["rhun_helm_n","Rhun_Chieftain_Helm",[("RhunHelmDeathDealer1",0)],itp_type_head_armor|0,0,1500,weight(3.5)|head_armor(45)|difficulty(0),imodbits_elf_armor],
["rhun_helm_o","Rhun_Chieftain_Helm",[("RhunHelmDeathDealer2",0)],itp_type_head_armor|0,0,1500,weight(4)|head_armor(45)|difficulty(0),imodbits_elf_armor],
########WEAPONS##########
["rhun_greataxe","Rhun_Great_Axe",[("rhun_greataxe",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,300,weight(5)|difficulty(0)|spd_rtng(89)|weapon_length(115)|swing_damage(43,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["rhun_battleaxe","Rhun_Battle_Axe",[("rhun_battle_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,300,weight(4)|difficulty(0)|spd_rtng(86)|weapon_length(108)|swing_damage(43,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["rhun_falchion","Rhun_Falchion",[("rhun_falchion",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(77)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["rhun_glaive","Rhun_Glaive",[("rhun_glaive",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_two_handed|itp_cant_use_on_horseback|itp_wooden_parry,itc_cutting_spear|itcf_carry_axe_back,400,weight(4.5)|difficulty(0)|spd_rtng(83)|weapon_length(156)|swing_damage(38,cut)|thrust_damage(21,pierce),imodbits_weapon_bad],
#["rhun_bill",        "Rhun Bill",[("rhun_bill"         ,0)],itp_type_polearm|itp_shop|itp_spear|itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,                            352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(166)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
#["rhun_knife",       "Rhun Knife",[("rhun_knife"        ,0)],itp_type_one_handed_wpn|itp_shop|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 4 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["rhun_greatfalchion","Rhun_Great_Falchion",[("rhun_greatfalchion",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_shop,itc_greatsword|itcf_carry_sword_back,524,weight(3)|difficulty(0)|spd_rtng(92)|weapon_length(102)|swing_damage(42,cut)|thrust_damage(31,pierce),imodbits_weapon_bad],
["rhun_greatsword","Rhun_Great_Sword",[("rhun_greatsword",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_shop,itc_greatsword|itcf_carry_sword_back,524,weight(3)|difficulty(0)|spd_rtng(94)|weapon_length(101)|swing_damage(40,cut)|thrust_damage(31,pierce),imodbits_weapon_bad],
["rhun_shortsword","Rhun_Shortsword",[("rhun_shortsword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["rhun_sword","Rhun_Sword",[("rhun_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(2.9)|difficulty(0)|spd_rtng(92)|weapon_length(89)|swing_damage(32,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
########shields##########
["rhun_shield","Rhun_Kite_Shield",[("rhun_shield",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,200,weight(2.5)|hit_points(480)|body_armor(5)|spd_rtng(82)|weapon_length(80),imodbits_shield,],
#TLD DALE ITEMS##########
########ARMORS##########
["dale_armor_a","Dale_Jacket",[("dale_footman",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(7)|head_armor(0)|body_armor(14)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["dale_armor_b","Dale_Cloak_Jacket",[("WIP_dale_footman_cloak",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(8)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["dale_armor_c","Dale_Archer_Jacket",[("dale_new_archer_c",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(7)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["dale_armor_d","Dale_Archer_Jacket",[("dale_new_archer_f",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(7)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["dale_armor_e","Dale_Coat_Over_Mail",[("dale_heavy_lvam_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(18)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_armor,],
["dale_armor_f","Dale_Coat_Over_Mail",[("dale_heavy_lvam_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(18)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_armor,],
["dale_armor_g","Dale_Coat_Over_Mail",[("dale_heavy_lvam_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(18)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_armor,],
["dale_armor_h","Dale_Cloak_Long_Maille",[("dale_heavy_cloak_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(19)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["dale_armor_i","Dale_Cloak_Long_Maille",[("dale_heavy_cloak_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(19)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["dale_armor_j","Dale_Cloak_Long_Maille",[("dale_heavy_cloak_d",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1500,weight(19)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0),imodbits_elf_armor,],
["dale_armor_k","Dale_Noble_Armor",[("dale_heavy_belt_a",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(2)|body_armor(38)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["dale_armor_l","Dale_Noble_Gorget",[("dale_noble_gorget_b",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(2)|body_armor(38)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
###########HELMS##########
["dale_helmet_a","Dale Light Infantry Helm",[("dale_inf_helm_a",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(35)|difficulty(0),imodbits_armor | imodbit_cracked],
["dale_helmet_b","Dale Light Archer's Helm",[("dwarven_archer_helmet_t1",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
["dale_helmet_c","Dale Infantry Helm",[("dale_inf_helm_b",0)],itp_type_head_armor|itp_shop,0,1100,weight(2)|head_armor(33)|difficulty(0),imodbits_armor | imodbit_cracked],
["dale_helmet_d","Dale Archer's Helm",[("dwarven_archer_helmet_t2",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["dale_helmet_e","Dale Heavy Infantry Helm",[("dale_inf_helm_b",0)],itp_type_head_armor|itp_shop,0,1100,weight(2)|head_armor(33)|difficulty(0),imodbits_armor | imodbit_cracked],
["dale_helmet_f","Dale Heavy Archer's Helm",[("dwarven_archer_helmet_t3",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
#["dale_hood", "Dale Hood",[("dale_hood",0)], itp_shop| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#########WEAPONS##########
["dale_sword","Dale_Shortsword",[("dale_sword_b",0),("scab_dale_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(108)|weapon_length(88)|swing_damage(28,cut)|thrust_damage(21,pierce),imodbits_weapon],
["dale_sword_long","Dale_Longsword",[("dale_sword_a",0),("scab_dale_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(95)|swing_damage(29,cut)|thrust_damage(22,pierce),imodbits_weapon],
["dale_sword_broad","Dale_Broadsword",[("dale_sword_c",0),("scab_dale_sword_c",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(77)|swing_damage(30,cut)|thrust_damage(21,pierce),imodbits_weapon],
["dale_pike","Dale_Spear",[("dale_spear",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_cant_use_on_horseback|itp_penalty_with_shield|itp_wooden_parry,itc_pike,125,weight(3)|difficulty(0)|spd_rtng(95)|weapon_length(171)|swing_damage(0,blunt)|thrust_damage(30,pierce),imodbits_weapon_wood],
["dale_billhook","Dale_Billhook",[("dale_billhook",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_cant_use_on_horseback|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear,125,weight(3)|difficulty(0)|spd_rtng(95)|weapon_length(185)|swing_damage(16,blunt)|thrust_damage(31,pierce),imodbits_weapon_wood],
#####SHIELDS##########
["dale_shield_a","Dale_Shield",[("dwarf_shield_n",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(90)|weapon_length(60),imodbits_shield,],
["dale_shield_b","Dale_Shield",[("dwarf_shield_e",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(90)|weapon_length(60),imodbits_shield,],
["dale_shield_c","Dale_Shield",[("dwarf_shield_m",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,300,weight(2)|hit_points(500)|body_armor(5)|spd_rtng(90)|weapon_length(60),imodbits_shield,],
["dale_shield_d","Dale_Shield",[("dwarf_shield_m",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_round_shield,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(90)|weapon_length(60),imodbits_shield,],
#TLD UMBAR ITEMS##########
##ARMOR##########
["umb_armor_a","Corsair_Leather_Armor",[("corsair_leather",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,300,weight(7)|head_armor(0)|body_armor(10)|leg_armor(4)|difficulty(0),imodbits_cloth,],
["umb_armor_a1","Corsair_Heavy_Leather_Armor",[("corsair_leather_pauldron",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(9)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["umb_armor_b","Corsair_Raider_Armor",[("corsair_leather_cape",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(8)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["umb_armor_c","Corsair_Padded_Armor",[("corsair_padded",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(12)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0),imodbits_cloth,],
["umb_armor_d","Corsair_Heavy_Padded_Armor",[("corsair_padded_pauldron",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,700,weight(14)|head_armor(0)|body_armor(18)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["umb_armor_e","Corsair_Padded_Raider_Armor",[("corsair_padded_cape",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(13)|head_armor(0)|body_armor(16)|leg_armor(5)|difficulty(0),imodbits_cloth,],
["umb_armor_f","Corsair_Hauberk",[("corsair_chain",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1200,weight(20)|head_armor(1)|body_armor(21)|leg_armor(7)|difficulty(0),imodbits_armor,],
["umb_armor_g","Corsair_Hauberk_Pauldrons",[("corsair_chain_pauldron",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2000,weight(22)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0),imodbits_elf_armor,],
["umb_armor_h","Corsair_Heavy_Raider_Armor",[("corsair_chain_cape",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1300,weight(21)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
#######HELMS##########
["umb_helm_a","Corsair_Shell_Helm",[("shell_helmet",0)],itp_type_head_armor|itp_shop,0,1200,weight(3)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["umb_helm_b","Corsair_Shell_Helm",[("shell_helmet_blue",0)],itp_type_head_armor|itp_shop,0,1200,weight(3)|head_armor(35)|difficulty(0),imodbits_elf_armor],
["umb_helm_c","Corsair_Militia_Helm",[("umbar_militia_helmet",0)],itp_type_head_armor|itp_shop,0,700,weight(2)|head_armor(25)|difficulty(0),imodbits_armor | imodbit_cracked],
["umb_helm_d","Corsair_Militia_Helm",[("umbar_militia_helmet_b",0)],itp_type_head_armor|itp_shop,0,700,weight(2)|head_armor(25)|difficulty(0),imodbits_armor | imodbit_cracked],
["umb_helm_e","Corsair_Raider_Helm",[("raider_helmet",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["umb_helm_f","Corsair_Raider_Helm",[("raider_helmet_b",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(28)|difficulty(0),imodbits_armor | imodbit_cracked],
["umb_hood","Umbar_Hood",[("umbar_hood",0)],itp_type_head_armor|itp_shop,0,300,weight(1)|head_armor(10)|difficulty(0),imodbits_cloth],
["corsair_boots","Corsair_Boots",[("corsair_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature|itp_civilian,0,400,weight(1)|leg_armor(14)|difficulty(0),imodbits_cloth],
########SHIELDS##########
["umb_shield_a","Corsair_Buckler",[("corsair_buckler_long_a",0),("corsair_buckler_long_a_carry",ixmesh_carry)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_buckler_left,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(40),imodbits_shield,],
["umb_shield_b","Corsair_Buckler",[("corsair_buckler_round_a",0),("corsair_buckler_round_a_carry",ixmesh_carry)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_buckler_left,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(40),imodbits_shield,],
["umb_shield_c","Corsair_Buckler",[("corsair_buckler_round_b",0),("corsair_buckler_round_b_carry",ixmesh_carry)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_buckler_left,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(40),imodbits_shield,],
["umb_shield_d","Corsair_Buckler",[("corsair_buckler_round_c",0),("corsair_buckler_round_c_carry",ixmesh_carry)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_buckler_left,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(40),imodbits_shield,],
["umb_shield_e","Corsair_Buckler",[("corsair_buckler_long_b",0),("corsair_buckler_long_b_carry",ixmesh_carry)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_buckler_left,200,weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(40),imodbits_shield,],
##########WEAPONS##########umbar_weapon_rapier
["umbar_cutlass","Umbar_Cutlass",[("corsair_cutlass",0),("scab_corsair_cutlass",ixmesh_carry|imodbits_good)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(1.5)|difficulty(0)|spd_rtng(103)|weapon_length(86)|swing_damage(28,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["kraken","Kraken_Cutlass",[("umbar_weapon_kraken_cutlass",0),("scab_kraken_cutlass",ixmesh_carry|imodbits_good)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_scimitar|itcf_carry_sword_left_hip,200,weight(1.5)|difficulty(0)|spd_rtng(103)|weapon_length(103)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_weapon_bad],
["umbar_rapier","Umbar_Sword",[("corsair_sword_a",0),("scab_corsair_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,400,weight(1.5)|difficulty(0)|spd_rtng(105)|weapon_length(81)|swing_damage(23,cut)|thrust_damage(31,pierce),imodbits_weapon_bad],
#["corsair_eket"   ,"Umbarian Eket"  ,[("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_shop|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 47 , weight(0.75)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["corsair_harpoon","Corsair_Harpoon",[("corsair_harpoon",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_show_holster_when_drawn,200,weight(4)|difficulty(0)|shoot_speed(27)|spd_rtng(89)|weapon_length(87)|thrust_damage(63,pierce)|max_ammo(2),imodbits_thrown],
["corsair_sword","Corsair_Eket",[("corsair_sword",0),("scab_corsair_sword",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.5)|difficulty(0)|spd_rtng(101)|weapon_length(90)|swing_damage(29,cut)|thrust_damage(24,pierce),imodbits_weapon_bad],
["corsair_throwing_dagger","Umbarian_Throwing_Daggers",[("corsair_throwing_dagger",0)],itp_type_thrown|itp_shop|itp_primary|0,itcf_throw_knife,200,weight(3.5)|difficulty(0)|shoot_speed(24)|spd_rtng(110)|weapon_length(0)|thrust_damage(40,cut)|max_ammo(10),imodbits_thrown],
["umbar_pike","Umbar_Pike",[("corsair_pike",0)],itp_type_polearm|itp_shop|itp_primary|itp_cant_use_on_horseback|itp_spear|itp_penalty_with_shield|itp_wooden_parry,itc_pike,400,weight(3)|difficulty(12)|spd_rtng(81)|weapon_length(191)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_weapon_wood],
#
#TLD NORTHMENMEN ITEMS##########
######ARMOR##########
["woodman_tunic","Woodman_Tunic",[("woodman_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,300,weight(4)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["woodman_scout","Woodman_Scout_Cape",[("woodman_scout",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,600,weight(14)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["woodman_padded","Woodman_Padded_Armor",[("woodman_padded",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(16)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["beorn_tunic","Beorning_Tunic",[("beorn_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,400,weight(4)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0),imodbits_cloth,],
["beorn_padded","Beorning_Padded_Armor",[("beorn_padded",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,800,weight(12)|head_armor(0)|body_armor(16)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["beorn_heavy","Beorning_Heavy_Armor",[("beorn_heavy",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1000,weight(15)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0),imodbits_elf_armor,],
["beorn_berserk","Beorning_Berserker_Kit",[("beorn_berserker",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,500,weight(6)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0),imodbits_cloth,],
["beorn_chief","Beorning_Chieftan's_Tunic",[("beorn_chieftain",0)],itp_type_body_armor|itp_covers_legs,0,1200,weight(18)|head_armor(0)|body_armor(24)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
######HELMS##########
["beorn_helmet","North_Skullcap",[("beorn_helmet",0)],itp_type_head_armor|itp_shop,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
#["northm_helm_b", "Northmen Helm",[("skull_cap_new",0)], itp_shop|itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#####SHIELDS##########
["beorn_shield","Northmen_Shield",[("dwarf_shield_f",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,200,weight(3)|hit_points(480)|body_armor(8)|spd_rtng(82)|weapon_length(60),imodbits_shield,],
######WEAPONS###########
["beorn_axe","Beorning_Axe",[("beorning_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(5)|difficulty(0)|spd_rtng(91)|weapon_length(76)|swing_damage(41,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
# use itm_dale_sword, itm_dwarf_sword_a, itm_dwarf_sword_b for Beorning's imported swords
#["northm_sword" ,"Northman Sword"  ,[("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["beorn_staff","Woodman's_Staff",[("woodman_staff",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,100,weight(2)|difficulty(0)|spd_rtng(104)|weapon_length(104)|swing_damage(20,blunt)|thrust_damage(20,blunt),imodbits_weapon_wood],
#["beorn_stave"  ,"Woodman's Stave" ,[("woodman_stave"   ,0)], itp_type_polearm|itp_shop|itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back, 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(100)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["beorn_battle_axe","Beorning_War_Axe",[("beorning_war_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(6)|difficulty(0)|spd_rtng(88)|weapon_length(71)|swing_damage(43,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
###TLD DWARF ITEMS##########
########SHIELDS##########
["dwarf_shield_a","Dwarven_Shield",[("dwarf_shield_a",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_b","Dwarven_Shield",[("dwarf_shield_b",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_c","Dwarven_Shield",[("dwarf_shield_c",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_d","Dwarven_Shield",[("dwarf_shield_d",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_f","Dwarven_Shield",[("dwarf_shield_f",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_g","Dwarven_Shield",[("dwarf_shield_g",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
# duplicate["dwarf_shield_h",         "Dwarven Shield",[("dwarf_shield_h",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
["dwarf_shield_i","Dwarven_Shield",[("dwarf_shield_i",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_j","Dwarven_Shield",[("dwarf_shield_j",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_k","Dwarven_Shield",[("dwarf_shield_k",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_shield_l","Dwarven_Shield",[("dwarf_shield_l",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,400,weight(3)|hit_points(700)|body_armor(10)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
#went to dale shields
#["dwarf_shield_e", "Dwarven Shield",[("dwarf_shield_e",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dwarf_shield_m", "Dwarven Shield",[("dwarf_shield_m",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#["dwarf_shield_n", "Dwarven Shield",[("dwarf_shield_n",0)], itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield ],
#WEAPONS###########

##Shield Bear Seax imod Hack Start
] + (is_a_wb_item==1 and [
["dwarf_sword_a","Dwarf_Sword",[("dwarf_sword_a",0),("scab_dwarf_sword_a",ixmesh_carry),("beorning_seax", imodbit_fine),("beorning_seax_sheath",imodbit_fine|ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(62)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_good],
] or [
["dwarf_sword_a","Dwarf_Sword",[("dwarf_sword_a",0),("scab_dwarf_sword_a",ixmesh_carry),("beorning_seax_mb", imodbit_fine),("beorning_seax_sheath_mb",imodbit_fine|ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(62)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_good],
]) + [ 
##Shield Bear Seax imod Hack END

["dwarf_sword_b","Dwarf_Sword",[("dwarf_sword_b",0),("scab_dwarf_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(66)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_good],
["dwarf_sword_c","Dwarf_Sword",[("dwarf_sword_c",0),("scab_dwarf_sword_c",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(66)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_good],
["dwarf_sword_d","Dwarf_Sword",[("dwarf_sword_d",0),("scab_dwarf_sword_d",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_shop,itc_longsword|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn,400,weight(1.25)|difficulty(0)|spd_rtng(103)|weapon_length(58)|swing_damage(29,cut)|thrust_damage(21,pierce),imodbits_weapon_good],
#["dwarf_sword_e", "Dwarf Sword",[("dwarf_sword107",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(96)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_f", "Dwarf Sword",[("dwarf_sword110",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_g", "Dwarf Sword",[("dwarf_sword111",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(91)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_h", "Dwarf Sword",[("dwarf_sword16",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(91)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_i", "Dwarf Sword",[("dwarf_sword18",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(92)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_j", "Dwarf Sword",[("dwarf_sword20",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["dwarf_sword_k", "Dwarf Sword",[("dwarf_sword123",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_shop|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["dwarf_adz","Dwarf_Adz",[("dwarf_adz",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,400,weight(2)|difficulty(0)|spd_rtng(94)|weapon_length(68)|swing_damage(43,pierce)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_great_axe","Dwarf_Great_Axe",[("dwarf_great_axe",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,700,weight(4)|difficulty(0)|spd_rtng(86)|weapon_length(102)|swing_damage(45,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_great_mattock","Dwarf_Great_Mattock",[("dwarf_great_mattock",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,500,weight(3)|difficulty(0)|spd_rtng(92)|weapon_length(94)|swing_damage(30,pierce)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_great_pick","Dwarf_Great_Pick",[("dwarf_great_pick",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,400,weight(3)|difficulty(0)|spd_rtng(96)|weapon_length(93)|swing_damage(30,pierce)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_war_pick","Dwarf_War_Pick",[("dwarf_war_pick",0)],itp_type_polearm|itp_shop|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,400,weight(2)|difficulty(0)|spd_rtng(98)|weapon_length(94)|swing_damage(28,pierce)|thrust_damage(26,pierce),imodbits_weapon_good],
["dwarf_mattock","Dwarf_Mattock",[("dwarf_mattock",0)],itp_type_polearm|itp_shop|itp_primary|itp_wooden_parry|itp_cant_use_on_horseback,itc_scimitar|itcf_carry_axe_left_hip,200,weight(3)|difficulty(0)|spd_rtng(96)|weapon_length(99)|swing_damage(19,pierce)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_hand_axe","Dwarf_Short_Axe",[("dwarf_1h_axe",0)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,500,weight(2)|difficulty(0)|spd_rtng(97)|weapon_length(54)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
["dwarf_throwing_axe","Dwarf_Throwing_Axe",[("dwarf_throw_axe",0)],itp_type_thrown|itp_shop|itp_primary|itp_bonus_against_shield,itcf_throw_axe,300,weight(5)|difficulty(0)|shoot_speed(20)|spd_rtng(99)|weapon_length(33)|thrust_damage(65,cut)|max_ammo(4),imodbits_thrown],
["dwarf_spear",  "Dwarf_Spear",[("dwarf_spear",0)],  itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_staff,400,weight(2.25)|difficulty(0)|spd_rtng(98)|weapon_length(140)|swing_damage(20,blunt)|thrust_damage(26,pierce),imodbits_weapon_good],
["dwarf_spear_b","Dwarf_Pike", [("dwarf_spear_b",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_staff,800,weight(2.25)|difficulty(0)|spd_rtng(95)|weapon_length(165)|swing_damage(22,blunt)|thrust_damage(29,pierce),imodbits_weapon_good],
["dwarf_spear_c","Dwarf_Pike", [("dwarf_spear_c",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable,itc_staff,600,weight(2.25)|difficulty(0)|spd_rtng(97)|weapon_length(150)|swing_damage(22,blunt)|thrust_damage(27,pierce),imodbits_weapon_good],

#HELMS#########
["dwarf_helm_a","Dwarf_Coif",[("DwarfHelmCoif",0)],itp_type_head_armor|itp_shop,0,500,weight(1)|head_armor(20)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_b","Dwarf_Coif_with_Mask",[("DwarfHelmCoifMask",0)],itp_type_head_armor|itp_shop,0,700,weight(2)|head_armor(28)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_c","Dwarf_Helm_with_Mask",[("DwarfHelmCoifMask_B",0)],itp_type_head_armor|itp_shop,0,900,weight(2)|head_armor(33)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_h","Dwarf_Helm",[("DwarfHelmConicalMask",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(37)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_i","Dwarf_Frisian_Helm",[("DwarfHelmFrisianChain",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_j","Dwarf_Frisian_Mask",[("DwarfHelmFrisianMask_A",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
#["dwarf_helm_k", "Dwarf Helm",[("DwarfHelmFrisianMask_B",0)],    itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dwarf_helm_l","Dwarf_Hood",[("DwarfHelmHood",0)],itp_type_head_armor|itp_shop,0,100,weight(1)|head_armor(12)|difficulty(0),imodbits_elf_cloth],
["dwarf_helm_m","Dwarf_Iron_Face",[("DwarfHelmIronheadFace",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
#["dwarf_helm_n", "Dwarf Helm",[("DwarfHelmIronheadLeather",0)],  itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dwarf_helm_o","Dwarf_Nasal_Tophelm",[("DwarfHelmIronheadNasal",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_p","Dwarf_King_Helm",[("DwarfHelmKingCrown",0)],itp_type_head_armor|0,0,2000,weight(2)|head_armor(50)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_q","Dwarf_Miner_Helm",[("DwarfHelmMiner",0)],itp_type_head_armor|itp_shop,0,500,weight(2)|head_armor(22)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_r","Dwarf_Miner_Cap",[("DwarfHelmMinerCap",0)],itp_type_head_armor|itp_shop,0,120,weight(1)|head_armor(14)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_u","Dwarf_Round_Mask",[("DwarfHelmRoundMask",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
["dwarf_helm_v","Dwarf_Chain_Sallet",[("DwarfHelmSalletChain",0)],itp_type_head_armor|itp_shop,0,1000,weight(2)|head_armor(35)|difficulty(0),imodbits_elf_armor],
#["dwarf_helm_w", "Dwarf Helm",[("DwarfHelmSalletLeather",0)],    itp_shop|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dwarf_helm_x","Dwarf_Masked_Sallet",[("DwarfHelmSalletSargeant",0)],itp_type_head_armor|itp_shop,0,1200,weight(2)|head_armor(40)|difficulty(0),imodbits_elf_armor],
#########ARMOR##########
["dwarf_armor_a","Dwarven_Tunic_over_Mail",[("dwarf_tunicmail",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1008,weight(16)|head_armor(0)|body_armor(32)|leg_armor(13)|difficulty(0),imodbits_elf_armor,],
["leather_dwarf_armor","Dwarven_Pad_over_Mail",[("dwarf_padmail",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1108,weight(16)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(0),imodbits_elf_armor,],
["dwarf_vest","Dwarven_Archer_Armor",[("dwarf_tunicmailarcher",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,1108,weight(14)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(0),imodbits_elf_armor,],
["dwarf_armor_b","Dwarven_Pad_over_Tunic",[("dwarf_padtunic",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,908,weight(10)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0),imodbits_elf_cloth,],
["dwarf_armor_c","Dwarven_Scale_over_Mail",[("dwarf_scalemail",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,2008,weight(18)|head_armor(2)|body_armor(40)|leg_armor(13)|difficulty(0),imodbits_elf_armor,],
["leather_dwarf_armor_b","Dwarven_Tunic",[("dwarf_tunic_erebor",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,258,weight(5)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0),imodbits_elf_cloth,],
["dwarf_vest_b","Iron_Hills_Tunic",[("dwarf_tunic_ironhills",0)],itp_type_body_armor|itp_covers_legs|itp_shop,0,308,weight(5)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0),imodbits_elf_cloth,],
#["dwarf_dol_greaves", "Dwarven Plate Boots",[("dwarf_dol_greaves",0)], itp_shop|itp_type_foot_armor |itp_attach_armature,0, 760 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["dwarf_pad_boots","Dwarven_Padded_Boots",[("dwarf_pad_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,708,weight(1)|leg_armor(15)|difficulty(0),imodbits_elf_cloth],
["dwarf_chain_boots","Dwarven_Mail_Chausses",[("dwarf_chain_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1208,weight(2)|leg_armor(25)|difficulty(0),imodbits_elf_armor],
["dwarf_scale_boots","Dwarven_Scale_Boots",[("dwarf_scale_boots",0)],itp_type_foot_armor|itp_shop|itp_attach_armature,0,1508,weight(2)|leg_armor(30)|difficulty(0),imodbits_elf_armor],
###VARIOUS RANDOM MESHES FROM OLD TLD NEEDED FOR TROOPS
#["woodsman_jerkin", "Woodsman's Jerkin",[("woodsman_jerkin",0)], itp_shop|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["white_robe", "White_Robe",[("robe",0)],itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

## Shield Bear Club Imod Hack Start
] + (is_a_wb_item==1 and [
["good_mace","Mace",[("good_mace",0), ("beorning_club", imodbit_masterwork)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(67)|swing_damage(25,blunt)|thrust_damage(15,blunt),imodbits_weapon_bad],
] or [
["good_mace","Mace",[("good_mace",0), ("beorning_club_mb", imodbit_masterwork)],itp_type_one_handed_wpn|itp_primary|itp_shop|itp_wooden_parry|itp_wooden_attack,itc_scimitar|itcf_carry_mace_left_hip,200,weight(2.5)|difficulty(0)|spd_rtng(90)|weapon_length(67)|swing_damage(25,blunt)|thrust_damage(15,blunt),imodbits_weapon_bad],
]) + [
## Shield Bear Club Imod Hack End

["far_harad_shield_paint","Wicker_Shield",[("far_harad_c_giles",0)],itp_type_shield|itp_wooden_parry|itp_shop,itcf_carry_kite_shield,200,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),imodbits_shield,[(ti_on_init_item,[(cur_item_set_tableau_material, "tableau_far_harad_shield",0),])]],
#["rohan_shield_a"        , "Rohan Shield" ,[("rohan_shield_green",0)],itp_shop|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 80  , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|weapon_length(40),imodbits_shield,[(ti_on_init_item,[(cur_item_set_tableau_material, "tableau_rohan_plain_shield",0)])]],
["nazgulrobe","Nazgul_Robe",[("nazgulrobe",0), ("old_nazgulrobe",imodbit_old)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,1,weight(5)|head_armor(60)|body_armor(70)|leg_armor(70)|difficulty(0),0,],
["whiterobe","White_Robe",[("whiterobe",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,1,weight(5)|head_armor(60)|body_armor(70)|leg_armor(70)|difficulty(0),0,],
#BANNERS 
# TODO: PLEASE DO NOT CHANGE BANNER ORDER, THIS IS A PLANNED FEATURE FOR THE MORALE SYSTEM. -CC #
["mordor_banner","Mordor_Banner",[("banner_mordor",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(25,blunt),imodbits_weapon_wood],
["isengard_banner","Isengard_banner",[("banner_isengard",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(25,blunt),imodbits_weapon_wood],
["woodelf_banner","Mirkwood_Banner",[("banner_mirkwood",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(100)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(35,pierce),imodbits_weapon_good],
["lorien_banner","Lothlorien_Banner",[("banner_lorien",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(100)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(35,pierce),imodbits_weapon_good],
["imladris_banner","Imladris_Banner",[("banner_rivendell",0)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(100)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(35,pierce),imodbits_weapon_good],
["gondor_lance_banner","Gondor_Lance_With_Banner",[("banner_lance_gondor",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(120)|swing_damage(15,blunt)|thrust_damage(35,pierce),imodbits_weapon_good],
["amroth_lance_banner","Dol_Amroth_Lance_With_Banner",[("banner_lance_dolamroth",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(120)|thrust_damage(35,pierce),imodbits_weapon_good],
["rohan_lance_banner_sun","Rohan_Lance_With_Sun_Banner",[("banner_lance_rohan_b",0)],itp_type_polearm|itp_shop|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(217)|thrust_damage(35,pierce),imodbits_weapon_good],
["rohan_lance_banner_horse","Rohan_Lance_With_Horse_Banner",[("banner_lance_rohan_a",0)],itp_type_polearm|itp_primary|itp_spear|itp_penalty_with_shield|itp_wooden_parry|itp_couchable, itc_banner,1000,weight(3)|difficulty(0)|spd_rtng(90)|weapon_length(217)|thrust_damage(35,pierce),imodbits_weapon_good],
#
["merry_outfit","hobbit_outfit",[("merry",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(1)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0),0,],
["pippin_outfit","hobbit_outfit",[("pippin",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(1)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0),0,],
#
["ent_body","Ent_Body",[("ent_body",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(65)|leg_armor(0)|difficulty(70),0,],
["ent_head_helm","Ent_Head",[("ent_head1",0)],itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(60)|difficulty(70),0],
["ent_head_helm2","Ent_Head",[("ent_head2",0)],itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(60)|difficulty(70),0],
["ent_head_helm3","Ent_Head",[("ent_head3",0)],itp_type_head_armor|itp_unique,0,1,weight(250)|head_armor(60)|difficulty(70),0],
["ent_feet_boots","Ent_Feet",[("ent_foot",0)],itp_type_foot_armor|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(0)|leg_armor(60)|difficulty(70),0],
["ent_hands","Ent_Hands",[("ent_hand_L",0)],itp_type_hand_armor|itp_unique,0,1,weight(250)|body_armor(1)|difficulty(70),0],
["galadriel","Galadriel_suit",[("galadriel",0)],itp_type_body_armor|itp_covers_legs|itp_unique|itp_civilian,0,1,weight(225)|head_armor(60)|body_armor(80)|leg_armor(60)|difficulty(0),0,],
["empty_hands","empty_hands",[("0",0)],itp_type_hand_armor|itp_unique|itp_no_pick_up_from_ground,0,130,weight(225)|body_armor(1)|difficulty(0),0],
["empty_legs","empty_legs",[("0",0)],itp_type_foot_armor|itp_unique|itp_no_pick_up_from_ground,0,130,weight(225)|leg_armor(1)|difficulty(0),0],
["empty_head","empty head",[("0",0),("chieftainhelm",imodbit_old)],itp_type_head_armor|itp_unique|itp_covers_head|itp_no_pick_up_from_ground,0,1,weight(250)|head_armor(50)|difficulty(0),0],
#### TLD REWARD ITEMS BEGIN
# magic items begin
["ent_water","Strange_bowl_of_water",[("ent_water",0)],itp_unique|itp_type_goods,0,200,weight(2)|abundance(0)|0,imodbits_none],
["map","Maps_of_Middle_Earth",[("middle_earth_map",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["athelas_reward","Athelas_Plant",[("athelas_plant",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["phial_reward","Light_of_Galadriel",[("galadriel_light",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["scroll_reward","On_the_Fall_of_Gondolin",[("quenya_scroll",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["hammer_reward","Smith's_Hammer",[("smith_hammer",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["khand_knife_reward","Khand_Sacrificial_Knife",[("khand_sacrificial_knife",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["angmar_whip_reward","Master's_Whip",[("AngmarWhip",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["horn_gondor_reward","Horn_of_Gondor",[("GondorHorn",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["harad_totem_reward","Harad_Totem",[("harad_totem",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["elven_amulet_reward","Elven_Amulet",[("elven_amulet",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["torque_reward","Evil_Torque",[("reward_torque",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["orc_brew","Orc_Brew",[("orc_brew",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|max_ammo(150),imodbits_none],
["rohan_saddle","Saddle_of_Thengel",[("RohanSaddle",0)],itp_unique|itp_type_goods,0,5000,weight(4)|abundance(0)|0,imodbits_none],
["mearas_reward","Mearh_Stallion",[("mearh",0)],itp_type_horse|itp_unique,0,400,hit_points(180)|body_armor(60)|difficulty(2)|horse_speed(45)|horse_maneuver(40)|horse_charge(40),imodbits_horse_basic|0],
["sword_of_arathorn","Arathorn's_Sword",[("aragorn_sword",0),("scab_aragorn_sword",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_unique,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,2000,weight(2.05)|difficulty(15)|spd_rtng(110)|weapon_length(120)|swing_damage(40,pierce)|thrust_damage(30,pierce),imodbits_weapon_good],
["riv_armor_reward","Rivendell_Decorated_Armor",[("rivendellrewardarmour",0)],itp_type_body_armor|itp_covers_legs|0,0,6000,weight(12)|head_armor(2)|body_armor(50)|leg_armor(20)|difficulty(15),imodbits_elf_armor,],
["westernesse1h_reward","Sword_of_Westernesse",      [("westernesse_1h",0),("scab_1h_westernesse",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_unique,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,3000,weight(1.25)|difficulty(15)|spd_rtng(130)|weapon_length(100)|swing_damage(40,pierce)|thrust_damage(30,pierce),imodbits_weapon_good],
["westernesse2h_reward","Sword_of_The_Great_Serpent",[("westernesse_2h",0),("scab_2h_westernesse",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_unique,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,200,weight(3)|difficulty(18)|spd_rtng(120)|weapon_length(120)|swing_damage(50,pierce)|thrust_damage(45,pierce),imodbits_weapon_good],
["mirkwood_sword_reward","Greenwood_Relic_Sword",[("mirkwood_sword",0),("scab_mirkwood_sword",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_unique,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,200,weight(3)|difficulty(18)|spd_rtng(120)|weapon_length(120)|swing_damage(50,pierce)|thrust_damage(45,pierce),imodbits_weapon_good],
["nazgul_sword","Nazgul_Sword",[("nazgul_sword",0),("nazgul_sword_scab",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_unique,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,200,weight(3)|difficulty(18)|spd_rtng(120)|weapon_length(120)|swing_damage(50,pierce)|thrust_damage(45,pierce),imodbits_weapon_good],
["cooking_cauldron","Cooking_Cauldron",[("cauldron_a",0)],itp_unique|itp_type_goods,0,1000,weight(3)|abundance(0)|0,imodbits_none],
["eorl_cavalry_sword","Sword_of_Eorl",[("eorl_cavalry_sword",0)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_unique,itc_longsword|itcf_carry_sword_left_hip,3000,weight(1.25)|difficulty(12)|spd_rtng(120)|weapon_length(92)|swing_damage(40,pierce)|thrust_damage(30,pierce),imodbits_weapon_good],
["garlic_reward","Garlic",[("garlic",0)],itp_unique|itp_type_goods,0,1000,weight(3)|abundance(0)|0,imodbits_none],
["silmarillion_reward","Silmarillion",[("JIKBookClosed",0)],itp_unique|itp_type_goods,0,1000,weight(3)|abundance(0)|0,imodbits_none],
["herbarium_reward","Middle_Earth_Herbarium",[("JIKBookOpen",0)],itp_unique|itp_type_goods,0,1000,weight(3)|abundance(0)|0,imodbits_none],
["book_of_moria","Book_of_Mazarbul",[("JIKBookClosed",0)],itp_unique|itp_type_goods,0,1000,weight(3)|abundance(0)|0,imodbits_none],
["ring_a_reward","Tulcarisil",[("reward_ring_a",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["ring_b_reward","Finwarisil",[("reward_ring_b",0)],itp_unique|itp_type_goods,0,1000,weight(0.2)|abundance(0)|0,imodbits_none],
["dale_bow_reward","Bow_of_Bard",[("mirkwood_bow",0),("mirkwood_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_unique,itcf_shoot_bow|itcf_carry_bow_back,3000,weight(1.5)|difficulty(5)|shoot_speed(67)|spd_rtng(95)|thrust_damage(32,pierce),0],
["explosive_reward","Isengard_Mine",[("reward_isenmine",0)],itp_unique|itp_type_goods,0,1000,weight(5)|abundance(0)|0,imodbits_none],
["corsair_trident","Trident_of_Sea_Fury",[("corsair_trident",0)],itp_type_polearm|itp_unique|itp_primary|itp_spear|itp_two_handed|itp_cant_use_on_horseback,itc_cutting_spear|itcf_carry_axe_back,2000,weight(4.5)|difficulty(12)|spd_rtng(94)|weapon_length(166)|swing_damage(25,cut)|thrust_damage(35,pierce),imodbits_weapon_wood],
["crebain_reward","Isengard_Crebain",[("prop_reward_crebain",0)],itp_unique|itp_type_goods,0,1000,weight(5)|abundance(0)|0,imodbits_none],
["miruvor_reward","Miruvor_Flask",[("reward_miruvor",0)],itp_unique|itp_type_goods,0,1000,weight(5)|abundance(0)|0,imodbits_none],
["wheeled_cage","Giant_wheeled_cage",[("wheeled_cage",0)],itp_unique|itp_type_goods,0,1000,weight(250)|abundance(0)|0,imodbits_none],
["orc_throwing_axes_reward","Gundabad_Flying_Axes",[("orc_throwing_axe",0)],itp_type_thrown|itp_unique|itp_primary|itp_bonus_against_shield,itcf_throw_axe,150,weight(4)|difficulty(0)|shoot_speed(30)|spd_rtng(103)|weapon_length(33)|thrust_damage(46,cut)|max_ammo(5),imodbits_thrown],
["corsair_throwing_dagger_reward","Poisoned_Throwing_Daggers",[("corsair_throwing_dagger",0)],itp_type_thrown|itp_unique|itp_primary|0,itcf_throw_knife,200,weight(3.5)|difficulty(0)|shoot_speed(24)|spd_rtng(110)|weapon_length(0)|thrust_damage(50,cut)|max_ammo(10),imodbits_thrown],
["dwarf_shield_reward","Mithril_Dwarven_Shield",[("dwarf_shield_j",0)],itp_type_shield|itp_wooden_parry|itp_unique,itcf_carry_kite_shield,400,weight(3)|hit_points(800)|body_armor(28)|spd_rtng(82)|weapon_length(60),imodbits_shield_good,],
["dwarf_great_axe_reward","Dwarf_Sharp_Axe",[("dwarf_great_axe",0)],itp_type_polearm|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,700,weight(6)|difficulty(0)|spd_rtng(83)|weapon_length(102)|swing_damage(55,pierce)|thrust_damage(0,pierce),imodbits_weapon_good],
["isen_uruk_heavy_reward","Uruk-hai_General_Armor",[("urukhai_isen_h",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,3000,weight(30)|head_armor(0)|body_armor(38)|leg_armor(17)|difficulty(0),imodbits_orc_armor,],
["lorien_bow_reward","Noldorin_Bow",[("Elfbow",0),("Elfbow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed|itp_unique,itcf_shoot_bow|itcf_carry_bow_back,1000,weight(1.5)|difficulty(3)|shoot_speed(50)|spd_rtng(83)|thrust_damage(36,pierce),imodbits_good_bow,[]],
["lorien_sword_reward","Galadhrim_Sword",[("lorien_sword_hand_and_half",0),("scab_lorien_sword_hand_and_half",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_unique,itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,900,weight(2.5)|difficulty(0)|spd_rtng(125)|weapon_length(103)|swing_damage(33,cut)|thrust_damage(33,pierce),imodbits_weapon_good],
["dale_sword_reward","Marchwarden_Sword",[("dale_sword_a",0),("scab_dale_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_unique,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.25)|difficulty(0)|spd_rtng(98)|weapon_length(95)|swing_damage(41,cut)|thrust_damage(24,pierce),imodbits_weapon],
["dale_armor_reward","Esgaroth_Noble_Gorget",[("dale_noble_gorget_b",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,2000,weight(22)|head_armor(4)|body_armor(38)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["leather_gloves_reward","Hunting_Gloves",[("lthr_glove_L",0)],itp_type_hand_armor|itp_unique,0,200,weight(0.2)|body_armor(3)|difficulty(0),imodbits_cloth,[]],

##Shield Bear Shield imod Hack Start
] + (is_a_wb_item==1 and [
["beorn_shield_reward","Beorning_Shield",[("beorning_shield",0)],itp_type_shield|itp_wooden_parry|itp_unique,itcf_carry_round_shield,  430 , weight(4.5)|hit_points(690)|body_armor(9)|spd_rtng(90)|weapon_length(50),imodbits_shield,],
] or [
["beorn_shield_reward","Beorning_Shield",[("beorning_shield_mb",0)],itp_type_shield|itp_wooden_parry|itp_unique,itcf_carry_round_shield,  430 , weight(4.5)|hit_points(690)|body_armor(9)|spd_rtng(90)|weapon_length(50),imodbits_shield,],
]) + [ 
##Shield Bear Shield imod Hack END

["beorn_axe_reward","Bear_Axe",[("beorning_war_axe",0)],itp_type_polearm|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback,itc_nodachi|itcf_carry_axe_back,300,weight(6)|difficulty(0)|spd_rtng(110)|weapon_length(71)|swing_damage(65,cut)|thrust_damage(0,pierce),imodbits_weapon_good],
["moria_arrow_reward","Moria_Poisoned_Arrows",[("orc_hook_arrow",0),("orc_hook_arrow_flying",ixmesh_flying_ammo),("orc_quiver",ixmesh_carry)],itp_type_arrows,itcf_carry_quiver_back_right,700,weight(3)|thrust_damage(11,cut)|max_ammo(40)|weapon_length(95),imodbits_missile,[]],

["khamul_helm","Helm_of_Khamul",[("helmet_khamul_small",0)],itp_type_head_armor|itp_unique,0,3000,weight(3)|head_armor(50)|difficulty(12),0],
["gandstaff","Wizards_Staff",[("gandstaff",0)],itp_primary|itp_wooden_parry|itp_type_polearm|itp_spear|itp_penalty_with_shield|itp_wooden_attack,itc_staff,1,weight(2.5)|difficulty(0)|spd_rtng(103)|weapon_length(118)|swing_damage(50,blunt)|thrust_damage(40,blunt),0],
["sarustaff","Wizards_Staff",[("sarustaff",0)],itp_primary|itp_wooden_parry|itp_type_polearm|itp_spear|itp_penalty_with_shield|itp_wooden_attack,itc_staff,1,weight(2.5)|difficulty(0)|spd_rtng(103)|weapon_length(118)|swing_damage(50,blunt)|thrust_damage(40,blunt),0],
["rohan_armor_th","Rohan_Royal_Armor",[("theoden_armor",0)],itp_type_body_armor|itp_covers_legs,0,4000,weight(20)|head_armor(0)|body_armor(44)|leg_armor(15)|difficulty(15),imodbits_elf_armor,],
["denethor_robe","Stewards_Robe",[("denethor_robe",0)],itp_type_body_armor|itp_covers_legs,0,1000,weight(20)|head_armor(0)|body_armor(44)|leg_armor(15)|difficulty(0),imodbits_elf_armor,],
["prisoner_coll_chain","Prisoner_Chains",[("prisoner_coll_chain",0)],itp_type_head_armor|itp_doesnt_cover_hair,0,10,weight(10)|head_armor(2)|difficulty(0),0],
["witchking_helmet","Wicked_Helm",[("witchking_helmet",0)],itp_type_head_armor|itp_unique,0,3000,weight(2.5)|head_armor(50)|difficulty(0),0],
# let   witchking_helmet  be the last item (mtarini)
["lorien_royal_armor","Lorien_Royal_Armor",[("lorien_royal",0)],itp_type_body_armor|itp_covers_legs,0,5000,weight(19)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(15),imodbits_elf_armor,],
["feet_chains","Feet Chains",[("chains_full",0)],itp_type_foot_armor|itp_attach_armature,0,200,weight(10)|leg_armor(0)|difficulty(0),imodbits_none],
["feet_chains_dwarf","Feet Chains",[("chains_full_dwarf",0)],itp_type_foot_armor|itp_attach_armature,0,200,weight(10)|leg_armor(0)|difficulty(0),imodbits_none],

["spider","Spider",[("spider",0)], itp_type_horse|itp_unique, 0, 1200, hit_points(60)|body_armor(30)|difficulty(3)|horse_speed(50)|horse_maneuver(75)|horse_charge(25),imodbits_none,[]],
["bear","Bear",    [("bear",0)],   itp_type_horse|itp_unique, 0, 1200, hit_points(130)|body_armor(40)|horse_speed(50)|horse_maneuver(40)|horse_charge(25),imodbits_none,[]],
["wolf","Wolf",    [("wolf",0)],   itp_type_horse|itp_unique, 0, 1200, hit_points(50)|body_armor(25)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_none,[]],

["defiled_armor_gondor","Defiled_Gondor_Leader's_Surcoat",[("defile_gondor",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,3000,weight(21)|head_armor(0)|body_armor(30)|leg_armor(6)|difficulty(0),imodbits_none,[(ti_on_init_item,[(cur_item_set_tableau_material, "tableau_defiled_gondor_armor",0)])]],
["defiled_armor_rohan","Defiled_Rohan_Hauberk",[("defile_rohan",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,1600,weight(17)|head_armor(0)|body_armor(25)|leg_armor(9)|difficulty(0),imodbits_none, [(ti_on_init_item,[(cur_item_set_tableau_material, "tableau_defiled_rohan_armor",0)])]],
["defiled_armor_dale","Defiled_Dale_Noble_Armor",[("defile_dale",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,2000,weight(21)|head_armor(2)|body_armor(30)|leg_armor(11)|difficulty(0),imodbits_none, [(ti_on_init_item,[(cur_item_set_tableau_material, "tableau_defiled_dale_armor",0)])]],

["save_compartibility_item10","INVALID_ITEM",[("practice_sword",0)],itp_type_goods,0,3,weight(1.5)|abundance(90)|0,imodbits_none],

]
