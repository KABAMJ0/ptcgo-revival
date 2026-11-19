from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="5b60c12c-3219-5467-bcfb-fd49becb11b9",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FalinksV.Name",
    display_name="Falinks V",
    searchable_by=["Falinks V", "Basic", "V", "FalinksV"],
    subtypes=["Basic", "V"],
    collector_number=115,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Ability(
            title="Iron Defense Formation",
            game_text="All of your Pok\u00e9mon that have \"Falinks\" in their name take 20 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=lock_self_attack(),
        ),
    ],
)