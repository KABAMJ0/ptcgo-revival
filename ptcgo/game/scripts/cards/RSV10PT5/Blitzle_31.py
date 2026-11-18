from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ffcaf9e1-ef78-50f7-9b82-df9dd34cb2a6",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=["Blitzle", "Basic", "Blitzle"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=522,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)