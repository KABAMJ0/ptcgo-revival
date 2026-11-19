from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="923357b4-3a6e-5697-8ddc-8826689b1d26",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerponex.Name",
    display_name="Hearthflame Mask Ogerpon ex",
    searchable_by=["Hearthflame Mask Ogerpon ex", "Basic", "Tera", "ex", "HearthflameMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=212,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Wrathful Hearth",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 20, base=0),
        ),
        Attack(
            title="Dynamic Blaze",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 140 more damage, and discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)