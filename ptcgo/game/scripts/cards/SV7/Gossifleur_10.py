from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ff0bcbe-1c0e-56a8-b2e6-a00dc5d211b3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    display_name="Gossifleur",
    searchable_by=["Gossifleur", "Basic", "Gossifleur"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=829,
    abilities=[
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)