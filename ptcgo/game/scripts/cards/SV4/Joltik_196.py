from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a423d480-8623-5641-9fb7-fc3b1d93ef98",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic", "Joltik"],
    subtypes=["Basic"],
    collector_number=196,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Flail Around",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)