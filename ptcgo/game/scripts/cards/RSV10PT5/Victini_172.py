from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef11a40e-b3c6-5bda-8e5b-156011fc2725",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=172,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V-Force",
            game_text="If you have 4 or fewer Benched Pok\u00e9mon, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)