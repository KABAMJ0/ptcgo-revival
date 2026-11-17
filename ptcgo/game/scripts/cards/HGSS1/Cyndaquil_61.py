from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e129ca8-1d1a-5bc9-9b78-241a2937f939",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    display_name="Cyndaquil",
    searchable_by=["Cyndaquil", "Basic", "Cyndaquil"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)