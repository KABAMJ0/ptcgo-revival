from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d8b20c4-e32e-5f49-bdfe-f06113e4b4ad",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikouex.Name",
    display_name="Raikou ex",
    searchable_by=["Raikou ex", "Basic", "ex", "Raikouex"],
    subtypes=["Basic", "ex"],
    collector_number=121,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Thunder-Clad",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for an Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)