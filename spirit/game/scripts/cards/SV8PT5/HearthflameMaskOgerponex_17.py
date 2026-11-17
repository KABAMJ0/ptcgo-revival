from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="718d5d0d-5a6a-53b0-a567-c4800d230143",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerponex.Name",
    display_name="Hearthflame Mask Ogerpon ex",
    searchable_by=["Hearthflame Mask Ogerpon ex", "Basic", "Tera", "ex", "HearthflameMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=17,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1017,
    abilities=[
        Attack(
            title="Wrathful Hearth",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
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