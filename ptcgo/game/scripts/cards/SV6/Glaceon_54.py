from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0df66dbb-2277-55d8-90fc-4970b99c5fdc",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Glaceon"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Permeating Chill",
            game_text="At the end of your opponent's next turn, put 9 damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Icicle Missile",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)