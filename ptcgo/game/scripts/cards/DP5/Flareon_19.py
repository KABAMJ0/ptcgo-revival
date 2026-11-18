from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cfa87aa5-131f-55ab-ad76-29ce8669a650",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy card attached to Flareon and then discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)