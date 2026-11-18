from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da42fc39-78f5-59d5-ba13-2bf728d79221",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    display_name="Dreepy",
    searchable_by=["Dreepy", "Basic", "Dreepy"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=885,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)