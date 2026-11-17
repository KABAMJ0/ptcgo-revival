from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de4c7f86-77f0-5372-814e-93d54fd53eab",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name",
    display_name="Melmetal ex",
    searchable_by=["Melmetal ex", "Stage 1", "ex", "Melmetalex"],
    subtypes=["Stage 1", "ex"],
    collector_number=105,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Iron Swing",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)