from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ec62c98-a547-5ba4-886d-38691762c3f5",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluzaex.Name",
    display_name="Veluza ex",
    searchable_by=["Veluza ex", "Basic", "ex", "Veluzaex"],
    subtypes=["Basic", "ex"],
    collector_number=43,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Purging Strike",
            game_text="You may discard your hand. If you discarded any cards in this way, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)