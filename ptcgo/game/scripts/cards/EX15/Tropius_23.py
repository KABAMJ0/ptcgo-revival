from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9c3c22e-84ae-5fdf-a5b4-a862b98c751b",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius δ",
    searchable_by=["Tropius \u03b4", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Ability(
            title="Tropical Heal",
            game_text="Once during your turn, when you put Tropius from your hand onto your Bench, you may remove all Special Conditions, Imprison markers, and Shock-wave markers from your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Grind",
            game_text="Does 10 damage times the amount of Energy attached to Tropius.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)