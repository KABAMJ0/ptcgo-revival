from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="427edc60-d33d-58c7-acc2-2fa21dd70596",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Tail Slap",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)