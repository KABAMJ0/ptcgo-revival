from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c5a4b23-6471-5c57-b0bb-6818290db749",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlink.Name",
    display_name="N's Klink",
    searchable_by=["N's Klink", "Basic", "NsKlink"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=599,
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