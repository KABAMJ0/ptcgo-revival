from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import pokemon_of_types, takes_less_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="dae97bf1-3dc1-5a71-add0-373c89bb5829",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="EX11",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to Azumarill by attacks from Fire Pok\u00e9mon and Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, attacker_pred=pokemon_of_types(PokemonTypes.FIRE, PokemonTypes.WATER)),
        ),
        Attack(
            title="Bubblebeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)