from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ebafa68-179c-5118-ae4c-5638a0f0df14",
    key="SMP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozma.Name",
    display_name="Dawn Wings Necrozma",
    searchable_by=["Dawn Wings Necrozma", "Basic", "Ultra Beast", "DawnWingsNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="SMP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Attack(
            title="Gulf Stream",
            game_text="If you have exactly 6 Prize cards remaining, this attack does 20 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Sword of Dawn",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)