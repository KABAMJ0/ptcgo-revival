from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="256c2277-093a-55db-879b-13bf537198c0",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    display_name="Alolan Graveler",
    searchable_by=["Alolan Graveler", "Stage 1", "AlolanGraveler"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Electric Punch",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)