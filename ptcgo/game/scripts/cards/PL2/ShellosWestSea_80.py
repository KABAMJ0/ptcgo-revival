from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9aa3438-5fd8-5994-b013-0e44c27e6a31",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosWestSea.Name",
    display_name="Shellos West Sea",
    searchable_by=["Shellos West Sea", "Basic", "ShellosWestSea"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=422,
    abilities=[
        Attack(
            title="Healing Sea",
            game_text="Flip 2 coins. Choose 1 of your Pok\u00e9mon. For each heads, remove 1 damage counter from that Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)