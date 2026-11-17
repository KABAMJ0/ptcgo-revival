from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="67b2ca21-904d-5d86-8e49-95b5d3899941",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic", "Ferroseed"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=597,
    abilities=[
        Attack(
            title="Zzzt",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)