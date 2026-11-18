from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c098c6ae-c612-521c-8126-875d6d1211ae",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Sky Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)