from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35dc7ca0-feda-5cff-95f7-656bb204c446",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic", "Helioptile"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=694,
    abilities=[
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)