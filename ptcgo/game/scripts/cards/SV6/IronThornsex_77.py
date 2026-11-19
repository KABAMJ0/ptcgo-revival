from ptcgo.game.card_effects.attacks_common import energy_move_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="561a6b23-0e24-5c99-b4c1-3115577e99f2",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronThornsex.Name",
    display_name="Iron Thorns ex",
    searchable_by=["Iron Thorns ex", "Basic", "ex", "Future", "IronThornsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=77,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=995,
    abilities=[
        Ability(
            title="Initialization",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, Pok\u00e9mon with a Rule Box in play (both yours and your opponent's) have no Abilities, except for Future Pok\u00e9mon. (Pok\u00e9mon ex, Pok\u00e9mon V, etc. have Rule Boxes.)",
            effect=unimplemented,
        ),
        Attack(
            title="Volt Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=energy_move_attack(1),
        ),
    ],
)