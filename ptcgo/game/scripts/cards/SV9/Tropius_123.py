from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37f552d6-3792-53ab-870a-c9b4dc928fc3",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=357,
    abilities=[
        Attack(
            title="Fruit Bearing",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)