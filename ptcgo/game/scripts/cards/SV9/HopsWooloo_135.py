from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96081495-83ac-5758-a50c-02aee39d4aee",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsWooloo.Name",
    display_name="Hop's Wooloo",
    searchable_by=["Hop's Wooloo", "Basic", "HopsWooloo"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)