from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b6bc05e-f706-5286-8435-8026fe026aee",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Leaf Supply",
            game_text="You may attach a basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Dual Cut",
            game_text="Flip 2 coins. This attack does 70 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)