from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="ce3650cc-fa4e-56b5-9c30-0038c796df18",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=48,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Ability(
            title="Roar of the Sword",
            game_text="Once during your turn, you may search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Storm Slash",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.PSYCHIC), per=30, base=60),
        ),
    ],
)