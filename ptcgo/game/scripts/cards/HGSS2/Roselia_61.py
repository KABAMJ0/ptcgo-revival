from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8dd13ea-658e-57a0-91a2-0e754e1e9a97",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads. Roselia is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)